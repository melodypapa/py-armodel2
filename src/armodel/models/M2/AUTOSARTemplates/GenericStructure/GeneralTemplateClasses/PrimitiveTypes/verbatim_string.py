"""VerbatimString primitive type.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 316)
  - AUTOSAR_FO_TPS_ARXMLSerializationRules.pdf (page 32)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 114)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_PrimitiveTypes.primitives.json"""

# This primitive represents a string in which white-space needs to be preserved. Tags: xml.xsd.customType=VERBATIM-STRING xml.xsd.type=string xml.xsd.whiteSpace=preserve
VerbatimString = str
