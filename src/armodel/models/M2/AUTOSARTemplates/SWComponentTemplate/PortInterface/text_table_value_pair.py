"""TextTableValuePair AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 146)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
)


class TextTableValuePair(ARObject):
    """AUTOSAR TextTableValuePair."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    first_value: Optional[Numerical]
    second_value: Optional[Numerical]
    def __init__(self) -> None:
        """Initialize TextTableValuePair."""
        super().__init__()
        self.first_value: Optional[Numerical] = None
        self.second_value: Optional[Numerical] = None

    def serialize(self) -> ET.Element:
        """Serialize TextTableValuePair to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TextTableValuePair, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize first_value
        if self.first_value is not None:
            serialized = SerializationHelper.serialize_item(self.first_value, "Numerical")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FIRST-VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize second_value
        if self.second_value is not None:
            serialized = SerializationHelper.serialize_item(self.second_value, "Numerical")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SECOND-VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TextTableValuePair":
        """Deserialize XML element to TextTableValuePair object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TextTableValuePair object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TextTableValuePair, cls).deserialize(element)

        # Parse first_value
        child = SerializationHelper.find_child_element(element, "FIRST-VALUE")
        if child is not None:
            first_value_value = child.text
            obj.first_value = first_value_value

        # Parse second_value
        child = SerializationHelper.find_child_element(element, "SECOND-VALUE")
        if child is not None:
            second_value_value = child.text
            obj.second_value = second_value_value

        return obj



class TextTableValuePairBuilder:
    """Builder for TextTableValuePair."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TextTableValuePair = TextTableValuePair()

    def build(self) -> TextTableValuePair:
        """Build and return TextTableValuePair object.

        Returns:
            TextTableValuePair instance
        """
        # TODO: Add validation
        return self._obj
