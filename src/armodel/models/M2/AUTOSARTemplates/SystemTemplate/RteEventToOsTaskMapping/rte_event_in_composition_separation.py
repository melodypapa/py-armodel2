"""RteEventInCompositionSeparation AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)


class RteEventInCompositionSeparation(Identifiable):
    """AUTOSAR RteEventInCompositionSeparation."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "rte_event_instance_refs": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=RTEEvent,
        ),  # rteEventInstanceRefs
    }

    def __init__(self) -> None:
        """Initialize RteEventInCompositionSeparation."""
        super().__init__()
        self.rte_event_instance_refs: list[RTEEvent] = []


class RteEventInCompositionSeparationBuilder:
    """Builder for RteEventInCompositionSeparation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RteEventInCompositionSeparation = RteEventInCompositionSeparation()

    def build(self) -> RteEventInCompositionSeparation:
        """Build and return RteEventInCompositionSeparation object.

        Returns:
            RteEventInCompositionSeparation instance
        """
        # TODO: Add validation
        return self._obj
