"""EthIpProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ipv4_props import (
    Ipv4Props,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ipv6_props import (
    Ipv6Props,
)


class EthIpProps(ARElement):
    """AUTOSAR EthIpProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("ipv4_props", None, False, False, Ipv4Props),  # ipv4Props
        ("ipv6_props", None, False, False, Ipv6Props),  # ipv6Props
    ]

    def __init__(self) -> None:
        """Initialize EthIpProps."""
        super().__init__()
        self.ipv4_props: Optional[Ipv4Props] = None
        self.ipv6_props: Optional[Ipv6Props] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EthIpProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EthIpProps":
        """Create EthIpProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EthIpProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EthIpProps since parent returns ARObject
        return cast("EthIpProps", obj)


class EthIpPropsBuilder:
    """Builder for EthIpProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EthIpProps = EthIpProps()

    def build(self) -> EthIpProps:
        """Build and return EthIpProps object.

        Returns:
            EthIpProps instance
        """
        # TODO: Add validation
        return self._obj
