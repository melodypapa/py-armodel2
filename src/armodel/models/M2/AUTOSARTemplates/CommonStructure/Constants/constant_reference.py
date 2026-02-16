"""ConstantReference AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
    ValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.constant_specification import (
    ConstantSpecification,
)


class ConstantReference(ValueSpecification):
    """AUTOSAR ConstantReference."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("constant", None, False, False, ConstantSpecification),  # constant
    ]

    def __init__(self) -> None:
        """Initialize ConstantReference."""
        super().__init__()
        self.constant: Optional[ConstantSpecification] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ConstantReference to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ConstantReference":
        """Create ConstantReference from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ConstantReference instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ConstantReference since parent returns ARObject
        return cast("ConstantReference", obj)


class ConstantReferenceBuilder:
    """Builder for ConstantReference."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ConstantReference = ConstantReference()

    def build(self) -> ConstantReference:
        """Build and return ConstantReference object.

        Returns:
            ConstantReference instance
        """
        # TODO: Add validation
        return self._obj
