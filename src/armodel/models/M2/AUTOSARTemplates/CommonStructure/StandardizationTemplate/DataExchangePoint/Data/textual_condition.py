"""TextualCondition AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 105)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Data.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.abstract_condition import (
    AbstractCondition,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class TextualCondition(AbstractCondition):
    """AUTOSAR TextualCondition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    text: String
    def __init__(self) -> None:
        """Initialize TextualCondition."""
        super().__init__()
        self.text: String = None

    def serialize(self) -> ET.Element:
        """Serialize TextualCondition to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TextualCondition, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize text
        if self.text is not None:
            serialized = SerializationHelper.serialize_item(self.text, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TEXT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TextualCondition":
        """Deserialize XML element to TextualCondition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TextualCondition object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TextualCondition, cls).deserialize(element)

        # Parse text
        child = SerializationHelper.find_child_element(element, "TEXT")
        if child is not None:
            text_value = child.text
            obj.text = text_value

        return obj



class TextualConditionBuilder:
    """Builder for TextualCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TextualCondition = TextualCondition()

    def build(self) -> TextualCondition:
        """Build and return TextualCondition object.

        Returns:
            TextualCondition instance
        """
        # TODO: Add validation
        return self._obj
