"""AlignmentType primitive type."""

# This primitive represents the alignment of objects within a memory section. The value is in number of bits or UNKNOWN (deprecated), 8 , 16, 32, 64 UNSPECIFIED, BOOLEAN, or PTR. Typical values for numbers are 8, 16, 32, 64. Tags: xml.xsd.customType=ALIGNMENT-TYPE xml.xsd.pattern=[1-9][0-9]*|0[xX][0-9a-fA-F]*|0[bB] [0-1]+|0[0-7]*|UNSPECIFIED|UNKNOWN|BOOLEAN|PTR xml.xsd.type=string Table 8.3: AlignmentType
AlignmentType = str
