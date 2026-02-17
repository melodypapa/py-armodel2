"""InstanceEventInCompositionInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 959)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Composition_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.composition_sw_component_type import (
    CompositionSwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)


class InstanceEventInCompositionInstanceRef(ARObject):
    """AUTOSAR InstanceEventInCompositionInstanceRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "base": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CompositionSwComponentType,
        ),  # base
        "context_prototypes": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (SwComponent),
        ),  # contextPrototypes
        "target_event": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=RTEEvent,
        ),  # targetEvent
    }

    def __init__(self) -> None:
        """Initialize InstanceEventInCompositionInstanceRef."""
        super().__init__()
        self.base: Optional[CompositionSwComponentType] = None
        self.context_prototypes: list[Any] = []
        self.target_event: Optional[RTEEvent] = None


class InstanceEventInCompositionInstanceRefBuilder:
    """Builder for InstanceEventInCompositionInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: InstanceEventInCompositionInstanceRef = InstanceEventInCompositionInstanceRef()

    def build(self) -> InstanceEventInCompositionInstanceRef:
        """Build and return InstanceEventInCompositionInstanceRef object.

        Returns:
            InstanceEventInCompositionInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
