"""RteEventInSystemSeparation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 214)

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


class RteEventInSystemSeparation(Identifiable):
    """AUTOSAR RteEventInSystemSeparation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    rte_event_instance_refs: list[RTEEvent]
    def __init__(self) -> None:
        """Initialize RteEventInSystemSeparation."""
        super().__init__()
        self.rte_event_instance_refs: list[RTEEvent] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "RteEventInSystemSeparation":
        """Deserialize XML element to RteEventInSystemSeparation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RteEventInSystemSeparation object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RteEventInSystemSeparation, cls).deserialize(element)

        # Parse rte_event_instance_refs (list from container "RTE-EVENT-INSTANCE-REFS")
        obj.rte_event_instance_refs = []
        container = ARObject._find_child_element(element, "RTE-EVENT-INSTANCE-REFS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.rte_event_instance_refs.append(child_value)

        return obj



class RteEventInSystemSeparationBuilder:
    """Builder for RteEventInSystemSeparation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RteEventInSystemSeparation = RteEventInSystemSeparation()

    def build(self) -> RteEventInSystemSeparation:
        """Build and return RteEventInSystemSeparation object.

        Returns:
            RteEventInSystemSeparation instance
        """
        # TODO: Add validation
        return self._obj
