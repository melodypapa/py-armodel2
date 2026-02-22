"""McFunctionDataRefSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 187)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 455)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_MeasurementCalibrationSupport_RptSupport.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization.decorators import atp_variant

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.FlatMap.flat_instance_descriptor import (
    FlatInstanceDescriptor,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.mc_data_instance import (
    McDataInstance,
)


@atp_variant()

class McFunctionDataRefSet(ARObject):
    """AUTOSAR McFunctionDataRefSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    flat_map_entrie_refs: list[ARRef]
    mc_data_instance_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize McFunctionDataRefSet."""
        super().__init__()
        self.flat_map_entrie_refs: list[ARRef] = []
        self.mc_data_instance_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize McFunctionDataRefSet to XML element with atp_variant wrapper.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(McFunctionDataRefSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Create inner element to hold attributes before wrapping
        inner_elem = ET.Element("INNER")

        # Serialize flat_map_entrie_refs (list from container "FLAT-MAP-ENTRIE-REFS")
        if self.flat_map_entrie_refs:
            container = ET.Element("FLAT-MAP-ENTRIE-REFS")
            for item in self.flat_map_entrie_refs:
                if is_ref:
                    # For reference lists, serialize as reference
                    if hasattr(item, "serialize"):
                        container.append(item.serialize())
                elif is_primitive_type("FlatInstanceDescriptor", package_data):
                    # Simple primitive type
                    child = ET.Element("FLAT-MAP-ENTRIE")
                    child.text = str(item)
                    container.append(child)
                elif is_enum_type("FlatInstanceDescriptor", package_data):
                    # Enum type - use serialize method
                    if hasattr(item, "serialize"):
                        container.append(item.serialize())
                else:
                    # Complex object type
                    if hasattr(item, "serialize"):
                        container.append(item.serialize())
            inner_elem.append(container)

        # Serialize mc_data_instance_refs (list from container "MC-DATA-INSTANCE-REFS")
        if self.mc_data_instance_refs:
            container = ET.Element("MC-DATA-INSTANCE-REFS")
            for item in self.mc_data_instance_refs:
                if is_ref:
                    # For reference lists, serialize as reference
                    if hasattr(item, "serialize"):
                        container.append(item.serialize())
                elif is_primitive_type("McDataInstance", package_data):
                    # Simple primitive type
                    child = ET.Element("MC-DATA-INSTANCE")
                    child.text = str(item)
                    container.append(child)
                elif is_enum_type("McDataInstance", package_data):
                    # Enum type - use serialize method
                    if hasattr(item, "serialize"):
                        container.append(item.serialize())
                else:
                    # Complex object type
                    if hasattr(item, "serialize"):
                        container.append(item.serialize())
            inner_elem.append(container)

        # Wrap inner element in atp_variant VARIANTS/CONDITIONAL structure
        wrapped = SerializationHelper.serialize_with_atp_variant(inner_elem, "McFunctionDataRefSet")
        elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "McFunctionDataRefSet":
        """Deserialize XML element to McFunctionDataRefSet object with atp_variant unwrapping.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized McFunctionDataRefSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(McFunctionDataRefSet, cls).deserialize(element)

        # Unwrap atp_variant VARIANTS/CONDITIONAL structure
        inner_elem = SerializationHelper.deserialize_from_atp_variant(element, "McFunctionDataRefSet")
        if inner_elem is None:
            # No wrapper structure found, return object with default values
            return obj

        # Parse flat_map_entrie_refs (list from container "FLAT-MAP-ENTRIE-REFS")
        obj.flat_map_entrie_refs = []
        container = SerializationHelper.find_child_element(inner_elem, "FLAT-MAP-ENTRIE-REFS")
        if container is not None:
            for child in container:
                if is_ref:
                    child_tag = SerializationHelper.strip_namespace(child.tag)
                    if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                        child_value = ARRef.deserialize(child)
                    else:
                        child_value = SerializationHelper.deserialize_by_tag(child, None)
                elif is_primitive_type("FlatInstanceDescriptor", package_data):
                    child_value = child.text
                elif is_enum_type("FlatInstanceDescriptor", package_data):
                    child_value = FlatInstanceDescriptor.deserialize(child)
                else:
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.flat_map_entrie_refs.append(child_value)

        # Parse mc_data_instance_refs (list from container "MC-DATA-INSTANCE-REFS")
        obj.mc_data_instance_refs = []
        container = SerializationHelper.find_child_element(inner_elem, "MC-DATA-INSTANCE-REFS")
        if container is not None:
            for child in container:
                if is_ref:
                    child_tag = SerializationHelper.strip_namespace(child.tag)
                    if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                        child_value = ARRef.deserialize(child)
                    else:
                        child_value = SerializationHelper.deserialize_by_tag(child, None)
                elif is_primitive_type("McDataInstance", package_data):
                    child_value = child.text
                elif is_enum_type("McDataInstance", package_data):
                    child_value = McDataInstance.deserialize(child)
                else:
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mc_data_instance_refs.append(child_value)

        return obj



class McFunctionDataRefSetBuilder:
    """Builder for McFunctionDataRefSet with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: McFunctionDataRefSet = McFunctionDataRefSet()


    def with_flat_map_entries(self, items: list[FlatInstanceDescriptor]) -> "McFunctionDataRefSetBuilder":
        """Set flat_map_entries list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.flat_map_entries = list(items) if items else []
        return self

    def with_mc_data_instances(self, items: list[McDataInstance]) -> "McFunctionDataRefSetBuilder":
        """Set mc_data_instances list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.mc_data_instances = list(items) if items else []
        return self


    def add_flat_map_entrie(self, item: FlatInstanceDescriptor) -> "McFunctionDataRefSetBuilder":
        """Add a single item to flat_map_entries list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.flat_map_entries.append(item)
        return self

    def clear_flat_map_entries(self) -> "McFunctionDataRefSetBuilder":
        """Clear all items from flat_map_entries list.

        Returns:
            self for method chaining
        """
        self._obj.flat_map_entries = []
        return self

    def add_mc_data_instance(self, item: McDataInstance) -> "McFunctionDataRefSetBuilder":
        """Add a single item to mc_data_instances list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.mc_data_instances.append(item)
        return self

    def clear_mc_data_instances(self) -> "McFunctionDataRefSetBuilder":
        """Clear all items from mc_data_instances list.

        Returns:
            self for method chaining
        """
        self._obj.mc_data_instances = []
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


    def build(self) -> McFunctionDataRefSet:
        """Build and return the McFunctionDataRefSet instance with validation."""
        self._validate_instance()
        pass
        return self._obj