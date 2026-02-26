"""UriString AUTOSAR primitive type.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 114)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_PrimitiveTypes.primitives.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_primitive import ARPrimitive

# A Uniform Resource Identifier (URI), is a compact string of characters used to identify or name a resource. Tags: xml.xsd.customType=URI-STRING xml.xsd.type=string Table 4.66: UriString
class UriString(ARPrimitive):
    """AUTOSAR UriString primitive type.

    Inherits deserialize() from ARPrimitive which automatically converts
    XML text content to the appropriate Python type based on python_type.
    """

    python_type: type = str
    """The underlying Python type for this primitive."""

    def __init__(self, value: Optional[str] = None) -> None:
        """Initialize UriString.

        Args:
            value: The primitive value
        """
        super().__init__()
        self.value: Optional[str] = value
