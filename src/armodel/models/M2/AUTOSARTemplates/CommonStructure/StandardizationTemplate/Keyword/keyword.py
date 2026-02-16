"""Keyword AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
)


class Keyword(Identifiable):
    """AUTOSAR Keyword."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("abbr_name", None, True, False, None),  # abbrName
        ("classifications", None, False, True, None),  # classifications
    ]

    def __init__(self) -> None:
        """Initialize Keyword."""
        super().__init__()
        self.abbr_name: NameToken = None
        self.classifications: list[NameToken] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert Keyword to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Keyword":
        """Create Keyword from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            Keyword instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to Keyword since parent returns ARObject
        return cast("Keyword", obj)


class KeywordBuilder:
    """Builder for Keyword."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Keyword = Keyword()

    def build(self) -> Keyword:
        """Build and return Keyword object.

        Returns:
            Keyword instance
        """
        # TODO: Add validation
        return self._obj
