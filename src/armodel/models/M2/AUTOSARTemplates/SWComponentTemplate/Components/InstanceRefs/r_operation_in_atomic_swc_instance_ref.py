"""ROperationInAtomicSwcInstanceRef AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs.operation_in_atomic_swc_instance_ref import (
    OperationInAtomicSwcInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_required_port_prototype import (
    AbstractRequiredPortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)


class ROperationInAtomicSwcInstanceRef(OperationInAtomicSwcInstanceRef):
    """AUTOSAR ROperationInAtomicSwcInstanceRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "context_r_port_prototype": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=AbstractRequiredPortPrototype,
        ),  # contextRPortPrototype
        "target_required_operation": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ClientServerOperation,
        ),  # targetRequiredOperation
    }

    def __init__(self) -> None:
        """Initialize ROperationInAtomicSwcInstanceRef."""
        super().__init__()
        self.context_r_port_prototype: Optional[AbstractRequiredPortPrototype] = None
        self.target_required_operation: Optional[ClientServerOperation] = None


class ROperationInAtomicSwcInstanceRefBuilder:
    """Builder for ROperationInAtomicSwcInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ROperationInAtomicSwcInstanceRef = ROperationInAtomicSwcInstanceRef()

    def build(self) -> ROperationInAtomicSwcInstanceRef:
        """Build and return ROperationInAtomicSwcInstanceRef object.

        Returns:
            ROperationInAtomicSwcInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
