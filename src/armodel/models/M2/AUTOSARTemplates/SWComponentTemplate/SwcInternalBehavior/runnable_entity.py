"""RunnableEntity AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
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
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.parameter_access import (
    ParameterAccess,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.runnable_entity import (
    RunnableEntity,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServerCall.server_call_point import (
    ServerCallPoint,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.variable_access import (
    VariableAccess,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.wait_point import (
    WaitPoint,
)


class RunnableEntity(ExecutableEntity):
    """AUTOSAR RunnableEntity."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("arguments", None, False, True, RunnableEntity),  # arguments
        ("asynchronous_servers", None, False, True, any (AsynchronousServer)),  # asynchronousServers
        ("can_be_invoked", None, True, False, None),  # canBeInvoked
        ("data_reads", None, False, True, VariableAccess),  # dataReads
        ("data_receives", None, False, True, VariableAccess),  # dataReceives
        ("data_send_points", None, False, True, VariableAccess),  # dataSendPoints
        ("data_writes", None, False, True, VariableAccess),  # dataWrites
        ("externals", None, False, True, ExternalTriggeringPoint),  # externals
        ("internals", None, False, True, InternalTriggeringPoint),  # internals
        ("mode_access_points", None, False, True, ModeAccessPoint),  # modeAccessPoints
        ("mode_switch_points", None, False, True, ModeSwitchPoint),  # modeSwitchPoints
        ("parameter_accesses", None, False, True, ParameterAccess),  # parameterAccesses
        ("read_locals", None, False, True, VariableAccess),  # readLocals
        ("server_call_points", None, False, True, ServerCallPoint),  # serverCallPoints
        ("symbol", None, True, False, None),  # symbol
        ("wait_points", None, False, True, WaitPoint),  # waitPoints
        ("written_locals", None, False, True, VariableAccess),  # writtenLocals
    ]

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

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert RunnableEntity to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RunnableEntity":
        """Create RunnableEntity from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            RunnableEntity instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to RunnableEntity since parent returns ARObject
        return cast("RunnableEntity", obj)


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
