"""RunnableEntity AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 331)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 524)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2050)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 240)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 461)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 203)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.executable_entity import (
    ExecutableEntity,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    CIdentifier,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.Trigger.external_triggering_point import (
    ExternalTriggeringPoint,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.Trigger.internal_triggering_point import (
    InternalTriggeringPoint,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ModeDeclarationGroup.mode_access_point import (
    ModeAccessPoint,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ModeDeclarationGroup.mode_switch_point import (
    ModeSwitchPoint,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServerCall.server_call_point import (
    ServerCallPoint,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.variable_access import (
    VariableAccess,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.parameter_access import (
        ParameterAccess,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.wait_point import (
        WaitPoint,
    )



class RunnableEntity(ExecutableEntity):
    """AUTOSAR RunnableEntity."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    arguments: list[RunnableEntity]
    asynchronous_servers: list[Any]
    can_be_invoked: Optional[Boolean]
    data_reads: list[VariableAccess]
    data_receives: list[VariableAccess]
    data_send_points: list[VariableAccess]
    data_writes: list[VariableAccess]
    external_refs: list[ARRef]
    internal_refs: list[ARRef]
    mode_access_points: list[ModeAccessPoint]
    mode_switch_points: list[ModeSwitchPoint]
    parameter_accesses: list[ParameterAccess]
    read_locals: list[VariableAccess]
    server_call_points: list[ServerCallPoint]
    symbol: Optional[CIdentifier]
    wait_points: list[WaitPoint]
    written_locals: list[VariableAccess]
    def __init__(self) -> None:
        """Initialize RunnableEntity."""
        super().__init__()
        self.arguments: list[RunnableEntity] = []
        self.asynchronous_servers: list[Any] = []
        self.can_be_invoked: Optional[Boolean] = None
        self.data_reads: list[VariableAccess] = []
        self.data_receives: list[VariableAccess] = []
        self.data_send_points: list[VariableAccess] = []
        self.data_writes: list[VariableAccess] = []
        self.external_refs: list[ARRef] = []
        self.internal_refs: list[ARRef] = []
        self.mode_access_points: list[ModeAccessPoint] = []
        self.mode_switch_points: list[ModeSwitchPoint] = []
        self.parameter_accesses: list[ParameterAccess] = []
        self.read_locals: list[VariableAccess] = []
        self.server_call_points: list[ServerCallPoint] = []
        self.symbol: Optional[CIdentifier] = None
        self.wait_points: list[WaitPoint] = []
        self.written_locals: list[VariableAccess] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "RunnableEntity":
        """Deserialize XML element to RunnableEntity object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RunnableEntity object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse arguments (list)
        obj.arguments = []
        for child in ARObject._find_all_child_elements(element, "ARGUMENTS"):
            arguments_value = ARObject._deserialize_by_tag(child, "RunnableEntity")
            obj.arguments.append(arguments_value)

        # Parse asynchronous_servers (list)
        obj.asynchronous_servers = []
        for child in ARObject._find_all_child_elements(element, "ASYNCHRONOUS-SERVERS"):
            asynchronous_servers_value = child.text
            obj.asynchronous_servers.append(asynchronous_servers_value)

        # Parse can_be_invoked
        child = ARObject._find_child_element(element, "CAN-BE-INVOKED")
        if child is not None:
            can_be_invoked_value = child.text
            obj.can_be_invoked = can_be_invoked_value

        # Parse data_reads (list)
        obj.data_reads = []
        for child in ARObject._find_all_child_elements(element, "DATA-READS"):
            data_reads_value = ARObject._deserialize_by_tag(child, "VariableAccess")
            obj.data_reads.append(data_reads_value)

        # Parse data_receives (list)
        obj.data_receives = []
        for child in ARObject._find_all_child_elements(element, "DATA-RECEIVES"):
            data_receives_value = ARObject._deserialize_by_tag(child, "VariableAccess")
            obj.data_receives.append(data_receives_value)

        # Parse data_send_points (list)
        obj.data_send_points = []
        for child in ARObject._find_all_child_elements(element, "DATA-SEND-POINTS"):
            data_send_points_value = ARObject._deserialize_by_tag(child, "VariableAccess")
            obj.data_send_points.append(data_send_points_value)

        # Parse data_writes (list)
        obj.data_writes = []
        for child in ARObject._find_all_child_elements(element, "DATA-WRITES"):
            data_writes_value = ARObject._deserialize_by_tag(child, "VariableAccess")
            obj.data_writes.append(data_writes_value)

        # Parse external_refs (list)
        obj.external_refs = []
        for child in ARObject._find_all_child_elements(element, "EXTERNALS"):
            external_refs_value = ARObject._deserialize_by_tag(child, "ExternalTriggeringPoint")
            obj.external_refs.append(external_refs_value)

        # Parse internal_refs (list)
        obj.internal_refs = []
        for child in ARObject._find_all_child_elements(element, "INTERNALS"):
            internal_refs_value = ARObject._deserialize_by_tag(child, "InternalTriggeringPoint")
            obj.internal_refs.append(internal_refs_value)

        # Parse mode_access_points (list)
        obj.mode_access_points = []
        for child in ARObject._find_all_child_elements(element, "MODE-ACCESS-POINTS"):
            mode_access_points_value = ARObject._deserialize_by_tag(child, "ModeAccessPoint")
            obj.mode_access_points.append(mode_access_points_value)

        # Parse mode_switch_points (list)
        obj.mode_switch_points = []
        for child in ARObject._find_all_child_elements(element, "MODE-SWITCH-POINTS"):
            mode_switch_points_value = ARObject._deserialize_by_tag(child, "ModeSwitchPoint")
            obj.mode_switch_points.append(mode_switch_points_value)

        # Parse parameter_accesses (list)
        obj.parameter_accesses = []
        for child in ARObject._find_all_child_elements(element, "PARAMETER-ACCESSES"):
            parameter_accesses_value = ARObject._deserialize_by_tag(child, "ParameterAccess")
            obj.parameter_accesses.append(parameter_accesses_value)

        # Parse read_locals (list)
        obj.read_locals = []
        for child in ARObject._find_all_child_elements(element, "READ-LOCALS"):
            read_locals_value = ARObject._deserialize_by_tag(child, "VariableAccess")
            obj.read_locals.append(read_locals_value)

        # Parse server_call_points (list)
        obj.server_call_points = []
        for child in ARObject._find_all_child_elements(element, "SERVER-CALL-POINTS"):
            server_call_points_value = ARObject._deserialize_by_tag(child, "ServerCallPoint")
            obj.server_call_points.append(server_call_points_value)

        # Parse symbol
        child = ARObject._find_child_element(element, "SYMBOL")
        if child is not None:
            symbol_value = child.text
            obj.symbol = symbol_value

        # Parse wait_points (list)
        obj.wait_points = []
        for child in ARObject._find_all_child_elements(element, "WAIT-POINTS"):
            wait_points_value = ARObject._deserialize_by_tag(child, "WaitPoint")
            obj.wait_points.append(wait_points_value)

        # Parse written_locals (list)
        obj.written_locals = []
        for child in ARObject._find_all_child_elements(element, "WRITTEN-LOCALS"):
            written_locals_value = ARObject._deserialize_by_tag(child, "VariableAccess")
            obj.written_locals.append(written_locals_value)

        return obj



class RunnableEntityBuilder:
    """Builder for RunnableEntity."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RunnableEntity = RunnableEntity()

    def build(self) -> RunnableEntity:
        """Build and return RunnableEntity object.

        Returns:
            RunnableEntity instance
        """
        # TODO: Add validation
        return self._obj
