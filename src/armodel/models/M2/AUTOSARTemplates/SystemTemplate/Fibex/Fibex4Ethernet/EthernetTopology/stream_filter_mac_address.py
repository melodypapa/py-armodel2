"""StreamFilterMACAddress AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 137)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    MacAddressString,
)


class StreamFilterMACAddress(ARObject):
    """AUTOSAR StreamFilterMACAddress."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    mac_address_string: Optional[MacAddressString]
    def __init__(self) -> None:
        """Initialize StreamFilterMACAddress."""
        super().__init__()
        self.mac_address_string: Optional[MacAddressString] = None


class StreamFilterMACAddressBuilder:
    """Builder for StreamFilterMACAddress."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: StreamFilterMACAddress = StreamFilterMACAddress()

    def build(self) -> StreamFilterMACAddress:
        """Build and return StreamFilterMACAddress object.

        Returns:
            StreamFilterMACAddress instance
        """
        # TODO: Add validation
        return self._obj
