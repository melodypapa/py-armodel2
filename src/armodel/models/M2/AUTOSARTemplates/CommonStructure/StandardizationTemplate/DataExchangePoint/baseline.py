"""Baseline AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 79)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.DocumentationOnM1.documentation import (
    Documentation,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_def import (
    SdgDef,
)


class Baseline(ARObject):
    """AUTOSAR Baseline."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    custom_sdg_def_refs: list[ARRef]
    custom_refs: list[ARRef]
    standards: list[String]
    def __init__(self) -> None:
        """Initialize Baseline."""
        super().__init__()
        self.custom_sdg_def_refs: list[ARRef] = []
        self.custom_refs: list[ARRef] = []
        self.standards: list[String] = []

    def serialize(self) -> ET.Element:
        """Serialize Baseline to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Baseline, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize custom_sdg_def_refs (list to container "CUSTOM-SDG-DEF-REFS")
        if self.custom_sdg_def_refs:
            wrapper = ET.Element("CUSTOM-SDG-DEF-REFS")
            for item in self.custom_sdg_def_refs:
                serialized = SerializationHelper.serialize_item(item, "SdgDef")
                if serialized is not None:
                    child_elem = ET.Element("CUSTOM-SDG-DEF-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize custom_refs (list to container "CUSTOM-REFS")
        if self.custom_refs:
            wrapper = ET.Element("CUSTOM-REFS")
            for item in self.custom_refs:
                serialized = SerializationHelper.serialize_item(item, "Documentation")
                if serialized is not None:
                    child_elem = ET.Element("CUSTOM-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize standards (list to container "STANDARDS")
        if self.standards:
            wrapper = ET.Element("STANDARDS")
            for item in self.standards:
                serialized = SerializationHelper.serialize_item(item, "String")
                if serialized is not None:
                    child_elem = ET.Element("STANDARD")
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
    def deserialize(cls, element: ET.Element) -> "Baseline":
        """Deserialize XML element to Baseline object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Baseline object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Baseline, cls).deserialize(element)

        # Parse custom_sdg_def_refs (list from container "CUSTOM-SDG-DEF-REFS")
        obj.custom_sdg_def_refs = []
        container = SerializationHelper.find_child_element(element, "CUSTOM-SDG-DEF-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.custom_sdg_def_refs.append(child_value)

        # Parse custom_refs (list from container "CUSTOM-REFS")
        obj.custom_refs = []
        container = SerializationHelper.find_child_element(element, "CUSTOM-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.custom_refs.append(child_value)

        # Parse standards (list from container "STANDARDS")
        obj.standards = []
        container = SerializationHelper.find_child_element(element, "STANDARDS")
        if container is not None:
            for child in container:
                # Extract primitive value (String) as text
                child_value = child.text
                if child_value is not None:
                    obj.standards.append(child_value)

        return obj



class BaselineBuilder:
    """Builder for Baseline with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: Baseline = Baseline()


    def with_custom_sdg_defs(self, items: list[SdgDef]) -> "BaselineBuilder":
        """Set custom_sdg_defs list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.custom_sdg_defs = list(items) if items else []
        return self

    def with_customs(self, items: list[Documentation]) -> "BaselineBuilder":
        """Set customs list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.customs = list(items) if items else []
        return self

    def with_standards(self, items: list[String]) -> "BaselineBuilder":
        """Set standards list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.standards = list(items) if items else []
        return self


    def add_custom_sdg_def(self, item: SdgDef) -> "BaselineBuilder":
        """Add a single item to custom_sdg_defs list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.custom_sdg_defs.append(item)
        return self

    def clear_custom_sdg_defs(self) -> "BaselineBuilder":
        """Clear all items from custom_sdg_defs list.

        Returns:
            self for method chaining
        """
        self._obj.custom_sdg_defs = []
        return self

    def add_custom(self, item: Documentation) -> "BaselineBuilder":
        """Add a single item to customs list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.customs.append(item)
        return self

    def clear_customs(self) -> "BaselineBuilder":
        """Clear all items from customs list.

        Returns:
            self for method chaining
        """
        self._obj.customs = []
        return self

    def add_standard(self, item: String) -> "BaselineBuilder":
        """Add a single item to standards list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.standards.append(item)
        return self

    def clear_standards(self) -> "BaselineBuilder":
        """Clear all items from standards list.

        Returns:
            self for method chaining
        """
        self._obj.standards = []
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


    def build(self) -> Baseline:
        """Build and return the Baseline instance with validation."""
        self._validate_instance()
        pass
        return self._obj