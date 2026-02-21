"""EventTriggeringConstraint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 100)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_EventTriggeringConstraint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.timing_constraint import (
    TimingConstraint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event import (
    TimingDescriptionEvent,
)
from abc import ABC, abstractmethod


class EventTriggeringConstraint(TimingConstraint, ABC):
    """AUTOSAR EventTriggeringConstraint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    event_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize EventTriggeringConstraint."""
        super().__init__()
        self.event_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize EventTriggeringConstraint to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EventTriggeringConstraint, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize event_ref
        if self.event_ref is not None:
            serialized = ARObject._serialize_item(self.event_ref, "TimingDescriptionEvent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EVENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EventTriggeringConstraint":
        """Deserialize XML element to EventTriggeringConstraint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EventTriggeringConstraint object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EventTriggeringConstraint, cls).deserialize(element)

        # Parse event_ref
        child = ARObject._find_child_element(element, "EVENT-REF")
        if child is not None:
            event_ref_value = ARRef.deserialize(child)
            obj.event_ref = event_ref_value

        return obj



class EventTriggeringConstraintBuilder:
    """Builder for EventTriggeringConstraint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EventTriggeringConstraint = EventTriggeringConstraint()

    def build(self) -> EventTriggeringConstraint:
        """Build and return EventTriggeringConstraint object.

        Returns:
            EventTriggeringConstraint instance
        """
        # TODO: Add validation
        return self._obj
