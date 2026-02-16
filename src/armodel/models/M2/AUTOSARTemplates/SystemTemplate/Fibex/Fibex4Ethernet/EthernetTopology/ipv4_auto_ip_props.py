"""Ipv4AutoIpProps AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class Ipv4AutoIpProps(ARObject):
    """AUTOSAR Ipv4AutoIpProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "tcp_ip_auto_ip_init": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # tcpIpAutoIpInit
    }

    def __init__(self) -> None:
        """Initialize Ipv4AutoIpProps."""
        super().__init__()
        self.tcp_ip_auto_ip_init: Optional[TimeValue] = None


class Ipv4AutoIpPropsBuilder:
    """Builder for Ipv4AutoIpProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Ipv4AutoIpProps = Ipv4AutoIpProps()

    def build(self) -> Ipv4AutoIpProps:
        """Build and return Ipv4AutoIpProps object.

        Returns:
            Ipv4AutoIpProps instance
        """
        # TODO: Add validation
        return self._obj
