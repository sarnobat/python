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
        
        idx = 1
        xref = None
        if isinstance(items[idx], Tree) and items[idx].data == "xref":
            xref = items[idx]
            idx += 1

        tag = items[idx]
        idx += 1

        # Check for value
        if idx < len(items) and isinstance(items[idx], Tree) and items[idx].data != "record":
            value = items[idx]
            idx += 1
        else:
            value = None

        # Remaining items are subrecords
        subrecords = items[idx:] if idx < len(items) else []

        return {
            "level": int(level.children[0]),
            "xref": xref.children[0] if xref else None,
            "tag": tag.children[0],
            "value": value.children[0] if value else None,
            "children": subrecords
        }

print("Parsed\n------")
transformer = GEDCOMTransformer()
parsed = transformer.transform(tree)

print(parsed)

