"""String primitive type.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 336)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 1006)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2060)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 113)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_PrimitiveTypes.primitives.json"""

# This represents a String in which white-space shall be normalized before processing. For example: in order to compare two Strings: • leading and trailing white-space needs to be removed • consecutive white-space (blank, cr, lf, tab) needs to be replaced by one blank. Tags: xml.xsd.customType=STRING xml.xsd.type=string Table D.65: String 336 of 381 Document ID 89: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Basic Software Module Description Template AUTOSAR CP R23-11
String = str
