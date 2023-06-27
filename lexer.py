import re
from expressions import *

class Token:
    def __init__(self, token_type, value):
        self.type = token_type
        self.value = value

    def __repr__(self):
        return f'Token({self.type}, {self.value})'

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception('Invalid character')

    def advance(self):
        self.pos += 1
        if self.pos >= len(self.text):
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def peek(self):
        if self.pos + 1 >= len(self.text):
            return None
        else:
            return self.text[self.pos + 1]

    def skip_comment(self):
        while self.current_char != '\n':
            self.advance()

    def get_number(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        if self.current_char == '.':
            result += self.current_char
            self.advance()
            while self.current_char is not None and self.current_char.isdigit():
                result += self.current_char
                self.advance()
            return Token('FLOAT', float(result))
        else:
            return Token('INTEGER', int(result))

    def get_string(self):
        quote_char = self.current_char
        self.advance()
        result = ''
        while self.current_char is not None and self.current_char != quote_char:
            result += self.current_char
            self.advance()
        if self.current_char == quote_char:
            self.advance()
            return Token('STRING', quote_char + result + quote_char)
        else:
            self.error()

    def get_identifier(self):
        result = ''
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
            result += self.current_char
            self.advance()
        if result in KEYWORDS:
            return Token(KEYWORDS[result], result)
        else:
            return Token('IDENTIFIER', result)

    def get_tokens(self):
        tokens = []
        while self.current_char is not None:
            if self.current_char.isspace():
                self.advance()
            elif self.current_char == '#':
                self.skip_comment()
            elif self.current_char.isdigit():
                tokens.append(self.get_number())
            elif self.current_char in ('"', "'"):
                tokens.append(self.get_string())
            elif self.current_char.isalpha() or self.current_char == '_':
                tokens.append(self.get_identifier())
            else:
                found_match = False
                for pattern, token_type in TOKENS:
                    match = re.match(pattern, self.text[self.pos:])
                    if match:
                        found_match = True
                        value = match.group(0)
                        tokens.append(Token(token_type, value))
                        self.pos += len(value)
                        self.current_char = self.text[self.pos]
                        break
                if not found_match:
                    self.error()

        return tokens

