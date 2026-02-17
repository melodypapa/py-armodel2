"""CanControllerXlConfigurationRequirements AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 71)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Float,
    PositiveInteger,
    TimeValue,
)


class CanControllerXlConfigurationRequirements(ARObject):
    """AUTOSAR CanControllerXlConfigurationRequirements."""

    error_signaling: Optional[Boolean]
    max_number_of_time_quanta_per: Optional[Any]
    max_pwm_l: Optional[PositiveInteger]
    max_pwm_o: Optional[PositiveInteger]
    max_pwm_s: Optional[PositiveInteger]
    max_sample: Optional[Float]
    max_sync_jump: Optional[Float]
    max_trcv_delay: Optional[TimeValue]
    min_number_of_time_quanta_per: Optional[Any]
    min_pwm_l: Optional[PositiveInteger]
    min_pwm_o: Optional[PositiveInteger]
    min_pwm_s: Optional[PositiveInteger]
    min_sample_point: Optional[Float]
    min_sync_jump: Optional[Float]
    min_trcv_delay: Optional[TimeValue]
    trcv_pwm_mode: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize CanControllerXlConfigurationRequirements."""
        super().__init__()
        self.error_signaling: Optional[Boolean] = None
        self.max_number_of_time_quanta_per: Optional[Any] = None
        self.max_pwm_l: Optional[PositiveInteger] = None
        self.max_pwm_o: Optional[PositiveInteger] = None
        self.max_pwm_s: Optional[PositiveInteger] = None
        self.max_sample: Optional[Float] = None
        self.max_sync_jump: Optional[Float] = None
        self.max_trcv_delay: Optional[TimeValue] = None
        self.min_number_of_time_quanta_per: Optional[Any] = None
        self.min_pwm_l: Optional[PositiveInteger] = None
        self.min_pwm_o: Optional[PositiveInteger] = None
        self.min_pwm_s: Optional[PositiveInteger] = None
        self.min_sample_point: Optional[Float] = None
        self.min_sync_jump: Optional[Float] = None
        self.min_trcv_delay: Optional[TimeValue] = None
        self.trcv_pwm_mode: Optional[Boolean] = None


class CanControllerXlConfigurationRequirementsBuilder:
    """Builder for CanControllerXlConfigurationRequirements."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanControllerXlConfigurationRequirements = CanControllerXlConfigurationRequirements()

    def build(self) -> CanControllerXlConfigurationRequirements:
        """Build and return CanControllerXlConfigurationRequirements object.

        Returns:
            CanControllerXlConfigurationRequirements instance
        """
        # TODO: Add validation
        return self._obj
