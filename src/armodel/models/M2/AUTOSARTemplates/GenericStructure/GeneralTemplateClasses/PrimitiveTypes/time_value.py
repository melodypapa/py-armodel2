"""TimeValue primitive type.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 350)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 174)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 478)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_PrimitiveTypes.primitives.json"""

# This primitive type is taken for expressing time values. The numerical value is supposed to be interpreted in the physical unit second. Tags: xml.xsd.customType=TIME-VALUE xml.xsd.type=double Table D.76: TimeValue
TimeValue = float
