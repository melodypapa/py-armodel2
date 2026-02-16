"""ValueSpecification AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)


class ValueSpecification(ARObject):
    """AUTOSAR ValueSpecification."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("short_label", None, True, False, None),  # shortLabel
    ]

    def __init__(self) -> None:
        """Initialize ValueSpecification."""
        super().__init__()
        self.short_label: Optional[Identifier] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ValueSpecification to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ValueSpecification":
        """Create ValueSpecification from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ValueSpecification instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ValueSpecification since parent returns ARObject
        return cast("ValueSpecification", obj)


class ValueSpecificationBuilder:
    """Builder for ValueSpecification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ValueSpecification = ValueSpecification()

    def build(self) -> ValueSpecification:
        """Build and return ValueSpecification object.

        Returns:
            ValueSpecification instance
        """
        # TODO: Add validation
        return self._obj
