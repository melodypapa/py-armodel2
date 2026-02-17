"""SectionInitializationPolicyType primitive type.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 146)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 417)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 113)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 207)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_PrimitiveTypes.primitives.json"""

# SectionInitializationPolicyType describes the intended initialization of MemorySections. The following values are standardized in AUTOSAR Methodology: • INIT: To be used for (explicitly or not explicitly) initialized variables. • CLEARED: To be used for not explicitly initialized variables. • POWER-ON-CLEARED: To be used for variables that are not explicitly initialized (cleared) during normal start-up. Instead these are cleared only after power on reset. Please note that the values are defined similar to the representation of enumeration types in the XML schema to ensure backward compatibility. Tags: xml.xsd.customType=SECTION-INITIALIZATION-POLICY-TYPE xml.xsd.type=NMTOKEN Table 8.6: SectionInitializationPolicyType
SectionInitializationPolicyType = str
