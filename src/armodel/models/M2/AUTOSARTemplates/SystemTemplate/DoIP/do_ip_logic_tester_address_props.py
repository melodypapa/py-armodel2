"""DoIpLogicTesterAddressProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DoIP.abstract_do_ip_logic_address_props import (
    AbstractDoIpLogicAddressProps,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DoIP.do_ip_routing_activation import (
    DoIpRoutingActivation,
)


class DoIpLogicTesterAddressProps(AbstractDoIpLogicAddressProps):
    """AUTOSAR DoIpLogicTesterAddressProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("do_ip_testers", None, False, True, DoIpRoutingActivation),  # doIpTesters
    ]

    def __init__(self) -> None:
        """Initialize DoIpLogicTesterAddressProps."""
        super().__init__()
        self.do_ip_testers: list[DoIpRoutingActivation] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DoIpLogicTesterAddressProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DoIpLogicTesterAddressProps":
        """Create DoIpLogicTesterAddressProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DoIpLogicTesterAddressProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DoIpLogicTesterAddressProps since parent returns ARObject
        return cast("DoIpLogicTesterAddressProps", obj)


class DoIpLogicTesterAddressPropsBuilder:
    """Builder for DoIpLogicTesterAddressProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DoIpLogicTesterAddressProps = DoIpLogicTesterAddressProps()

    def build(self) -> DoIpLogicTesterAddressProps:
        """Build and return DoIpLogicTesterAddressProps object.

        Returns:
            DoIpLogicTesterAddressProps instance
        """
        # TODO: Add validation
        return self._obj
