"""AnyVersionString primitive type.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 423)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_PrimitiveTypes.primitives.json"""

# Tags: xml.xsd.customType=ANY-VERSION-STRING xml.xsd.pattern=[0-9]+|ANY xml.xsd.type=string Table E.7: AnyVersionString
AnyVersionString = str
