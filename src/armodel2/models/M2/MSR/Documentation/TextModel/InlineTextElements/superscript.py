"""Superscript AUTOSAR primitive type.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 318)

JSON Source: packages/M2_MSR_Documentation_TextModel_InlineTextElements.primitives.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_primitive import ARPrimitive

# This is text which is rendered superscript or subscript depending on the role. Tags: xml.xsd.customType=SUPSCRIPT xml.xsd.type=string Table 9.38: Superscript
class Superscript(ARPrimitive):
    """AUTOSAR Superscript primitive type.

    Inherits deserialize() from ARPrimitive which automatically converts
    XML text content to the appropriate Python type based on python_type.
    """

    python_type: type = str
    """The underlying Python type for this primitive."""

    def __init__(self, value: Optional[str] = None) -> None:
        """Initialize Superscript.

        Args:
            value: The primitive value
        """
        super().__init__()
        self.value: Optional[str] = value
