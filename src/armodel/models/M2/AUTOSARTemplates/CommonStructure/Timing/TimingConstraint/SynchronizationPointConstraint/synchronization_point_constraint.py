"""SynchronizationPointConstraint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 132)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_SynchronizationPointConstraint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.timing_constraint import (
    TimingConstraint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.abstract_event import (
    AbstractEvent,
)


class SynchronizationPointConstraint(TimingConstraint):
    """AUTOSAR SynchronizationPointConstraint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    source_eecs: list[Any]
    source_events: list[AbstractEvent]
    target_eecs: list[Any]
    target_events: list[AbstractEvent]
    def __init__(self) -> None:
        """Initialize SynchronizationPointConstraint."""
        super().__init__()
        self.source_eecs: list[Any] = []
        self.source_events: list[AbstractEvent] = []
        self.target_eecs: list[Any] = []
        self.target_events: list[AbstractEvent] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SynchronizationPointConstraint":
        """Deserialize XML element to SynchronizationPointConstraint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SynchronizationPointConstraint object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse source_eecs (list)
        obj.source_eecs = []
        for child in ARObject._find_all_child_elements(element, "SOURCE-EECS"):
            source_eecs_value = child.text
            obj.source_eecs.append(source_eecs_value)

        # Parse source_events (list)
        obj.source_events = []
        for child in ARObject._find_all_child_elements(element, "SOURCE-EVENTS"):
            source_events_value = ARObject._deserialize_by_tag(child, "AbstractEvent")
            obj.source_events.append(source_events_value)

        # Parse target_eecs (list)
        obj.target_eecs = []
        for child in ARObject._find_all_child_elements(element, "TARGET-EECS"):
            target_eecs_value = child.text
            obj.target_eecs.append(target_eecs_value)

        # Parse target_events (list)
        obj.target_events = []
        for child in ARObject._find_all_child_elements(element, "TARGET-EVENTS"):
            target_events_value = ARObject._deserialize_by_tag(child, "AbstractEvent")
            obj.target_events.append(target_events_value)

        return obj



class SynchronizationPointConstraintBuilder:
    """Builder for SynchronizationPointConstraint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SynchronizationPointConstraint = SynchronizationPointConstraint()

    def build(self) -> SynchronizationPointConstraint:
        """Build and return SynchronizationPointConstraint object.

        Returns:
            SynchronizationPointConstraint instance
        """
        # TODO: Add validation
        return self._obj
