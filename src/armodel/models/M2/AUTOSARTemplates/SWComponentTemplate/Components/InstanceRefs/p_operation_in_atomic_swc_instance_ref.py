"""POperationInAtomicSwcInstanceRef AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs.operation_in_atomic_swc_instance_ref import (
    OperationInAtomicSwcInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_provided_port_prototype import (
    AbstractProvidedPortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)


class POperationInAtomicSwcInstanceRef(OperationInAtomicSwcInstanceRef):
    """AUTOSAR POperationInAtomicSwcInstanceRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "context_p_port_prototype": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=AbstractProvidedPortPrototype,
        ),  # contextPPortPrototype
        "target_provided_operation": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ClientServerOperation,
        ),  # targetProvidedOperation
    }

    def __init__(self) -> None:
        """Initialize POperationInAtomicSwcInstanceRef."""
        super().__init__()
        self.context_p_port_prototype: Optional[AbstractProvidedPortPrototype] = None
        self.target_provided_operation: Optional[ClientServerOperation] = None


class POperationInAtomicSwcInstanceRefBuilder:
    """Builder for POperationInAtomicSwcInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: POperationInAtomicSwcInstanceRef = POperationInAtomicSwcInstanceRef()

    def build(self) -> POperationInAtomicSwcInstanceRef:
        """Build and return POperationInAtomicSwcInstanceRef object.

        Returns:
            POperationInAtomicSwcInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
