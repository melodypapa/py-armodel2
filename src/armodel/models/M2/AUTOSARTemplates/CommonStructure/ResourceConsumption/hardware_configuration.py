"""HardwareConfiguration AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 161)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ResourceConsumption.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class HardwareConfiguration(ARObject):
    """AUTOSAR HardwareConfiguration."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    additional: Optional[String]
    processor_mode: Optional[String]
    processor_speed: Optional[String]
    def __init__(self) -> None:
        """Initialize HardwareConfiguration."""
        super().__init__()
        self.additional: Optional[String] = None
        self.processor_mode: Optional[String] = None
        self.processor_speed: Optional[String] = None


class HardwareConfigurationBuilder:
    """Builder for HardwareConfiguration."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: HardwareConfiguration = HardwareConfiguration()

    def build(self) -> HardwareConfiguration:
        """Build and return HardwareConfiguration object.

        Returns:
            HardwareConfiguration instance
        """
        # TODO: Add validation
        return self._obj
