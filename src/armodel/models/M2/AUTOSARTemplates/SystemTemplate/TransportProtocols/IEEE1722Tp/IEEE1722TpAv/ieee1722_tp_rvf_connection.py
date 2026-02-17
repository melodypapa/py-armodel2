"""IEEE1722TpRvfConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 649)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols_IEEE1722Tp_IEEE1722TpAv.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "rvf_active_pixels": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # rvfActivePixels
        "rvf_color_space": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=IEEE1722TpRvfColorSpaceEnum,
        ),  # rvfColorSpace
        "rvf_event_default": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # rvfEventDefault
        "rvf_frame_rate": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=IEEE1722TpRvfFrameRateEnum,
        ),  # rvfFrameRate
        "rvf_interlaced": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # rvfInterlaced
        "rvf_pixel_depth": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (IEEE1722TpRvfPixel),
        ),  # rvfPixelDepth
        "rvf_pixel_format": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (IEEE1722TpRvfPixel),
        ),  # rvfPixelFormat
        "rvf_total_lines": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # rvfTotalLines
    }

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
