"""ArrayValueSpecification AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.composite_value_specification import (
    CompositeValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
    ValueSpecification,
)


class ArrayValueSpecification(CompositeValueSpecification):
    """AUTOSAR ArrayValueSpecification."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("elements", None, False, True, ValueSpecification),  # elements
        ("intended_partial", None, True, False, None),  # intendedPartial
    ]

    def __init__(self) -> None:
        """Initialize ArrayValueSpecification."""
        super().__init__()
        self.elements: list[ValueSpecification] = []
        self.intended_partial: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ArrayValueSpecification to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ArrayValueSpecification":
        """Create ArrayValueSpecification from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ArrayValueSpecification instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ArrayValueSpecification since parent returns ARObject
        return cast("ArrayValueSpecification", obj)


class ArrayValueSpecificationBuilder:
    """Builder for ArrayValueSpecification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ArrayValueSpecification = ArrayValueSpecification()

    def build(self) -> ArrayValueSpecification:
        """Build and return ArrayValueSpecification object.

        Returns:
            ArrayValueSpecification instance
        """
        # TODO: Add validation
        return self._obj
