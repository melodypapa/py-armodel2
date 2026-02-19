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
    def serialize(self) -> ET.Element:
        """Serialize IEEE1722TpRvfConnection to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IEEE1722TpRvfConnection, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize rvf_active_pixels
        if self.rvf_active_pixels is not None:
            serialized = ARObject._serialize_item(self.rvf_active_pixels, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RVF-ACTIVE-PIXELS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rvf_color_space
        if self.rvf_color_space is not None:
            serialized = ARObject._serialize_item(self.rvf_color_space, "IEEE1722TpRvfColorSpaceEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RVF-COLOR-SPACE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rvf_event_default
        if self.rvf_event_default is not None:
            serialized = ARObject._serialize_item(self.rvf_event_default, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RVF-EVENT-DEFAULT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rvf_frame_rate
        if self.rvf_frame_rate is not None:
            serialized = ARObject._serialize_item(self.rvf_frame_rate, "IEEE1722TpRvfFrameRateEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RVF-FRAME-RATE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rvf_interlaced
        if self.rvf_interlaced is not None:
            serialized = ARObject._serialize_item(self.rvf_interlaced, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RVF-INTERLACED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rvf_pixel_depth
        if self.rvf_pixel_depth is not None:
            serialized = ARObject._serialize_item(self.rvf_pixel_depth, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RVF-PIXEL-DEPTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rvf_pixel_format
        if self.rvf_pixel_format is not None:
            serialized = ARObject._serialize_item(self.rvf_pixel_format, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RVF-PIXEL-FORMAT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rvf_total_lines
        if self.rvf_total_lines is not None:
            serialized = ARObject._serialize_item(self.rvf_total_lines, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RVF-TOTAL-LINES")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

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
