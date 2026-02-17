"""RegularExpression primitive type.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 112)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_PrimitiveTypes.primitives.json"""

# This is a regular expression as defined in http://www.w3.org/TR/xmlschema-2 As of now it is still produced as a string in XSD. Tags: xml.xsd.customType=REGULAR-EXPRESSION xml.xsd.type=string Table 4.60: RegularExpression 112 of 535 Document ID 202: AUTOSAR_FO_TPS_GenericStructureTemplate Generic Structure Template AUTOSAR FO R23-11
RegularExpression = str
