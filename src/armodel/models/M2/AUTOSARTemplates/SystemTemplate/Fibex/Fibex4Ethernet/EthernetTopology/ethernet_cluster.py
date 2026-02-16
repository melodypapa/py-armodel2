"""EthernetCluster AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.mac_multicast_group import (
    MacMulticastGroup,
)


class EthernetCluster(ARObject):
    """AUTOSAR EthernetCluster."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("coupling_port", None, True, False, None),  # couplingPort
        ("mac_multicast_groups", None, False, True, MacMulticastGroup),  # macMulticastGroups
    ]

    def __init__(self) -> None:
        """Initialize EthernetCluster."""
        super().__init__()
        self.coupling_port: Optional[TimeValue] = None
        self.mac_multicast_groups: list[MacMulticastGroup] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EthernetCluster to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EthernetCluster":
        """Create EthernetCluster from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EthernetCluster instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EthernetCluster since parent returns ARObject
        return cast("EthernetCluster", obj)


class EthernetClusterBuilder:
    """Builder for EthernetCluster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EthernetCluster = EthernetCluster()

    def build(self) -> EthernetCluster:
        """Build and return EthernetCluster object.

        Returns:
            EthernetCluster instance
        """
        # TODO: Add validation
        return self._obj
