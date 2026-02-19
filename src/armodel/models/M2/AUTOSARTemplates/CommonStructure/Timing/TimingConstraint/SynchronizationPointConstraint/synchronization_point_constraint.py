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
    def serialize(self) -> ET.Element:
        """Serialize SynchronizationPointConstraint to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SynchronizationPointConstraint, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize source_eecs (list to container "SOURCE-EECS")
        if self.source_eecs:
            wrapper = ET.Element("SOURCE-EECS")
            for item in self.source_eecs:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize source_events (list to container "SOURCE-EVENTS")
        if self.source_events:
            wrapper = ET.Element("SOURCE-EVENTS")
            for item in self.source_events:
                serialized = ARObject._serialize_item(item, "AbstractEvent")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize target_eecs (list to container "TARGET-EECS")
        if self.target_eecs:
            wrapper = ET.Element("TARGET-EECS")
            for item in self.target_eecs:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize target_events (list to container "TARGET-EVENTS")
        if self.target_events:
            wrapper = ET.Element("TARGET-EVENTS")
            for item in self.target_events:
                serialized = ARObject._serialize_item(item, "AbstractEvent")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SynchronizationPointConstraint":
        """Deserialize XML element to SynchronizationPointConstraint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SynchronizationPointConstraint object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SynchronizationPointConstraint, cls).deserialize(element)

        # Parse source_eecs (list from container "SOURCE-EECS")
        obj.source_eecs = []
        container = ARObject._find_child_element(element, "SOURCE-EECS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.source_eecs.append(child_value)

        # Parse source_events (list from container "SOURCE-EVENTS")
        obj.source_events = []
        container = ARObject._find_child_element(element, "SOURCE-EVENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.source_events.append(child_value)

        # Parse target_eecs (list from container "TARGET-EECS")
        obj.target_eecs = []
        container = ARObject._find_child_element(element, "TARGET-EECS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.target_eecs.append(child_value)

        # Parse target_events (list from container "TARGET-EVENTS")
        obj.target_events = []
        container = ARObject._find_child_element(element, "TARGET-EVENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.target_events.append(child_value)

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
