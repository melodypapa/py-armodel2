"""HeapUsage AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 152)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2026)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ResourceConsumption_HeapUsage.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.hardware_configuration import (
    HardwareConfiguration,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_element import (
    HwElement,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.software_context import (
    SoftwareContext,
)


class HeapUsage(Identifiable):
    """AUTOSAR HeapUsage."""
    """Abstract base class - do not instantiate directly."""

    def __init__(self) -> None:
        """Initialize HeapUsage."""
        super().__init__()
        self.hardware: Optional[HardwareConfiguration] = None
        self.hw_element: Optional[HwElement] = None
        self.software_context: Optional[SoftwareContext] = None


class HeapUsageBuilder:
    """Builder for HeapUsage."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: HeapUsage = HeapUsage()

    def build(self) -> HeapUsage:
        """Build and return HeapUsage object.

        Returns:
            HeapUsage instance
        """
        # TODO: Add validation
        return self._obj
