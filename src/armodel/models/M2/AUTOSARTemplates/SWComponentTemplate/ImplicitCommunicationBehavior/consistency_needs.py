"""ConsistencyNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 221)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 178)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_ImplicitCommunicationBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior.data_prototype_group import (
    DataPrototypeGroup,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior.runnable_entity_group import (
    RunnableEntityGroup,
)


class ConsistencyNeeds(Identifiable):
    """AUTOSAR ConsistencyNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    dpg_does_not_refs: list[ARRef]
    dpg_requirese_refs: list[ARRef]
    reg_does_not_refs: list[ARRef]
    reg_requirese_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize ConsistencyNeeds."""
        super().__init__()
        self.dpg_does_not_refs: list[ARRef] = []
        self.dpg_requirese_refs: list[ARRef] = []
        self.reg_does_not_refs: list[ARRef] = []
        self.reg_requirese_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize ConsistencyNeeds to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ConsistencyNeeds, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize dpg_does_not_refs (list to container "DPG-DOES-NOT-REFS")
        if self.dpg_does_not_refs:
            wrapper = ET.Element("DPG-DOES-NOT-REFS")
            for item in self.dpg_does_not_refs:
                serialized = SerializationHelper.serialize_item(item, "DataPrototypeGroup")
                if serialized is not None:
                    child_elem = ET.Element("DPG-DOES-NOT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize dpg_requirese_refs (list to container "DPG-REQUIRESE-REFS")
        if self.dpg_requirese_refs:
            wrapper = ET.Element("DPG-REQUIRESE-REFS")
            for item in self.dpg_requirese_refs:
                serialized = SerializationHelper.serialize_item(item, "DataPrototypeGroup")
                if serialized is not None:
                    child_elem = ET.Element("DPG-REQUIRESE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize reg_does_not_refs (list to container "REG-DOES-NOT-REFS")
        if self.reg_does_not_refs:
            wrapper = ET.Element("REG-DOES-NOT-REFS")
            for item in self.reg_does_not_refs:
                serialized = SerializationHelper.serialize_item(item, "RunnableEntityGroup")
                if serialized is not None:
                    child_elem = ET.Element("REG-DOES-NOT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize reg_requirese_refs (list to container "REG-REQUIRESE-REFS")
        if self.reg_requirese_refs:
            wrapper = ET.Element("REG-REQUIRESE-REFS")
            for item in self.reg_requirese_refs:
                serialized = SerializationHelper.serialize_item(item, "RunnableEntityGroup")
                if serialized is not None:
                    child_elem = ET.Element("REG-REQUIRESE-REF")
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
    def deserialize(cls, element: ET.Element) -> "ConsistencyNeeds":
        """Deserialize XML element to ConsistencyNeeds object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ConsistencyNeeds object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ConsistencyNeeds, cls).deserialize(element)

        # Parse dpg_does_not_refs (list from container "DPG-DOES-NOT-REFS")
        obj.dpg_does_not_refs = []
        container = SerializationHelper.find_child_element(element, "DPG-DOES-NOT-REFS")
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
                    obj.dpg_does_not_refs.append(child_value)

        # Parse dpg_requirese_refs (list from container "DPG-REQUIRESE-REFS")
        obj.dpg_requirese_refs = []
        container = SerializationHelper.find_child_element(element, "DPG-REQUIRESE-REFS")
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
                    obj.dpg_requirese_refs.append(child_value)

        # Parse reg_does_not_refs (list from container "REG-DOES-NOT-REFS")
        obj.reg_does_not_refs = []
        container = SerializationHelper.find_child_element(element, "REG-DOES-NOT-REFS")
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
                    obj.reg_does_not_refs.append(child_value)

        # Parse reg_requirese_refs (list from container "REG-REQUIRESE-REFS")
        obj.reg_requirese_refs = []
        container = SerializationHelper.find_child_element(element, "REG-REQUIRESE-REFS")
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
                    obj.reg_requirese_refs.append(child_value)

        return obj



