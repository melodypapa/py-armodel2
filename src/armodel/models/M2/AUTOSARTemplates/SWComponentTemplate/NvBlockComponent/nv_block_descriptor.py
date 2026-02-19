"""NvBlockDescriptor AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 669)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_NvBlockComponent.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.constant_specification import (
    ConstantSpecification,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.data_type_mapping_set import (
    DataTypeMappingSet,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.InstantiationDataDefProps.instantiation_data_def_props import (
    InstantiationDataDefProps,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent.nv_block_data_mapping import (
    NvBlockDataMapping,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.nv_block_needs import (
    NvBlockNeeds,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.parameter_data_prototype import (
    ParameterDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServiceMapping.role_based_port_assignment import (
    RoleBasedPortAssignment,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.timing_event import (
    TimingEvent,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


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
    constant_values: list[ConstantSpecification]
    data_type_refs: list[ARRef]
    instantiation_data_defs: list[InstantiationDataDefProps]
    mode_switch_events: list[Any]
    nv_block_data_refs: list[ARRef]
    nv_block_needs: Optional[NvBlockNeeds]
    ram_block_ref: Optional[ARRef]
    rom_block_ref: Optional[ARRef]
    support_dirty: Optional[Boolean]
    timing_event: Optional[TimingEvent]
    writing_strategies: list[Any]
    def __init__(self) -> None:
        """Initialize NvBlockDescriptor."""
        super().__init__()
        self.client_server_ports: list[RoleBasedPortAssignment] = []
        self.constant_values: list[ConstantSpecification] = []
        self.data_type_refs: list[ARRef] = []
        self.instantiation_data_defs: list[InstantiationDataDefProps] = []
        self.mode_switch_events: list[Any] = []
        self.nv_block_data_refs: list[ARRef] = []
        self.nv_block_needs: Optional[NvBlockNeeds] = None
        self.ram_block_ref: Optional[ARRef] = None
        self.rom_block_ref: Optional[ARRef] = None
        self.support_dirty: Optional[Boolean] = None
        self.timing_event: Optional[TimingEvent] = None
        self.writing_strategies: list[Any] = []
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
        container = ARObject._find_child_element(element, "CLIENT-SERVER-PORTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.client_server_ports.append(child_value)

        # Parse constant_values (list from container "CONSTANT-VALUES")
        obj.constant_values = []
        container = ARObject._find_child_element(element, "CONSTANT-VALUES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.constant_values.append(child_value)

        # Parse data_type_refs (list from container "DATA-TYPES")
        obj.data_type_refs = []
        container = ARObject._find_child_element(element, "DATA-TYPES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.data_type_refs.append(child_value)

        # Parse instantiation_data_defs (list from container "INSTANTIATION-DATA-DEFS")
        obj.instantiation_data_defs = []
        container = ARObject._find_child_element(element, "INSTANTIATION-DATA-DEFS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.instantiation_data_defs.append(child_value)

        # Parse mode_switch_events (list from container "MODE-SWITCH-EVENTS")
        obj.mode_switch_events = []
        container = ARObject._find_child_element(element, "MODE-SWITCH-EVENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mode_switch_events.append(child_value)

        # Parse nv_block_data_refs (list from container "NV-BLOCK-DATAS")
        obj.nv_block_data_refs = []
        container = ARObject._find_child_element(element, "NV-BLOCK-DATAS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.nv_block_data_refs.append(child_value)

        # Parse nv_block_needs
        child = ARObject._find_child_element(element, "NV-BLOCK-NEEDS")
        if child is not None:
            nv_block_needs_value = ARObject._deserialize_by_tag(child, "NvBlockNeeds")
            obj.nv_block_needs = nv_block_needs_value

        # Parse ram_block_ref
        child = ARObject._find_child_element(element, "RAM-BLOCK")
        if child is not None:
            ram_block_ref_value = ARObject._deserialize_by_tag(child, "VariableDataPrototype")
            obj.ram_block_ref = ram_block_ref_value

        # Parse rom_block_ref
        child = ARObject._find_child_element(element, "ROM-BLOCK")
        if child is not None:
            rom_block_ref_value = ARObject._deserialize_by_tag(child, "ParameterDataPrototype")
            obj.rom_block_ref = rom_block_ref_value

        # Parse support_dirty
        child = ARObject._find_child_element(element, "SUPPORT-DIRTY")
        if child is not None:
            support_dirty_value = child.text
            obj.support_dirty = support_dirty_value

        # Parse timing_event
        child = ARObject._find_child_element(element, "TIMING-EVENT")
        if child is not None:
            timing_event_value = ARObject._deserialize_by_tag(child, "TimingEvent")
            obj.timing_event = timing_event_value

        # Parse writing_strategies (list from container "WRITING-STRATEGIES")
        obj.writing_strategies = []
        container = ARObject._find_child_element(element, "WRITING-STRATEGIES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.writing_strategies.append(child_value)

        return obj



class NvBlockDescriptorBuilder:
    """Builder for NvBlockDescriptor."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: NvBlockDescriptor = NvBlockDescriptor()

    def build(self) -> NvBlockDescriptor:
        """Build and return NvBlockDescriptor object.

        Returns:
            NvBlockDescriptor instance
        """
        # TODO: Add validation
        return self._obj
