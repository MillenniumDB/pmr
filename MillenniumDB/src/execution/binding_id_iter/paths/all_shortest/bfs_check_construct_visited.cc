#include "bfs_check_construct_visited.h"

#include <cassert>

#include "base/ids/var_id.h"
#include "execution/binding_id_iter/paths/path_manager.h"
#include "query_optimizer/quad_model/quad_model.h"
#include "storage/index/bplus_tree/bplus_tree.h"
#include "storage/index/bplus_tree/bplus_tree_leaf.h"
#include "storage/index/record.h"

using namespace std;
using namespace Paths::AllShortest;

BFSCheckConstructVisited::BFSCheckConstructVisited(ThreadInfo*  thread_info,
                                                   VarId        path_var,
                                                   Id           start,
                                                   Id           end,
                                                   RPQ_DFA      automaton) :
    thread_info (thread_info),
    path_var    (path_var),
    start       (start),
    end         (end),
    automaton   (automaton) { }


void BFSCheckConstructVisited::begin(BindingId& _parent_binding) {
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
}


bool BFSCheckConstructVisited::next() {
    // Check if first node is end state
    if (is_first) {
        is_first = false;

        auto current_state = open.front();
        auto node_iter     = quad_model.nodes->get_range(&thread_info->interruption_requested,
                                                         Record<1>({ current_state->node_id.id }),
                                                         Record<1>({ current_state->node_id.id }));
        // Return false if node does not exists in bd
        if (node_iter->next() == nullptr) {
            queue<const SearchState*> empty;
            open.swap(empty);
            return false;
        }
        if (automaton.is_final_state[automaton.start_state] && (current_state->node_id == end_object_id)) {
            auto path_id = path_manager.set_path(current_state, path_var);
            parent_binding->add(path_var, path_id);

            // Empty queue because the only state with 0 distance is the first state
            queue<const SearchState*> empty;
            open.swap(empty);

            results_found++;
            return true;
        }
    }
    while (open.size() > 0) {
        auto current_state = open.front();
        auto has_next_pair = current_state_has_next(current_state);
        // Check if a new state need to be added to Open.
        // If current_state has next then has_next_pair.second is true
        if (has_next_pair.second) {
            // If a state that have been not added to open is founded, then
            // has_next_pair.first is a pointer to the state in visited, in other
            // case, is a pointer to visited.end()
            if (has_next_pair.first != visited.end()) {
                // If the pointer does not points to visited.end, the state
                // will be added to open
                open.push(has_next_pair.first.operator->());
            }
        }

        // Check if current_state is in a final automaton state. In current_state_has_next
        // methods only nodes with an optimal distance to start node are added to Open. Then
        // is a node reaches to final state in the automaton, then it node will have an optimal
        // path to start node
        if (automaton.is_final_state[current_state->automaton_state] && current_state->node_id == end_object_id) {
            parent_binding->add(path_var, ObjectId(ObjectId::MASK_POSITIVE_INT | visited.size()));
            // Clear open
            queue<const SearchState*> empty;
            open.swap(empty);
            return true;
        }
        // Pop state when all paths have been returned (if corresponds) and
        // it does not have more state to add to the open
        if (!has_next_pair.second) {
            open.pop();
            iter = nullptr;
        }
    }
    return false;
}


pair<robin_hood::unordered_node_set<SearchState>::iterator, bool>
  BFSCheckConstructVisited::current_state_has_next(const SearchState* current_state)
{
    if (iter == nullptr) { // if is first time that SearchState is explore
        current_transition = 0;
        // Check automaton state has transitions
        if (current_transition >= automaton.from_to_connections[current_state->automaton_state].size()) {
            return make_pair(visited.end(), false);
        }
        // Constructs iter
        set_iter(current_state);
    }
    // Iterate over automaton_start state transitions
    while (current_transition < automaton.from_to_connections[current_state->automaton_state].size()) {
        auto& transition   = automaton.from_to_connections[current_state->automaton_state][current_transition];

        // Iterate over next_childs
        for (auto child_record = iter->next(); child_record != nullptr; child_record = iter->next()) {
            SearchState next_state_key(ObjectId(child_record->ids[2]),
                                       transition.to,
                                       current_state->distance + 1,
                                       const_cast<SearchState*>(current_state),
                                       transition.inverse,
                                       transition.type_id);

            auto visited_search = visited.find(next_state_key);
            // Check if state has already been found
            if (visited_search != visited.end()) {
                // Check if the node found has an optimal distance (it is to say, the distance
                // of the new state have to be equal to the previous node)
                if (visited_search->distance == next_state_key.distance) {
                    visited_search->path_iter.add(current_state, transition.inverse, transition.type_id);
                }
                return make_pair(visited.end(), true);
            } else {
                return visited.emplace(ObjectId(child_record->ids[2]),
                                       transition.to,
                                       current_state->distance + 1,
                                       const_cast<SearchState*>(current_state),
                                       transition.inverse,
                                       transition.type_id);
            }
        }
        // Constructs new iter
        current_transition++;
        if (current_transition < automaton.from_to_connections[current_state->automaton_state].size()) {
            set_iter(current_state);
        }
    }
    return make_pair(visited.end(), false);
}


void BFSCheckConstructVisited::set_iter(const SearchState* current_state) {
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


void BFSCheckConstructVisited::reset() {
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
}


void BFSCheckConstructVisited::analyze(std::ostream& os, int indent) const {
    os << std::string(indent, ' ');
    os << "Paths::AllShortest::BFSCheckConstructVisited(bpt_searches: " << bpt_searches << ", found: " << results_found << ")";
}
