"""IEEE1722TpRvfConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 649)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols_IEEE1722Tp_IEEE1722TpAv.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.ieee1722_tp_av_connection import (
    IEEE1722TpAvConnection,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAv import (
    IEEE1722TpRvfColorSpaceEnum,
    IEEE1722TpRvfFrameRateEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class IEEE1722TpRvfConnection(IEEE1722TpAvConnection):
    """AUTOSAR IEEE1722TpRvfConnection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    rvf_active_pixels: Optional[PositiveInteger]
    rvf_color_space: Optional[IEEE1722TpRvfColorSpaceEnum]
    rvf_event_default: Optional[PositiveInteger]
    rvf_frame_rate: Optional[IEEE1722TpRvfFrameRateEnum]
    rvf_interlaced: Optional[Boolean]
    rvf_pixel_depth: Optional[Any]
    rvf_pixel_format: Optional[Any]
    rvf_total_lines: Optional[PositiveInteger]
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "IEEE1722TpRvfConnection":
        """Deserialize XML element to IEEE1722TpRvfConnection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IEEE1722TpRvfConnection object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IEEE1722TpRvfConnection, cls).deserialize(element)

        # Parse rvf_active_pixels
        child = ARObject._find_child_element(element, "RVF-ACTIVE-PIXELS")
        if child is not None:
            rvf_active_pixels_value = child.text
            obj.rvf_active_pixels = rvf_active_pixels_value

        # Parse rvf_color_space
        child = ARObject._find_child_element(element, "RVF-COLOR-SPACE")
        if child is not None:
            rvf_color_space_value = IEEE1722TpRvfColorSpaceEnum.deserialize(child)
            obj.rvf_color_space = rvf_color_space_value

        # Parse rvf_event_default
        child = ARObject._find_child_element(element, "RVF-EVENT-DEFAULT")
        if child is not None:
            rvf_event_default_value = child.text
            obj.rvf_event_default = rvf_event_default_value

        # Parse rvf_frame_rate
        child = ARObject._find_child_element(element, "RVF-FRAME-RATE")
        if child is not None:
            rvf_frame_rate_value = IEEE1722TpRvfFrameRateEnum.deserialize(child)
            obj.rvf_frame_rate = rvf_frame_rate_value

        # Parse rvf_interlaced
        child = ARObject._find_child_element(element, "RVF-INTERLACED")
        if child is not None:
            rvf_interlaced_value = child.text
            obj.rvf_interlaced = rvf_interlaced_value

        # Parse rvf_pixel_depth
        child = ARObject._find_child_element(element, "RVF-PIXEL-DEPTH")
        if child is not None:
            rvf_pixel_depth_value = child.text
            obj.rvf_pixel_depth = rvf_pixel_depth_value

        # Parse rvf_pixel_format
        child = ARObject._find_child_element(element, "RVF-PIXEL-FORMAT")
        if child is not None:
            rvf_pixel_format_value = child.text
            obj.rvf_pixel_format = rvf_pixel_format_value

        # Parse rvf_total_lines
        child = ARObject._find_child_element(element, "RVF-TOTAL-LINES")
        if child is not None:
            rvf_total_lines_value = child.text
            obj.rvf_total_lines = rvf_total_lines_value

        return obj



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
