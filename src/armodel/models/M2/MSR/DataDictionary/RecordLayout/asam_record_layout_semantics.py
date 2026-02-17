"""AsamRecordLayoutSemantics primitive type.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 427)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 107)

JSON Source: packages/M2_MSR_DataDictionary_RecordLayout.primitives.json"""

# This meta-class is used to denote the semantics in particular in terms of the corresponding A2L-Keyword. This is to support the mapping of the more general record layouts in AUTOSAR/MSR to the specific A2L keywords. It is possible to express the specific semantics of A2l RecordLayout keywords in SwRecordlayoutGroup but not always vice versa. Therefore the mapping is provided in this optional attribute. It is specified as NMTOKEN to reduce the direct dependency of ASAM an AUTOSAR standards. Tags: xml.xsd.customType=ASAM-RECORD-LAYOUT-SEMANTICS xml.xsd.type=NMTOKEN Table 5.103: AsamRecordLayoutSemantics The values of SwRecordLayoutGroup.category can, for example, be taken from the ASAM MCD 2D specification provided in [15]. Examples are: • INDEX_INCR • INDEX_DECR • COLUMN_DIR • ROW_DIR • ALTERNATE_WITH_X • ALTERNATE_WITH_Y • ALTERNATE_CURVES
AsamRecordLayoutSemantics = str
