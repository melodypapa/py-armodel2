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
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.executable_entity import (
    ExecutableEntity,
)
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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "arguments": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class="RunnableEntity",
        ),  # arguments
        "asynchronous_servers": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=Any,
        ),  # asynchronousServers
        "can_be_invoked": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # canBeInvoked
        "data_reads": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=VariableAccess,
        ),  # dataReads
        "data_receives": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=VariableAccess,
        ),  # dataReceives
        "data_send_points": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=VariableAccess,
        ),  # dataSendPoints
        "data_writes": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=VariableAccess,
        ),  # dataWrites
        "externals": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ExternalTriggeringPoint,
        ),  # externals
        "internals": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=InternalTriggeringPoint,
        ),  # internals
        "mode_access_points": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ModeAccessPoint,
        ),  # modeAccessPoints
        "mode_switch_points": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ModeSwitchPoint,
        ),  # modeSwitchPoints
        "parameter_accesses": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class="ParameterAccess",
        ),  # parameterAccesses
        "read_locals": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=VariableAccess,
        ),  # readLocals
        "server_call_points": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ServerCallPoint,
        ),  # serverCallPoints
        "symbol": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # symbol
        "wait_points": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class="WaitPoint",
        ),  # waitPoints
        "written_locals": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=VariableAccess,
        ),  # writtenLocals
    }

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
        self.externals: list[ExternalTriggeringPoint] = []
        self.internals: list[InternalTriggeringPoint] = []
        self.mode_access_points: list[ModeAccessPoint] = []
        self.mode_switch_points: list[ModeSwitchPoint] = []
        self.parameter_accesses: list[ParameterAccess] = []
        self.read_locals: list[VariableAccess] = []
        self.server_call_points: list[ServerCallPoint] = []
        self.symbol: Optional[CIdentifier] = None
        self.wait_points: list[WaitPoint] = []
        self.written_locals: list[VariableAccess] = []


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
