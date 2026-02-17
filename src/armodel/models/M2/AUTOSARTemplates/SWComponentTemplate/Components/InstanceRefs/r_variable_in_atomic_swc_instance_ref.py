"""RVariableInAtomicSwcInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 943)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs.variable_in_atomic_swc_instance_ref import (
    VariableInAtomicSwcInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_required_port_prototype import (
    AbstractRequiredPortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class RVariableInAtomicSwcInstanceRef(VariableInAtomicSwcInstanceRef):
    """AUTOSAR RVariableInAtomicSwcInstanceRef."""

    context_r_port_prototype: Optional[AbstractRequiredPortPrototype]
    target_data_element: Optional[VariableDataPrototype]
    def __init__(self) -> None:
        """Initialize RVariableInAtomicSwcInstanceRef."""
        super().__init__()
        self.context_r_port_prototype: Optional[AbstractRequiredPortPrototype] = None
        self.target_data_element: Optional[VariableDataPrototype] = None


class RVariableInAtomicSwcInstanceRefBuilder:
    """Builder for RVariableInAtomicSwcInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RVariableInAtomicSwcInstanceRef = RVariableInAtomicSwcInstanceRef()

    def build(self) -> RVariableInAtomicSwcInstanceRef:
        """Build and return RVariableInAtomicSwcInstanceRef object.

        Returns:
            RVariableInAtomicSwcInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
