"""UnlimitedInteger primitive type."""

# An instance of UnlimitedInteger is an element in the set of integer numbers ( ..., -2, -1, 0, 1, 2, ...). The range is limited by constraint 2534. The value can be expressed in decimal, octal, hexadecimal and binary representation. Negative numbers can only be expressed in decimal notation. Tags: xml.xsd.customType=UNLIMITED-INTEGER xml.xsd.pattern=0|[\+\-]?[1-9][0-9]*|0[xX][0-9a-fA-F]+|0[bB][0-1]+|0[0-7]+ xml.xsd.type=string Table E.83: UnlimitedInteger
UnlimitedInteger = str
