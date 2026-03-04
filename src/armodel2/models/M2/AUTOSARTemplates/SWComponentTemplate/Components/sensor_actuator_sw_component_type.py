"""SensorActuatorSwComponentType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 646)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2055)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 244)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.atomic_sw_component_type import (
    AtomicSwComponentType,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.atomic_sw_component_type import AtomicSwComponentTypeBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_description_entity import (
    HwDescriptionEntity,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SensorActuatorSwComponentType(AtomicSwComponentType):
    """AUTOSAR SensorActuatorSwComponentType."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SENSOR-ACTUATOR-SW-COMPONENT-TYPE"


    sensor_actuator_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "SENSOR-ACTUATOR-REF": ("_POLYMORPHIC", "sensor_actuator_ref", ["HwElement", "HwPin", "HwPinGroup", "HwType"]),
    }


    def __init__(self) -> None:
        """Initialize SensorActuatorSwComponentType."""
        super().__init__()
        self.sensor_actuator_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize SensorActuatorSwComponentType to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SensorActuatorSwComponentType, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize sensor_actuator_ref
        if self.sensor_actuator_ref is not None:
            serialized = SerializationHelper.serialize_item(self.sensor_actuator_ref, "HwDescriptionEntity")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SENSOR-ACTUATOR-REF")
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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "SENSOR-ACTUATOR-REF":
                setattr(obj, "sensor_actuator_ref", ARRef.deserialize(child))

        return obj



class SensorActuatorSwComponentTypeBuilder(AtomicSwComponentTypeBuilder):
    """Builder for SensorActuatorSwComponentType with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SensorActuatorSwComponentType = SensorActuatorSwComponentType()


    def with_sensor_actuator(self, value: Optional[HwDescriptionEntity]) -> "SensorActuatorSwComponentTypeBuilder":
        """Set sensor_actuator attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sensor_actuator = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "sensorActuator",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> SensorActuatorSwComponentType:
        """Build and return the SensorActuatorSwComponentType instance with validation."""
        self._validate_instance()
        return self._obj