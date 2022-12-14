#pragma once

#include <array>
#include <queue>
#include <memory>

#include "base/binding/binding_id_iter.h"
#include "base/ids/id.h"
#include "base/thread/thread_info.h"
#include "execution/binding_id_iter/paths/all_shortest/search_state.h"
#include "parser/query/paths/automaton/rpq_automaton.h"
#include "storage/index/bplus_tree/bplus_tree.h"
#include "third_party/robin_hood/robin_hood.h"

namespace Paths { namespace AllShortest {

// returns all the shortest paths between two fixed nodes
class BFSCheck : public BindingIdIter {
private:
    // Attributes determined in the constructor
    ThreadInfo*   thread_info;
    VarId         path_var;
    Id            start;
    Id            end;
    const RPQ_DFA automaton;

    // Attributes determined in begin
    BindingId* parent_binding;
    ObjectId end_object_id;
    bool is_first = true;

    // Ranges to search in BPT. They are not local variables because some positions are reused.
    std::array<uint64_t, 4> min_ids;
    std::array<uint64_t, 4> max_ids;

    // Structs for BFS
    robin_hood::unordered_node_set<SearchState> visited;

    // open stores a pointer to a SearchState stored in visited.
    std::queue<const SearchState*> open;

    // UINT64_MAX means optimal_distance is not setted yet
    uint64_t optimal_distance;

    // Stores the children of state in expansion
    std::unique_ptr<BptIter<4>> iter;

    // The index of the transition that set_iter method uses to
    // construct iter attribute.
    uint32_t current_transition = 0;

    // Statistics
    uint_fast32_t results_found = 0;
    uint_fast32_t bpt_searches  = 0;

    const SearchState* saved_state_reached = nullptr;

    bool expand_neighbors(const SearchState* current_state);

    // Constructs iter according to transition
    void set_iter(const SearchState* current_state);

public:
    BFSCheck(ThreadInfo* thread_info,
             VarId       path_var,
             Id          start,
             Id          end,
             RPQ_DFA     automaton);

    void analyze(std::ostream& os, int indent = 0) const override;

    void begin(BindingId& parent_binding) override;

    void reset() override;

    bool next() override;

    void assign_nulls() override { }
};
}} // namespace Paths::AllShortest
