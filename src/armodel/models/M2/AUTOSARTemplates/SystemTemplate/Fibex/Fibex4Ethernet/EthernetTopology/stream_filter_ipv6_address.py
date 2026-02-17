"""StreamFilterIpv6Address AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 138)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Ip6AddressString,
)


class StreamFilterIpv6Address(ARObject):
    """AUTOSAR StreamFilterIpv6Address."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "ipv6_address": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # ipv6Address
    }

    def __init__(self) -> None:
        """Initialize StreamFilterIpv6Address."""
        super().__init__()
        self.ipv6_address: Optional[Ip6AddressString] = None


class StreamFilterIpv6AddressBuilder:
    """Builder for StreamFilterIpv6Address."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: StreamFilterIpv6Address = StreamFilterIpv6Address()

    def build(self) -> StreamFilterIpv6Address:
        """Build and return StreamFilterIpv6Address object.

        Returns:
            StreamFilterIpv6Address instance
        """
        # TODO: Add validation
        return self._obj
