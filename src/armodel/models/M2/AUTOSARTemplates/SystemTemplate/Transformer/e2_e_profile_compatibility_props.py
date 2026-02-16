"""E2EProfileCompatibilityProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class E2EProfileCompatibilityProps(ARElement):
    """AUTOSAR E2EProfileCompatibilityProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("transit_to_invalid", None, True, False, None),  # transitToInvalid
    ]

    def __init__(self) -> None:
        """Initialize E2EProfileCompatibilityProps."""
        super().__init__()
        self.transit_to_invalid: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert E2EProfileCompatibilityProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "E2EProfileCompatibilityProps":
        """Create E2EProfileCompatibilityProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            E2EProfileCompatibilityProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to E2EProfileCompatibilityProps since parent returns ARObject
        return cast("E2EProfileCompatibilityProps", obj)


class E2EProfileCompatibilityPropsBuilder:
    """Builder for E2EProfileCompatibilityProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: E2EProfileCompatibilityProps = E2EProfileCompatibilityProps()

    def build(self) -> E2EProfileCompatibilityProps:
        """Build and return E2EProfileCompatibilityProps object.

        Returns:
            E2EProfileCompatibilityProps instance
        """
        # TODO: Add validation
        return self._obj
