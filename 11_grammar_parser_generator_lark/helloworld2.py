
from lark import Lark

grammar = """
start: WORD "," WORD "!"
%import common.WORD
%ignore " "
"""

parser = Lark(grammar)

