"""SomeipSdClientServiceInstanceConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2058)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.initial_sd_delay_config import (
    InitialSdDelayConfig,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SomeipSdClientServiceInstanceConfig(ARElement):
    """AUTOSAR SomeipSdClientServiceInstanceConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SOMEIP-SD-CLIENT-SERVICE-INSTANCE-CONFIG"


    initial_find_behavior: Optional[InitialSdDelayConfig]
    priority: Optional[PositiveInteger]
    service_find: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "INITIAL-FIND-BEHAVIOR": lambda obj, elem: setattr(obj, "initial_find_behavior", SerializationHelper.deserialize_by_tag(elem, "InitialSdDelayConfig")),
        "PRIORITY": lambda obj, elem: setattr(obj, "priority", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "SERVICE-FIND": lambda obj, elem: setattr(obj, "service_find", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize SomeipSdClientServiceInstanceConfig."""
        super().__init__()
        self.initial_find_behavior: Optional[InitialSdDelayConfig] = None
        self.priority: Optional[PositiveInteger] = None
        self.service_find: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize SomeipSdClientServiceInstanceConfig to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SomeipSdClientServiceInstanceConfig, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize initial_find_behavior
        if self.initial_find_behavior is not None:
            serialized = SerializationHelper.serialize_item(self.initial_find_behavior, "InitialSdDelayConfig")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INITIAL-FIND-BEHAVIOR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize priority
        if self.priority is not None:
            serialized = SerializationHelper.serialize_item(self.priority, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PRIORITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize service_find
        if self.service_find is not None:
            serialized = SerializationHelper.serialize_item(self.service_find, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SERVICE-FIND")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SomeipSdClientServiceInstanceConfig":
        """Deserialize XML element to SomeipSdClientServiceInstanceConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SomeipSdClientServiceInstanceConfig object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SomeipSdClientServiceInstanceConfig, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "INITIAL-FIND-BEHAVIOR":
                setattr(obj, "initial_find_behavior", SerializationHelper.deserialize_by_tag(child, "InitialSdDelayConfig"))
            elif tag == "PRIORITY":
                setattr(obj, "priority", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "SERVICE-FIND":
                setattr(obj, "service_find", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class SomeipSdClientServiceInstanceConfigBuilder(ARElementBuilder):
    """Builder for SomeipSdClientServiceInstanceConfig with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SomeipSdClientServiceInstanceConfig = SomeipSdClientServiceInstanceConfig()


    def with_initial_find_behavior(self, value: Optional[InitialSdDelayConfig]) -> "SomeipSdClientServiceInstanceConfigBuilder":
        """Set initial_find_behavior attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.initial_find_behavior = value
        return self

    def with_priority(self, value: Optional[PositiveInteger]) -> "SomeipSdClientServiceInstanceConfigBuilder":
        """Set priority attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.priority = value
        return self

    def with_service_find(self, value: Optional[PositiveInteger]) -> "SomeipSdClientServiceInstanceConfigBuilder":
        """Set service_find attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.service_find = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "initialFindBehavior",
        "priority",
        "serviceFind",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> SomeipSdClientServiceInstanceConfig:
        """Build and return the SomeipSdClientServiceInstanceConfig instance with validation."""
        self._validate_instance()
        return self._obj