"""CIdentifier primitive type.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 291)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 108)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 43)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_PrimitiveTypes.primitives.json"""

# This datatype represents a string, that follows the rules of C-identifiers. Tags: xml.xsd.customType=C-IDENTIFIER xml.xsd.pattern=[a-zA-Z_][a-zA-Z0-9_]* xml.xsd.type=string
CIdentifier = str
