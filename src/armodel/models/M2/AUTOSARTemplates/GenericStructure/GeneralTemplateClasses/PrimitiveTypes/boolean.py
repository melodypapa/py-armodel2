"""Boolean primitive type.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 206)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 425)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_PrimitiveTypes.primitives.json"""

# A Boolean value denotes a logical condition that is either ’true’ or ’false’. It can be one of "0", "1", "true", "false" Tags: xml.xsd.customType=BOOLEAN xml.xsd.pattern=0|1|true|false xml.xsd.type=string Table D.8: Boolean
Boolean = bool
