"""TDHeaderIdRange AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 70)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class TDHeaderIdRange(ARObject):
    """AUTOSAR TDHeaderIdRange."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    max_header_id: Optional[Integer]
    min_header_id: Optional[Integer]
    def __init__(self) -> None:
        """Initialize TDHeaderIdRange."""
        super().__init__()
        self.max_header_id: Optional[Integer] = None
        self.min_header_id: Optional[Integer] = None

    def serialize(self) -> ET.Element:
        """Serialize TDHeaderIdRange to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TDHeaderIdRange, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize max_header_id
        if self.max_header_id is not None:
            serialized = SerializationHelper.serialize_item(self.max_header_id, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-HEADER-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize min_header_id
        if self.min_header_id is not None:
            serialized = SerializationHelper.serialize_item(self.min_header_id, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MIN-HEADER-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDHeaderIdRange":
        """Deserialize XML element to TDHeaderIdRange object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDHeaderIdRange object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TDHeaderIdRange, cls).deserialize(element)

        # Parse max_header_id
        child = SerializationHelper.find_child_element(element, "MAX-HEADER-ID")
        if child is not None:
            max_header_id_value = child.text
            obj.max_header_id = max_header_id_value

        # Parse min_header_id
        child = SerializationHelper.find_child_element(element, "MIN-HEADER-ID")
        if child is not None:
            min_header_id_value = child.text
            obj.min_header_id = min_header_id_value

        return obj



class TDHeaderIdRangeBuilder:
    """Builder for TDHeaderIdRange."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDHeaderIdRange = TDHeaderIdRange()

    def build(self) -> TDHeaderIdRange:
        """Build and return TDHeaderIdRange object.

        Returns:
            TDHeaderIdRange instance
        """
        # TODO: Add validation
        return self._obj
