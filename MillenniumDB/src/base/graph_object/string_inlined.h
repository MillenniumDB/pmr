#pragma once

#include <cassert>
#include <cstring>

class StringInlined {
public:
    char id[8];

    StringInlined(const char _id[8]) : id { _id[0], _id[1], _id[2], _id[3], _id[4], _id[5], _id[6], _id[7] } {
        assert(_id[7] == '\0');
    }
};
