"""TimingDescriptionEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 253)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description import (
    TimingDescription,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingClock.timing_clock import (
    TimingClock,
)
from abc import ABC, abstractmethod


class TimingDescriptionEvent(TimingDescription, ABC):
    """AUTOSAR TimingDescriptionEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    clock_reference_ref: Optional[ARRef]
    occurrence: Optional[Any]
    def __init__(self) -> None:
        """Initialize TimingDescriptionEvent."""
        super().__init__()
        self.clock_reference_ref: Optional[ARRef] = None
        self.occurrence: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize TimingDescriptionEvent to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TimingDescriptionEvent, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize clock_reference_ref
        if self.clock_reference_ref is not None:
            serialized = ARObject._serialize_item(self.clock_reference_ref, "TimingClock")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CLOCK-REFERENCE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize occurrence
        if self.occurrence is not None:
            serialized = ARObject._serialize_item(self.occurrence, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OCCURRENCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TimingDescriptionEvent":
        """Deserialize XML element to TimingDescriptionEvent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TimingDescriptionEvent object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TimingDescriptionEvent, cls).deserialize(element)

        # Parse clock_reference_ref
        child = ARObject._find_child_element(element, "CLOCK-REFERENCE-REF")
        if child is not None:
            clock_reference_ref_value = ARRef.deserialize(child)
            obj.clock_reference_ref = clock_reference_ref_value

        # Parse occurrence
        child = ARObject._find_child_element(element, "OCCURRENCE")
        if child is not None:
            occurrence_value = child.text
            obj.occurrence = occurrence_value

        return obj



class TimingDescriptionEventBuilder:
    """Builder for TimingDescriptionEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TimingDescriptionEvent = TimingDescriptionEvent()

    def build(self) -> TimingDescriptionEvent:
        """Build and return TimingDescriptionEvent object.

        Returns:
            TimingDescriptionEvent instance
        """
        # TODO: Add validation
        return self._obj
