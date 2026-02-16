"""Frame AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_to_frame_mapping import (
    PduToFrameMapping,
)


class Frame(FibexElement):
    """AUTOSAR Frame."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("frame_length", None, True, False, None),  # frameLength
        ("pdu_to_frames", None, False, True, PduToFrameMapping),  # pduToFrames
    ]

    def __init__(self) -> None:
        """Initialize Frame."""
        super().__init__()
        self.frame_length: Optional[Integer] = None
        self.pdu_to_frames: list[PduToFrameMapping] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert Frame to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Frame":
        """Create Frame from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            Frame instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to Frame since parent returns ARObject
        return cast("Frame", obj)


class FrameBuilder:
    """Builder for Frame."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Frame = Frame()

    def build(self) -> Frame:
        """Build and return Frame object.

        Returns:
            Frame instance
        """
        # TODO: Add validation
        return self._obj
