"""SwcImplementation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 344)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 623)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2069)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcImplementation.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Implementation.implementation import (
    Implementation,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Implementation.implementation import ImplementationBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcImplementation.per_instance_memory_size import (
    PerInstanceMemorySize,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.swc_internal_behavior import (
    SwcInternalBehavior,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SwcImplementation(Implementation):
    """AUTOSAR SwcImplementation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    behavior_ref: Optional[ARRef]
    per_instance_memory_sizes: list[PerInstanceMemorySize]
    required_rte_vendor: Optional[String]
    def __init__(self) -> None:
        """Initialize SwcImplementation."""
        super().__init__()
        self.behavior_ref: Optional[ARRef] = None
        self.per_instance_memory_sizes: list[PerInstanceMemorySize] = []
        self.required_rte_vendor: Optional[String] = None

    def serialize(self) -> ET.Element:
        """Serialize SwcImplementation to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwcImplementation, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize behavior_ref
        if self.behavior_ref is not None:
            serialized = SerializationHelper.serialize_item(self.behavior_ref, "SwcInternalBehavior")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BEHAVIOR-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize per_instance_memory_sizes (list to container "PER-INSTANCE-MEMORY-SIZES")
        if self.per_instance_memory_sizes:
            wrapper = ET.Element("PER-INSTANCE-MEMORY-SIZES")
            for item in self.per_instance_memory_sizes:
                serialized = SerializationHelper.serialize_item(item, "PerInstanceMemorySize")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize required_rte_vendor
        if self.required_rte_vendor is not None:
            serialized = SerializationHelper.serialize_item(self.required_rte_vendor, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REQUIRED-RTE-VENDOR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwcImplementation":
        """Deserialize XML element to SwcImplementation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwcImplementation object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwcImplementation, cls).deserialize(element)

        # Parse behavior_ref
        child = SerializationHelper.find_child_element(element, "BEHAVIOR-REF")
        if child is not None:
            behavior_ref_value = ARRef.deserialize(child)
            obj.behavior_ref = behavior_ref_value

        # Parse per_instance_memory_sizes (list from container "PER-INSTANCE-MEMORY-SIZES")
        obj.per_instance_memory_sizes = []
        container = SerializationHelper.find_child_element(element, "PER-INSTANCE-MEMORY-SIZES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.per_instance_memory_sizes.append(child_value)

        # Parse required_rte_vendor
        child = SerializationHelper.find_child_element(element, "REQUIRED-RTE-VENDOR")
        if child is not None:
            required_rte_vendor_value = child.text
            obj.required_rte_vendor = required_rte_vendor_value

        return obj



class SwcImplementationBuilder(ImplementationBuilder):
    """Builder for SwcImplementation with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SwcImplementation = SwcImplementation()


    def with_behavior(self, value: Optional[SwcInternalBehavior]) -> "SwcImplementationBuilder":
        """Set behavior attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.behavior = value
        return self

    def with_per_instance_memory_sizes(self, items: list[PerInstanceMemorySize]) -> "SwcImplementationBuilder":
        """Set per_instance_memory_sizes list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.per_instance_memory_sizes = list(items) if items else []
        return self

    def with_required_rte_vendor(self, value: Optional[String]) -> "SwcImplementationBuilder":
        """Set required_rte_vendor attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.required_rte_vendor = value
        return self


    def add_per_instance_memory_size(self, item: PerInstanceMemorySize) -> "SwcImplementationBuilder":
        """Add a single item to per_instance_memory_sizes list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.per_instance_memory_sizes.append(item)
        return self

    def clear_per_instance_memory_sizes(self) -> "SwcImplementationBuilder":
        """Clear all items from per_instance_memory_sizes list.

        Returns:
            self for method chaining
        """
        self._obj.per_instance_memory_sizes = []
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


    def build(self) -> SwcImplementation:
        """Build and return the SwcImplementation instance with validation."""
        self._validate_instance()
        pass
        return self._obj