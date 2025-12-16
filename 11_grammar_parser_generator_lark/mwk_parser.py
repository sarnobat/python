# cat ~/mwk.git/apple_notes_read_only/main_iphone.mwk.becomesempty | head -100 | python3 /Volumes/git/github/python/11_grammar_parser_generator_lark/mwk_parser.py
from lark import Lark, Transformer, Token, Tree
import sys

grammar = r"""
start: unparseable snippet* unparseable 

%import common.WS_INLINE
%import common.NUMBER
%import common.NEWLINE

// we can't %ignore newlines, because we need to preserve the corpus newlines

HEADING3.1:     /===\s[^=\n]*\s*===/
HASHTAG: /#[^\n]*/ NEWLINE
DATESTAMP:      /[0-9]{4}-[0-9]{2}-[0-9]{2}/
WHITESPACE:     /\s+/
# BODY1:           /(.|\s)+?(?=(=== ===|\d{4}-\d{2}-\d{2}|\Z))/
BODY1: /(?!\d{4}-\d{2}-\d{2})(?!#)(.|\s)+?(?=(===[^\r\n]*===|\#[^\n]*\n|\d{4}-\d{2}-\d{2}|\Z))/
# BODY1: /(?!#)(?!#)(.|\s)+?(?=(===[^\r\n]*===|\#[^\n]*\n|\d{4}-\d{2}-\d{2}|\Z))/
# BODY_LINE: /(?!===)(?!\d{4}-\d{2}-\d{2})[^\n]+/


body: BODY1 -> parse_body
# body: (BODY_LINE NEWLINE*)+
hashtags:       HASHTAG*     -> parse_hashtags
snippet:        HEADING3 NEWLINE* hashtags? body? NEWLINE? DATESTAMP? NEWLINE \
                                        -> parse_snippet
                | HEADING3 NEWLINE* body? NEWLINE*         -> parse_ending

unparseable:    body? -> parse_unparseable
"""

class MwkTransformer(Transformer):

    def parse_unparseable   (self, args):
        # print("parse_unparseable(): "    + str(args[0]), end="\n")
        # return args[0]
        return args

    def parse_whitespace    (self, args):
        print("parse_whitespace(): "    + args[0], end="")
        return args[0]
        
    def parse_unhandled     (self, args):
        print("parse_unhandled(): "     + args[0])
        return args[0]

    def parse_ending        (self, args):
        print("parse_ending(): "        + args[0])
        return args[0]
    
    def HASHTAG(self, args):
        # args = [text, newline]
        # return args[0] + args[1]
        return args.value.strip()


    # def NEWLINE(self, tok: Token) -> None:
    #     return None   # remove NEWLINE entirely

    # def BODY1(self, args):
    #     print("BODY1(): " + args.value, end="")
    #     return args.value.strip()

    def parse_body(self, args :list[str]):
        # print("parse_body(): " + str(type(args)), end="")
        # args is a list of strings (BODY_LINE and NEWLINE)
        return "".join(args)

    def parse_hashtags(self, args):
        print("parse_hashtags(): "      + str(args))
        return args


    def parse_snippet        (self, args):

        for(i, a) in enumerate(args):
            print(f"args[{i}] = {a}")

        print("snippet(): heading "     + args[0])
        print("snippet(): newline "             + args[1], end="")
        print("snippet(): hashtag: "             + str(args[2]), end="\n")
        print("snippet(): body:"             + args[3], end="")
        print("snippet():   " + args[5])
        print("snippet(): datestamp = " + args[4])
        return args[0]

parser =  Lark(grammar, parser="earley", lexer="dynamic_complete")

def main():
    text = sys.stdin.read().strip()

    tree = parser.parse(text)

    result = MwkTransformer().transform(tree)

if __name__ == '__main__':
    main()

