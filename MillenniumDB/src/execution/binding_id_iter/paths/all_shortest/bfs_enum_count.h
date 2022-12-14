#pragma once

#include <array>
#include <memory>
#include <queue>

#include "base/binding/binding_id_iter.h"
#include "base/ids/id.h"
#include "base/thread/thread_info.h"
#include "execution/binding_id_iter/paths/all_shortest/search_state_count.h"
#include "parser/query/paths/automaton/rpq_automaton.h"
#include "third_party/robin_hood/robin_hood.h"

template <std::size_t N> class BptIter;

namespace Paths { namespace AllShortest {

/*
BFSEnumCount finds all reachable nodes according to the RPQ from a fixed start
node and returns the count of shortest paths between the start node and the
reached node
*/
class BFSEnumCount : public BindingIdIter {
private:
    // Attributes determined in the constructor
    ThreadInfo*   thread_info;
    VarId         path_var;
    Id            start;
    VarId         end;
    const RPQ_DFA automaton;

    // Attributes determined in begin
    BindingId* parent_binding;

    bool first_next;

    // Structs for BFS
    robin_hood::unordered_node_set<SearchStateCount> visited;

    // open stores a pointer to a SearchState stored in visited.
    std::queue<const SearchStateCount*> open;

    robin_hood::unordered_set<uint64_t> reached_final;

    // Statistics
    uint_fast32_t results_found = 0;
    uint_fast32_t bpt_searches  = 0;

    void explore_neighbors(const SearchStateCount* current_state);

    std::unique_ptr<BptIter<4>> get_iter(const SearchStateCount* current_state, const RPQ_DFA::Transition&);

public:
    BFSEnumCount(ThreadInfo* thread_info, VarId path_var, Id start, VarId end, RPQ_DFA automaton);

    void analyze(std::ostream& os, int indent = 0) const override;
    void begin(BindingId& parent_binding) override;
    void reset() override;
    void assign_nulls() override;
    bool next() override;
};
}} // namespace Paths::AllShortest
