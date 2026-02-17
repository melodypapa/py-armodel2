"""ECUMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 182)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_ECUResourceMapping.classes.json"""

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
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.ECUResourceMapping.hw_port_mapping import (
    HwPortMapping,
)


class ECUMapping(Identifiable):
    """AUTOSAR ECUMapping."""

    comm_controllers: list[Any]
    ecu: Optional[HwElement]
    ecu_instance: Optional[EcuInstance]
    hw_port_mapping: HwPortMapping
    def __init__(self) -> None:
        """Initialize ECUMapping."""
        super().__init__()
        self.comm_controllers: list[Any] = []
        self.ecu: Optional[HwElement] = None
        self.ecu_instance: Optional[EcuInstance] = None
        self.hw_port_mapping: HwPortMapping = None


class ECUMappingBuilder:
    """Builder for ECUMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ECUMapping = ECUMapping()

    def build(self) -> ECUMapping:
        """Build and return ECUMapping object.

        Returns:
            ECUMapping instance
        """
        # TODO: Add validation
        return self._obj
