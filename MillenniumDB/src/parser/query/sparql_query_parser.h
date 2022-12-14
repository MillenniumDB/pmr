#pragma once

#include <iostream>

#include "antlr4-runtime.h"

#include "parser/query/grammar/sparql/autogenerated/SparqlLexer.h"
#include "parser/query/grammar/sparql/autogenerated/SparqlParser.h"
#include "parser/query/grammar/sparql/query_visitor.h"
#include "parser/query/op/op.h"
#include "parser/query/op/sparql/op_visitor/check_scoped_blank_nodes.h"
#include "parser/query/op/sparql/op_visitor/check_var_names.h"
#include "parser/query/op/sparql/op_visitor/check_well_designed.h"
#include "parser/query/op/sparql/op_visitor/optimize_optional_tree.h"

namespace SPARQL {

class QueryParser {
public:
    static std::unique_ptr<Op>
      get_query_plan(const std::string& query, antlr4::ANTLRErrorListener* error_listener = nullptr) {
        antlr4::ANTLRInputStream  input(query);
        SparqlLexer               lexer(&input);
        antlr4::CommonTokenStream tokens(&lexer);
        SparqlParser              parser(&tokens);

        parser.getInterpreter<antlr4::atn::ParserATNSimulator>()->setPredictionMode(antlr4::atn::PredictionMode::SLL);

        if (error_listener != nullptr) {
            parser.removeErrorListeners();
            parser.addErrorListener(error_listener);
        }
        SparqlParser::QueryContext* tree = parser.query();
        QueryVisitor                visitor;
        visitor.visitQuery(tree);

        auto res = std::move(visitor.current_op);

        std::cout << *res << "\n";

        CheckVarNames check_var_names;
        res->accept_visitor(check_var_names);

        CheckWellDesigned check_well_designed;
        res->accept_visitor(check_well_designed);

        OptimizeOptionalTree optimize_optional_tree;
        res->accept_visitor(optimize_optional_tree);

        CheckScopedBlankNodes check_scoped_blank_nodes;
        res->accept_visitor(check_scoped_blank_nodes);

        std::cout << *res << "\n";

        return res;
    }
};
} // namespace SPARQL