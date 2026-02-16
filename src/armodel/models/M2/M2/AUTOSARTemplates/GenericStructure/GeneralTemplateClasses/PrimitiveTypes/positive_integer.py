"""PositiveInteger primitive type."""

# This is a positive integer which can be denoted in decimal, binary, octal and hexadecimal. The value is between 0 and 4294967295. Tags: xml.xsd.customType=POSITIVE-INTEGER xml.xsd.pattern=0|[\+]?[1-9][0-9]*|0[xX][0-9a-fA-F]+|0[bB][0-1]+|0[0-7]+ xml.xsd.type=string Table C.9: PositiveInteger
PositiveInteger = str
