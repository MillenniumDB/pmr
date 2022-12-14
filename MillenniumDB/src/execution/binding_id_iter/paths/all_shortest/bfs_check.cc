#include "bfs_check.h"

#include <cassert>

#include "base/ids/var_id.h"
#include "execution/binding_id_iter/paths/path_manager.h"
#include "query_optimizer/quad_model/quad_model.h"
#include "storage/index/bplus_tree/bplus_tree.h"
#include "storage/index/bplus_tree/bplus_tree_leaf.h"
#include "storage/index/record.h"

using namespace std;
using namespace Paths::AllShortest;

BFSCheck::BFSCheck(ThreadInfo* thread_info,
                   VarId       path_var,
                   Id          start,
                   Id          end,
                   RPQ_DFA     automaton) :
    thread_info (thread_info),
    path_var    (path_var),
    start       (start),
    end         (end),
    automaton   (automaton) { }


void BFSCheck::begin(BindingId& _parent_binding) {
    parent_binding = &_parent_binding;

    // Init start object id
    ObjectId start_object_id(std::holds_alternative<ObjectId>(start) ? std::get<ObjectId>(start)
                                                                     : (*parent_binding)[std::get<VarId>(start)]);

    end_object_id = std::holds_alternative<ObjectId>(end)
                    ? std::get<ObjectId>(end)
                    : (*parent_binding)[std::get<VarId>(end)];

    // Add start_object_id to open and visited structures
    auto start_state = visited.emplace(start_object_id, automaton.start_state, 0);
    open.push(start_state.first.operator->());
    is_first = true;

    min_ids[2] = 0;
    max_ids[2] = 0xFFFFFFFFFFFFFFFF;
    min_ids[3] = 0;
    max_ids[3] = 0xFFFFFFFFFFFFFFFF;

    optimal_distance = UINT64_MAX;
}


bool BFSCheck::next() {
    // Check if first node is end state
    if (is_first) {
        is_first = false;

        auto current_state = open.front();
        auto node_iter     = quad_model.nodes->get_range(&thread_info->interruption_requested,
                                                         Record<1>({ current_state->node_id.id }),
                                                         Record<1>({ current_state->node_id.id }));
        // Return false if node does not exists in bd
        if (node_iter->next() == nullptr) {
            open.pop();
            return false;
        }
        if (automaton.is_final_state[automaton.start_state] && (current_state->node_id == end_object_id)) {
            auto new_state = visited.emplace(current_state->node_id, automaton.start_state, 0);
            auto path_id = path_manager.set_path(new_state.first.operator->(), path_var);
            parent_binding->add(path_var, path_id);

            // Empty queue because the only state with 0 distance is the first state
            open.pop();

            results_found++;
            return true;
        }
    }

    // check for next enumeration of state_reached
    if (saved_state_reached != nullptr) {
enumeration:
        if (__builtin_expect(!!(thread_info->interruption_requested), 0)) {
            throw InterruptedException();
        }
        if (saved_state_reached->path_iter.next()) {
            auto path_id = path_manager.set_path(saved_state_reached, path_var);
            parent_binding->add(path_var, path_id);

            results_found++;
            return true;
        } else {
            saved_state_reached = nullptr;
        }
    }

    while (open.size() > 0) {
        auto current_state = open.front();
        bool reached_final_state = expand_neighbors(current_state);

        // Check if a new state need to be added to open.
        if (reached_final_state) {
            saved_state_reached->path_iter.start_enumeration();
            goto enumeration;
        }  else {
            // Pop and visit next state
            iter = nullptr;
            open.pop();
        }
    }
    return false;
}


