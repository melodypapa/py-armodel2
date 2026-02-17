"""Address primitive type.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 107)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_PrimitiveTypes.primitives.json"""

# This is used to specify an address within the CPU. Tags: xml.xsd.customType=ADDRESS xml.xsd.pattern=0[xX][0-9a-fA-F]+ xml.xsd.type=string Table 4.40: Address
Address = str
