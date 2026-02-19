"""TimingEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 532)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 254)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_RTEEvents.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class TimingEvent(RTEEvent):
    """AUTOSAR TimingEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    offset: Optional[TimeValue]
    period: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize TimingEvent."""
        super().__init__()
        self.offset: Optional[TimeValue] = None
        self.period: Optional[TimeValue] = None
    def serialize(self) -> ET.Element:
        """Serialize TimingEvent to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TimingEvent, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize offset
        if self.offset is not None:
            serialized = ARObject._serialize_item(self.offset, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OFFSET")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize period
        if self.period is not None:
            serialized = ARObject._serialize_item(self.period, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PERIOD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TimingEvent":
        """Deserialize XML element to TimingEvent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TimingEvent object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TimingEvent, cls).deserialize(element)

        # Parse offset
        child = ARObject._find_child_element(element, "OFFSET")
        if child is not None:
            offset_value = child.text
            obj.offset = offset_value

        # Parse period
        child = ARObject._find_child_element(element, "PERIOD")
        if child is not None:
            period_value = child.text
            obj.period = period_value

        return obj



class TimingEventBuilder:
    """Builder for TimingEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TimingEvent = TimingEvent()

    def build(self) -> TimingEvent:
        """Build and return TimingEvent object.

        Returns:
            TimingEvent instance
        """
        # TODO: Add validation
        return self._obj
