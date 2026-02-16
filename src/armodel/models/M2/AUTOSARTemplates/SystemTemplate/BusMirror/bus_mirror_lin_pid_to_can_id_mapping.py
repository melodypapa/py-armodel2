"""BusMirrorLinPidToCanIdMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_frame_triggering import (
    LinFrameTriggering,
)


class BusMirrorLinPidToCanIdMapping(ARObject):
    """AUTOSAR BusMirrorLinPidToCanIdMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("remapped_can_id", None, True, False, None),  # remappedCanId
        ("source_lin_pid", None, False, False, LinFrameTriggering),  # sourceLinPid
    ]

    def __init__(self) -> None:
        """Initialize BusMirrorLinPidToCanIdMapping."""
        super().__init__()
        self.remapped_can_id: Optional[PositiveInteger] = None
        self.source_lin_pid: Optional[LinFrameTriggering] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BusMirrorLinPidToCanIdMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BusMirrorLinPidToCanIdMapping":
        """Create BusMirrorLinPidToCanIdMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BusMirrorLinPidToCanIdMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BusMirrorLinPidToCanIdMapping since parent returns ARObject
        return cast("BusMirrorLinPidToCanIdMapping", obj)


class BusMirrorLinPidToCanIdMappingBuilder:
    """Builder for BusMirrorLinPidToCanIdMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BusMirrorLinPidToCanIdMapping = BusMirrorLinPidToCanIdMapping()

    def build(self) -> BusMirrorLinPidToCanIdMapping:
        """Build and return BusMirrorLinPidToCanIdMapping object.

        Returns:
            BusMirrorLinPidToCanIdMapping instance
        """
        # TODO: Add validation
        return self._obj
