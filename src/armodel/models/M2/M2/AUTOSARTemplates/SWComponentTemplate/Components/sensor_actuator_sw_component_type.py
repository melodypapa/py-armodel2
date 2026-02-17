"""SensorActuatorSwComponentType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 646)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2055)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 244)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.atomic_sw_component_type import (
    AtomicSwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_description_entity import (
    HwDescriptionEntity,
)


class SensorActuatorSwComponentType(AtomicSwComponentType):
    """AUTOSAR SensorActuatorSwComponentType."""

    def __init__(self) -> None:
        """Initialize SensorActuatorSwComponentType."""
        super().__init__()
        self.sensor_actuator: Optional[HwDescriptionEntity] = None


class SensorActuatorSwComponentTypeBuilder:
    """Builder for SensorActuatorSwComponentType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SensorActuatorSwComponentType = SensorActuatorSwComponentType()

    def build(self) -> SensorActuatorSwComponentType:
        """Build and return SensorActuatorSwComponentType object.

        Returns:
            SensorActuatorSwComponentType instance
        """
        # TODO: Add validation
        return self._obj
