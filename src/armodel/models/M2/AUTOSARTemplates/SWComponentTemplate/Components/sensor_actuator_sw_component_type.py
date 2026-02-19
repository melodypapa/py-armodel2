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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_description_entity import (
    HwDescriptionEntity,
)


class SensorActuatorSwComponentType(AtomicSwComponentType):
    """AUTOSAR SensorActuatorSwComponentType."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    sensor_actuator: Optional[HwDescriptionEntity]
    def __init__(self) -> None:
        """Initialize SensorActuatorSwComponentType."""
        super().__init__()
        self.sensor_actuator: Optional[HwDescriptionEntity] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SensorActuatorSwComponentType":
        """Deserialize XML element to SensorActuatorSwComponentType object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SensorActuatorSwComponentType object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse sensor_actuator
        child = ARObject._find_child_element(element, "SENSOR-ACTUATOR")
        if child is not None:
            sensor_actuator_value = ARObject._deserialize_by_tag(child, "HwDescriptionEntity")
            obj.sensor_actuator = sensor_actuator_value

        return obj



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
