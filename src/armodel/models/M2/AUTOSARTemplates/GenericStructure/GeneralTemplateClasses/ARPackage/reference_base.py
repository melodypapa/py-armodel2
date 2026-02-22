"""ReferenceBase AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 72)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_ARPackage.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Identifier,
    ReferrableSubtypesEnum,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_package import (
        ARPackage,
    )



class ReferenceBase(ARObject):
    """AUTOSAR ReferenceBase."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    short_label: Identifier
    is_default: Boolean
    is_global: Boolean
    base_is_this_package: Boolean
    package_ref: Optional[ARRef]
    global_element_refs: list[ReferrableSubtypesEnum]
    global_in_package_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize ReferenceBase."""
        super().__init__()
        self.short_label: Identifier = None
        self.is_default: Boolean = None
        self.is_global: Boolean = None
        self.base_is_this_package: Boolean = None
        self.package_ref: Optional[ARRef] = None
        self.global_element_refs: list[ReferrableSubtypesEnum] = []
        self.global_in_package_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize ReferenceBase to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ReferenceBase, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize short_label
        if self.short_label is not None:
            serialized = SerializationHelper.serialize_item(self.short_label, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHORT-LABEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize is_default
        if self.is_default is not None:
            serialized = SerializationHelper.serialize_item(self.is_default, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IS-DEFAULT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize is_global
        if self.is_global is not None:
            serialized = SerializationHelper.serialize_item(self.is_global, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IS-GLOBAL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize base_is_this_package
        if self.base_is_this_package is not None:
            serialized = SerializationHelper.serialize_item(self.base_is_this_package, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BASE-IS-THIS-PACKAGE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize package_ref
        if self.package_ref is not None:
            serialized = SerializationHelper.serialize_item(self.package_ref, "ARPackage")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PACKAGE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize global_element_refs (list to container "GLOBAL-ELEMENT-REFS")
        if self.global_element_refs:
            wrapper = ET.Element("GLOBAL-ELEMENT-REFS")
            for item in self.global_element_refs:
                serialized = SerializationHelper.serialize_item(item, "ReferrableSubtypesEnum")
                if serialized is not None:
                    child_elem = ET.Element("GLOBAL-ELEMENT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize global_in_package_refs (list to container "GLOBAL-IN-PACKAGE-REFS")
        if self.global_in_package_refs:
            wrapper = ET.Element("GLOBAL-IN-PACKAGE-REFS")
            for item in self.global_in_package_refs:
                serialized = SerializationHelper.serialize_item(item, "ARPackage")
                if serialized is not None:
                    child_elem = ET.Element("GLOBAL-IN-PACKAGE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ReferenceBase":
        """Deserialize XML element to ReferenceBase object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ReferenceBase object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ReferenceBase, cls).deserialize(element)

        # Parse short_label
        child = SerializationHelper.find_child_element(element, "SHORT-LABEL")
        if child is not None:
            short_label_value = SerializationHelper.deserialize_by_tag(child, "Identifier")
            obj.short_label = short_label_value

        # Parse is_default
        child = SerializationHelper.find_child_element(element, "IS-DEFAULT")
        if child is not None:
            is_default_value = child.text
            obj.is_default = is_default_value

        # Parse is_global
        child = SerializationHelper.find_child_element(element, "IS-GLOBAL")
        if child is not None:
            is_global_value = child.text
            obj.is_global = is_global_value

        # Parse base_is_this_package
        child = SerializationHelper.find_child_element(element, "BASE-IS-THIS-PACKAGE")
        if child is not None:
            base_is_this_package_value = child.text
            obj.base_is_this_package = base_is_this_package_value

        # Parse package_ref
        child = SerializationHelper.find_child_element(element, "PACKAGE-REF")
        if child is not None:
            package_ref_value = ARRef.deserialize(child)
            obj.package_ref = package_ref_value

        # Parse global_element_refs (list from container "GLOBAL-ELEMENT-REFS")
        obj.global_element_refs = []
        container = SerializationHelper.find_child_element(element, "GLOBAL-ELEMENT-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.global_element_refs.append(child_value)

        # Parse global_in_package_refs (list from container "GLOBAL-IN-PACKAGE-REFS")
        obj.global_in_package_refs = []
        container = SerializationHelper.find_child_element(element, "GLOBAL-IN-PACKAGE-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.global_in_package_refs.append(child_value)

        return obj



class ReferenceBaseBuilder:
    """Builder for ReferenceBase with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: ReferenceBase = ReferenceBase()


    def with_short_label(self, value: Identifier) -> "ReferenceBaseBuilder":
        """Set short_label attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.short_label = value
        return self

    def with_is_default(self, value: Boolean) -> "ReferenceBaseBuilder":
        """Set is_default attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.is_default = value
        return self

    def with_is_global(self, value: Boolean) -> "ReferenceBaseBuilder":
        """Set is_global attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.is_global = value
        return self

    def with_base_is_this_package(self, value: Boolean) -> "ReferenceBaseBuilder":
        """Set base_is_this_package attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.base_is_this_package = value
        return self

    def with_package(self, value: Optional[ARPackage]) -> "ReferenceBaseBuilder":
        """Set package attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.package = value
        return self

    def with_global_elements(self, items: list[ReferrableSubtypesEnum]) -> "ReferenceBaseBuilder":
        """Set global_elements list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.global_elements = list(items) if items else []
        return self

    def with_global_in_packages(self, items: list[ARPackage]) -> "ReferenceBaseBuilder":
        """Set global_in_packages list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.global_in_packages = list(items) if items else []
        return self


    def add_global_element(self, item: ReferrableSubtypesEnum) -> "ReferenceBaseBuilder":
        """Add a single item to global_elements list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.global_elements.append(item)
        return self

    def clear_global_elements(self) -> "ReferenceBaseBuilder":
        """Clear all items from global_elements list.

        Returns:
            self for method chaining
        """
        self._obj.global_elements = []
        return self

    def add_global_in_package(self, item: ARPackage) -> "ReferenceBaseBuilder":
        """Add a single item to global_in_packages list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.global_in_packages.append(item)
        return self

    def clear_global_in_packages(self) -> "ReferenceBaseBuilder":
        """Clear all items from global_in_packages list.

        Returns:
            self for method chaining
        """
        self._obj.global_in_packages = []
        return self


    @staticmethod
    def _coerce_to_int(value: Any) -> int:
        """Coerce value to int.

        Args:
            value: Value to coerce

        Returns:
            Integer value

        Raises:
            ValueError: If value cannot be coerced to int
        """
        if isinstance(value, int):
            return value
        if isinstance(value, str) and value.isdigit():
            return int(value)
        if isinstance(value, float):
            return int(value)
        if isinstance(value, bool):
            return int(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to int: {value}")

    @staticmethod
    def _coerce_to_float(value: Any) -> float:
        """Coerce value to float.

        Args:
            value: Value to coerce

        Returns:
            Float value

        Raises:
            ValueError: If value cannot be coerced to float
        """
        if isinstance(value, float):
            return value
        if isinstance(value, int):
            return float(value)
        if isinstance(value, str):
            try:
                return float(value)
            except ValueError:
                pass
        raise ValueError(f"Cannot coerce {type(value).__name__} to float: {value}")

    @staticmethod
    def _coerce_to_bool(value: Any) -> bool:
        """Coerce value to bool.

        Args:
            value: Value to coerce

        Returns:
            Boolean value

        Raises:
            ValueError: If value cannot be coerced to bool
        """
        if isinstance(value, bool):
            return value
        if isinstance(value, int):
            return bool(value)
        if isinstance(value, str):
            if value.lower() in ("true", "1", "yes"):
                return True
            if value.lower() in ("false", "0", "no"):
                return False
        raise ValueError(f"Cannot coerce {type(value).__name__} to bool: {value}")

    @staticmethod
    def _coerce_to_str(value: Any) -> str:
        """Coerce value to str.

        Args:
            value: Value to coerce

        Returns:
            String value
        """
        return str(value)


    @staticmethod
    def _coerce_to_list(value: Any, item_type: str) -> list:
        """Coerce value to list.

        Args:
            value: Value to coerce
            item_type: Expected item type (for error messages)

        Returns:
            List value

        Raises:
            ValueError: If value cannot be coerced to list
        """
        if isinstance(value, list):
            return value
        if isinstance(value, tuple):
            return list(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to list[{item_type}]: {value}")


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel.core import GlobalSettingsManager, BuilderValidationMode

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


    def build(self) -> ReferenceBase:
        """Build and return the ReferenceBase instance with validation."""
        self._validate_instance()
        pass
        return self._obj