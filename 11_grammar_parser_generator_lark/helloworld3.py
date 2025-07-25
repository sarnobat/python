from lark import Lark

grammar = """
start: add_expr
     | sub_expr

add_expr: NUMBER "+" NUMBER

sub_expr: NUMBER "-" NUMBER

%import common.NUMBER
%ignore " "
"""


parser = Lark(grammar)

def main():
    print(parser.parse("1+1"))
    print(parser.parse("2-1"))
    print(parser.parse("3 - 2"))    

if __name__ == '__main__':
    main()

