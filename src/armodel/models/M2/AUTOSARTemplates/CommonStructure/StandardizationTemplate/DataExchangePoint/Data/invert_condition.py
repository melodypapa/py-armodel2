"""InvertCondition AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.abstract_condition import (
    AbstractCondition,
)


class InvertCondition(AbstractCondition):
    """AUTOSAR InvertCondition."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("condition", None, False, False, AbstractCondition),  # condition
    ]

    def __init__(self) -> None:
        """Initialize InvertCondition."""
        super().__init__()
        self.condition: AbstractCondition = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert InvertCondition to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "InvertCondition":
        """Create InvertCondition from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            InvertCondition instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to InvertCondition since parent returns ARObject
        return cast("InvertCondition", obj)


class InvertConditionBuilder:
    """Builder for InvertCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: InvertCondition = InvertCondition()

    def build(self) -> InvertCondition:
        """Build and return InvertCondition object.

        Returns:
            InvertCondition instance
        """
        # TODO: Add validation
        return self._obj
