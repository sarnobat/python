from lark import Lark, Transformer
import sys

grammar = """
start: d


%import common.WS_INLINE
%import common.NUMBER

%ignore " "
%ignore WS_INLINE

HEADING2:   /==/



DATESTAMP:  /[0-9]{4}-[0-9]{2}-[0-9]{2}/


snippet:    HEADING2 -> snippet

d:          DATESTAMP -> datestamp

add_expr:   NUMBER "+" NUMBER -> add_expr


"""

class CalcTransformer(Transformer):

    def snippet(self, args):
        print("snippet()")
        return args[0]

    def datestamp(self, args):
        print("datestamp()")
        return args[0]

    def add_expr(self, args):
        return int(args[0]) + int(args[1])

    def sub_expr(self, args):
        return int(args[0]) - int(args[1])


parser = Lark(grammar, parser='lalr', 
    transformer=CalcTransformer())

def main():
    text = sys.stdin.read().strip()

    tree = parser.parse(text)

if __name__ == '__main__':
    main()

