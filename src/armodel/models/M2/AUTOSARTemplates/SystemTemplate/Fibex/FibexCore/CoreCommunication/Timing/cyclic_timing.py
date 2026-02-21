"""CyclicTiming AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 396)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication_Timing.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.describable import (
    Describable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing.time_range_type import (
    TimeRangeType,
)


class CyclicTiming(Describable):
    """AUTOSAR CyclicTiming."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    time_offset: Optional[TimeRangeType]
    time_period: Optional[TimeRangeType]
    def __init__(self) -> None:
        """Initialize CyclicTiming."""
        super().__init__()
        self.time_offset: Optional[TimeRangeType] = None
        self.time_period: Optional[TimeRangeType] = None

    def serialize(self) -> ET.Element:
        """Serialize CyclicTiming to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CyclicTiming, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize time_offset
        if self.time_offset is not None:
            serialized = SerializationHelper.serialize_item(self.time_offset, "TimeRangeType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME-OFFSET")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize time_period
        if self.time_period is not None:
            serialized = SerializationHelper.serialize_item(self.time_period, "TimeRangeType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME-PERIOD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CyclicTiming":
        """Deserialize XML element to CyclicTiming object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CyclicTiming object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CyclicTiming, cls).deserialize(element)

        # Parse time_offset
        child = SerializationHelper.find_child_element(element, "TIME-OFFSET")
        if child is not None:
            time_offset_value = SerializationHelper.deserialize_by_tag(child, "TimeRangeType")
            obj.time_offset = time_offset_value

        # Parse time_period
        child = SerializationHelper.find_child_element(element, "TIME-PERIOD")
        if child is not None:
            time_period_value = SerializationHelper.deserialize_by_tag(child, "TimeRangeType")
            obj.time_period = time_period_value

        return obj



class CyclicTimingBuilder:
    """Builder for CyclicTiming."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CyclicTiming = CyclicTiming()

    def build(self) -> CyclicTiming:
        """Build and return CyclicTiming object.

        Returns:
            CyclicTiming instance
        """
        # TODO: Add validation
        return self._obj
