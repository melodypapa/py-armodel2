"""DiagRequirementIdString primitive type.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 754)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 109)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_PrimitiveTypes.primitives.json"""

# This string denotes an Identifier for a requirement. Tags: xml.xsd.customType=DIAG-REQUIREMENT-ID-STRING xml.xsd.pattern=[0-9a-zA-Z_\-]+ xml.xsd.type=string Table 13.16: DiagRequirementIdString
DiagRequirementIdString = str
