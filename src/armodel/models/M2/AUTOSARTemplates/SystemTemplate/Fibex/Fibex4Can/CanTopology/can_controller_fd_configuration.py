"""CanControllerFdConfiguration AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class CanControllerFdConfiguration(ARObject):
    """AUTOSAR CanControllerFdConfiguration."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "padding_value": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # paddingValue
        "prop_seg": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # propSeg
        "ssp_offset": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # sspOffset
        "sync_jump_width": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # syncJumpWidth
        "time_seg1": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # timeSeg1
        "time_seg2": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # timeSeg2
        "tx_bit_rate_switch": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # txBitRateSwitch
    }

    def __init__(self) -> None:
        """Initialize CanControllerFdConfiguration."""
        super().__init__()
        self.padding_value: Optional[PositiveInteger] = None
        self.prop_seg: Optional[PositiveInteger] = None
        self.ssp_offset: Optional[PositiveInteger] = None
        self.sync_jump_width: Optional[PositiveInteger] = None
        self.time_seg1: Optional[PositiveInteger] = None
        self.time_seg2: Optional[PositiveInteger] = None
        self.tx_bit_rate_switch: Optional[Boolean] = None


class CanControllerFdConfigurationBuilder:
    """Builder for CanControllerFdConfiguration."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanControllerFdConfiguration = CanControllerFdConfiguration()

    def build(self) -> CanControllerFdConfiguration:
        """Build and return CanControllerFdConfiguration object.

        Returns:
            CanControllerFdConfiguration instance
        """
        # TODO: Add validation
        return self._obj
