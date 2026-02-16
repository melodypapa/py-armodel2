"""HwPortMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_connector import (
    CommunicationConnector,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_pin_group import (
    HwPinGroup,
)


class HwPortMapping(ARObject):
    """AUTOSAR HwPortMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("communication_connector", None, False, False, CommunicationConnector),  # communicationConnector
        ("hw_pin_group", None, False, False, HwPinGroup),  # hwPinGroup
    ]

    def __init__(self) -> None:
        """Initialize HwPortMapping."""
        super().__init__()
        self.communication_connector: Optional[CommunicationConnector] = None
        self.hw_pin_group: Optional[HwPinGroup] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert HwPortMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "HwPortMapping":
        """Create HwPortMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            HwPortMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to HwPortMapping since parent returns ARObject
        return cast("HwPortMapping", obj)


class HwPortMappingBuilder:
    """Builder for HwPortMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: HwPortMapping = HwPortMapping()

    def build(self) -> HwPortMapping:
        """Build and return HwPortMapping object.

        Returns:
            HwPortMapping instance
        """
        # TODO: Add validation
        return self._obj
