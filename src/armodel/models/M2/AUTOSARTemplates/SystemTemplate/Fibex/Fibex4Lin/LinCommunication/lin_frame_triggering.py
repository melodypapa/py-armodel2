"""LinFrameTriggering AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.frame_triggering import (
    FrameTriggering,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class LinFrameTriggering(FrameTriggering):
    """AUTOSAR LinFrameTriggering."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("identifier", None, True, False, None),  # identifier
        ("lin_checksum", None, False, False, LinChecksumType),  # linChecksum
    ]

    def __init__(self) -> None:
        """Initialize LinFrameTriggering."""
        super().__init__()
        self.identifier: Optional[Integer] = None
        self.lin_checksum: Optional[LinChecksumType] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert LinFrameTriggering to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LinFrameTriggering":
        """Create LinFrameTriggering from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            LinFrameTriggering instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to LinFrameTriggering since parent returns ARObject
        return cast("LinFrameTriggering", obj)


class LinFrameTriggeringBuilder:
    """Builder for LinFrameTriggering."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LinFrameTriggering = LinFrameTriggering()

    def build(self) -> LinFrameTriggering:
        """Build and return LinFrameTriggering object.

        Returns:
            LinFrameTriggering instance
        """
        # TODO: Add validation
        return self._obj
