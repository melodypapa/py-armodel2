"""EndToEndProtectionSet AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.EndToEndProtection.end_to_end_protection import (
    EndToEndProtection,
)


class EndToEndProtectionSet(ARElement):
    """AUTOSAR EndToEndProtectionSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("end_to_ends", None, False, True, EndToEndProtection),  # endToEnds
    ]

    def __init__(self) -> None:
        """Initialize EndToEndProtectionSet."""
        super().__init__()
        self.end_to_ends: list[EndToEndProtection] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EndToEndProtectionSet to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EndToEndProtectionSet":
        """Create EndToEndProtectionSet from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EndToEndProtectionSet instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EndToEndProtectionSet since parent returns ARObject
        return cast("EndToEndProtectionSet", obj)


class EndToEndProtectionSetBuilder:
    """Builder for EndToEndProtectionSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EndToEndProtectionSet = EndToEndProtectionSet()

    def build(self) -> EndToEndProtectionSet:
        """Build and return EndToEndProtectionSet object.

        Returns:
            EndToEndProtectionSet instance
        """
        # TODO: Add validation
        return self._obj
