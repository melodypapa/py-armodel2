"""IEEE1722TpRvfConnection AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.ieee1722_tp_av_connection import (
    IEEE1722TpAvConnection,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class IEEE1722TpRvfConnection(IEEE1722TpAvConnection):
    """AUTOSAR IEEE1722TpRvfConnection."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("rvf_active_pixels", None, True, False, None),  # rvfActivePixels
        ("rvf_color_space", None, False, False, IEEE1722TpRvfColorSpaceEnum),  # rvfColorSpace
        ("rvf_event_default", None, True, False, None),  # rvfEventDefault
        ("rvf_frame_rate", None, False, False, IEEE1722TpRvfFrameRateEnum),  # rvfFrameRate
        ("rvf_interlaced", None, True, False, None),  # rvfInterlaced
        ("rvf_pixel_depth", None, False, False, any (IEEE1722TpRvfPixel)),  # rvfPixelDepth
        ("rvf_pixel_format", None, False, False, any (IEEE1722TpRvfPixel)),  # rvfPixelFormat
        ("rvf_total_lines", None, True, False, None),  # rvfTotalLines
    ]

    def __init__(self) -> None:
        """Initialize IEEE1722TpRvfConnection."""
        super().__init__()
        self.rvf_active_pixels: Optional[PositiveInteger] = None
        self.rvf_color_space: Optional[IEEE1722TpRvfColorSpaceEnum] = None
        self.rvf_event_default: Optional[PositiveInteger] = None
        self.rvf_frame_rate: Optional[IEEE1722TpRvfFrameRateEnum] = None
        self.rvf_interlaced: Optional[Boolean] = None
        self.rvf_pixel_depth: Optional[Any] = None
        self.rvf_pixel_format: Optional[Any] = None
        self.rvf_total_lines: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert IEEE1722TpRvfConnection to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IEEE1722TpRvfConnection":
        """Create IEEE1722TpRvfConnection from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            IEEE1722TpRvfConnection instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to IEEE1722TpRvfConnection since parent returns ARObject
        return cast("IEEE1722TpRvfConnection", obj)


class IEEE1722TpRvfConnectionBuilder:
    """Builder for IEEE1722TpRvfConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IEEE1722TpRvfConnection = IEEE1722TpRvfConnection()

    def build(self) -> IEEE1722TpRvfConnection:
        """Build and return IEEE1722TpRvfConnection object.

        Returns:
            IEEE1722TpRvfConnection instance
        """
        # TODO: Add validation
        return self._obj
