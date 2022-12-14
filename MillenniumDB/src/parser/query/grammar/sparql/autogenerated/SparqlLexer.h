
// Generated from SparqlLexer.g4 by ANTLR 4.9.3

#pragma once


#include "antlr4-runtime.h"




class  SparqlLexer : public antlr4::Lexer {
public:
  enum {
    WS = 1, BASE = 2, PREFIX = 3, SELECT = 4, DISTINCT = 5, REDUCED = 6, 
    CONSTRUCT = 7, DESCRIBE = 8, ASK = 9, FROM = 10, NAMED = 11, WHERE = 12, 
    ORDER = 13, BY = 14, ASC = 15, DESC = 16, LIMIT = 17, OFFSET = 18, VALUES = 19, 
    OPTIONAL = 20, GRAPH = 21, UNION = 22, FILTER = 23, A = 24, STR = 25, 
    LANG = 26, LANGMATCHES = 27, DATATYPE = 28, BOUND = 29, SAMETERM = 30, 
    ISIRI = 31, ISURI = 32, ISBLANK = 33, ISLITERAL = 34, REGEX = 35, SUBSTR = 36, 
    TRUE = 37, FALSE = 38, LOAD = 39, CLEAR = 40, DROP = 41, ADD = 42, MOVE = 43, 
    COPY = 44, CREATE = 45, DELETE = 46, INSERT = 47, USING = 48, SILENT = 49, 
    DEFAULT = 50, ALL = 51, DATA = 52, WITH = 53, INTO = 54, TO = 55, AS = 56, 
    GROUP = 57, HAVING = 58, UNDEF = 59, BINDINGS = 60, SERVICE = 61, BIND = 62, 
    MINUS = 63, IRI = 64, URI = 65, BNODE = 66, RAND = 67, ABS = 68, CEIL = 69, 
    FLOOR = 70, ROUND = 71, CONCAT = 72, STRLEN = 73, UCASE = 74, LCASE = 75, 
    ENCODE_FOR_URI = 76, CONTAINS = 77, STRSTARTS = 78, STRENDS = 79, STRBEFORE = 80, 
    STRAFTER = 81, REPLACE = 82, YEAR = 83, MONTH = 84, DAY = 85, HOURS = 86, 
    MINUTES = 87, SECONDS = 88, TIMEZONE = 89, TZ = 90, NOW = 91, UUID = 92, 
    STRUUID = 93, MD5 = 94, SHA1 = 95, SHA256 = 96, SHA384 = 97, SHA512 = 98, 
    COALESCE = 99, IF = 100, STRLANG = 101, STRDT = 102, ISNUMERIC = 103, 
    COUNT = 104, SUM = 105, MIN = 106, MAX = 107, AVG = 108, SAMPLE = 109, 
    GROUP_CONCAT = 110, NOT = 111, IN = 112, EXISTS = 113, SEPARATOR = 114, 
    IRIREF = 115, PNAME_NS = 116, PNAME_LN = 117, BLANK_NODE_LABEL = 118, 
    VAR1 = 119, VAR2 = 120, LANGTAG = 121, INTEGER = 122, DECIMAL = 123, 
    DOUBLE = 124, INTEGER_POSITIVE = 125, DECIMAL_POSITIVE = 126, DOUBLE_POSITIVE = 127, 
    INTEGER_NEGATIVE = 128, DECIMAL_NEGATIVE = 129, DOUBLE_NEGATIVE = 130, 
    STRING_LITERAL1 = 131, STRING_LITERAL2 = 132, STRING_LITERAL_LONG1 = 133, 
    STRING_LITERAL_LONG2 = 134, COMMENT = 135, REFERENCE = 136, LESS_EQUAL = 137, 
    GREATER_EQUAL = 138, NOT_EQUAL = 139, AND = 140, OR = 141, INVERSE = 142, 
    OPEN_BRACE = 143, CLOSE_BRACE = 144, OPEN_CURLY_BRACE = 145, CLOSE_CURLY_BRACE = 146, 
    OPEN_SQUARE_BRACKET = 147, CLOSE_SQUARE_BRACKET = 148, SEMICOLON = 149, 
    DOT = 150, PLUS_SIGN = 151, MINUS_SIGN = 152, ASTERISK = 153, QUESTION_MARK = 154, 
    COMMA = 155, NEGATION = 156, DIVIDE = 157, EQUAL = 158, LESS = 159, 
    GREATER = 160, PIPE = 161, ANY = 162
  };

  explicit SparqlLexer(antlr4::CharStream *input);
  ~SparqlLexer();

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

