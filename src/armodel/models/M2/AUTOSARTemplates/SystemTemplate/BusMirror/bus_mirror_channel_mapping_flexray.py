"""BusMirrorChannelMappingFlexray AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.BusMirror.bus_mirror_channel_mapping import (
    BusMirrorChannelMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class BusMirrorChannelMappingFlexray(BusMirrorChannelMapping):
    """AUTOSAR BusMirrorChannelMappingFlexray."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("transmission", None, True, False, None),  # transmission
    ]

    def __init__(self) -> None:
        """Initialize BusMirrorChannelMappingFlexray."""
        super().__init__()
        self.transmission: Optional[TimeValue] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BusMirrorChannelMappingFlexray to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BusMirrorChannelMappingFlexray":
        """Create BusMirrorChannelMappingFlexray from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BusMirrorChannelMappingFlexray instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BusMirrorChannelMappingFlexray since parent returns ARObject
        return cast("BusMirrorChannelMappingFlexray", obj)


class BusMirrorChannelMappingFlexrayBuilder:
    """Builder for BusMirrorChannelMappingFlexray."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BusMirrorChannelMappingFlexray = BusMirrorChannelMappingFlexray()

    def build(self) -> BusMirrorChannelMappingFlexray:
        """Build and return BusMirrorChannelMappingFlexray object.

        Returns:
            BusMirrorChannelMappingFlexray instance
        """
        # TODO: Add validation
        return self._obj
