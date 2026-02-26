"""CIdentifierWithIndex AUTOSAR primitive type.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 108)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_PrimitiveTypes.primitives.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_primitive import ARPrimitive

# This datatype represents a string, that follows the rules of C-identifiers with an index. Tags: xml.xsd.customType=C-IDENTIFIER-WITH-INDEX xml.xsd.pattern=[a-zA-Z_][a-zA-Z0-9_]*\[[0-9]+\] xml.xsd.type=string Table 4.46: CIdentifierWithIndex 108 of 535 Document ID 202: AUTOSAR_FO_TPS_GenericStructureTemplate Generic Structure Template AUTOSAR FO R23-11
class CIdentifierWithIndex(ARPrimitive):
    """AUTOSAR CIdentifierWithIndex primitive type.

    Inherits deserialize() from ARPrimitive which automatically converts
    XML text content to the appropriate Python type based on python_type.
    """

    python_type: type = str
    """The underlying Python type for this primitive."""

    def __init__(self, value: Optional[str] = None) -> None:
        """Initialize CIdentifierWithIndex.

        Args:
            value: The primitive value
        """
        super().__init__()
        self.value: Optional[str] = value
