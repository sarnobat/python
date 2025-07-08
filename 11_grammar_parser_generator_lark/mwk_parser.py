# cat ~/mwk.git/apple_notes_read_only/main_iphone.mwk.becomesempty | head -100 | python3 /Volumes/git/github/python/11_grammar_parser_generator_lark/mwk_parser.py
from lark import Lark, Transformer
import sys

grammar = """
start: unparseable snippet* unparseable 

%import common.WS_INLINE
%import common.NUMBER
%import common.NEWLINE

// we can't %ignore newlines, because we need to preserve the corpus newlines

HEADING3.1:     /=== ===/
DATESTAMP:      /[0-9]{4}-[0-9]{2}-[0-9]{2}/
WHITESPACE:     /\s+/
BODY:           /(.|\s)+/

snippet:        HEADING3 NEWLINE BODY NEWLINE DATESTAMP NEWLINE \
                                        -> parse_snippet
                | HEADING3              -> parse_ending

unparseable:    BODY -> parse_unparseable
"""

class CalcTransformer(Transformer):

    def parse_unparseable   (self, args):
        print("parse_unparseable(): "    + args[0], end="")
        return args[0]

    def parse_whitespace    (self, args):
        print("parse_whitespace(): "    + args[0], end="")
        return args[0]
        
    def parse_unhandled     (self, args):
        print("parse_unhandled(): "     + args[0])
        return args[0]

    def parse_ending        (self, args):
        print("parse_ending(): "        + args[0])
        return args[0]

    def parse_snippet        (self, args):
        print("snippet(): heading "     + args[0])
        print("snippet(): "             + args[1], end="")
        print("snippet(): "             + args[2])
        print("snippet(): "             + args[3], end="")
        print("snippet(): datestamp = " + args[4])
        return args[0]

parser =  Lark(grammar, parser="earley", lexer="dynamic_complete")

def main():
    text = sys.stdin.read().strip()

    tree = parser.parse(text)

    result = CalcTransformer().transform(tree)

if __name__ == '__main__':
    main()

