"""NvBlockSwComponentType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 663)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2040)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.atomic_sw_component_type import (
    AtomicSwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent.bulk_nv_data_descriptor import (
    BulkNvDataDescriptor,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent.nv_block_descriptor import (
    NvBlockDescriptor,
)


class NvBlockSwComponentType(AtomicSwComponentType):
    """AUTOSAR NvBlockSwComponentType."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    bulk_nv_datas: list[BulkNvDataDescriptor]
    nv_blocks: list[NvBlockDescriptor]
    def __init__(self) -> None:
        """Initialize NvBlockSwComponentType."""
        super().__init__()
        self.bulk_nv_datas: list[BulkNvDataDescriptor] = []
        self.nv_blocks: list[NvBlockDescriptor] = []

    def serialize(self) -> ET.Element:
        """Serialize NvBlockSwComponentType to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(NvBlockSwComponentType, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize bulk_nv_datas (list to container "BULK-NV-DATAS")
        if self.bulk_nv_datas:
            wrapper = ET.Element("BULK-NV-DATAS")
            for item in self.bulk_nv_datas:
                serialized = SerializationHelper.serialize_item(item, "BulkNvDataDescriptor")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize nv_blocks (list to container "NV-BLOCKS")
        if self.nv_blocks:
            wrapper = ET.Element("NV-BLOCKS")
            for item in self.nv_blocks:
                serialized = SerializationHelper.serialize_item(item, "NvBlockDescriptor")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "NvBlockSwComponentType":
        """Deserialize XML element to NvBlockSwComponentType object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized NvBlockSwComponentType object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(NvBlockSwComponentType, cls).deserialize(element)

        # Parse bulk_nv_datas (list from container "BULK-NV-DATAS")
        obj.bulk_nv_datas = []
        container = SerializationHelper.find_child_element(element, "BULK-NV-DATAS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.bulk_nv_datas.append(child_value)

        # Parse nv_blocks (list from container "NV-BLOCKS")
        obj.nv_blocks = []
        container = SerializationHelper.find_child_element(element, "NV-BLOCKS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.nv_blocks.append(child_value)

        return obj



class NvBlockSwComponentTypeBuilder:
    """Builder for NvBlockSwComponentType with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: NvBlockSwComponentType = NvBlockSwComponentType()


    def with_short_name(self, value: Identifier) -> "NvBlockSwComponentTypeBuilder":
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

    def with_short_name_fragments(self, items: list[ShortNameFragment]) -> "NvBlockSwComponentTypeBuilder":
        """Set short_name_fragments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = list(items) if items else []
        return self

    def with_long_name(self, value: Optional[MultilanguageLongName]) -> "NvBlockSwComponentTypeBuilder":
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

    def with_admin_data(self, value: Optional[AdminData]) -> "NvBlockSwComponentTypeBuilder":
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

    def with_annotations(self, items: list[Annotation]) -> "NvBlockSwComponentTypeBuilder":
        """Set annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.annotations = list(items) if items else []
        return self

    def with_desc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "NvBlockSwComponentTypeBuilder":
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

    def with_category(self, value: Optional[CategoryString]) -> "NvBlockSwComponentTypeBuilder":
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

    def with_introduction(self, value: Optional[DocumentationBlock]) -> "NvBlockSwComponentTypeBuilder":
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

    def with_uuid(self, value: Optional[String]) -> "NvBlockSwComponentTypeBuilder":
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

    def with_consistency_needses(self, items: list[ConsistencyNeeds]) -> "NvBlockSwComponentTypeBuilder":
        """Set consistency_needses list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.consistency_needses = list(items) if items else []
        return self

    def with_ports(self, items: list[PortPrototype]) -> "NvBlockSwComponentTypeBuilder":
        """Set ports list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.ports = list(items) if items else []
        return self

    def with_port_groups(self, items: list[PortGroup]) -> "NvBlockSwComponentTypeBuilder":
        """Set port_groups list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.port_groups = list(items) if items else []
        return self

    def with_swc_mapping_constraints(self, items: list[SwComponentMappingConstraints]) -> "NvBlockSwComponentTypeBuilder":
        """Set swc_mapping_constraints list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.swc_mapping_constraints = list(items) if items else []
        return self

    def with_sw_component_documentation(self, value: Optional[SwComponentDocumentation]) -> "NvBlockSwComponentTypeBuilder":
        """Set sw_component_documentation attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_component_documentation = value
        return self

    def with_unit_groups(self, items: list[UnitGroup]) -> "NvBlockSwComponentTypeBuilder":
        """Set unit_groups list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.unit_groups = list(items) if items else []
        return self

    def with_internal_behavior(self, value: Optional[SwcInternalBehavior]) -> "NvBlockSwComponentTypeBuilder":
        """Set internal_behavior attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.internal_behavior = value
        return self

    def with_symbol_props(self, value: Optional[SymbolProps]) -> "NvBlockSwComponentTypeBuilder":
        """Set symbol_props attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.symbol_props = value
        return self

    def with_bulk_nv_datas(self, items: list[BulkNvDataDescriptor]) -> "NvBlockSwComponentTypeBuilder":
        """Set bulk_nv_datas list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.bulk_nv_datas = list(items) if items else []
        return self

    def with_nv_blocks(self, items: list[NvBlockDescriptor]) -> "NvBlockSwComponentTypeBuilder":
        """Set nv_blocks list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.nv_blocks = list(items) if items else []
        return self


    def add_short_name_fragment(self, item: ShortNameFragment) -> "NvBlockSwComponentTypeBuilder":
        """Add a single item to short_name_fragments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments.append(item)
        return self

    def clear_short_name_fragments(self) -> "NvBlockSwComponentTypeBuilder":
        """Clear all items from short_name_fragments list.

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = []
        return self

    def add_annotation(self, item: Annotation) -> "NvBlockSwComponentTypeBuilder":
        """Add a single item to annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.annotations.append(item)
        return self

    def clear_annotations(self) -> "NvBlockSwComponentTypeBuilder":
        """Clear all items from annotations list.

        Returns:
            self for method chaining
        """
        self._obj.annotations = []
        return self

    def add_consistency_needse(self, item: ConsistencyNeeds) -> "NvBlockSwComponentTypeBuilder":
        """Add a single item to consistency_needses list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.consistency_needses.append(item)
        return self

    def clear_consistency_needses(self) -> "NvBlockSwComponentTypeBuilder":
        """Clear all items from consistency_needses list.

        Returns:
            self for method chaining
        """
        self._obj.consistency_needses = []
        return self

    def add_port(self, item: PortPrototype) -> "NvBlockSwComponentTypeBuilder":
        """Add a single item to ports list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.ports.append(item)
        return self

    def clear_ports(self) -> "NvBlockSwComponentTypeBuilder":
        """Clear all items from ports list.

        Returns:
            self for method chaining
        """
        self._obj.ports = []
        return self

    def add_port_group(self, item: PortGroup) -> "NvBlockSwComponentTypeBuilder":
        """Add a single item to port_groups list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.port_groups.append(item)
        return self

    def clear_port_groups(self) -> "NvBlockSwComponentTypeBuilder":
        """Clear all items from port_groups list.

        Returns:
            self for method chaining
        """
        self._obj.port_groups = []
        return self

    def add_swc_mapping_constraint(self, item: SwComponentMappingConstraints) -> "NvBlockSwComponentTypeBuilder":
        """Add a single item to swc_mapping_constraints list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.swc_mapping_constraints.append(item)
        return self

    def clear_swc_mapping_constraints(self) -> "NvBlockSwComponentTypeBuilder":
        """Clear all items from swc_mapping_constraints list.

        Returns:
            self for method chaining
        """
        self._obj.swc_mapping_constraints = []
        return self

    def add_unit_group(self, item: UnitGroup) -> "NvBlockSwComponentTypeBuilder":
        """Add a single item to unit_groups list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.unit_groups.append(item)
        return self

    def clear_unit_groups(self) -> "NvBlockSwComponentTypeBuilder":
        """Clear all items from unit_groups list.

        Returns:
            self for method chaining
        """
        self._obj.unit_groups = []
        return self

    def add_bulk_nv_data(self, item: BulkNvDataDescriptor) -> "NvBlockSwComponentTypeBuilder":
        """Add a single item to bulk_nv_datas list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.bulk_nv_datas.append(item)
        return self

    def clear_bulk_nv_datas(self) -> "NvBlockSwComponentTypeBuilder":
        """Clear all items from bulk_nv_datas list.

        Returns:
            self for method chaining
        """
        self._obj.bulk_nv_datas = []
        return self

    def add_nv_block(self, item: NvBlockDescriptor) -> "NvBlockSwComponentTypeBuilder":
        """Add a single item to nv_blocks list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.nv_blocks.append(item)
        return self

    def clear_nv_blocks(self) -> "NvBlockSwComponentTypeBuilder":
        """Clear all items from nv_blocks list.

        Returns:
            self for method chaining
        """
        self._obj.nv_blocks = []
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


    def build(self) -> NvBlockSwComponentType:
        """Build and return the NvBlockSwComponentType instance with validation."""
        self._validate_instance()
        pass
        return self._obj