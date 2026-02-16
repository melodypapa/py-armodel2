"""AttributeCondition AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ModelRestrictionTypes.abstract_multiplicity_restriction import (
    AbstractMultiplicityRestriction,
)


class AttributeCondition(AbstractMultiplicityRestriction):
    """AUTOSAR AttributeCondition."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize AttributeCondition."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert AttributeCondition to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AttributeCondition":
        """Create AttributeCondition from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            AttributeCondition instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to AttributeCondition since parent returns ARObject
        return cast("AttributeCondition", obj)


class AttributeConditionBuilder:
    """Builder for AttributeCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AttributeCondition = AttributeCondition()

    def build(self) -> AttributeCondition:
        """Build and return AttributeCondition object.

        Returns:
            AttributeCondition instance
        """
        # TODO: Add validation
        return self._obj
