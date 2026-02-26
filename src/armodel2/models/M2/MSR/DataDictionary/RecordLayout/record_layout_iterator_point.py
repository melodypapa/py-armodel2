"""RecordLayoutIteratorPoint AUTOSAR primitive type.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 425)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 112)

JSON Source: packages/M2_MSR_DataDictionary_RecordLayout.primitives.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_primitive import ARPrimitive

# This meta-class denotes a start / endpoint for the iteration of a SwRecordLayoutGroup. It can be an integer or one of the keywords MAX-TEXT-SIZE|ARRAY-SIZE. Note that negative numbers are counted backwards. Therefore e.g. -1 refers to the last value. Tags: xml.xsd.customType=RECORD-LAYOUT-ITERATOR-POINT xml.xsd.pattern=-?([0-9]+|MAX-TEXT-SIZE|ARRAY-SIZE) xml.xsd.type=string Table 5.102: RecordLayoutIteratorPoint [TPS_SWCT_01489] Description of standardized values of SwRecordLayoutV. swRecordLayoutVProp (cid:100) Property Description The value of the axis for the current iterator point. This is e.g. the particular point on an input-axis, but VALUE also the particular character in a string. COUNT The amount of values of the axis. LEFTDIFF The difference to the previous axis point. RIGHTDIFF The difference to the next axis point. DIST The distance value of this axis in case of a fixed axis with distance specification. SHIFT The shift value of this axis in case of a fixed axis with shift/offset. OFFSET The offset value of this axis in case of a fixed axis with shift/offset. FILL Fill with the hex value specified as contents of swRecordLayoutVFixValue. RESERVED Position shall be ignored by MCD tools. IDENTIFIER An “identifier” is deposited at the position. FIXLEFTDIFF Difference between this and a fixed left-hand value specified in swRecordLayoutVFixValue. FIXRIGHTDIFF Difference between this and a fixed right-hand value specified in swRecordLayoutVFixValue. (cid:99)(RS_SWCT_03215) 425 of 1228 Document ID 62: AUTOSAR_CP_TPS_SoftwareComponentTemplate Software Component Template AUTOSAR CP R23-11 Figure 5.54 and Figure 5.55 illustrate most of these properties. Current point 0 VALUE LLEEFFTTDDIIFFFF RRIIGGHHTTDDIIFFFF FFIIXXLLEEFFTTDDIIFFFF FFIIXXRRIIGGHHTTDDIIFFFF 111 222 333 444 CCOOUUNNTT == 44 Figure 5.54: Values for swRecordLayoutVProp for individual axis VVaalluuee == OOFFFFSSEETT ++ nn ** 22^^SSHHIIFFTT 00 VVaalluuee == OOFFFFSSEETT ++ nn ** DDIISSTT OOFFFFSSEETT DDIISSTT DDIISSTT 22^^SSHHIIFFTT Figure 5.55: Values for swRecordLayoutVProp for fixed axis [TPS_SWCT_01296] Different approaches of ASAM MCD-2MC and AUTOSAR with respect to SwRecordLayout (cid:100)ASAM MCD-2D specification (also known as A2L, or ASAP) uses keywords in record layouts where MSR/AUTOSAR uses the more generic approach specified here. It may happen that this generic approach cannot always be safely mapped to the A2L keywords. Therefore, SwRecordLayoutGroup.category can assist the conversion to the current A2L format.(cid:99)(RS_SWCT_03215) 426 of 1228 Document ID 62: AUTOSAR_CP_TPS_SoftwareComponentTemplate Software Component Template AUTOSAR CP R23-11
class RecordLayoutIteratorPoint(ARPrimitive):
    """AUTOSAR RecordLayoutIteratorPoint primitive type.

    Inherits deserialize() from ARPrimitive which automatically converts
    XML text content to the appropriate Python type based on python_type.
    """

    python_type: type = str
    """The underlying Python type for this primitive."""

    def __init__(self, value: Optional[str] = None) -> None:
        """Initialize RecordLayoutIteratorPoint.

        Args:
            value: The primitive value
        """
        super().__init__()
        self.value: Optional[str] = value
