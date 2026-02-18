"""POperationInAtomicSwcInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 948)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    context_p_port_prototype: Optional[AbstractProvidedPortPrototype]
    target_provided_operation: Optional[ClientServerOperation]
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
