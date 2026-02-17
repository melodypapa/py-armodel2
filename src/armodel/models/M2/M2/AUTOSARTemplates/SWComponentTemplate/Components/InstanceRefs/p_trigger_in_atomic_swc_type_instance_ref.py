"""PTriggerInAtomicSwcTypeInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 946)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "context_p_port_prototype": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=AbstractProvidedPortPrototype,
        ),  # contextPPortPrototype
        "target_trigger": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Trigger,
        ),  # targetTrigger
    }

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
