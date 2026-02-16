"""EndToEndProtection AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.EndToEndProtection.end_to_end_protection import (
    EndToEndProtection,
)


class EndToEndProtection(Identifiable):
    """AUTOSAR EndToEndProtection."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("end_to_ends", None, False, True, EndToEndProtection),  # endToEnds
    ]

    def __init__(self) -> None:
        """Initialize EndToEndProtection."""
        super().__init__()
        self.end_to_ends: list[EndToEndProtection] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EndToEndProtection to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EndToEndProtection":
        """Create EndToEndProtection from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EndToEndProtection instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EndToEndProtection since parent returns ARObject
        return cast("EndToEndProtection", obj)


class EndToEndProtectionBuilder:
    """Builder for EndToEndProtection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EndToEndProtection = EndToEndProtection()

    def build(self) -> EndToEndProtection:
        """Build and return EndToEndProtection object.

        Returns:
            EndToEndProtection instance
        """
        # TODO: Add validation
        return self._obj
