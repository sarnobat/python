# cat ~/mwk.git/apple_notes_read_only/main_iphone.mwk.becomesempty | head -100 | tail | python3 mwk_parser.py
from lark import Lark, Transformer
import sys

grammar = """
start: snippet+

%import common.WS_INLINE
%import common.NUMBER
%import common.NEWLINE

// we can't ignore newlines, because we need to preserve the corpus newlines

HEADING3:       /=== ===/
HEADING2:       /== /
DATESTAMP:      /[0-9]{4}-[0-9]{2}-[0-9]{2}/
WHITESPACE:     /\s+/
BODY.-1:        /(.|\s)+\s/

snippet:        HEADING3 NEWLINE BODY DATESTAMP  -> parse_snippet
                | HEADING3   -> parse_snippet
d:              DATESTAMP               -> parse_datestamp
add_expr:       NUMBER "+" NUMBER       -> add_expr
whitespace:     WHITESPACE              -> parse_whitespace

"""

class CalcTransformer(Transformer):

    def parse_whitespace(self, args):
        # print("parse_whitespace(): " + str(type(args[0])))
        print("parse_whitespace(): " + args[0], end="")
        return args[0]
        
    def parse_unhandled(self, args):
        print("parse_unhandled(): " + args[0])
        return args[0]

    def parse_snippet(self, args):
        print("snippet(): " + args[0])
        print("snippet(): " + args[1])
        print("snippet(): " + args[2])
        print("snippet(): " + args[3])
        return args[0]

    def parse_datestamp(self, args):
        print("parse_datestamp(): " + args[0])
        return args[0]

    def add_expr(self, args):
        return int(args[0]) + int(args[1])

    def sub_expr(self, args):
        return int(args[0]) - int(args[1])


parser = Lark(grammar, parser='lalr', lexer="contextual",
    transformer=CalcTransformer())

def main():
    text = sys.stdin.read().strip()

    tree = parser.parse(text)

if __name__ == '__main__':
    main()

