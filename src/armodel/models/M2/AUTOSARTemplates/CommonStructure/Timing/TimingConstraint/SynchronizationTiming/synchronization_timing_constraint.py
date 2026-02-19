"""SynchronizationTimingConstraint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 92)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_SynchronizationTiming.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.timing_constraint import (
    TimingConstraint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.SynchronizationTiming import (
    EventOccurrenceKindEnum,
    SynchronizationTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event import (
    TimingDescriptionEvent,
)


class SynchronizationTimingConstraint(TimingConstraint):
    """AUTOSAR SynchronizationTimingConstraint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    event: Optional[EventOccurrenceKindEnum]
    scopes: list[TimingDescriptionEvent]
    scope_events: list[TimingDescriptionEvent]
    synchronization: Optional[SynchronizationTypeEnum]
    tolerance: Optional[MultidimensionalTime]
    def __init__(self) -> None:
        """Initialize SynchronizationTimingConstraint."""
        super().__init__()
        self.event: Optional[EventOccurrenceKindEnum] = None
        self.scopes: list[TimingDescriptionEvent] = []
        self.scope_events: list[TimingDescriptionEvent] = []
        self.synchronization: Optional[SynchronizationTypeEnum] = None
        self.tolerance: Optional[MultidimensionalTime] = None
    def serialize(self) -> ET.Element:
        """Serialize SynchronizationTimingConstraint to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SynchronizationTimingConstraint, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize event
        if self.event is not None:
            serialized = ARObject._serialize_item(self.event, "EventOccurrenceKindEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EVENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize scopes (list to container "SCOPES")
        if self.scopes:
            wrapper = ET.Element("SCOPES")
            for item in self.scopes:
                serialized = ARObject._serialize_item(item, "TimingDescriptionEvent")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize scope_events (list to container "SCOPE-EVENTS")
        if self.scope_events:
            wrapper = ET.Element("SCOPE-EVENTS")
            for item in self.scope_events:
                serialized = ARObject._serialize_item(item, "TimingDescriptionEvent")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize synchronization
        if self.synchronization is not None:
            serialized = ARObject._serialize_item(self.synchronization, "SynchronizationTypeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SYNCHRONIZATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tolerance
        if self.tolerance is not None:
            serialized = ARObject._serialize_item(self.tolerance, "MultidimensionalTime")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TOLERANCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SynchronizationTimingConstraint":
        """Deserialize XML element to SynchronizationTimingConstraint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SynchronizationTimingConstraint object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SynchronizationTimingConstraint, cls).deserialize(element)

        # Parse event
        child = ARObject._find_child_element(element, "EVENT")
        if child is not None:
            event_value = EventOccurrenceKindEnum.deserialize(child)
            obj.event = event_value

        # Parse scopes (list from container "SCOPES")
        obj.scopes = []
        container = ARObject._find_child_element(element, "SCOPES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.scopes.append(child_value)

        # Parse scope_events (list from container "SCOPE-EVENTS")
        obj.scope_events = []
        container = ARObject._find_child_element(element, "SCOPE-EVENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.scope_events.append(child_value)

        # Parse synchronization
        child = ARObject._find_child_element(element, "SYNCHRONIZATION")
        if child is not None:
            synchronization_value = SynchronizationTypeEnum.deserialize(child)
            obj.synchronization = synchronization_value

        # Parse tolerance
        child = ARObject._find_child_element(element, "TOLERANCE")
        if child is not None:
            tolerance_value = ARObject._deserialize_by_tag(child, "MultidimensionalTime")
            obj.tolerance = tolerance_value

        return obj



class SynchronizationTimingConstraintBuilder:
    """Builder for SynchronizationTimingConstraint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SynchronizationTimingConstraint = SynchronizationTimingConstraint()

    def build(self) -> SynchronizationTimingConstraint:
        """Build and return SynchronizationTimingConstraint object.

        Returns:
            SynchronizationTimingConstraint instance
        """
        # TODO: Add validation
        return self._obj
