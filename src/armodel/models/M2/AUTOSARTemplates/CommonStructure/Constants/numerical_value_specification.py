"""NumericalValueSpecification AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
    ValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
)


class NumericalValueSpecification(ValueSpecification):
    """AUTOSAR NumericalValueSpecification."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("value", None, True, False, None),  # value
    ]

    def __init__(self) -> None:
        """Initialize NumericalValueSpecification."""
        super().__init__()
        self.value: Optional[Numerical] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert NumericalValueSpecification to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "NumericalValueSpecification":
        """Create NumericalValueSpecification from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            NumericalValueSpecification instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to NumericalValueSpecification since parent returns ARObject
        return cast("NumericalValueSpecification", obj)


class NumericalValueSpecificationBuilder:
    """Builder for NumericalValueSpecification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: NumericalValueSpecification = NumericalValueSpecification()

    def build(self) -> NumericalValueSpecification:
        """Build and return NumericalValueSpecification object.

        Returns:
            NumericalValueSpecification instance
        """
        # TODO: Add validation
        return self._obj
