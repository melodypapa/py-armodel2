"""NvBlockDescriptor AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 669)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_NvBlockComponent.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
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
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Constants.constant_specification_mapping_set import (
    ConstantSpecificationMappingSet,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.data_type_mapping_set import (
    DataTypeMappingSet,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.InstantiationDataDefProps.instantiation_data_def_props import (
    InstantiationDataDefProps,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent.mode_switch_event_triggered_activity import (
    ModeSwitchEventTriggeredActivity,
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
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.role_based_data_assignment import (
    RoleBasedDataAssignment,
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

    _XML_TAG = "NV-BLOCK-DESCRIPTOR"


    client_server_ports: list[RoleBasedPortAssignment]
    constant_value_mapping_refs: list[ARRef]
    data_type_mapping_refs: list[ARRef]
    instantiation_data_def_propses: list[InstantiationDataDefProps]
    mode_switch_event_triggered_activities: list[ModeSwitchEventTriggeredActivity]
    nv_block_data_mappings: list[NvBlockDataMapping]
    nv_block_needs: Optional[NvBlockNeeds]
    ram_block: Optional[VariableDataPrototype]
    rom_block: Optional[ParameterDataPrototype]
    support_dirty_flag: Optional[Boolean]
    timing_event_ref: Optional[ARRef]
    writing_strategies: list[RoleBasedDataAssignment]
    _DESERIALIZE_DISPATCH = {
        "CLIENT-SERVER-PORTS": lambda obj, elem: obj.client_server_ports.append(SerializationHelper.deserialize_by_tag(elem, "RoleBasedPortAssignment")),
        "CONSTANT-VALUE-MAPPING-REFS": lambda obj, elem: [obj.constant_value_mapping_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "DATA-TYPE-MAPPING-REFS": lambda obj, elem: [obj.data_type_mapping_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "INSTANTIATION-DATA-DEF-PROPSS": lambda obj, elem: obj.instantiation_data_def_propses.append(SerializationHelper.deserialize_by_tag(elem, "InstantiationDataDefProps")),
        "MODE-SWITCH-EVENT-TRIGGERED-ACTIVITYS": lambda obj, elem: obj.mode_switch_event_triggered_activities.append(SerializationHelper.deserialize_by_tag(elem, "ModeSwitchEventTriggeredActivity")),
        "NV-BLOCK-DATA-MAPPINGS": lambda obj, elem: obj.nv_block_data_mappings.append(SerializationHelper.deserialize_by_tag(elem, "NvBlockDataMapping")),
        "NV-BLOCK-NEEDS": lambda obj, elem: setattr(obj, "nv_block_needs", SerializationHelper.deserialize_by_tag(elem, "NvBlockNeeds")),
        "RAM-BLOCK": lambda obj, elem: setattr(obj, "ram_block", SerializationHelper.deserialize_by_tag(elem, "VariableDataPrototype")),
        "ROM-BLOCK": lambda obj, elem: setattr(obj, "rom_block", SerializationHelper.deserialize_by_tag(elem, "ParameterDataPrototype")),
        "SUPPORT-DIRTY-FLAG": lambda obj, elem: setattr(obj, "support_dirty_flag", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "TIMING-EVENT-REF": lambda obj, elem: setattr(obj, "timing_event_ref", ARRef.deserialize(elem)),
        "WRITING-STRATEGYS": lambda obj, elem: obj.writing_strategies.append(SerializationHelper.deserialize_by_tag(elem, "RoleBasedDataAssignment")),
    }


    def __init__(self) -> None:
        """Initialize NvBlockDescriptor."""
        super().__init__()
        self.client_server_ports: list[RoleBasedPortAssignment] = []
        self.constant_value_mapping_refs: list[ARRef] = []
        self.data_type_mapping_refs: list[ARRef] = []
        self.instantiation_data_def_propses: list[InstantiationDataDefProps] = []
        self.mode_switch_event_triggered_activities: list[ModeSwitchEventTriggeredActivity] = []
        self.nv_block_data_mappings: list[NvBlockDataMapping] = []
        self.nv_block_needs: Optional[NvBlockNeeds] = None
        self.ram_block: Optional[VariableDataPrototype] = None
        self.rom_block: Optional[ParameterDataPrototype] = None
        self.support_dirty_flag: Optional[Boolean] = None
        self.timing_event_ref: Optional[ARRef] = None
        self.writing_strategies: list[RoleBasedDataAssignment] = []

    def serialize(self) -> ET.Element:
        """Serialize NvBlockDescriptor to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Serialize instantiation_data_def_propses (list to container "INSTANTIATION-DATA-DEF-PROPSS")
        if self.instantiation_data_def_propses:
            wrapper = ET.Element("INSTANTIATION-DATA-DEF-PROPSS")
            for item in self.instantiation_data_def_propses:
                serialized = SerializationHelper.serialize_item(item, "InstantiationDataDefProps")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize mode_switch_event_triggered_activities (list to container "MODE-SWITCH-EVENT-TRIGGERED-ACTIVITYS")
        if self.mode_switch_event_triggered_activities:
            wrapper = ET.Element("MODE-SWITCH-EVENT-TRIGGERED-ACTIVITYS")
            for item in self.mode_switch_event_triggered_activities:
                serialized = SerializationHelper.serialize_item(item, "ModeSwitchEventTriggeredActivity")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize nv_block_data_mappings (list to container "NV-BLOCK-DATA-MAPPINGS")
        if self.nv_block_data_mappings:
            wrapper = ET.Element("NV-BLOCK-DATA-MAPPINGS")
            for item in self.nv_block_data_mappings:
                serialized = SerializationHelper.serialize_item(item, "NvBlockDataMapping")
                if serialized is not None:
                    wrapper.append(serialized)
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

        # Serialize ram_block
        if self.ram_block is not None:
            serialized = SerializationHelper.serialize_item(self.ram_block, "VariableDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RAM-BLOCK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rom_block
        if self.rom_block is not None:
            serialized = SerializationHelper.serialize_item(self.rom_block, "ParameterDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ROM-BLOCK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize support_dirty_flag
        if self.support_dirty_flag is not None:
            serialized = SerializationHelper.serialize_item(self.support_dirty_flag, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SUPPORT-DIRTY-FLAG")
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
                serialized = SerializationHelper.serialize_item(item, "RoleBasedDataAssignment")
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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CLIENT-SERVER-PORTS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.client_server_ports.append(SerializationHelper.deserialize_by_tag(item_elem, "RoleBasedPortAssignment"))
            elif tag == "CONSTANT-VALUE-MAPPING-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.constant_value_mapping_refs.append(ARRef.deserialize(item_elem))
            elif tag == "DATA-TYPE-MAPPING-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.data_type_mapping_refs.append(ARRef.deserialize(item_elem))
            elif tag == "INSTANTIATION-DATA-DEF-PROPSS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.instantiation_data_def_propses.append(SerializationHelper.deserialize_by_tag(item_elem, "InstantiationDataDefProps"))
            elif tag == "MODE-SWITCH-EVENT-TRIGGERED-ACTIVITYS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.mode_switch_event_triggered_activities.append(SerializationHelper.deserialize_by_tag(item_elem, "ModeSwitchEventTriggeredActivity"))
            elif tag == "NV-BLOCK-DATA-MAPPINGS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.nv_block_data_mappings.append(SerializationHelper.deserialize_by_tag(item_elem, "NvBlockDataMapping"))
            elif tag == "NV-BLOCK-NEEDS":
                setattr(obj, "nv_block_needs", SerializationHelper.deserialize_by_tag(child, "NvBlockNeeds"))
            elif tag == "RAM-BLOCK":
                setattr(obj, "ram_block", SerializationHelper.deserialize_by_tag(child, "VariableDataPrototype"))
            elif tag == "ROM-BLOCK":
                setattr(obj, "rom_block", SerializationHelper.deserialize_by_tag(child, "ParameterDataPrototype"))
            elif tag == "SUPPORT-DIRTY-FLAG":
                setattr(obj, "support_dirty_flag", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "TIMING-EVENT-REF":
                setattr(obj, "timing_event_ref", ARRef.deserialize(child))
            elif tag == "WRITING-STRATEGYS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.writing_strategies.append(SerializationHelper.deserialize_by_tag(item_elem, "RoleBasedDataAssignment"))

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

    def with_constant_value_mappings(self, items: list[ConstantSpecificationMappingSet]) -> "NvBlockDescriptorBuilder":
        """Set constant_value_mappings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.constant_value_mappings = list(items) if items else []
        return self

    def with_data_type_mappings(self, items: list[DataTypeMappingSet]) -> "NvBlockDescriptorBuilder":
        """Set data_type_mappings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.data_type_mappings = list(items) if items else []
        return self

    def with_instantiation_data_def_propses(self, items: list[InstantiationDataDefProps]) -> "NvBlockDescriptorBuilder":
        """Set instantiation_data_def_propses list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.instantiation_data_def_propses = list(items) if items else []
        return self

    def with_mode_switch_event_triggered_activities(self, items: list[ModeSwitchEventTriggeredActivity]) -> "NvBlockDescriptorBuilder":
        """Set mode_switch_event_triggered_activities list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.mode_switch_event_triggered_activities = list(items) if items else []
        return self

    def with_nv_block_data_mappings(self, items: list[NvBlockDataMapping]) -> "NvBlockDescriptorBuilder":
        """Set nv_block_data_mappings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.nv_block_data_mappings = list(items) if items else []
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

    def with_support_dirty_flag(self, value: Optional[Boolean]) -> "NvBlockDescriptorBuilder":
        """Set support_dirty_flag attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.support_dirty_flag = value
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

    def with_writing_strategies(self, items: list[RoleBasedDataAssignment]) -> "NvBlockDescriptorBuilder":
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

    def add_constant_value_mapping(self, item: ConstantSpecificationMappingSet) -> "NvBlockDescriptorBuilder":
        """Add a single item to constant_value_mappings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.constant_value_mappings.append(item)
        return self

    def clear_constant_value_mappings(self) -> "NvBlockDescriptorBuilder":
        """Clear all items from constant_value_mappings list.

        Returns:
            self for method chaining
        """
        self._obj.constant_value_mappings = []
        return self

    def add_data_type_mapping(self, item: DataTypeMappingSet) -> "NvBlockDescriptorBuilder":
        """Add a single item to data_type_mappings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.data_type_mappings.append(item)
        return self

    def clear_data_type_mappings(self) -> "NvBlockDescriptorBuilder":
        """Clear all items from data_type_mappings list.

        Returns:
            self for method chaining
        """
        self._obj.data_type_mappings = []
        return self

    def add_instantiation_data_def_props(self, item: InstantiationDataDefProps) -> "NvBlockDescriptorBuilder":
        """Add a single item to instantiation_data_def_propses list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.instantiation_data_def_propses.append(item)
        return self

    def clear_instantiation_data_def_propses(self) -> "NvBlockDescriptorBuilder":
        """Clear all items from instantiation_data_def_propses list.

        Returns:
            self for method chaining
        """
        self._obj.instantiation_data_def_propses = []
        return self

    def add_mode_switch_event_triggered_activity(self, item: ModeSwitchEventTriggeredActivity) -> "NvBlockDescriptorBuilder":
        """Add a single item to mode_switch_event_triggered_activities list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.mode_switch_event_triggered_activities.append(item)
        return self

    def clear_mode_switch_event_triggered_activities(self) -> "NvBlockDescriptorBuilder":
        """Clear all items from mode_switch_event_triggered_activities list.

        Returns:
            self for method chaining
        """
        self._obj.mode_switch_event_triggered_activities = []
        return self

    def add_nv_block_data_mapping(self, item: NvBlockDataMapping) -> "NvBlockDescriptorBuilder":
        """Add a single item to nv_block_data_mappings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.nv_block_data_mappings.append(item)
        return self

    def clear_nv_block_data_mappings(self) -> "NvBlockDescriptorBuilder":
        """Clear all items from nv_block_data_mappings list.

        Returns:
            self for method chaining
        """
        self._obj.nv_block_data_mappings = []
        return self

    def add_writing_strategy(self, item: RoleBasedDataAssignment) -> "NvBlockDescriptorBuilder":
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