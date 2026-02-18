"""AsamRecordLayoutSemantics AUTOSAR primitive type.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 427)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 107)

JSON Source: packages/M2_MSR_DataDictionary_RecordLayout.primitives.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_primitive import ARPrimitive

# This meta-class is used to denote the semantics in particular in terms of the corresponding A2L-Keyword. This is to support the mapping of the more general record layouts in AUTOSAR/MSR to the specific A2L keywords. It is possible to express the specific semantics of A2l RecordLayout keywords in SwRecordlayoutGroup but not always vice versa. Therefore the mapping is provided in this optional attribute. It is specified as NMTOKEN to reduce the direct dependency of ASAM an AUTOSAR standards. Tags: xml.xsd.customType=ASAM-RECORD-LAYOUT-SEMANTICS xml.xsd.type=NMTOKEN Table 5.103: AsamRecordLayoutSemantics The values of SwRecordLayoutGroup.category can, for example, be taken from the ASAM MCD 2D specification provided in [15]. Examples are: • INDEX_INCR • INDEX_DECR • COLUMN_DIR • ROW_DIR • ALTERNATE_WITH_X • ALTERNATE_WITH_Y • ALTERNATE_CURVES
class AsamRecordLayoutSemantics(ARPrimitive):
    """AUTOSAR AsamRecordLayoutSemantics primitive type.

    Inherits deserialize() from ARPrimitive which automatically converts
    XML text content to the appropriate Python type based on python_type.
    """

    python_type: type = str
    """The underlying Python type for this primitive."""

    def __init__(self, value: Optional[str] = None) -> None:
        """Initialize AsamRecordLayoutSemantics.

        Args:
            value: The primitive value
        """
        super().__init__()
        self.value: Optional[str] = value
