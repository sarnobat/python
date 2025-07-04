from lark import Lark, Transformer

grammar = """
start: add_expr
     | sub_expr

add_expr: NUMBER "+" NUMBER -> add_expr

sub_expr: NUMBER "-" NUMBER -> sub_expr

%import common.NUMBER
%ignore " "
"""

class CalcTransformer(Transformer):

    def add_expr(self, args):
        return int(args[0]) + int(args[1])

    def sub_expr(self, args):
        return int(args[0]) - int(args[1])

parser = Lark(grammar, parser='lalr', 
    transformer=CalcTransformer())

def main():
    print(parser.parse("1+1"))
    print(parser.parse("2-1"))
    print(parser.parse("3 - 2"))

if __name__ == '__main__':
    main()

