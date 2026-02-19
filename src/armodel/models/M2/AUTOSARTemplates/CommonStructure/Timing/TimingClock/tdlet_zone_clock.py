"""TDLETZoneClock AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 252)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingClock.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingClock.timing_clock import (
    TimingClock,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)


class TDLETZoneClock(TimingClock):
    """AUTOSAR TDLETZoneClock."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    accuracy_ext: Optional[MultidimensionalTime]
    accuracy_int: Optional[MultidimensionalTime]
    def __init__(self) -> None:
        """Initialize TDLETZoneClock."""
        super().__init__()
        self.accuracy_ext: Optional[MultidimensionalTime] = None
        self.accuracy_int: Optional[MultidimensionalTime] = None
    def serialize(self) -> ET.Element:
        """Serialize TDLETZoneClock to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TDLETZoneClock, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize accuracy_ext
        if self.accuracy_ext is not None:
            serialized = ARObject._serialize_item(self.accuracy_ext, "MultidimensionalTime")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ACCURACY-EXT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize accuracy_int
        if self.accuracy_int is not None:
            serialized = ARObject._serialize_item(self.accuracy_int, "MultidimensionalTime")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ACCURACY-INT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDLETZoneClock":
        """Deserialize XML element to TDLETZoneClock object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDLETZoneClock object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TDLETZoneClock, cls).deserialize(element)

        # Parse accuracy_ext
        child = ARObject._find_child_element(element, "ACCURACY-EXT")
        if child is not None:
            accuracy_ext_value = ARObject._deserialize_by_tag(child, "MultidimensionalTime")
            obj.accuracy_ext = accuracy_ext_value

        # Parse accuracy_int
        child = ARObject._find_child_element(element, "ACCURACY-INT")
        if child is not None:
            accuracy_int_value = ARObject._deserialize_by_tag(child, "MultidimensionalTime")
            obj.accuracy_int = accuracy_int_value

        return obj



class TDLETZoneClockBuilder:
    """Builder for TDLETZoneClock."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDLETZoneClock = TDLETZoneClock()

    def build(self) -> TDLETZoneClock:
        """Build and return TDLETZoneClock object.

        Returns:
            TDLETZoneClock instance
        """
        # TODO: Add validation
        return self._obj
