"""InternalBehavior AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 64)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 319)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 516)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2033)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 231)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 453)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_InternalBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Constants.constant_specification_mapping_set import (
    ConstantSpecificationMappingSet,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.exclusive_area import (
    ExclusiveArea,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.exclusive_area_nesting_order import (
    ExclusiveAreaNestingOrder,
)

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.data_type_mapping_set import (
        DataTypeMappingSet,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.parameter_data_prototype import (
        ParameterDataPrototype,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
        VariableDataPrototype,
    )



from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class InternalBehavior(Identifiable, ABC):
    """AUTOSAR InternalBehavior."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    constant_memories: list[ParameterDataPrototype]
    constant_value_mapping_refs: list[ARRef]
    data_type_mapping_refs: list[ARRef]
    exclusive_areas: list[ExclusiveArea]
    exclusive_area_nesting_orders: list[ExclusiveAreaNestingOrder]
    static_memories: list[VariableDataPrototype]
    _DESERIALIZE_DISPATCH = {
        "CONSTANT-MEMORIES": lambda obj, elem: obj.constant_memories.append(SerializationHelper.deserialize_by_tag(elem, "ParameterDataPrototype")),
        "CONSTANT-VALUE-MAPPINGS": lambda obj, elem: obj.constant_value_mapping_refs.append(ARRef.deserialize(elem)),
        "DATA-TYPE-MAPPINGS": lambda obj, elem: obj.data_type_mapping_refs.append(ARRef.deserialize(elem)),
        "EXCLUSIVE-AREAS": lambda obj, elem: obj.exclusive_areas.append(SerializationHelper.deserialize_by_tag(elem, "ExclusiveArea")),
        "EXCLUSIVE-AREA-NESTING-ORDERS": lambda obj, elem: obj.exclusive_area_nesting_orders.append(SerializationHelper.deserialize_by_tag(elem, "ExclusiveAreaNestingOrder")),
        "STATIC-MEMORIES": lambda obj, elem: obj.static_memories.append(SerializationHelper.deserialize_by_tag(elem, "VariableDataPrototype")),
    }


    def __init__(self) -> None:
        """Initialize InternalBehavior."""
        super().__init__()
        self.constant_memories: list[ParameterDataPrototype] = []
        self.constant_value_mapping_refs: list[ARRef] = []
        self.data_type_mapping_refs: list[ARRef] = []
        self.exclusive_areas: list[ExclusiveArea] = []
        self.exclusive_area_nesting_orders: list[ExclusiveAreaNestingOrder] = []
        self.static_memories: list[VariableDataPrototype] = []

    def serialize(self) -> ET.Element:
        """Serialize InternalBehavior to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(InternalBehavior, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize constant_memories (list to container "CONSTANT-MEMORIES")
        if self.constant_memories:
            wrapper = ET.Element("CONSTANT-MEMORIES")
            for item in self.constant_memories:
                serialized = SerializationHelper.serialize_item(item, "ParameterDataPrototype")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize constant_value_mapping_refs (list to container "CONSTANT-VALUE-MAPPING-REFS")
        if self.constant_value_mapping_refs:
            wrapper = ET.Element("CONSTANT-VALUE-MAPPING-REFS")
            for item in self.constant_value_mapping_refs:
                serialized = SerializationHelper.serialize_item(item, "ConstantSpecificationMappingSet")
                if serialized is not None:
                    child_elem = ET.Element("CONSTANT-VALUE-MAPPING-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize data_type_mapping_refs (list to container "DATA-TYPE-MAPPING-REFS")
        if self.data_type_mapping_refs:
            wrapper = ET.Element("DATA-TYPE-MAPPING-REFS")
            for item in self.data_type_mapping_refs:
                serialized = SerializationHelper.serialize_item(item, "DataTypeMappingSet")
                if serialized is not None:
                    child_elem = ET.Element("DATA-TYPE-MAPPING-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize exclusive_areas (list to container "EXCLUSIVE-AREAS")
        if self.exclusive_areas:
            wrapper = ET.Element("EXCLUSIVE-AREAS")
            for item in self.exclusive_areas:
                serialized = SerializationHelper.serialize_item(item, "ExclusiveArea")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize exclusive_area_nesting_orders (list to container "EXCLUSIVE-AREA-NESTING-ORDERS")
        if self.exclusive_area_nesting_orders:
            wrapper = ET.Element("EXCLUSIVE-AREA-NESTING-ORDERS")
            for item in self.exclusive_area_nesting_orders:
                serialized = SerializationHelper.serialize_item(item, "ExclusiveAreaNestingOrder")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize static_memories (list to container "STATIC-MEMORIES")
        if self.static_memories:
            wrapper = ET.Element("STATIC-MEMORIES")
            for item in self.static_memories:
                serialized = SerializationHelper.serialize_item(item, "VariableDataPrototype")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "InternalBehavior":
        """Deserialize XML element to InternalBehavior object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized InternalBehavior object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(InternalBehavior, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CONSTANT-MEMORIES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.constant_memories.append(SerializationHelper.deserialize_by_tag(item_elem, "ParameterDataPrototype"))
            elif tag == "CONSTANT-VALUE-MAPPINGS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.constant_value_mapping_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "ConstantSpecificationMappingSet"))
            elif tag == "DATA-TYPE-MAPPINGS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.data_type_mapping_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "DataTypeMappingSet"))
            elif tag == "EXCLUSIVE-AREAS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.exclusive_areas.append(SerializationHelper.deserialize_by_tag(item_elem, "ExclusiveArea"))
            elif tag == "EXCLUSIVE-AREA-NESTING-ORDERS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.exclusive_area_nesting_orders.append(SerializationHelper.deserialize_by_tag(item_elem, "ExclusiveAreaNestingOrder"))
            elif tag == "STATIC-MEMORIES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.static_memories.append(SerializationHelper.deserialize_by_tag(item_elem, "VariableDataPrototype"))

        return obj



class InternalBehaviorBuilder(IdentifiableBuilder):
    """Builder for InternalBehavior with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: InternalBehavior = InternalBehavior()


    def with_constant_memories(self, items: list[ParameterDataPrototype]) -> "InternalBehaviorBuilder":
        """Set constant_memories list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.constant_memories = list(items) if items else []
        return self

    def with_constant_value_mappings(self, items: list[ConstantSpecificationMappingSet]) -> "InternalBehaviorBuilder":
        """Set constant_value_mappings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.constant_value_mappings = list(items) if items else []
        return self

    def with_data_type_mappings(self, items: list[DataTypeMappingSet]) -> "InternalBehaviorBuilder":
        """Set data_type_mappings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.data_type_mappings = list(items) if items else []
        return self

    def with_exclusive_areas(self, items: list[ExclusiveArea]) -> "InternalBehaviorBuilder":
        """Set exclusive_areas list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.exclusive_areas = list(items) if items else []
        return self

    def with_exclusive_area_nesting_orders(self, items: list[ExclusiveAreaNestingOrder]) -> "InternalBehaviorBuilder":
        """Set exclusive_area_nesting_orders list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.exclusive_area_nesting_orders = list(items) if items else []
        return self

    def with_static_memories(self, items: list[VariableDataPrototype]) -> "InternalBehaviorBuilder":
        """Set static_memories list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.static_memories = list(items) if items else []
        return self


    def add_constant_memory(self, item: ParameterDataPrototype) -> "InternalBehaviorBuilder":
        """Add a single item to constant_memories list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.constant_memories.append(item)
        return self

    def clear_constant_memories(self) -> "InternalBehaviorBuilder":
        """Clear all items from constant_memories list.

        Returns:
            self for method chaining
        """
        self._obj.constant_memories = []
        return self

    def add_constant_value_mapping(self, item: ConstantSpecificationMappingSet) -> "InternalBehaviorBuilder":
        """Add a single item to constant_value_mappings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.constant_value_mappings.append(item)
        return self

    def clear_constant_value_mappings(self) -> "InternalBehaviorBuilder":
        """Clear all items from constant_value_mappings list.

        Returns:
            self for method chaining
        """
        self._obj.constant_value_mappings = []
        return self

    def add_data_type_mapping(self, item: DataTypeMappingSet) -> "InternalBehaviorBuilder":
        """Add a single item to data_type_mappings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.data_type_mappings.append(item)
        return self

    def clear_data_type_mappings(self) -> "InternalBehaviorBuilder":
        """Clear all items from data_type_mappings list.

        Returns:
            self for method chaining
        """
        self._obj.data_type_mappings = []
        return self

    def add_exclusive_area(self, item: ExclusiveArea) -> "InternalBehaviorBuilder":
        """Add a single item to exclusive_areas list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.exclusive_areas.append(item)
        return self

    def clear_exclusive_areas(self) -> "InternalBehaviorBuilder":
        """Clear all items from exclusive_areas list.

        Returns:
            self for method chaining
        """
        self._obj.exclusive_areas = []
        return self

    def add_exclusive_area_nesting_order(self, item: ExclusiveAreaNestingOrder) -> "InternalBehaviorBuilder":
        """Add a single item to exclusive_area_nesting_orders list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.exclusive_area_nesting_orders.append(item)
        return self

    def clear_exclusive_area_nesting_orders(self) -> "InternalBehaviorBuilder":
        """Clear all items from exclusive_area_nesting_orders list.

        Returns:
            self for method chaining
        """
        self._obj.exclusive_area_nesting_orders = []
        return self

    def add_static_memory(self, item: VariableDataPrototype) -> "InternalBehaviorBuilder":
        """Add a single item to static_memories list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.static_memories.append(item)
        return self

    def clear_static_memories(self) -> "InternalBehaviorBuilder":
        """Clear all items from static_memories list.

        Returns:
            self for method chaining
        """
        self._obj.static_memories = []
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


    @abstractmethod
    def build(self) -> InternalBehavior:
        """Build and return the InternalBehavior instance (abstract)."""
        raise NotImplementedError