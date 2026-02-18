"""StackUsage AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 149)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2059)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ResourceConsumption_StackUsage.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.executable_entity import (
    ExecutableEntity,
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
from abc import ABC, abstractmethod


class StackUsage(Identifiable, ABC):
    """AUTOSAR StackUsage."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    executable_entity: Optional[ExecutableEntity]
    hardware: Optional[HardwareConfiguration]
    hw_element: Optional[HwElement]
    software_context: Optional[SoftwareContext]
    def __init__(self) -> None:
        """Initialize StackUsage."""
        super().__init__()
        self.executable_entity: Optional[ExecutableEntity] = None
        self.hardware: Optional[HardwareConfiguration] = None
        self.hw_element: Optional[HwElement] = None
        self.software_context: Optional[SoftwareContext] = None


class StackUsageBuilder:
    """Builder for StackUsage."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: StackUsage = StackUsage()

    def build(self) -> StackUsage:
        """Build and return StackUsage object.

        Returns:
            StackUsage instance
        """
        # TODO: Add validation
        return self._obj
