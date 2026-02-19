"""RteEventInCompositionSeparation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 212)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_RteEventToOsTaskMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)


class RteEventInCompositionSeparation(Identifiable):
    """AUTOSAR RteEventInCompositionSeparation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    rte_event_instance_refs: list[RTEEvent]
    def __init__(self) -> None:
        """Initialize RteEventInCompositionSeparation."""
        super().__init__()
        self.rte_event_instance_refs: list[RTEEvent] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "RteEventInCompositionSeparation":
        """Deserialize XML element to RteEventInCompositionSeparation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RteEventInCompositionSeparation object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse rte_event_instance_refs (list)
        obj.rte_event_instance_refs = []
        for child in ARObject._find_all_child_elements(element, "RTE-EVENT-INSTANCE-REFS"):
            rte_event_instance_refs_value = ARObject._deserialize_by_tag(child, "RTEEvent")
            obj.rte_event_instance_refs.append(rte_event_instance_refs_value)

        return obj



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
