# Copyright (c) 2023 Amirmohammad Zarif. All rights reserved.
# Department of Engineering, WTIAU
# Compiler Design Course
# Prof. Najari

from lexer import Lexer

if __name__ == "__main__":
    f = open('input_program.py', 'r')

    _text = f.read()
    
    lexer = Lexer(str(_text))

    _tokens = lexer.get_tokens()

    for token in _tokens:
        print(token)
