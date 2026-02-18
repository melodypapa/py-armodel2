"""CanControllerFdConfigurationRequirements AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 66)

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


class CanControllerFdConfigurationRequirements(ARObject):
    """AUTOSAR CanControllerFdConfigurationRequirements."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    max_number_of_time_quanta_per: Optional[Any]
    max_sample: Optional[Float]
    max_sync_jump: Optional[Float]
    max_trcv_delay: Optional[TimeValue]
    min_number_of_time_quanta_per: Optional[Any]
    min_sample_point: Optional[Float]
    min_sync_jump: Optional[Float]
    min_trcv_delay: Optional[TimeValue]
    padding_value: Optional[PositiveInteger]
    tx_bit_rate_switch: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize CanControllerFdConfigurationRequirements."""
        super().__init__()
        self.max_number_of_time_quanta_per: Optional[Any] = None
        self.max_sample: Optional[Float] = None
        self.max_sync_jump: Optional[Float] = None
        self.max_trcv_delay: Optional[TimeValue] = None
        self.min_number_of_time_quanta_per: Optional[Any] = None
        self.min_sample_point: Optional[Float] = None
        self.min_sync_jump: Optional[Float] = None
        self.min_trcv_delay: Optional[TimeValue] = None
        self.padding_value: Optional[PositiveInteger] = None
        self.tx_bit_rate_switch: Optional[Boolean] = None


class CanControllerFdConfigurationRequirementsBuilder:
    """Builder for CanControllerFdConfigurationRequirements."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanControllerFdConfigurationRequirements = CanControllerFdConfigurationRequirements()

    def build(self) -> CanControllerFdConfigurationRequirements:
        """Build and return CanControllerFdConfigurationRequirements object.

        Returns:
            CanControllerFdConfigurationRequirements instance
        """
        # TODO: Add validation
        return self._obj
