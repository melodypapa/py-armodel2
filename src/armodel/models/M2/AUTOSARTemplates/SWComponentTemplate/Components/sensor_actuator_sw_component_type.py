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

    def serialize(self) -> ET.Element:
        """Serialize SensorActuatorSwComponentType to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SensorActuatorSwComponentType, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize sensor_actuator
        if self.sensor_actuator is not None:
            serialized = ARObject._serialize_item(self.sensor_actuator, "HwDescriptionEntity")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SENSOR-ACTUATOR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SensorActuatorSwComponentType":
        """Deserialize XML element to SensorActuatorSwComponentType object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SensorActuatorSwComponentType object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SensorActuatorSwComponentType, cls).deserialize(element)

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
