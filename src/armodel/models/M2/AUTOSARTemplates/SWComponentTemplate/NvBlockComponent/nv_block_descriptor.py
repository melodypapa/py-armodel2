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
