"""NvBlockDescriptor AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 669)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_NvBlockComponent.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Constants.constant_specification import (
    ConstantSpecification,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.data_type_mapping_set import (
    DataTypeMappingSet,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.InstantiationDataDefProps.instantiation_data_def_props import (
    InstantiationDataDefProps,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent.nv_block_data_mapping import (
    NvBlockDataMapping,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.nv_block_needs import (
    NvBlockNeeds,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.parameter_data_prototype import (
    ParameterDataPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServiceMapping.role_based_port_assignment import (
    RoleBasedPortAssignment,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.timing_event import (
    TimingEvent,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class NvBlockDescriptor(Identifiable):
    """AUTOSAR NvBlockDescriptor."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    client_server_ports: list[RoleBasedPortAssignment]
    constant_value_refs: list[ARRef]
    data_type_refs: list[ARRef]
    instantiation_data_defs: list[InstantiationDataDefProps]
    mode_switch_events: list[Any]
    nv_block_data_refs: list[ARRef]
    nv_block_needs: Optional[NvBlockNeeds]
    ram_block_ref: Optional[ARRef]
    rom_block_ref: Optional[ARRef]
    support_dirty: Optional[Boolean]
    timing_event_ref: Optional[ARRef]
    writing_strategies: list[Any]
    def __init__(self) -> None:
        """Initialize NvBlockDescriptor."""
        super().__init__()
        self.client_server_ports: list[RoleBasedPortAssignment] = []
        self.constant_value_refs: list[ARRef] = []
        self.data_type_refs: list[ARRef] = []
        self.instantiation_data_defs: list[InstantiationDataDefProps] = []
        self.mode_switch_events: list[Any] = []
        self.nv_block_data_refs: list[ARRef] = []
        self.nv_block_needs: Optional[NvBlockNeeds] = None
        self.ram_block_ref: Optional[ARRef] = None
        self.rom_block_ref: Optional[ARRef] = None
        self.support_dirty: Optional[Boolean] = None
        self.timing_event_ref: Optional[ARRef] = None
        self.writing_strategies: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize NvBlockDescriptor to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(NvBlockDescriptor, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize client_server_ports (list to container "CLIENT-SERVER-PORTS")
        if self.client_server_ports:
            wrapper = ET.Element("CLIENT-SERVER-PORTS")
            for item in self.client_server_ports:
                serialized = SerializationHelper.serialize_item(item, "RoleBasedPortAssignment")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize constant_value_refs (list to container "CONSTANT-VALUES")
        if self.constant_value_refs:
            wrapper = ET.Element("CONSTANT-VALUES")
            for item in self.constant_value_refs:
                serialized = SerializationHelper.serialize_item(item, "ConstantSpecification")
                if serialized is not None:
                    child_elem = ET.Element("CONSTANT-VALUE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize data_type_refs (list to container "DATA-TYPES")
        if self.data_type_refs:
            wrapper = ET.Element("DATA-TYPES")
            for item in self.data_type_refs:
                serialized = SerializationHelper.serialize_item(item, "DataTypeMappingSet")
                if serialized is not None:
                    child_elem = ET.Element("DATA-TYPE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize instantiation_data_defs (list to container "INSTANTIATION-DATA-DEFS")
        if self.instantiation_data_defs:
            wrapper = ET.Element("INSTANTIATION-DATA-DEFS")
            for item in self.instantiation_data_defs:
                serialized = SerializationHelper.serialize_item(item, "InstantiationDataDefProps")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize mode_switch_events (list to container "MODE-SWITCH-EVENTS")
        if self.mode_switch_events:
            wrapper = ET.Element("MODE-SWITCH-EVENTS")
            for item in self.mode_switch_events:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize nv_block_data_refs (list to container "NV-BLOCK-DATAS")
        if self.nv_block_data_refs:
            wrapper = ET.Element("NV-BLOCK-DATAS")
            for item in self.nv_block_data_refs:
                serialized = SerializationHelper.serialize_item(item, "NvBlockDataMapping")
                if serialized is not None:
                    child_elem = ET.Element("NV-BLOCK-DATA-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize nv_block_needs
        if self.nv_block_needs is not None:
            serialized = SerializationHelper.serialize_item(self.nv_block_needs, "NvBlockNeeds")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NV-BLOCK-NEEDS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ram_block_ref
        if self.ram_block_ref is not None:
            serialized = SerializationHelper.serialize_item(self.ram_block_ref, "VariableDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RAM-BLOCK-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rom_block_ref
        if self.rom_block_ref is not None:
            serialized = SerializationHelper.serialize_item(self.rom_block_ref, "ParameterDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ROM-BLOCK-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize support_dirty
        if self.support_dirty is not None:
            serialized = SerializationHelper.serialize_item(self.support_dirty, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SUPPORT-DIRTY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize timing_event_ref
        if self.timing_event_ref is not None:
            serialized = SerializationHelper.serialize_item(self.timing_event_ref, "TimingEvent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMING-EVENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize writing_strategies (list to container "WRITING-STRATEGYS")
        if self.writing_strategies:
            wrapper = ET.Element("WRITING-STRATEGYS")
            for item in self.writing_strategies:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "NvBlockDescriptor":
        """Deserialize XML element to NvBlockDescriptor object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized NvBlockDescriptor object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(NvBlockDescriptor, cls).deserialize(element)

        # Parse client_server_ports (list from container "CLIENT-SERVER-PORTS")
        obj.client_server_ports = []
        container = SerializationHelper.find_child_element(element, "CLIENT-SERVER-PORTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.client_server_ports.append(child_value)

        # Parse constant_value_refs (list from container "CONSTANT-VALUES")
        obj.constant_value_refs = []
        container = SerializationHelper.find_child_element(element, "CONSTANT-VALUES")
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
                    obj.constant_value_refs.append(child_value)

        # Parse data_type_refs (list from container "DATA-TYPES")
        obj.data_type_refs = []
        container = SerializationHelper.find_child_element(element, "DATA-TYPES")
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
                    obj.data_type_refs.append(child_value)

        # Parse instantiation_data_defs (list from container "INSTANTIATION-DATA-DEFS")
        obj.instantiation_data_defs = []
        container = SerializationHelper.find_child_element(element, "INSTANTIATION-DATA-DEFS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.instantiation_data_defs.append(child_value)

        # Parse mode_switch_events (list from container "MODE-SWITCH-EVENTS")
        obj.mode_switch_events = []
        container = SerializationHelper.find_child_element(element, "MODE-SWITCH-EVENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mode_switch_events.append(child_value)

        # Parse nv_block_data_refs (list from container "NV-BLOCK-DATAS")
        obj.nv_block_data_refs = []
        container = SerializationHelper.find_child_element(element, "NV-BLOCK-DATAS")
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
                    obj.nv_block_data_refs.append(child_value)

        # Parse nv_block_needs
        child = SerializationHelper.find_child_element(element, "NV-BLOCK-NEEDS")
        if child is not None:
            nv_block_needs_value = SerializationHelper.deserialize_by_tag(child, "NvBlockNeeds")
            obj.nv_block_needs = nv_block_needs_value

        # Parse ram_block_ref
        child = SerializationHelper.find_child_element(element, "RAM-BLOCK-REF")
        if child is not None:
            ram_block_ref_value = ARRef.deserialize(child)
            obj.ram_block_ref = ram_block_ref_value

        # Parse rom_block_ref
        child = SerializationHelper.find_child_element(element, "ROM-BLOCK-REF")
        if child is not None:
            rom_block_ref_value = ARRef.deserialize(child)
            obj.rom_block_ref = rom_block_ref_value

        # Parse support_dirty
        child = SerializationHelper.find_child_element(element, "SUPPORT-DIRTY")
        if child is not None:
            support_dirty_value = child.text
            obj.support_dirty = support_dirty_value

        # Parse timing_event_ref
        child = SerializationHelper.find_child_element(element, "TIMING-EVENT-REF")
        if child is not None:
            timing_event_ref_value = ARRef.deserialize(child)
            obj.timing_event_ref = timing_event_ref_value

        # Parse writing_strategies (list from container "WRITING-STRATEGYS")
        obj.writing_strategies = []
        container = SerializationHelper.find_child_element(element, "WRITING-STRATEGYS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.writing_strategies.append(child_value)

        return obj



class NvBlockDescriptorBuilder(IdentifiableBuilder):
    """Builder for NvBlockDescriptor with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: NvBlockDescriptor = NvBlockDescriptor()


    def with_client_server_ports(self, items: list[RoleBasedPortAssignment]) -> "NvBlockDescriptorBuilder":
        """Set client_server_ports list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.client_server_ports = list(items) if items else []
        return self

    def with_constant_values(self, items: list[ConstantSpecification]) -> "NvBlockDescriptorBuilder":
        """Set constant_values list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.constant_values = list(items) if items else []
        return self

    def with_data_types(self, items: list[DataTypeMappingSet]) -> "NvBlockDescriptorBuilder":
        """Set data_types list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.data_types = list(items) if items else []
        return self

    def with_instantiation_data_defs(self, items: list[InstantiationDataDefProps]) -> "NvBlockDescriptorBuilder":
        """Set instantiation_data_defs list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.instantiation_data_defs = list(items) if items else []
        return self

    def with_mode_switch_events(self, items: list[any (ModeSwitchEvent)]) -> "NvBlockDescriptorBuilder":
        """Set mode_switch_events list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.mode_switch_events = list(items) if items else []
        return self

    def with_nv_block_datas(self, items: list[NvBlockDataMapping]) -> "NvBlockDescriptorBuilder":
        """Set nv_block_datas list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.nv_block_datas = list(items) if items else []
        return self

    def with_nv_block_needs(self, value: Optional[NvBlockNeeds]) -> "NvBlockDescriptorBuilder":
        """Set nv_block_needs attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nv_block_needs = value
        return self

    def with_ram_block(self, value: Optional[VariableDataPrototype]) -> "NvBlockDescriptorBuilder":
        """Set ram_block attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ram_block = value
        return self

    def with_rom_block(self, value: Optional[ParameterDataPrototype]) -> "NvBlockDescriptorBuilder":
        """Set rom_block attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.rom_block = value
        return self

    def with_support_dirty(self, value: Optional[Boolean]) -> "NvBlockDescriptorBuilder":
        """Set support_dirty attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.support_dirty = value
        return self

    def with_timing_event(self, value: Optional[TimingEvent]) -> "NvBlockDescriptorBuilder":
        """Set timing_event attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.timing_event = value
        return self

    def with_writing_strategies(self, items: list[any (RoleBasedData)]) -> "NvBlockDescriptorBuilder":
        """Set writing_strategies list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.writing_strategies = list(items) if items else []
        return self


    def add_client_server_port(self, item: RoleBasedPortAssignment) -> "NvBlockDescriptorBuilder":
        """Add a single item to client_server_ports list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.client_server_ports.append(item)
        return self

    def clear_client_server_ports(self) -> "NvBlockDescriptorBuilder":
        """Clear all items from client_server_ports list.

        Returns:
            self for method chaining
        """
        self._obj.client_server_ports = []
        return self

    def add_constant_value(self, item: ConstantSpecification) -> "NvBlockDescriptorBuilder":
        """Add a single item to constant_values list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.constant_values.append(item)
        return self

    def clear_constant_values(self) -> "NvBlockDescriptorBuilder":
        """Clear all items from constant_values list.

        Returns:
            self for method chaining
        """
        self._obj.constant_values = []
        return self

    def add_data_type(self, item: DataTypeMappingSet) -> "NvBlockDescriptorBuilder":
        """Add a single item to data_types list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.data_types.append(item)
        return self

    def clear_data_types(self) -> "NvBlockDescriptorBuilder":
        """Clear all items from data_types list.

        Returns:
            self for method chaining
        """
        self._obj.data_types = []
        return self

    def add_instantiation_data_def(self, item: InstantiationDataDefProps) -> "NvBlockDescriptorBuilder":
        """Add a single item to instantiation_data_defs list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.instantiation_data_defs.append(item)
        return self

    def clear_instantiation_data_defs(self) -> "NvBlockDescriptorBuilder":
        """Clear all items from instantiation_data_defs list.

        Returns:
            self for method chaining
        """
        self._obj.instantiation_data_defs = []
        return self

    def add_mode_switch_event(self, item: any (ModeSwitchEvent)) -> "NvBlockDescriptorBuilder":
        """Add a single item to mode_switch_events list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.mode_switch_events.append(item)
        return self

    def clear_mode_switch_events(self) -> "NvBlockDescriptorBuilder":
        """Clear all items from mode_switch_events list.

        Returns:
            self for method chaining
        """
        self._obj.mode_switch_events = []
        return self

    def add_nv_block_data(self, item: NvBlockDataMapping) -> "NvBlockDescriptorBuilder":
        """Add a single item to nv_block_datas list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.nv_block_datas.append(item)
        return self

    def clear_nv_block_datas(self) -> "NvBlockDescriptorBuilder":
        """Clear all items from nv_block_datas list.

        Returns:
            self for method chaining
        """
        self._obj.nv_block_datas = []
        return self

    def add_writing_strategy(self, item: any (RoleBasedData)) -> "NvBlockDescriptorBuilder":
        """Add a single item to writing_strategies list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.writing_strategies.append(item)
        return self

    def clear_writing_strategies(self) -> "NvBlockDescriptorBuilder":
        """Clear all items from writing_strategies list.

        Returns:
            self for method chaining
        """
        self._obj.writing_strategies = []
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


    def build(self) -> NvBlockDescriptor:
        """Build and return the NvBlockDescriptor instance with validation."""
        self._validate_instance()
        pass
        return self._obj