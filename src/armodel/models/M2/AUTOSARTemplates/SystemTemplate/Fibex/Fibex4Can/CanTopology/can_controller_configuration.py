"""CanControllerConfiguration AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology.abstract_can_communication_controller_attributes import (
    AbstractCanCommunicationControllerAttributes,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class CanControllerConfiguration(AbstractCanCommunicationControllerAttributes):
    """AUTOSAR CanControllerConfiguration."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("prop_seg", None, True, False, None),  # propSeg
        ("sync_jump_width", None, True, False, None),  # syncJumpWidth
        ("time_seg1", None, True, False, None),  # timeSeg1
        ("time_seg2", None, True, False, None),  # timeSeg2
    ]

    def __init__(self) -> None:
        """Initialize CanControllerConfiguration."""
        super().__init__()
        self.prop_seg: Optional[Integer] = None
        self.sync_jump_width: Optional[Integer] = None
        self.time_seg1: Optional[Integer] = None
        self.time_seg2: Optional[Integer] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CanControllerConfiguration to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanControllerConfiguration":
        """Create CanControllerConfiguration from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CanControllerConfiguration instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CanControllerConfiguration since parent returns ARObject
        return cast("CanControllerConfiguration", obj)


class CanControllerConfigurationBuilder:
    """Builder for CanControllerConfiguration."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanControllerConfiguration = CanControllerConfiguration()

    def build(self) -> CanControllerConfiguration:
        """Build and return CanControllerConfiguration object.

        Returns:
            CanControllerConfiguration instance
        """
        # TODO: Add validation
        return self._obj
