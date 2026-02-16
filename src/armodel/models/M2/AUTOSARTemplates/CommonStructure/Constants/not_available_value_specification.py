"""NotAvailableValueSpecification AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
    ValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class NotAvailableValueSpecification(ValueSpecification):
    """AUTOSAR NotAvailableValueSpecification."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("default_pattern", None, True, False, None),  # defaultPattern
    ]

    def __init__(self) -> None:
        """Initialize NotAvailableValueSpecification."""
        super().__init__()
        self.default_pattern: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert NotAvailableValueSpecification to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "NotAvailableValueSpecification":
        """Create NotAvailableValueSpecification from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            NotAvailableValueSpecification instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to NotAvailableValueSpecification since parent returns ARObject
        return cast("NotAvailableValueSpecification", obj)


class NotAvailableValueSpecificationBuilder:
    """Builder for NotAvailableValueSpecification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: NotAvailableValueSpecification = NotAvailableValueSpecification()

    def build(self) -> NotAvailableValueSpecification:
        """Build and return NotAvailableValueSpecification object.

        Returns:
            NotAvailableValueSpecification instance
        """
        # TODO: Add validation
        return self._obj
