"""RecordValueSpecification AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.composite_value_specification import (
    CompositeValueSpecification,
)


class RecordValueSpecification(CompositeValueSpecification):
    """AUTOSAR RecordValueSpecification."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize RecordValueSpecification."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert RecordValueSpecification to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RecordValueSpecification":
        """Create RecordValueSpecification from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            RecordValueSpecification instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to RecordValueSpecification since parent returns ARObject
        return cast("RecordValueSpecification", obj)


class RecordValueSpecificationBuilder:
    """Builder for RecordValueSpecification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RecordValueSpecification = RecordValueSpecification()

    def build(self) -> RecordValueSpecification:
        """Build and return RecordValueSpecification object.

        Returns:
            RecordValueSpecification instance
        """
        # TODO: Add validation
        return self._obj
