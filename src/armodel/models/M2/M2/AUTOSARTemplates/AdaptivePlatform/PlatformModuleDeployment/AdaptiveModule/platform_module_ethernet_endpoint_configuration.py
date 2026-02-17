"""PlatformModuleEthernetEndpointConfiguration AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 65)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_AdaptivePlatform_PlatformModuleDeployment_AdaptiveModule.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Ip4AddressString,
    Ip6AddressString,
)


class PlatformModuleEthernetEndpointConfiguration(ARElement):
    """AUTOSAR PlatformModuleEthernetEndpointConfiguration."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "communication": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Any,
        ),  # communication
        "ipv4_multicast_ip": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # ipv4MulticastIp
        "ipv6_multicast_ip": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # ipv6MulticastIp
    }

    def __init__(self) -> None:
        """Initialize PlatformModuleEthernetEndpointConfiguration."""
        super().__init__()
        self.communication: Optional[Any] = None
        self.ipv4_multicast_ip: Optional[Ip4AddressString] = None
        self.ipv6_multicast_ip: Optional[Ip6AddressString] = None


class PlatformModuleEthernetEndpointConfigurationBuilder:
    """Builder for PlatformModuleEthernetEndpointConfiguration."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PlatformModuleEthernetEndpointConfiguration = PlatformModuleEthernetEndpointConfiguration()

    def build(self) -> PlatformModuleEthernetEndpointConfiguration:
        """Build and return PlatformModuleEthernetEndpointConfiguration object.

        Returns:
            PlatformModuleEthernetEndpointConfiguration instance
        """
        # TODO: Add validation
        return self._obj
