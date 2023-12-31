import re

TOKENS = [
    (r'\bif\b', 'IF'),
    (r'\belse\b', 'ELSE'),
    (r'\bwhile\b', 'WHILE'),
    (r'\bfor\b', 'FOR'),
    (r'\bin\b', 'IN'),
    (r'\bTrue\b', 'TRUE'),
    (r'\bFalse\b', 'FALSE'),
    (r'\bNone\b', 'NONE'),
    (r'\bdef\b', 'DEF'),
    (r'\breturn\b', 'RETURN'),
    (r'\bprint\b', 'PRINT'),
    (r'\binput\b', 'INPUT'),
    (r'\bint\b', 'INT'),
    (r'\bfloat\b', 'FLOAT'),
    (r'\bstr\b', 'STR'),
    (r'\blist\b', 'LIST'),
    (r'\btuple\b', 'TUPLE'),
    (r'\bset\b', 'SET'),
    (r'\bdict\b', 'DICT'),
    (r'\bclass\b', 'CLASS'),
    (r'\btry\b', 'TRY'),
    (r'\bexcept\b', 'EXCEPT'),
    (r'\braise\b', 'RAISE'),
    (r'\bassert\b', 'ASSERT'),
    (r'\bimport\b', 'IMPORT'),
    (r'\bfrom\b', 'FROM'),
    (r'#[^\n]*', 'COMMENT'),
    (r'\+\+', 'INCREMENT'),
    (r'--', 'DECREMENT'),
    (r'\+=', 'PLUS_EQUALS'),
    (r'-=', 'MINUS_EQUALS'),
    (r'\*=', 'TIMES_EQUALS'),
    (r'/=', 'DIVIDE_EQUALS'),
    (r'%=', 'MODULO_EQUALS'),
    (r'\*\*', 'POWER'),
    (r'\*', 'TIMES'),
    (r'/', 'DIVIDE'),
    (r'%', 'MODULO'),
    (r'\+', 'PLUS'),
    (r'-', 'MINUS'),
    (r'<=', 'LESS_THAN_OR_EQUAL'),
    (r'>=', 'GREATER_THAN_OR_EQUAL'),
    (r'<', 'LESS_THAN'),
    (r'>', 'GREATER_THAN'),
    (r'==', 'EQUALS'),
    (r'!=', 'NOT_EQUALS'),
    (r'=', 'ASSIGN'),
    (r'\(', 'LEFT_PAREN'),
    (r'\)', 'RIGHT_PAREN'),
    (r'\[', 'LEFT_BRACKET'),
    (r'\]', 'RIGHT_BRACKET'),
    (r'\{', 'LEFT_BRACE'),
    (r'\}', 'RIGHT_BRACE'),
    (r',', 'COMMA'),
    (r':', 'COLON'),
    (r';', 'SEMICOLON'),
    (r'\.', 'DOT'),
    (r'"[^"]*"', 'STRING'),
    (r"'[^']*'", 'STRING'),
    (r'\d+\.\d+', 'FLOAT'),
    (r'\d+', 'INTEGER'),
    (r'[a-zA-Z_][a-zA-Z0-9_]*', 'IDENTIFIER'),
    (r'\s+', None)
]

KEYWORDS = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR',
    'in': 'IN',
    'True': 'TRUE',
    'False': 'FALSE',
    'None': 'NONE',
    'def': 'DEF',
    'return': 'RETURN',
    'print': 'PRINT',
    'input': 'INPUT',
    'int': 'INT',
    'float': 'FLOAT',
    'str': 'STR',
    'list': 'LIST',
    'tuple': 'TUPLE',
    'set': 'SET',
    'dict': 'DICT',
    'class': 'CLASS',
    'try': 'TRY',
    'except': 'EXCEPT',
    'raise': 'RAISE',
    'assert': 'ASSERT',
    'import': 'IMPORT',
    'from': 'FROM'
}