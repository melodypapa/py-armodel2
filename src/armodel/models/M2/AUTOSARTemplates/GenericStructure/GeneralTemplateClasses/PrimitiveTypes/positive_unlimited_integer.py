"""PositiveUnlimitedInteger primitive type.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 459)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_PrimitiveTypes.primitives.json"""

# This is a positive unlimited integer which can be denoted in decimal, binary, octal and hexadecimal. Tags: xml.xsd.customType=POSITIVE-UNLIMITED-INTEGER xml.xsd.pattern=0|[\+]?[1-9][0-9]*|0[xX][0-9a-fA-F]+|0[bB][0-1]+|0[0-7]+ xml.xsd.type=string Table E.65: PositiveUnlimitedInteger
PositiveUnlimitedInteger = str
