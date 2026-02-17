"""Identifier primitive type.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 299)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 61)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 42)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_PrimitiveTypes.primitives.json"""

# An Identifier is a string with a number of constraints on its appearance, satisfying the requirements typical programming languages define for their Identifiers. This datatype represents a string, that can be used as a c-Identifier. It shall start with a letter, may consist of letters, digits and underscores. Tags: xml.xsd.customType=IDENTIFIER xml.xsd.maxLength=128 xml.xsd.pattern=[a-zA-Z][a-zA-Z0-9_]* xml.xsd.type=string
Identifier = str
