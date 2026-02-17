"""AnyServiceInstanceId primitive type.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 423)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_PrimitiveTypes.primitives.json"""

# This is a positive integer or the literal ALL (the value ANY is technically supported but deprecated) which can be denoted in decimal, octal and hexadecimal. The value is between 0 and 65535. Tags: xml.xsd.customType=ANY-SERVICE-INSTANCE-ID xml.xsd.pattern=[1-9][0-9]*|0[xX][0-9a-fA-F]+|0[0-7]*|0[bB][0-1]+|ANY|ALL xml.xsd.type=string Table E.6: AnyServiceInstanceId
AnyServiceInstanceId = str
