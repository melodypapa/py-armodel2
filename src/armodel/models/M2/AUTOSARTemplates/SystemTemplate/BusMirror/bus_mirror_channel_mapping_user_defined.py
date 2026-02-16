"""BusMirrorChannelMappingUserDefined AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.BusMirror.bus_mirror_channel_mapping import (
    BusMirrorChannelMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class BusMirrorChannelMappingUserDefined(BusMirrorChannelMapping):
    """AUTOSAR BusMirrorChannelMappingUserDefined."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("transmission", None, True, False, None),  # transmission
    ]

    def __init__(self) -> None:
        """Initialize BusMirrorChannelMappingUserDefined."""
        super().__init__()
        self.transmission: Optional[TimeValue] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BusMirrorChannelMappingUserDefined to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BusMirrorChannelMappingUserDefined":
        """Create BusMirrorChannelMappingUserDefined from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BusMirrorChannelMappingUserDefined instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BusMirrorChannelMappingUserDefined since parent returns ARObject
        return cast("BusMirrorChannelMappingUserDefined", obj)


class BusMirrorChannelMappingUserDefinedBuilder:
    """Builder for BusMirrorChannelMappingUserDefined."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BusMirrorChannelMappingUserDefined = BusMirrorChannelMappingUserDefined()

    def build(self) -> BusMirrorChannelMappingUserDefined:
        """Build and return BusMirrorChannelMappingUserDefined object.

        Returns:
            BusMirrorChannelMappingUserDefined instance
        """
        # TODO: Add validation
        return self._obj
