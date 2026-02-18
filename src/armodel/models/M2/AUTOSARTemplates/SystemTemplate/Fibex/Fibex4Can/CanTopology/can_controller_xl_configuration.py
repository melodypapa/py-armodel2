"""CanControllerXlConfiguration AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 70)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class CanControllerXlConfiguration(ARObject):
    """AUTOSAR CanControllerXlConfiguration."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    error_signaling: Optional[Boolean]
    prop_seg: Optional[PositiveInteger]
    pwm_l: Optional[PositiveInteger]
    pwm_o: Optional[PositiveInteger]
    pwm_s: Optional[PositiveInteger]
    ssp_offset: Optional[PositiveInteger]
    sync_jump_width: Optional[PositiveInteger]
    time_seg1: Optional[PositiveInteger]
    time_seg2: Optional[PositiveInteger]
    trcv_pwm_mode: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize CanControllerXlConfiguration."""
        super().__init__()
        self.error_signaling: Optional[Boolean] = None
        self.prop_seg: Optional[PositiveInteger] = None
        self.pwm_l: Optional[PositiveInteger] = None
        self.pwm_o: Optional[PositiveInteger] = None
        self.pwm_s: Optional[PositiveInteger] = None
        self.ssp_offset: Optional[PositiveInteger] = None
        self.sync_jump_width: Optional[PositiveInteger] = None
        self.time_seg1: Optional[PositiveInteger] = None
        self.time_seg2: Optional[PositiveInteger] = None
        self.trcv_pwm_mode: Optional[Boolean] = None


class CanControllerXlConfigurationBuilder:
    """Builder for CanControllerXlConfiguration."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanControllerXlConfiguration = CanControllerXlConfiguration()

    def build(self) -> CanControllerXlConfiguration:
        """Build and return CanControllerXlConfiguration object.

        Returns:
            CanControllerXlConfiguration instance
        """
        # TODO: Add validation
        return self._obj
