# Lexical
Lexical Analysis - Compiler Design Course

Prof. Najari

## Usage 
```bash
python main.py
```
The main file will take the input file's content from the specified file--in this case `input_program.py`-- and analyze it and return each token accordingly.

Ex) Let the input file be:

Input: `input_program.py`
```python
def add(x, y):
    return x + y

add_result = add(5,10)
print(add_result)

# This is a comment 
def square(x):
    return x * x

# Hey, Amir
result = square(5)
print(result)

```

Output:
``` Python
Token(DEF, def)
Token(IDENTIFIER, add)
Token(LEFT_PAREN, ()
Token(IDENTIFIER, x)
Token(COMMA, ,)
Token(IDENTIFIER, y)
Token(RIGHT_PAREN, ))
Token(COLON, :)
Token(RETURN, return)
Token(IDENTIFIER, x)
Token(PLUS, +)
Token(IDENTIFIER, y)
Token(IDENTIFIER, add_result)
Token(ASSIGN, =)
Token(IDENTIFIER, add)
Token(LEFT_PAREN, ()
Token(INTEGER, 5)
Token(COMMA, ,)
Token(INTEGER, 10)
Token(RIGHT_PAREN, ))
Token(PRINT, print)
Token(LEFT_PAREN, ()
Token(IDENTIFIER, add_result)
Token(RIGHT_PAREN, ))
Token(DEF, def)
Token(IDENTIFIER, square)
Token(LEFT_PAREN, ()
Token(IDENTIFIER, x)
Token(RIGHT_PAREN, ))
Token(COLON, :)
Token(RETURN, return)
Token(IDENTIFIER, x)
Token(TIMES, *)
Token(IDENTIFIER, x)
Token(IDENTIFIER, result)
Token(ASSIGN, =)
Token(IDENTIFIER, square)
Token(LEFT_PAREN, ()
Token(INTEGER, 5)
Token(RIGHT_PAREN, ))
Token(PRINT, print)
Token(LEFT_PAREN, ()
Token(IDENTIFIER, result)
Token(RIGHT_PAREN, ))
```
As shown in the output, the result shows that:
1. Comments were ignored
2. All the keywords have been recognized
3. Whitespaces were also ignored 
