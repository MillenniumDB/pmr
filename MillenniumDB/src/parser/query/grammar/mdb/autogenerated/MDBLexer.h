
// Generated from MDBLexer.g4 by ANTLR 4.9.3

#pragma once


#include "antlr4-runtime.h"




class  MDBLexer : public antlr4::Lexer {
public:
  enum {
    K_ANY = 1, K_AND = 2, K_AVG = 3, K_ALL_COUNT = 4, K_ALL_FILL_VISITED = 5, 
    K_ALL = 6, K_ASC = 7, K_BY = 8, K_BOOL = 9, K_COUNT = 10, K_DESCRIBE = 11, 
    K_DESC = 12, K_DISTINCT = 13, K_EDGE = 14, K_INTEGER = 15, K_INSERT = 16, 
    K_IS = 17, K_FALSE = 18, K_FLOAT = 19, K_GROUP = 20, K_LABEL = 21, K_LIMIT = 22, 
    K_MAX = 23, K_MATCH = 24, K_MIN = 25, K_OPTIONAL = 26, K_ORDER = 27, 
    K_OR = 28, K_PROPERTY = 29, K_NOT = 30, K_NULL = 31, K_SET = 32, K_SUM = 33, 
    K_STRING = 34, K_RETURN = 35, K_TRUE = 36, K_WHERE = 37, TRUE_PROP = 38, 
    FALSE_PROP = 39, ANON_ID = 40, EDGE_ID = 41, KEY = 42, TYPE = 43, TYPE_VAR = 44, 
    VARIABLE = 45, STRING = 46, UNSIGNED_INTEGER = 47, UNSIGNED_FLOAT = 48, 
    NAME = 49, LEQ = 50, GEQ = 51, EQ = 52, NEQ = 53, LT = 54, GT = 55, 
    SINGLE_EQ = 56, PATH_SEQUENCE = 57, PATH_ALTERNATIVE = 58, PATH_NEGATION = 59, 
    STAR = 60, PERCENT = 61, QUESTION_MARK = 62, PLUS = 63, MINUS = 64, 
    L_PAR = 65, R_PAR = 66, LCURLY_BRACKET = 67, RCURLY_BRACKET = 68, LSQUARE_BRACKET = 69, 
    RSQUARE_BRACKET = 70, COMMA = 71, COLON = 72, WHITE_SPACE = 73, SINGLE_LINE_COMMENT = 74, 
    UNRECOGNIZED = 75
  };

  enum {
    WS_CHANNEL = 2
  };

  explicit MDBLexer(antlr4::CharStream *input);
  ~MDBLexer();

  virtual std::string getGrammarFileName() const override;
  virtual const std::vector<std::string>& getRuleNames() const override;

  virtual const std::vector<std::string>& getChannelNames() const override;
  virtual const std::vector<std::string>& getModeNames() const override;
  virtual const std::vector<std::string>& getTokenNames() const override; // deprecated, use vocabulary instead
  virtual antlr4::dfa::Vocabulary& getVocabulary() const override;

  virtual const std::vector<uint16_t> getSerializedATN() const override;
  virtual const antlr4::atn::ATN& getATN() const override;

private:
  static std::vector<antlr4::dfa::DFA> _decisionToDFA;
  static antlr4::atn::PredictionContextCache _sharedContextCache;
  static std::vector<std::string> _ruleNames;
  static std::vector<std::string> _tokenNames;
  static std::vector<std::string> _channelNames;
  static std::vector<std::string> _modeNames;

  static std::vector<std::string> _literalNames;
  static std::vector<std::string> _symbolicNames;
  static antlr4::dfa::Vocabulary _vocabulary;
  static antlr4::atn::ATN _atn;
  static std::vector<uint16_t> _serializedATN;


  // Individual action functions triggered by action() above.

  // Individual semantic predicate functions triggered by sempred() above.

  struct Initializer {
    Initializer();
  };
  static Initializer _init;
};

