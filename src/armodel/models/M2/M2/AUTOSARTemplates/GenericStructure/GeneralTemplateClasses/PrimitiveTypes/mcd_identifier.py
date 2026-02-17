"""McdIdentifier primitive type.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 111)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_PrimitiveTypes.primitives.json"""

# This primitive denotes a name used for measurement and calibration systems and shall follow the restrictions for an ASAM ASAP2 ident. For detailed syntax see the xsd.pattern. The size limitations are not captured. McdIdentifiers are random names which may contain characters A through Z, a through z, underscore (_), numerals 0 through 9, points (’.’) and brackets ( ’[’,’]’ ). However, the following limitations apply: the first character shall be a letter or an underscore, brackets shall occur in pairs at the end of a partial string and shall contain a number or an alpha-numerical string (description of the index of an array element). Tags: xml.xsd.customType=MCD-IDENTIFIER xml.xsd.pattern=[a-zA-Z_][a-zA-Z0-9_]*(\[([a-zA-Z_][a-zA-Z0-9_]*|[0-9]+)\])*(\.[a-zA-Z_][a-z A-Z0-9_]*(\[([a-zA-Z_][a-zA-Z0-9_]*|[0-9]+)\])*)* xml.xsd.type=string Table 4.54: McdIdentifier
McdIdentifier = str
