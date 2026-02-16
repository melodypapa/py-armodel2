"""CanTpChannel AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class CanTpChannel(Identifiable):
    """AUTOSAR CanTpChannel."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("channel_id", None, True, False, None),  # channelId
    ]

    def __init__(self) -> None:
        """Initialize CanTpChannel."""
        super().__init__()
        self.channel_id: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CanTpChannel to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanTpChannel":
        """Create CanTpChannel from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CanTpChannel instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CanTpChannel since parent returns ARObject
        return cast("CanTpChannel", obj)


class CanTpChannelBuilder:
    """Builder for CanTpChannel."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanTpChannel = CanTpChannel()

    def build(self) -> CanTpChannel:
        """Build and return CanTpChannel object.

        Returns:
            CanTpChannel instance
        """
        # TODO: Add validation
        return self._obj
