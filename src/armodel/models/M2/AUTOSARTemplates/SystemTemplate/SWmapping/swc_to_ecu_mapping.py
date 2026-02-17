"""SwcToEcuMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 197)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SWmapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_element import (
    HwElement,
)


class SwcToEcuMapping(Identifiable):
    """AUTOSAR SwcToEcuMapping."""

    components: list[Any]
    controlled_hw: Optional[HwElement]
    ecu_instance: Optional[EcuInstance]
    processing_unit: Optional[HwElement]
    def __init__(self) -> None:
        """Initialize SwcToEcuMapping."""
        super().__init__()
        self.components: list[Any] = []
        self.controlled_hw: Optional[HwElement] = None
        self.ecu_instance: Optional[EcuInstance] = None
        self.processing_unit: Optional[HwElement] = None


class SwcToEcuMappingBuilder:
    """Builder for SwcToEcuMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwcToEcuMapping = SwcToEcuMapping()

    def build(self) -> SwcToEcuMapping:
        """Build and return SwcToEcuMapping object.

        Returns:
            SwcToEcuMapping instance
        """
        # TODO: Add validation
        return self._obj
