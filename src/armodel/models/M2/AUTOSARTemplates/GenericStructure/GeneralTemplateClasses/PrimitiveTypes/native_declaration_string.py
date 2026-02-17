"""NativeDeclarationString primitive type.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 333)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 112)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_PrimitiveTypes.primitives.json"""

# This string contains a native data declaration of a data type in a programming language. It is basically a string, but white-space shall be preserved. Tags: xml.xsd.customType=NATIVE-DECLARATION-STRING xml.xsd.type=string xml.xsd.whiteSpace=preserve Table 5.40: NativeDeclarationString
NativeDeclarationString = str
