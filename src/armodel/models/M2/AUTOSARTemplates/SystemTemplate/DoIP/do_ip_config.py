"""DoIpConfig AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DoIP.do_ip_interface import (
    DoIpInterface,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.do_ip_logic_address import (
    DoIpLogicAddress,
)


class DoIpConfig(ARObject):
    """AUTOSAR DoIpConfig."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("doip_interfaces", None, False, True, DoIpInterface),  # doipInterfaces
        ("logic_address", None, False, False, DoIpLogicAddress),  # logicAddress
    ]

    def __init__(self) -> None:
        """Initialize DoIpConfig."""
        super().__init__()
        self.doip_interfaces: list[DoIpInterface] = []
        self.logic_address: Optional[DoIpLogicAddress] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DoIpConfig to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DoIpConfig":
        """Create DoIpConfig from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DoIpConfig instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DoIpConfig since parent returns ARObject
        return cast("DoIpConfig", obj)


class DoIpConfigBuilder:
    """Builder for DoIpConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DoIpConfig = DoIpConfig()

    def build(self) -> DoIpConfig:
        """Build and return DoIpConfig object.

        Returns:
            DoIpConfig instance
        """
        # TODO: Add validation
        return self._obj
