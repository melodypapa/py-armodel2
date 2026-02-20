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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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
    response_ref: Optional[ARRef]
    segment_refs: list[ARRef]
    stimulus_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize TimingDescriptionEventChain."""
        super().__init__()
        self.is_pipelining: Optional[Boolean] = None
        self.response_ref: Optional[ARRef] = None
        self.segment_refs: list[ARRef] = []
        self.stimulus_ref: Optional[ARRef] = None

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

        # Serialize response_ref
        if self.response_ref is not None:
            serialized = ARObject._serialize_item(self.response_ref, "TimingDescriptionEvent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RESPONSE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize segment_refs (list to container "SEGMENT-REFS")
        if self.segment_refs:
            wrapper = ET.Element("SEGMENT-REFS")
            for item in self.segment_refs:
                serialized = ARObject._serialize_item(item, "TimingDescriptionEvent")
                if serialized is not None:
                    child_elem = ET.Element("SEGMENT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize stimulus_ref
        if self.stimulus_ref is not None:
            serialized = ARObject._serialize_item(self.stimulus_ref, "TimingDescriptionEvent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("STIMULUS-REF")
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

        # Parse response_ref
        child = ARObject._find_child_element(element, "RESPONSE-REF")
        if child is not None:
            response_ref_value = ARRef.deserialize(child)
            obj.response_ref = response_ref_value

        # Parse segment_refs (list from container "SEGMENT-REFS")
        obj.segment_refs = []
        container = ARObject._find_child_element(element, "SEGMENT-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.segment_refs.append(child_value)

        # Parse stimulus_ref
        child = ARObject._find_child_element(element, "STIMULUS-REF")
        if child is not None:
            stimulus_ref_value = ARRef.deserialize(child)
            obj.stimulus_ref = stimulus_ref_value

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
