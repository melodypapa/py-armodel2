"""PTriggerInAtomicSwcTypeInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 946)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs.trigger_in_atomic_swc_instance_ref import (
    TriggerInAtomicSwcInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_provided_port_prototype import (
    AbstractProvidedPortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)


class PTriggerInAtomicSwcTypeInstanceRef(TriggerInAtomicSwcInstanceRef):
    """AUTOSAR PTriggerInAtomicSwcTypeInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    context_p_port_prototype: Optional[AbstractProvidedPortPrototype]
    target_trigger: Optional[Trigger]
    def __init__(self) -> None:
        """Initialize PTriggerInAtomicSwcTypeInstanceRef."""
        super().__init__()
        self.context_p_port_prototype: Optional[AbstractProvidedPortPrototype] = None
        self.target_trigger: Optional[Trigger] = None


class PTriggerInAtomicSwcTypeInstanceRefBuilder:
    """Builder for PTriggerInAtomicSwcTypeInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PTriggerInAtomicSwcTypeInstanceRef = PTriggerInAtomicSwcTypeInstanceRef()

    def build(self) -> PTriggerInAtomicSwcTypeInstanceRef:
        """Build and return PTriggerInAtomicSwcTypeInstanceRef object.

        Returns:
            PTriggerInAtomicSwcTypeInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
