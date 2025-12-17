# cat ~/mwk.git/apple_notes_read_only/main_iphone.mwk.becomesempty | head -100 | python3 /Volumes/git/github/python/11_grammar_parser_generator_lark/mwk_parser.py
from sys import stderr
import json
from lark import Lark, Transformer, Token, Tree
import sys
from typing import Dict, Any, List

grammar = r"""
start: unparseable snippet* unparseable 

%import common.WS_INLINE
%import common.NUMBER
%import common.NEWLINE

// we can't %ignore newlines, because we need to preserve the corpus newlines

HEADING3.1:     /===\s[^=\n]*\s*===/
HASHTAG.1: /#[^\n]*/ NEWLINE
DATESTAMP.1:      /[0-9]{4}-[0-9]{2}-[0-9]{2}/
WHITESPACE:     /\s+/
# BODY1:           /(.|\s)+?(?=(=== ===|\d{4}-\d{2}-\d{2}|\Z))/
BODY1.2: /(?!\d{4}-\d{2}-\d{2})(?!#)(.|\s)+?(?=(===[^\r\n]*===|\#[^\n]*\n|\d{4}-\d{2}-\d{2}|\Z))/
# BODY1: /(?!#)(?!#)(.|\s)+?(?=(===[^\r\n]*===|\#[^\n]*\n|\d{4}-\d{2}-\d{2}|\Z))/
# BODY_LINE: /(?!===)(?!\d{4}-\d{2}-\d{2})[^\n]+/


body: BODY1 -> parse_body
# body: (BODY_LINE NEWLINE*)+
hashtags:       HASHTAG*     -> parse_hashtags
snippet:        HEADING3 NEWLINE* hashtags? body? NEWLINE DATESTAMP? NEWLINE? \
                                        -> parse_snippet
                | HEADING3 NEWLINE* body? NEWLINE*         -> parse_ending

unparseable:    body? -> parse_unparseable
"""

class MwkTransformer(Transformer):

    def heading_line(self, args):
        # HEADING3 NEWLINE
        return args[0]

    def datestamp_line(self, args):
        # DATESTAMP NEWLINE
        return args[0]

    def body_line(self, args):
        # BODY_LINE NEWLINE
        return args[0]

    def parse_snippet(self, args):
        result = {}
        for a in args:
            if a:
                result.update(a)
        return result

    def parse_ending(self, args):
        # HEADING3 only
        return args[0]

    def parse_unparseable(self, args):
        return {"unparseable": "".join(s for s in args if s)}

    def start(self, args):
        return args

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
        # print("parse_ending(): "        + args[0])
        return args
    
    def HEADING3(self, args):
        # args = [text, newline]
        # return args[0] + args[1]
        return { "heading": args.value.strip()}
    
    def DATESTAMP(self, args):
        # args = [text, newline]
        # return args[0] + args[1]
        return { "datestamp" : args.value.strip()}
    
    def HASHTAG(self, args):
        # args = [text, newline]
        # return args[0] + args[1]
        return args.value.strip()


    def NEWLINE(self, tok: Token) -> None:
        return None   # remove NEWLINE entirely

    # def BODY1(self, args):
    #     print("BODY1(): " + args.value, end="")
    #     return args.value.strip()

    def parse_body(self, args :list[str]):
        # print("parse_body(): " + str(type(args)), end="")
        # args is a list of strings (BODY_LINE and NEWLINE)
        return {"body": "".join(args)}

    def parse_hashtags(self, args):
        print("parse_hashtags(): "      + str(args), file=stderr)
        return {"hashtags":args}
        # tags: List[str] = []
        # for d in args:
        #     tags.extend(d["hashtags"])
        # return {"hashtags": tags}



    def parse_snippet        (self, args1):
        args = [s for s in args1 if s and s != ""]
        d = {}
        for(i, a) in enumerate(args):
            # print(f"args[{i}] = {a}")
            d.update(args[i])

        # print("snippet(): heading "     + args[0])
        # print("snippet():  "             + args[1], end="")
        # print("snippet(): hashtag: "             + str(args[2]), end="\n")
        # print("snippet(): body:"             + args[3], end="\n")
        # print("snippet(): datestamp = " + args[4])
        # print("snippet(): " + args[5])
        # print("parse_snippet(): " + str(d))
        return d

parser =  Lark(grammar, parser="earley", lexer="dynamic_complete")

def main():
    print("Reading from stdin...\n")
    text = sys.stdin.read().strip()
    print("Parsing...\n")

    tree = parser.parse(text)
    print("\nTransforming...\n")

<<<<<<< HEAD
    result = CalcTransformer().transform(tree)
    print("\nDone.")
=======
    result :Tree = MwkTransformer().transform(tree)

    #print("Final result: " + str(result.pretty()))
    # result = MwkTransformer().transform(tree)

    json_output = json.dumps(result, indent=2, ensure_ascii=False)
    print(json_output)

>>>>>>> e38b43b4f0b6f6c9cc4843a5b458650704f5eafe

if __name__ == '__main__':
    main()

