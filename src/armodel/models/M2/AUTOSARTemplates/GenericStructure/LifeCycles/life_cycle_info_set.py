"""LifeCycleInfoSet AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 391)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 195)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_LifeCycles.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles.life_cycle_info import (
    LifeCycleInfo,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles.life_cycle_period import (
    LifeCyclePeriod,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles.life_cycle_state import (
    LifeCycleState,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles.life_cycle_state_definition_group import (
    LifeCycleStateDefinitionGroup,
)


class LifeCycleInfoSet(ARElement):
    """AUTOSAR LifeCycleInfoSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    default_lc_state_ref: ARRef
    default_period_begin: Optional[LifeCyclePeriod]
    default_period_end: Optional[LifeCyclePeriod]
    life_cycle_infos: list[LifeCycleInfo]
    used_life_cycle_state_definition_group_ref: ARRef
    def __init__(self) -> None:
        """Initialize LifeCycleInfoSet."""
        super().__init__()
        self.default_lc_state_ref: ARRef = None
        self.default_period_begin: Optional[LifeCyclePeriod] = None
        self.default_period_end: Optional[LifeCyclePeriod] = None
        self.life_cycle_infos: list[LifeCycleInfo] = []
        self.used_life_cycle_state_definition_group_ref: ARRef = None

    def serialize(self) -> ET.Element:
        """Serialize LifeCycleInfoSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(LifeCycleInfoSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize default_lc_state_ref
        if self.default_lc_state_ref is not None:
            serialized = SerializationHelper.serialize_item(self.default_lc_state_ref, "LifeCycleState")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEFAULT-LC-STATE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize default_period_begin
        if self.default_period_begin is not None:
            serialized = SerializationHelper.serialize_item(self.default_period_begin, "LifeCyclePeriod")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEFAULT-PERIOD-BEGIN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize default_period_end
        if self.default_period_end is not None:
            serialized = SerializationHelper.serialize_item(self.default_period_end, "LifeCyclePeriod")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEFAULT-PERIOD-END")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize life_cycle_infos (list to container "LIFE-CYCLE-INFOS")
        if self.life_cycle_infos:
            wrapper = ET.Element("LIFE-CYCLE-INFOS")
            for item in self.life_cycle_infos:
                serialized = SerializationHelper.serialize_item(item, "LifeCycleInfo")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize used_life_cycle_state_definition_group_ref
        if self.used_life_cycle_state_definition_group_ref is not None:
            serialized = SerializationHelper.serialize_item(self.used_life_cycle_state_definition_group_ref, "LifeCycleStateDefinitionGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("USED-LIFE-CYCLE-STATE-DEFINITION-GROUP-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LifeCycleInfoSet":
        """Deserialize XML element to LifeCycleInfoSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LifeCycleInfoSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(LifeCycleInfoSet, cls).deserialize(element)

        # Parse default_lc_state_ref
        child = SerializationHelper.find_child_element(element, "DEFAULT-LC-STATE-REF")
        if child is not None:
            default_lc_state_ref_value = ARRef.deserialize(child)
            obj.default_lc_state_ref = default_lc_state_ref_value

        # Parse default_period_begin
        child = SerializationHelper.find_child_element(element, "DEFAULT-PERIOD-BEGIN")
        if child is not None:
            default_period_begin_value = SerializationHelper.deserialize_by_tag(child, "LifeCyclePeriod")
            obj.default_period_begin = default_period_begin_value

        # Parse default_period_end
        child = SerializationHelper.find_child_element(element, "DEFAULT-PERIOD-END")
        if child is not None:
            default_period_end_value = SerializationHelper.deserialize_by_tag(child, "LifeCyclePeriod")
            obj.default_period_end = default_period_end_value

        # Parse life_cycle_infos (list from container "LIFE-CYCLE-INFOS")
        obj.life_cycle_infos = []
        container = SerializationHelper.find_child_element(element, "LIFE-CYCLE-INFOS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.life_cycle_infos.append(child_value)

        # Parse used_life_cycle_state_definition_group_ref
        child = SerializationHelper.find_child_element(element, "USED-LIFE-CYCLE-STATE-DEFINITION-GROUP-REF")
        if child is not None:
            used_life_cycle_state_definition_group_ref_value = ARRef.deserialize(child)
            obj.used_life_cycle_state_definition_group_ref = used_life_cycle_state_definition_group_ref_value

        return obj



class LifeCycleInfoSetBuilder:
    """Builder for LifeCycleInfoSet with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: LifeCycleInfoSet = LifeCycleInfoSet()


    def with_short_name(self, value: Identifier) -> "LifeCycleInfoSetBuilder":
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

    def with_short_name_fragments(self, items: list[ShortNameFragment]) -> "LifeCycleInfoSetBuilder":
        """Set short_name_fragments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = list(items) if items else []
        return self

    def with_long_name(self, value: Optional[MultilanguageLongName]) -> "LifeCycleInfoSetBuilder":
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

    def with_admin_data(self, value: Optional[AdminData]) -> "LifeCycleInfoSetBuilder":
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

    def with_annotations(self, items: list[Annotation]) -> "LifeCycleInfoSetBuilder":
        """Set annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.annotations = list(items) if items else []
        return self

    def with_desc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "LifeCycleInfoSetBuilder":
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

    def with_category(self, value: Optional[CategoryString]) -> "LifeCycleInfoSetBuilder":
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

    def with_introduction(self, value: Optional[DocumentationBlock]) -> "LifeCycleInfoSetBuilder":
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

    def with_uuid(self, value: Optional[String]) -> "LifeCycleInfoSetBuilder":
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

    def with_default_lc_state(self, value: LifeCycleState) -> "LifeCycleInfoSetBuilder":
        """Set default_lc_state attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.default_lc_state = value
        return self

    def with_default_period_begin(self, value: Optional[LifeCyclePeriod]) -> "LifeCycleInfoSetBuilder":
        """Set default_period_begin attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.default_period_begin = value
        return self

    def with_default_period_end(self, value: Optional[LifeCyclePeriod]) -> "LifeCycleInfoSetBuilder":
        """Set default_period_end attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.default_period_end = value
        return self

    def with_life_cycle_infos(self, items: list[LifeCycleInfo]) -> "LifeCycleInfoSetBuilder":
        """Set life_cycle_infos list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.life_cycle_infos = list(items) if items else []
        return self

    def with_used_life_cycle_state_definition_group(self, value: LifeCycleStateDefinitionGroup) -> "LifeCycleInfoSetBuilder":
        """Set used_life_cycle_state_definition_group attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.used_life_cycle_state_definition_group = value
        return self


    def add_short_name_fragment(self, item: ShortNameFragment) -> "LifeCycleInfoSetBuilder":
        """Add a single item to short_name_fragments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments.append(item)
        return self

    def clear_short_name_fragments(self) -> "LifeCycleInfoSetBuilder":
        """Clear all items from short_name_fragments list.

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = []
        return self

    def add_annotation(self, item: Annotation) -> "LifeCycleInfoSetBuilder":
        """Add a single item to annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.annotations.append(item)
        return self

    def clear_annotations(self) -> "LifeCycleInfoSetBuilder":
        """Clear all items from annotations list.

        Returns:
            self for method chaining
        """
        self._obj.annotations = []
        return self

    def add_life_cycle_info(self, item: LifeCycleInfo) -> "LifeCycleInfoSetBuilder":
        """Add a single item to life_cycle_infos list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.life_cycle_infos.append(item)
        return self

    def clear_life_cycle_infos(self) -> "LifeCycleInfoSetBuilder":
        """Clear all items from life_cycle_infos list.

        Returns:
            self for method chaining
        """
        self._obj.life_cycle_infos = []
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


    def build(self) -> LifeCycleInfoSet:
        """Build and return the LifeCycleInfoSet instance with validation."""
        self._validate_instance()
        pass
        return self._obj