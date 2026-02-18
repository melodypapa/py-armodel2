"""TableSeparatorString AUTOSAR primitive type.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 337)

JSON Source: packages/M2_MSR_Documentation_BlockElements_OasisExchangeTable.primitives.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_primitive import ARPrimitive

# This represents the ability to denote a separator string within an OASIS exchange table. • 0: no line is displayed • 1: line is displayed Tags: xml.xsd.customType=TABLE-SEPARATOR-STRING xml.xsd.pattern=[0-1] xml.xsd.type=string Table 9.72: TableSeparatorString 337 of 535 Document ID 202: AUTOSAR_FO_TPS_GenericStructureTemplate Generic Structure Template AUTOSAR FO R23-11 9.3.4 Topics in Documentation [TPS_GST_00332] Topics in Documentation (cid:100)A topic (Topic1)7 is a logical unit, which subdivides a content of a chapter mainly by providing intermediate head lines.
class TableSeparatorString(ARPrimitive):
    """AUTOSAR TableSeparatorString primitive type.

    Inherits deserialize() from ARPrimitive which automatically converts
    XML text content to the appropriate Python type based on python_type.
    """

    python_type: type = str
    """The underlying Python type for this primitive."""

    def __init__(self, value: Optional[str] = None) -> None:
        """Initialize TableSeparatorString.

        Args:
            value: The primitive value
        """
        super().__init__()
        self.value: Optional[str] = value
