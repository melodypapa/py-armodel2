"""Ip4AddressString AUTOSAR primitive type.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 468)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 110)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_PrimitiveTypes.primitives.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_primitive import ARPrimitive

# This is used to specify an IP4 address. Notation: 255.255.255.255 Tags: xml.xsd.customType=IP4-ADDRESS-STRING xml.xsd.pattern=(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4] [0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)|ANY xml.xsd.type=string Table 6.142: Ip4AddressString
class Ip4AddressString(ARPrimitive):
    """AUTOSAR Ip4AddressString primitive type.

    Inherits deserialize() from ARPrimitive which automatically converts
    XML text content to the appropriate Python type based on python_type.
    """

    python_type: type = str
    """The underlying Python type for this primitive."""

    def __init__(self, value: Optional[str] = None) -> None:
        """Initialize Ip4AddressString.

        Args:
            value: The primitive value
        """
        super().__init__()
        self.value: Optional[str] = value
