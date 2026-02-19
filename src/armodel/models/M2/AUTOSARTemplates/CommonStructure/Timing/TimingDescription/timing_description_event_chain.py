"""TimingDescriptionEventChain AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 40)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description import (
    TimingDescription,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event import (
    TimingDescriptionEvent,
)


class TimingDescriptionEventChain(TimingDescription):
    """AUTOSAR TimingDescriptionEventChain."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    is_pipelining: Optional[Boolean]
    response: Optional[TimingDescriptionEvent]
    segments: list[TimingDescriptionEvent]
    stimulus: Optional[TimingDescriptionEvent]
    def __init__(self) -> None:
        """Initialize TimingDescriptionEventChain."""
        super().__init__()
        self.is_pipelining: Optional[Boolean] = None
        self.response: Optional[TimingDescriptionEvent] = None
        self.segments: list[TimingDescriptionEvent] = []
        self.stimulus: Optional[TimingDescriptionEvent] = None
    def serialize(self) -> ET.Element:
        """Serialize TimingDescriptionEventChain to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TimingDescriptionEventChain, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize is_pipelining
        if self.is_pipelining is not None:
            serialized = ARObject._serialize_item(self.is_pipelining, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IS-PIPELINING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize response
        if self.response is not None:
            serialized = ARObject._serialize_item(self.response, "TimingDescriptionEvent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RESPONSE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize segments (list to container "SEGMENTS")
        if self.segments:
            wrapper = ET.Element("SEGMENTS")
            for item in self.segments:
                serialized = ARObject._serialize_item(item, "TimingDescriptionEvent")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize stimulus
        if self.stimulus is not None:
            serialized = ARObject._serialize_item(self.stimulus, "TimingDescriptionEvent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("STIMULUS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TimingDescriptionEventChain":
        """Deserialize XML element to TimingDescriptionEventChain object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TimingDescriptionEventChain object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TimingDescriptionEventChain, cls).deserialize(element)

        # Parse is_pipelining
        child = ARObject._find_child_element(element, "IS-PIPELINING")
        if child is not None:
            is_pipelining_value = child.text
            obj.is_pipelining = is_pipelining_value

        # Parse response
        child = ARObject._find_child_element(element, "RESPONSE")
        if child is not None:
            response_value = ARObject._deserialize_by_tag(child, "TimingDescriptionEvent")
            obj.response = response_value

        # Parse segments (list from container "SEGMENTS")
        obj.segments = []
        container = ARObject._find_child_element(element, "SEGMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.segments.append(child_value)

        # Parse stimulus
        child = ARObject._find_child_element(element, "STIMULUS")
        if child is not None:
            stimulus_value = ARObject._deserialize_by_tag(child, "TimingDescriptionEvent")
            obj.stimulus = stimulus_value

        return obj



class TimingDescriptionEventChainBuilder:
    """Builder for TimingDescriptionEventChain."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TimingDescriptionEventChain = TimingDescriptionEventChain()

    def build(self) -> TimingDescriptionEventChain:
        """Build and return TimingDescriptionEventChain object.

        Returns:
            TimingDescriptionEventChain instance
        """
        # TODO: Add validation
        return self._obj
