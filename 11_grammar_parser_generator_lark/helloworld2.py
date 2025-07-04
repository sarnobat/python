
from lark import Lark

grammar = """
start: WORD "," WORD "!"
%import common.WORD
%ignore " "
"""

parser = Lark(grammar)

def main():
    print(parser.parse("Hello, world!"))
    print(parser.parse("Adios, amigo!"))

if __name__ == '__main__':
    main()