bool BFSCheck::expand_neighbors(const SearchState* current_state) {
    // check if this is the first time that current_state is explored
    if (iter == nullptr) {
        current_transition = 0;
        // check if automaton state has outer transitions
        if (current_transition >= automaton.from_to_connections[current_state->automaton_state].size()) {
            return false;
        }
        // Constructs iter
        set_iter(current_state);
    }
    // iterate over the remaining transitions of current_state.
    // don't start from the beginning, resume where it left thanks to current_transition and iter
    while (current_transition < automaton.from_to_connections[current_state->automaton_state].size()) {
        auto& transition= automaton.from_to_connections[current_state->automaton_state][current_transition];

        // iterate over records until there is no more records or reach a final state with shortest path
        for (auto child_record = iter->next(); child_record != nullptr; child_record = iter->next()) {
            SearchState next_state(ObjectId(child_record->ids[2]),
                                   transition.to,
                                   current_state->distance + 1);

            // check if next state has already been visited
            auto visited_search = visited.find(next_state);
            if (visited_search != visited.end()) {
                // consider next_state only if it has an optimal distance
                if (visited_search->distance == next_state.distance) {
                    visited_search->path_iter.add(current_state, transition.inverse, transition.type_id);
                    if (next_state.node_id == end_object_id &&
                        automaton.is_final_state[next_state.automaton_state])
                    {
                        if (optimal_distance == next_state.distance)
                        {
                            saved_state_reached = visited_search.operator->();
                            return true;
                        }
                    }
                }
            } else {
                // Add state to visited and the queue and keep going unless is a optimal final state
                auto reached_state = visited.emplace(ObjectId(child_record->ids[2]),
                                                     transition.to,
                                                     current_state->distance + 1,
                                                     current_state,
                                                     transition.inverse,
                                                     transition.type_id).first;
                open.push(reached_state.operator->());

                if (reached_state->node_id == end_object_id
                    && automaton.is_final_state[transition.to])
                {
                    // auto found_reached_final = reached_final.find(next_state.node_id.id);
                    if (optimal_distance != UINT64_MAX) {
                        if (optimal_distance == next_state.distance) {
                            saved_state_reached = reached_state.operator->();
                            return true;
                        }
                    } else {
                        optimal_distance = next_state.distance;
                        saved_state_reached = reached_state.operator->();
                        return true;
                    }
                }
            }
        }
        // Constructs new iter
        current_transition++;
        if (current_transition < automaton.from_to_connections[current_state->automaton_state].size()) {
            set_iter(current_state);
        }
    }
    return false;
}


void BFSCheck::set_iter(const SearchState* current_state) {
    // Get iter from correct bpt_tree according to inverse attribute
    const auto& transition = automaton.from_to_connections[current_state->automaton_state][current_transition];
    if (transition.inverse) {
        min_ids[0] = current_state->node_id.id;
        max_ids[0] = current_state->node_id.id;
        min_ids[1] = transition.type_id.id;
        max_ids[1] = transition.type_id.id;
        iter = quad_model.to_type_from_edge->get_range(&thread_info->interruption_requested,
                                                       Record<4>(min_ids),
                                                       Record<4>(max_ids));
    } else {
        min_ids[0] = transition.type_id.id;
        max_ids[0] = transition.type_id.id;
        min_ids[1] = current_state->node_id.id;
        max_ids[1] = current_state->node_id.id;
        iter = quad_model.type_from_to_edge->get_range(&thread_info->interruption_requested,
                                                       Record<4>(min_ids),
                                                       Record<4>(max_ids));
    }
    bpt_searches++;
}


void BFSCheck::reset() {
    // Empty structures
    queue<const SearchState*> empty;
    open.swap(empty);
    visited.clear();
    is_first = true;
    iter     = nullptr;

    // Add start object id to structures
    ObjectId start_object_id(std::holds_alternative<ObjectId>(start) ? std::get<ObjectId>(start)
                                                                     : (*parent_binding)[std::get<VarId>(start)]);

    auto start_state = visited.emplace(start_object_id, automaton.start_state, 0);

    open.push(start_state.first.operator->());

    // Set end_object_id
    if (std::holds_alternative<ObjectId>(end)) {
        end_object_id = std::get<ObjectId>(end);
    } else {
        auto end_var_id = std::get<VarId>(end);
        end_object_id   = (*parent_binding)[end_var_id];
    }
    optimal_distance = UINT64_MAX;
}


void BFSCheck::analyze(std::ostream& os, int indent) const {
    os << std::string(indent, ' ');
    os << "Paths::AllShortest::BFSCheck(bpt_searches: " << bpt_searches << ", found: " << results_found << ")";
}
