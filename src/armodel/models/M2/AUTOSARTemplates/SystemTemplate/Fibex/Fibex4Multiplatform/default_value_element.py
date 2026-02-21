"""DefaultValueElement AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 841)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Multiplatform.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class DefaultValueElement(ARObject):
    """AUTOSAR DefaultValueElement."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    element_byte_value: Optional[Integer]
    element_position: Optional[Integer]
    def __init__(self) -> None:
        """Initialize DefaultValueElement."""
        super().__init__()
        self.element_byte_value: Optional[Integer] = None
        self.element_position: Optional[Integer] = None

    def serialize(self) -> ET.Element:
        """Serialize DefaultValueElement to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DefaultValueElement, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize element_byte_value
        if self.element_byte_value is not None:
            serialized = SerializationHelper.serialize_item(self.element_byte_value, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ELEMENT-BYTE-VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize element_position
        if self.element_position is not None:
            serialized = SerializationHelper.serialize_item(self.element_position, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ELEMENT-POSITION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DefaultValueElement":
        """Deserialize XML element to DefaultValueElement object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DefaultValueElement object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DefaultValueElement, cls).deserialize(element)

        # Parse element_byte_value
        child = SerializationHelper.find_child_element(element, "ELEMENT-BYTE-VALUE")
        if child is not None:
            element_byte_value_value = child.text
            obj.element_byte_value = element_byte_value_value

        # Parse element_position
        child = SerializationHelper.find_child_element(element, "ELEMENT-POSITION")
        if child is not None:
            element_position_value = child.text
            obj.element_position = element_position_value

        return obj



class DefaultValueElementBuilder:
    """Builder for DefaultValueElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DefaultValueElement = DefaultValueElement()

    def build(self) -> DefaultValueElement:
        """Build and return DefaultValueElement object.

        Returns:
            DefaultValueElement instance
        """
        # TODO: Add validation
        return self._obj
