"""CategoryString primitive type.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 109)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_PrimitiveTypes.primitives.json"""

# This represents the pattern applicable to categories. It is basically the same as Identifier but has a different semantics. Therefore it is modeled as a primitive of its own. Tags: xml.xsd.customType=CATEGORY-STRING xml.xsd.pattern=[a-zA-Z][a-zA-Z0-9_]* xml.xsd.type=string Table 4.47: CategoryString
CategoryString = str
