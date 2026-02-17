"""RTriggerInAtomicSwcInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 945)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs.trigger_in_atomic_swc_instance_ref import (
    TriggerInAtomicSwcInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_required_port_prototype import (
    AbstractRequiredPortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)


class RTriggerInAtomicSwcInstanceRef(TriggerInAtomicSwcInstanceRef):
    """AUTOSAR RTriggerInAtomicSwcInstanceRef."""

    def __init__(self) -> None:
        """Initialize RTriggerInAtomicSwcInstanceRef."""
        super().__init__()
        self.context_r_port_prototype: Optional[AbstractRequiredPortPrototype] = None
        self.target_trigger: Optional[Trigger] = None


class RTriggerInAtomicSwcInstanceRefBuilder:
    """Builder for RTriggerInAtomicSwcInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RTriggerInAtomicSwcInstanceRef = RTriggerInAtomicSwcInstanceRef()

    def build(self) -> RTriggerInAtomicSwcInstanceRef:
        """Build and return RTriggerInAtomicSwcInstanceRef object.

        Returns:
            RTriggerInAtomicSwcInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
