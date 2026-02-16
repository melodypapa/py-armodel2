"""FrameMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.frame_triggering import (
    FrameTriggering,
)


class FrameMapping(ARObject):
    """AUTOSAR FrameMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("introduction", None, False, False, DocumentationBlock),  # introduction
        ("source_frame", None, False, False, FrameTriggering),  # sourceFrame
        ("target_frame", None, False, False, FrameTriggering),  # targetFrame
    ]

    def __init__(self) -> None:
        """Initialize FrameMapping."""
        super().__init__()
        self.introduction: Optional[DocumentationBlock] = None
        self.source_frame: Optional[FrameTriggering] = None
        self.target_frame: Optional[FrameTriggering] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert FrameMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FrameMapping":
        """Create FrameMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            FrameMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to FrameMapping since parent returns ARObject
        return cast("FrameMapping", obj)


class FrameMappingBuilder:
    """Builder for FrameMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FrameMapping = FrameMapping()

    def build(self) -> FrameMapping:
        """Build and return FrameMapping object.

        Returns:
            FrameMapping instance
        """
        # TODO: Add validation
        return self._obj
