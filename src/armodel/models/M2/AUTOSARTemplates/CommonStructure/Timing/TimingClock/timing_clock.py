"""TimingClock AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 252)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingClock.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_domain import (
    GlobalTimeDomain,
)
from abc import ABC, abstractmethod


class TimingClock(Identifiable, ABC):
    """AUTOSAR TimingClock."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    platform_time: Optional[GlobalTimeDomain]
    def __init__(self) -> None:
        """Initialize TimingClock."""
        super().__init__()
        self.platform_time: Optional[GlobalTimeDomain] = None

    def serialize(self) -> ET.Element:
        """Serialize TimingClock to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TimingClock, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize platform_time
        if self.platform_time is not None:
            serialized = ARObject._serialize_item(self.platform_time, "GlobalTimeDomain")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PLATFORM-TIME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TimingClock":
        """Deserialize XML element to TimingClock object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TimingClock object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TimingClock, cls).deserialize(element)

        # Parse platform_time
        child = ARObject._find_child_element(element, "PLATFORM-TIME")
        if child is not None:
            platform_time_value = ARObject._deserialize_by_tag(child, "GlobalTimeDomain")
            obj.platform_time = platform_time_value

        return obj



class TimingClockBuilder:
    """Builder for TimingClock."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TimingClock = TimingClock()

    def build(self) -> TimingClock:
        """Build and return TimingClock object.

        Returns:
            TimingClock instance
        """
        # TODO: Add validation
        return self._obj
