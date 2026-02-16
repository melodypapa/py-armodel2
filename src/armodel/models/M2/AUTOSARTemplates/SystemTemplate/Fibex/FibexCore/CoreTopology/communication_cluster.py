"""CommunicationCluster AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveUnlimitedInteger,
    String,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import (
    PhysicalChannel,
)


class CommunicationCluster(ARObject):
    """AUTOSAR CommunicationCluster."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("baudrate", None, True, False, None),  # baudrate
        ("physical_channels", None, False, True, PhysicalChannel),  # physicalChannels
        ("protocol_name", None, True, False, None),  # protocolName
        ("protocol_version", None, True, False, None),  # protocolVersion
    ]

    def __init__(self) -> None:
        """Initialize CommunicationCluster."""
        super().__init__()
        self.baudrate: Optional[PositiveUnlimitedInteger] = None
        self.physical_channels: list[PhysicalChannel] = []
        self.protocol_name: Optional[String] = None
        self.protocol_version: Optional[String] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CommunicationCluster to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CommunicationCluster":
        """Create CommunicationCluster from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CommunicationCluster instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CommunicationCluster since parent returns ARObject
        return cast("CommunicationCluster", obj)


class CommunicationClusterBuilder:
    """Builder for CommunicationCluster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CommunicationCluster = CommunicationCluster()

    def build(self) -> CommunicationCluster:
        """Build and return CommunicationCluster object.

        Returns:
            CommunicationCluster instance
        """
        # TODO: Add validation
        return self._obj
