"""SensorActuatorSwComponentType AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.atomic_sw_component_type import (
    AtomicSwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_description_entity import (
    HwDescriptionEntity,
)


class SensorActuatorSwComponentType(AtomicSwComponentType):
    """AUTOSAR SensorActuatorSwComponentType."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "sensor_actuator": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=HwDescriptionEntity,
        ),  # sensorActuator
    }

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
