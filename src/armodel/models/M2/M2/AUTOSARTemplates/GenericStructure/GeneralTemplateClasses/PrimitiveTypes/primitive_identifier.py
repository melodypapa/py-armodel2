"""PrimitiveIdentifier primitive type."""

# This meta-class has the ability to contain a string. Please note that this meta-class has only been introduced to fix an issue with the generation of attributes on primitives in context with [TPS_XMLSPR_00024]. Tags: xml.xsd.customType=PRIMITIVE-IDENTIFIER xml.xsd.maxLength=128 xml.xsd.pattern=[a-zA-Z]([a-zA-Z0-9]|_[a-zA-Z0-9])*_? xml.xsd.type=string Table 4.58: PrimitiveIdentifier
PrimitiveIdentifier = str
