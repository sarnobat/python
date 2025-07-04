from lark import Lark, Transformer, Tree

gedcom_grammar = r"""
start: record+

record: level xref? tag value? subrecord*

subrecord: record

level: INT
xref: "@" /[^@]+/ "@"
tag: WORD
value: /[^\n\r]+/

%import common.INT
%import common.WORD
%import common.WS_INLINE
%ignore WS_INLINE
%ignore /\r?\n/
"""

parser = Lark(gedcom_grammar, start='start')

gedcom_text = """
0 @I1@ INDI
1 NAME John /Doe/
1 BIRT
2 DATE 1 JAN 1990
"""

tree = parser.parse(gedcom_text)
print(tree.pretty())

class GEDCOMTransformer(Transformer):
    def record(self, items):
        level = items[0]
        xref = items[1] if isinstance(items[1], Tree) and items[1].data == "xref" else None
        tag = items[2] if xref else items[1]
        value = items[3] if len(items) > (3 if xref else 2) else None
        subrecords = items[(4 if xref else 3):] if len(items) > (3 if xref else 2) else []
        return {"level": int(level.children[0]), "xref": xref, "tag": tag, "value": value, "children": subrecords}

transformer = GEDCOMTransformer()
parsed = transformer.transform(tree)
print(parsed)
