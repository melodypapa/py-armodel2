"""MacAddressString primitive type.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 111)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_PrimitiveTypes.primitives.json"""

# This primitive specifies a Mac Address. Notation: FF:FF:FF:FF:FF:FF Alternative notations, e.g. using dash instead of colon, or another grouping of numbers, is not allowed. Tags: xml.xsd.customType=MAC-ADDRESS-STRING xml.xsd.pattern=([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2} xml.xsd.type=string Table 4.53: MacAddressString
MacAddressString = str
