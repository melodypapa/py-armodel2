"""CanControllerFdConfiguration AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 66)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class CanControllerFdConfiguration(ARObject):
    """AUTOSAR CanControllerFdConfiguration."""

    padding_value: Optional[PositiveInteger]
    prop_seg: Optional[PositiveInteger]
    ssp_offset: Optional[PositiveInteger]
    sync_jump_width: Optional[PositiveInteger]
    time_seg1: Optional[PositiveInteger]
    time_seg2: Optional[PositiveInteger]
    tx_bit_rate_switch: Optional[Boolean]
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
