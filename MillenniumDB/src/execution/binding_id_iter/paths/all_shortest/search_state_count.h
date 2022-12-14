#pragma once

#include <memory>

#include "base/ids/object_id.h"

namespace Paths { namespace AllShortest {

struct SearchStateCount {
    const ObjectId node_id;
    const uint32_t automaton_state;
    const uint32_t distance;

    mutable uint64_t count;

    SearchStateCount(ObjectId node_id, uint32_t automaton_state, uint32_t distance, uint64_t count) :
        node_id         (node_id),
        automaton_state (automaton_state),
        distance        (distance),
        count           (count) { }

    bool operator==(const SearchStateCount& other) const {
        return automaton_state == other.automaton_state
               && node_id == other.node_id;
    }
};

}} // namespace Paths::AllShortest

// For unordered set
template<>
struct std::hash<Paths::AllShortest::SearchStateCount> {
    std::size_t operator() (const Paths::AllShortest::SearchStateCount& s) const {
        return s.automaton_state ^ s.node_id.id;
    }
};

