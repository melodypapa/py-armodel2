"""FlexrayFifoRange AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 87)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Flexray_FlexrayTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class FlexrayFifoRange(ARObject):
    """AUTOSAR FlexrayFifoRange."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    range_max: Optional[Integer]
    range_min: Optional[Integer]
    def __init__(self) -> None:
        """Initialize FlexrayFifoRange."""
        super().__init__()
        self.range_max: Optional[Integer] = None
        self.range_min: Optional[Integer] = None

    def serialize(self) -> ET.Element:
        """Serialize FlexrayFifoRange to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FlexrayFifoRange, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize range_max
        if self.range_max is not None:
            serialized = SerializationHelper.serialize_item(self.range_max, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RANGE-MAX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize range_min
        if self.range_min is not None:
            serialized = SerializationHelper.serialize_item(self.range_min, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RANGE-MIN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayFifoRange":
        """Deserialize XML element to FlexrayFifoRange object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FlexrayFifoRange object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FlexrayFifoRange, cls).deserialize(element)

        # Parse range_max
        child = SerializationHelper.find_child_element(element, "RANGE-MAX")
        if child is not None:
            range_max_value = child.text
            obj.range_max = range_max_value

        # Parse range_min
        child = SerializationHelper.find_child_element(element, "RANGE-MIN")
        if child is not None:
            range_min_value = child.text
            obj.range_min = range_min_value

        return obj



class FlexrayFifoRangeBuilder:
    """Builder for FlexrayFifoRange."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayFifoRange = FlexrayFifoRange()

    def build(self) -> FlexrayFifoRange:
        """Build and return FlexrayFifoRange object.

        Returns:
            FlexrayFifoRange instance
        """
        # TODO: Add validation
        return self._obj
