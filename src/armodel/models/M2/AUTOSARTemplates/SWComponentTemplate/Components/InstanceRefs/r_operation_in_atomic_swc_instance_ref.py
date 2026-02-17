"""ROperationInAtomicSwcInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 947)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

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
