"""TimeRangeType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 398)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication_Timing.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class TimeRangeType(ARObject):
    """AUTOSAR TimeRangeType."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    tolerance_tolerance: Optional[TimeRangeType]
    value: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize TimeRangeType."""
        super().__init__()
        self.tolerance_tolerance: Optional[TimeRangeType] = None
        self.value: Optional[TimeValue] = None

    def serialize(self) -> ET.Element:
        """Serialize TimeRangeType to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # Serialize tolerance_tolerance
        if self.tolerance_tolerance is not None:
            serialized = SerializationHelper.serialize_item(self.tolerance_tolerance, "TimeRangeType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TOLERANCE-TOLERANCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize value
        if self.value is not None:
            serialized = SerializationHelper.serialize_item(self.value, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TimeRangeType":
        """Deserialize XML element to TimeRangeType object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TimeRangeType object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse tolerance_tolerance
        child = SerializationHelper.find_child_element(element, "TOLERANCE-TOLERANCE")
        if child is not None:
            tolerance_tolerance_value = SerializationHelper.deserialize_by_tag(child, "TimeRangeType")
            obj.tolerance_tolerance = tolerance_tolerance_value

        # Parse value
        child = SerializationHelper.find_child_element(element, "VALUE")
        if child is not None:
            value_value = child.text
            obj.value = value_value

        return obj



class TimeRangeTypeBuilder:
    """Builder for TimeRangeType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TimeRangeType = TimeRangeType()

    def build(self) -> TimeRangeType:
        """Build and return TimeRangeType object.

        Returns:
            TimeRangeType instance
        """
        # TODO: Add validation
        return self._obj
