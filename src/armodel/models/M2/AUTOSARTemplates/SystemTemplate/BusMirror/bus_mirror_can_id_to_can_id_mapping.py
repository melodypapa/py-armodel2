"""BusMirrorCanIdToCanIdMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication.can_frame_triggering import (
    CanFrameTriggering,
)


class BusMirrorCanIdToCanIdMapping(ARObject):
    """AUTOSAR BusMirrorCanIdToCanIdMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("remapped_can_id", None, True, False, None),  # remappedCanId
        ("souce_can_id", None, False, False, CanFrameTriggering),  # souceCanId
    ]

    def __init__(self) -> None:
        """Initialize BusMirrorCanIdToCanIdMapping."""
        super().__init__()
        self.remapped_can_id: Optional[PositiveInteger] = None
        self.souce_can_id: Optional[CanFrameTriggering] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BusMirrorCanIdToCanIdMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BusMirrorCanIdToCanIdMapping":
        """Create BusMirrorCanIdToCanIdMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BusMirrorCanIdToCanIdMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BusMirrorCanIdToCanIdMapping since parent returns ARObject
        return cast("BusMirrorCanIdToCanIdMapping", obj)


class BusMirrorCanIdToCanIdMappingBuilder:
    """Builder for BusMirrorCanIdToCanIdMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BusMirrorCanIdToCanIdMapping = BusMirrorCanIdToCanIdMapping()

    def build(self) -> BusMirrorCanIdToCanIdMapping:
        """Build and return BusMirrorCanIdToCanIdMapping object.

        Returns:
            BusMirrorCanIdToCanIdMapping instance
        """
        # TODO: Add validation
        return self._obj
