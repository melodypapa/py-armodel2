"""BswSchedulableEntity AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 75)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 978)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_module_entity import (
    BswModuleEntity,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class BswSchedulableEntity(BswModuleEntity):
    """AUTOSAR BswSchedulableEntity."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize BswSchedulableEntity."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize BswSchedulableEntity to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BswSchedulableEntity, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswSchedulableEntity":
        """Deserialize XML element to BswSchedulableEntity object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswSchedulableEntity object
        """
        # Delegate to parent class to handle inherited attributes
        return super(BswSchedulableEntity, cls).deserialize(element)



class BswSchedulableEntityBuilder:
    """Builder for BswSchedulableEntity with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: BswSchedulableEntity = BswSchedulableEntity()


    def with_short_name(self, value: Identifier) -> "BswSchedulableEntityBuilder":
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

    def with_short_name_fragments(self, items: list[ShortNameFragment]) -> "BswSchedulableEntityBuilder":
        """Set short_name_fragments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = list(items) if items else []
        return self

    def with_long_name(self, value: Optional[MultilanguageLongName]) -> "BswSchedulableEntityBuilder":
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

    def with_admin_data(self, value: Optional[AdminData]) -> "BswSchedulableEntityBuilder":
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

    def with_annotations(self, items: list[Annotation]) -> "BswSchedulableEntityBuilder":
        """Set annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.annotations = list(items) if items else []
        return self

    def with_desc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "BswSchedulableEntityBuilder":
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

    def with_category(self, value: Optional[CategoryString]) -> "BswSchedulableEntityBuilder":
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

    def with_introduction(self, value: Optional[DocumentationBlock]) -> "BswSchedulableEntityBuilder":
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

    def with_uuid(self, value: Optional[String]) -> "BswSchedulableEntityBuilder":
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

    def with_activation_reasons(self, items: list[ExecutableEntityActivationReason]) -> "BswSchedulableEntityBuilder":
        """Set activation_reasons list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.activation_reasons = list(items) if items else []
        return self

    def with_can_enters(self, items: list[ExclusiveArea]) -> "BswSchedulableEntityBuilder":
        """Set can_enters list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.can_enters = list(items) if items else []
        return self

    def with_exclusive_area_nesting_orders(self, items: list[ExclusiveAreaNestingOrder]) -> "BswSchedulableEntityBuilder":
        """Set exclusive_area_nesting_orders list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.exclusive_area_nesting_orders = list(items) if items else []
        return self

    def with_minimum_start_interval(self, value: Optional[TimeValue]) -> "BswSchedulableEntityBuilder":
        """Set minimum_start_interval attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.minimum_start_interval = value
        return self

    def with_reentrancy_level(self, value: Optional[ReentrancyLevelEnum]) -> "BswSchedulableEntityBuilder":
        """Set reentrancy_level attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.reentrancy_level = value
        return self

    def with_runs_insides(self, items: list[ExclusiveArea]) -> "BswSchedulableEntityBuilder":
        """Set runs_insides list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.runs_insides = list(items) if items else []
        return self

    def with_sw_addr_method(self, value: Optional[SwAddrMethod]) -> "BswSchedulableEntityBuilder":
        """Set sw_addr_method attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_addr_method = value
        return self

    def with_accessed_mode_groups(self, items: list[ModeDeclarationGroup]) -> "BswSchedulableEntityBuilder":
        """Set accessed_mode_groups list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.accessed_mode_groups = list(items) if items else []
        return self

    def with_activation_points(self, items: list[BswInternalTriggeringPoint]) -> "BswSchedulableEntityBuilder":
        """Set activation_points list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.activation_points = list(items) if items else []
        return self

    def with_call_points(self, items: list[BswModuleCallPoint]) -> "BswSchedulableEntityBuilder":
        """Set call_points list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.call_points = list(items) if items else []
        return self

    def with_data_receive_points(self, items: list[BswVariableAccess]) -> "BswSchedulableEntityBuilder":
        """Set data_receive_points list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.data_receive_points = list(items) if items else []
        return self

    def with_data_send_points(self, items: list[BswVariableAccess]) -> "BswSchedulableEntityBuilder":
        """Set data_send_points list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.data_send_points = list(items) if items else []
        return self

    def with_implemented_entry(self, value: Optional[BswModuleEntry]) -> "BswSchedulableEntityBuilder":
        """Set implemented_entry attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.implemented_entry = value
        return self

    def with_issued_triggers(self, items: list[Trigger]) -> "BswSchedulableEntityBuilder":
        """Set issued_triggers list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.issued_triggers = list(items) if items else []
        return self

    def with_managed_mode_groups(self, items: list[ModeDeclarationGroupPrototype]) -> "BswSchedulableEntityBuilder":
        """Set managed_mode_groups list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.managed_mode_groups = list(items) if items else []
        return self

    def with_scheduler_name_prefix(self, value: Optional[BswSchedulerNamePrefix]) -> "BswSchedulableEntityBuilder":
        """Set scheduler_name_prefix attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.scheduler_name_prefix = value
        return self


    def add_short_name_fragment(self, item: ShortNameFragment) -> "BswSchedulableEntityBuilder":
        """Add a single item to short_name_fragments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments.append(item)
        return self

    def clear_short_name_fragments(self) -> "BswSchedulableEntityBuilder":
        """Clear all items from short_name_fragments list.

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = []
        return self

    def add_annotation(self, item: Annotation) -> "BswSchedulableEntityBuilder":
        """Add a single item to annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.annotations.append(item)
        return self

    def clear_annotations(self) -> "BswSchedulableEntityBuilder":
        """Clear all items from annotations list.

        Returns:
            self for method chaining
        """
        self._obj.annotations = []
        return self

    def add_activation_reason(self, item: ExecutableEntityActivationReason) -> "BswSchedulableEntityBuilder":
        """Add a single item to activation_reasons list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.activation_reasons.append(item)
        return self

    def clear_activation_reasons(self) -> "BswSchedulableEntityBuilder":
        """Clear all items from activation_reasons list.

        Returns:
            self for method chaining
        """
        self._obj.activation_reasons = []
        return self

    def add_can_enter(self, item: ExclusiveArea) -> "BswSchedulableEntityBuilder":
        """Add a single item to can_enters list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.can_enters.append(item)
        return self

    def clear_can_enters(self) -> "BswSchedulableEntityBuilder":
        """Clear all items from can_enters list.

        Returns:
            self for method chaining
        """
        self._obj.can_enters = []
        return self

    def add_exclusive_area_nesting_order(self, item: ExclusiveAreaNestingOrder) -> "BswSchedulableEntityBuilder":
        """Add a single item to exclusive_area_nesting_orders list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.exclusive_area_nesting_orders.append(item)
        return self

    def clear_exclusive_area_nesting_orders(self) -> "BswSchedulableEntityBuilder":
        """Clear all items from exclusive_area_nesting_orders list.

        Returns:
            self for method chaining
        """
        self._obj.exclusive_area_nesting_orders = []
        return self

    def add_runs_inside(self, item: ExclusiveArea) -> "BswSchedulableEntityBuilder":
        """Add a single item to runs_insides list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.runs_insides.append(item)
        return self

    def clear_runs_insides(self) -> "BswSchedulableEntityBuilder":
        """Clear all items from runs_insides list.

        Returns:
            self for method chaining
        """
        self._obj.runs_insides = []
        return self

    def add_accessed_mode_group(self, item: ModeDeclarationGroup) -> "BswSchedulableEntityBuilder":
        """Add a single item to accessed_mode_groups list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.accessed_mode_groups.append(item)
        return self

    def clear_accessed_mode_groups(self) -> "BswSchedulableEntityBuilder":
        """Clear all items from accessed_mode_groups list.

        Returns:
            self for method chaining
        """
        self._obj.accessed_mode_groups = []
        return self

    def add_activation_point(self, item: BswInternalTriggeringPoint) -> "BswSchedulableEntityBuilder":
        """Add a single item to activation_points list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.activation_points.append(item)
        return self

    def clear_activation_points(self) -> "BswSchedulableEntityBuilder":
        """Clear all items from activation_points list.

        Returns:
            self for method chaining
        """
        self._obj.activation_points = []
        return self

    def add_call_point(self, item: BswModuleCallPoint) -> "BswSchedulableEntityBuilder":
        """Add a single item to call_points list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.call_points.append(item)
        return self

    def clear_call_points(self) -> "BswSchedulableEntityBuilder":
        """Clear all items from call_points list.

        Returns:
            self for method chaining
        """
        self._obj.call_points = []
        return self

    def add_data_receive_point(self, item: BswVariableAccess) -> "BswSchedulableEntityBuilder":
        """Add a single item to data_receive_points list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.data_receive_points.append(item)
        return self

    def clear_data_receive_points(self) -> "BswSchedulableEntityBuilder":
        """Clear all items from data_receive_points list.

        Returns:
            self for method chaining
        """
        self._obj.data_receive_points = []
        return self

    def add_data_send_point(self, item: BswVariableAccess) -> "BswSchedulableEntityBuilder":
        """Add a single item to data_send_points list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.data_send_points.append(item)
        return self

    def clear_data_send_points(self) -> "BswSchedulableEntityBuilder":
        """Clear all items from data_send_points list.

        Returns:
            self for method chaining
        """
        self._obj.data_send_points = []
        return self

    def add_issued_trigger(self, item: Trigger) -> "BswSchedulableEntityBuilder":
        """Add a single item to issued_triggers list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.issued_triggers.append(item)
        return self

    def clear_issued_triggers(self) -> "BswSchedulableEntityBuilder":
        """Clear all items from issued_triggers list.

        Returns:
            self for method chaining
        """
        self._obj.issued_triggers = []
        return self

    def add_managed_mode_group(self, item: ModeDeclarationGroupPrototype) -> "BswSchedulableEntityBuilder":
        """Add a single item to managed_mode_groups list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.managed_mode_groups.append(item)
        return self

    def clear_managed_mode_groups(self) -> "BswSchedulableEntityBuilder":
        """Clear all items from managed_mode_groups list.

        Returns:
            self for method chaining
        """
        self._obj.managed_mode_groups = []
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


    def build(self) -> BswSchedulableEntity:
        """Build and return the BswSchedulableEntity instance with validation."""
        self._validate_instance()
        pass
        return self._obj