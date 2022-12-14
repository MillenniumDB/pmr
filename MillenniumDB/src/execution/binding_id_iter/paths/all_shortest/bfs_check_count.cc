#include "bfs_check_count.h"

#include <cassert>

#include "base/ids/var_id.h"
#include "execution/binding_id_iter/paths/path_manager.h"
#include "query_optimizer/quad_model/quad_model.h"
#include "storage/index/bplus_tree/bplus_tree.h"

using namespace std;
using namespace Paths::AllShortest;

BFSCheckCount::BFSCheckCount(ThreadInfo* thread_info, VarId path_var, Id start, Id end, RPQ_DFA automaton) :
    thread_info(thread_info), path_var(path_var), start(start), end(end), automaton(automaton) { }


void BFSCheckCount::begin(BindingId& _parent_binding) {
    parent_binding = &_parent_binding;

    // Init start object id
    ObjectId start_object_id(std::holds_alternative<ObjectId>(start) ? std::get<ObjectId>(start)
                                                                     : (*parent_binding)[std::get<VarId>(start)]);

    end_object_id =
      std::holds_alternative<ObjectId>(end) ? std::get<ObjectId>(end) : (*parent_binding)[std::get<VarId>(end)];

    // Add start_object_id to open and visited structures
    auto start_state = visited.emplace(start_object_id, automaton.start_state, 0, 1);
    open.push(start_state.first.operator->());
    first_next = true;
}


bool BFSCheckCount::next() {
    // Check if first node is final
    if (first_next) {
        first_next = false;

        auto current_state = open.front();
        auto node_iter     = quad_model.nodes->get_range(&thread_info->interruption_requested,
                                                     Record<1>({ current_state->node_id.id }),
                                                     Record<1>({ current_state->node_id.id }));
        if (node_iter->next() == nullptr) {
            // return false if node does not exists in bd
            open.pop();
            return false;
        }
    }

    while (open.size() > 0) {
        auto current_state = open.front();

        explore_neighbors(current_state);

        if (automaton.is_final_state[current_state->automaton_state]) {
            parent_binding->add(path_var, ObjectId(ObjectId::MASK_POSITIVE_INT | current_state->count));
            open.pop();

            // Empty queue
            queue<const SearchStateCount*> empty;
            open.swap(empty);

            return true;
        } else {
            open.pop();
        }
    }
    return false;
}


void BFSCheckCount::explore_neighbors(const SearchStateCount* current_state) {
    for (size_t current_transition = 0;
         current_transition < automaton.from_to_connections[current_state->automaton_state].size();
         current_transition++)
    {
        auto& transition = automaton.from_to_connections[current_state->automaton_state][current_transition];
        auto iter = get_iter(current_state, transition);

        for (auto child_record = iter->next(); child_record != nullptr; child_record = iter->next()) {
            SearchStateCount next_state(ObjectId(child_record->ids[2]),
                                        transition.to,
                                        current_state->distance + 1,
                                        current_state->count);

            auto visited_search = visited.find(next_state);
            if (visited_search != visited.end()) {
                if (visited_search->distance == next_state.distance) {
                    visited_search->count += current_state->count;
                }
            } else {
                auto new_visited_state = visited.emplace(ObjectId(child_record->ids[2]),
                                                         transition.to,
                                                         current_state->distance + 1,
                                                         current_state->count).first;
                open.push(new_visited_state.operator->());
            }
        }
    }
}

std::unique_ptr<BptIter<4>> BFSCheckCount::get_iter(const SearchStateCount* current_state, const RPQ_DFA::Transition& transition) {
    std::array<uint64_t, 4> min_ids;
    std::array<uint64_t, 4> max_ids;
    min_ids[2] = 0;
    max_ids[2] = 0xFFFFFFFFFFFFFFFF;
    min_ids[3] = 0;
    max_ids[3] = 0xFFFFFFFFFFFFFFFF;

    bpt_searches++;
    if (transition.inverse) {
        min_ids[0] = current_state->node_id.id;
        max_ids[0] = current_state->node_id.id;
        min_ids[1] = transition.type_id.id;
        max_ids[1] = transition.type_id.id;
        return quad_model.to_type_from_edge->get_range(&thread_info->interruption_requested,
                                                       Record<4>(min_ids),
                                                       Record<4>(max_ids));
    } else {
        min_ids[0] = transition.type_id.id;
        max_ids[0] = transition.type_id.id;
        min_ids[1] = current_state->node_id.id;
        max_ids[1] = current_state->node_id.id;
        return quad_model.type_from_to_edge->get_range(&thread_info->interruption_requested,
                                                       Record<4>(min_ids),
                                                       Record<4>(max_ids));
    }
}


void BFSCheckCount::reset() {
    // Empty open and visited
    queue<const SearchStateCount*> empty;
    open.swap(empty);
    visited.clear();
    first_next = true;

    // Add start object id to open and visited
    ObjectId start_object_id(std::holds_alternative<ObjectId>(start) ? std::get<ObjectId>(start)
                                                                     : (*parent_binding)[std::get<VarId>(start)]);

    auto state_inserted = visited.emplace(start_object_id, automaton.start_state, 0, 1);

    open.push(state_inserted.first.operator->());
}


void BFSCheckCount::analyze(std::ostream& os, int indent) const {
    os << std::string(indent, ' ');
    os << "Paths::AllShortest::BFSCheckCount(bpt_searches: " << bpt_searches << ", found: " << results_found << ")";
}
