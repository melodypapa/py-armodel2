"""DdsResourceLimits AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 537)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DdsResourceLimits(ARObject):
    """AUTOSAR DdsResourceLimits."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DDS-RESOURCE-LIMITS"


    max_instances: Optional[PositiveInteger]
    max_samples: Optional[PositiveInteger]
    max_samples_per_instance: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "MAX-INSTANCES": lambda obj, elem: setattr(obj, "max_instances", elem.text),
        "MAX-SAMPLES": lambda obj, elem: setattr(obj, "max_samples", elem.text),
        "MAX-SAMPLES-PER-INSTANCE": lambda obj, elem: setattr(obj, "max_samples_per_instance", elem.text),
    }


    def __init__(self) -> None:
        """Initialize DdsResourceLimits."""
        super().__init__()
        self.max_instances: Optional[PositiveInteger] = None
        self.max_samples: Optional[PositiveInteger] = None
        self.max_samples_per_instance: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize DdsResourceLimits to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DdsResourceLimits, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize max_instances
        if self.max_instances is not None:
            serialized = SerializationHelper.serialize_item(self.max_instances, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-INSTANCES")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_samples
        if self.max_samples is not None:
            serialized = SerializationHelper.serialize_item(self.max_samples, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-SAMPLES")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_samples_per_instance
        if self.max_samples_per_instance is not None:
            serialized = SerializationHelper.serialize_item(self.max_samples_per_instance, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-SAMPLES-PER-INSTANCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsResourceLimits":
        """Deserialize XML element to DdsResourceLimits object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DdsResourceLimits object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DdsResourceLimits, cls).deserialize(element)

        # Parse max_instances
        child = SerializationHelper.find_child_element(element, "MAX-INSTANCES")
        if child is not None:
            max_instances_value = child.text
            obj.max_instances = max_instances_value

        # Parse max_samples
        child = SerializationHelper.find_child_element(element, "MAX-SAMPLES")
        if child is not None:
            max_samples_value = child.text
            obj.max_samples = max_samples_value

        # Parse max_samples_per_instance
        child = SerializationHelper.find_child_element(element, "MAX-SAMPLES-PER-INSTANCE")
        if child is not None:
            max_samples_per_instance_value = child.text
            obj.max_samples_per_instance = max_samples_per_instance_value

        return obj



class DdsResourceLimitsBuilder(BuilderBase):
    """Builder for DdsResourceLimits with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DdsResourceLimits = DdsResourceLimits()


    def with_max_instances(self, value: Optional[PositiveInteger]) -> "DdsResourceLimitsBuilder":
        """Set max_instances attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.max_instances = value
        return self

    def with_max_samples(self, value: Optional[PositiveInteger]) -> "DdsResourceLimitsBuilder":
        """Set max_samples attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.max_samples = value
        return self

    def with_max_samples_per_instance(self, value: Optional[PositiveInteger]) -> "DdsResourceLimitsBuilder":
        """Set max_samples_per_instance attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.max_samples_per_instance = value
        return self




    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Get type hints for the class
        try:
            type_hints_dict = get_type_hints(type(self._obj))
        except Exception:
            # Cannot resolve type hints (e.g., forward references), skip validation
            return

        for attr_name, attr_type in type_hints_dict.items():
            if attr_name.startswith("_"):
                continue

            value = getattr(self._obj, attr_name)

            # Check required fields (not Optional)
            if value is None and not self._is_optional_type(attr_type):
                if mode == BuilderValidationMode.STRICT:
                    raise ValueError(
                        f"Required attribute '{attr_name}' is None"
                    )
                elif mode == BuilderValidationMode.LENIENT:
                    import warnings
                    warnings.warn(
                        f"Required attribute '{attr_name}' is None",
                        UserWarning
                    )

    @staticmethod
    def _is_optional_type(type_hint: Any) -> bool:
        """Check if a type hint is Optional.

        Args:
            type_hint: Type hint to check

        Returns:
            True if type is Optional, False otherwise
        """
        origin = getattr(type_hint, "__origin__", None)
        return origin is Union

    @staticmethod
    def _get_expected_type(type_hint: Any) -> type:
        """Extract expected type from type hint.

        Args:
            type_hint: Type hint to extract from

        Returns:
            Expected type
        """
        if isinstance(type_hint, str):
            return object
        origin = getattr(type_hint, "__origin__", None)
        if origin is Union:
            args = getattr(type_hint, "__args__", [])
            for arg in args:
                if arg is not type(None):
                    return arg
        elif origin is list:
            args = getattr(type_hint, "__args__", [object])
            return args[0] if args else object
        return type_hint if isinstance(type_hint, type) else object


    def build(self) -> DdsResourceLimits:
        """Build and return the DdsResourceLimits instance with validation."""
        self._validate_instance()
        pass
        return self._obj