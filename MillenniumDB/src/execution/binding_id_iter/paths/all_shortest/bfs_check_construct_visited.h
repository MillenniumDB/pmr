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
class BFSCheckConstructVisited : public BindingIdIter {
private:
    // Attributes determined in the constructor
    ThreadInfo*   thread_info;
    VarId         path_var;
    Id            start;
    Id            end;
    const RPQ_DFA automaton;

    // Attributes determined in begin
    BindingId* parent_binding;
    ObjectId   end_object_id;
    bool       is_first; // true in the first call of next

    // Ranges to search in BPT. They are not local variables because some positions are reused.
    std::array<uint64_t, 4> min_ids;
    std::array<uint64_t, 4> max_ids;

    // Structs for BFS
    robin_hood::unordered_node_set<SearchState> visited;
    // open stores a pointer to a Paths::All::SearchState stored in visited
    // that allows to avoid use visited.find to get a pointer and
    // use the state extracted of the open directly.
    std::queue<const SearchState*> open;

    // Stores the children of state in expansion
    std::unique_ptr<BptIter<4>> iter;
    // The index of the transition that set_iter method uses to
    // construct iter attribute.
    uint32_t current_transition = 0;

    // Statistics
    uint_fast32_t results_found = 0;
    uint_fast32_t bpt_searches  = 0;

    // Constructs iter according to transition
    void set_iter(const SearchState* current_state);

    std::pair<robin_hood::unordered_node_set<SearchState>::iterator, bool>
      current_state_has_next(const SearchState* current_state);

public:
    BFSCheckConstructVisited(ThreadInfo* thread_info,
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
