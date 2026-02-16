"""SensorActuatorSwComponentType AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.atomic_sw_component_type import (
    AtomicSwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_description_entity import (
    HwDescriptionEntity,
)


class SensorActuatorSwComponentType(AtomicSwComponentType):
    """AUTOSAR SensorActuatorSwComponentType."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("sensor_actuator", None, False, False, HwDescriptionEntity),  # sensorActuator
    ]

    def __init__(self) -> None:
        """Initialize SensorActuatorSwComponentType."""
        super().__init__()
        self.sensor_actuator: Optional[HwDescriptionEntity] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SensorActuatorSwComponentType to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SensorActuatorSwComponentType":
        """Create SensorActuatorSwComponentType from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SensorActuatorSwComponentType instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SensorActuatorSwComponentType since parent returns ARObject
        return cast("SensorActuatorSwComponentType", obj)


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