class ConsistencyNeedsBuilder:
    """Builder for ConsistencyNeeds with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: ConsistencyNeeds = ConsistencyNeeds()


    def with_short_name(self, value: Identifier) -> "ConsistencyNeedsBuilder":
        """Set short_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.short_name = value
        return self

    def with_short_name_fragments(self, items: list[ShortNameFragment]) -> "ConsistencyNeedsBuilder":
        """Set short_name_fragments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = list(items) if items else []
        return self

    def with_long_name(self, value: Optional[MultilanguageLongName]) -> "ConsistencyNeedsBuilder":
        """Set long_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.long_name = value
        return self

    def with_admin_data(self, value: Optional[AdminData]) -> "ConsistencyNeedsBuilder":
        """Set admin_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.admin_data = value
        return self

    def with_annotations(self, items: list[Annotation]) -> "ConsistencyNeedsBuilder":
        """Set annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.annotations = list(items) if items else []
        return self

    def with_desc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "ConsistencyNeedsBuilder":
        """Set desc attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.desc = value
        return self

    def with_category(self, value: Optional[CategoryString]) -> "ConsistencyNeedsBuilder":
        """Set category attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.category = value
        return self

    def with_introduction(self, value: Optional[DocumentationBlock]) -> "ConsistencyNeedsBuilder":
        """Set introduction attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.introduction = value
        return self

    def with_uuid(self, value: Optional[String]) -> "ConsistencyNeedsBuilder":
        """Set uuid attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.uuid = value
        return self

    def with_dpg_does_nots(self, items: list[DataPrototypeGroup]) -> "ConsistencyNeedsBuilder":
        """Set dpg_does_nots list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.dpg_does_nots = list(items) if items else []
        return self

    def with_dpg_requireses(self, items: list[DataPrototypeGroup]) -> "ConsistencyNeedsBuilder":
        """Set dpg_requireses list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.dpg_requireses = list(items) if items else []
        return self

    def with_reg_does_nots(self, items: list[RunnableEntityGroup]) -> "ConsistencyNeedsBuilder":
        """Set reg_does_nots list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.reg_does_nots = list(items) if items else []
        return self

    def with_reg_requireses(self, items: list[RunnableEntityGroup]) -> "ConsistencyNeedsBuilder":
        """Set reg_requireses list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.reg_requireses = list(items) if items else []
        return self


    def add_short_name_fragment(self, item: ShortNameFragment) -> "ConsistencyNeedsBuilder":
        """Add a single item to short_name_fragments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments.append(item)
        return self

    def clear_short_name_fragments(self) -> "ConsistencyNeedsBuilder":
        """Clear all items from short_name_fragments list.

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = []
        return self

    def add_annotation(self, item: Annotation) -> "ConsistencyNeedsBuilder":
        """Add a single item to annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.annotations.append(item)
        return self

    def clear_annotations(self) -> "ConsistencyNeedsBuilder":
        """Clear all items from annotations list.

        Returns:
            self for method chaining
        """
        self._obj.annotations = []
        return self

    def add_dpg_does_not(self, item: DataPrototypeGroup) -> "ConsistencyNeedsBuilder":
        """Add a single item to dpg_does_nots list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.dpg_does_nots.append(item)
        return self

    def clear_dpg_does_nots(self) -> "ConsistencyNeedsBuilder":
        """Clear all items from dpg_does_nots list.

        Returns:
            self for method chaining
        """
        self._obj.dpg_does_nots = []
        return self

    def add_dpg_requirese(self, item: DataPrototypeGroup) -> "ConsistencyNeedsBuilder":
        """Add a single item to dpg_requireses list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.dpg_requireses.append(item)
        return self

    def clear_dpg_requireses(self) -> "ConsistencyNeedsBuilder":
        """Clear all items from dpg_requireses list.

        Returns:
            self for method chaining
        """
        self._obj.dpg_requireses = []
        return self

    def add_reg_does_not(self, item: RunnableEntityGroup) -> "ConsistencyNeedsBuilder":
        """Add a single item to reg_does_nots list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.reg_does_nots.append(item)
        return self

    def clear_reg_does_nots(self) -> "ConsistencyNeedsBuilder":
        """Clear all items from reg_does_nots list.

        Returns:
            self for method chaining
        """
        self._obj.reg_does_nots = []
        return self

    def add_reg_requirese(self, item: RunnableEntityGroup) -> "ConsistencyNeedsBuilder":
        """Add a single item to reg_requireses list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.reg_requireses.append(item)
        return self

    def clear_reg_requireses(self) -> "ConsistencyNeedsBuilder":
        """Clear all items from reg_requireses list.

        Returns:
            self for method chaining
        """
        self._obj.reg_requireses = []
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


    def build(self) -> ConsistencyNeeds:
        """Build and return the ConsistencyNeeds instance with validation."""
        self._validate_instance()
        pass
        return self._obj