"""SymbolString primitive type.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 114)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_PrimitiveTypes.primitives.json"""

# This meta-class has the ability to contain a string plus an additional namePattern. Please note that this meta-class has only been introduced to fix an issue with the backwards compatibility between R4.0.3 and R4.1.1 in the context of McDataInstance Tags: xml.xsd.customType=SYMBOL-STRING xml.xsd.type=string
SymbolString = str
