"""TextualCondition AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.abstract_condition import (
    AbstractCondition,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class TextualCondition(AbstractCondition):
    """AUTOSAR TextualCondition."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("text", None, True, False, None),  # text
    ]

    def __init__(self) -> None:
        """Initialize TextualCondition."""
        super().__init__()
        self.text: String = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TextualCondition to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TextualCondition":
        """Create TextualCondition from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TextualCondition instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TextualCondition since parent returns ARObject
        return cast("TextualCondition", obj)


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
