"""KeywordSet AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.Keyword.keyword import (
    Keyword,
)


class KeywordSet(ARElement):
    """AUTOSAR KeywordSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("keywords", None, False, True, Keyword),  # keywords
    ]

    def __init__(self) -> None:
        """Initialize KeywordSet."""
        super().__init__()
        self.keywords: list[Keyword] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert KeywordSet to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "KeywordSet":
        """Create KeywordSet from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            KeywordSet instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to KeywordSet since parent returns ARObject
        return cast("KeywordSet", obj)


class KeywordSetBuilder:
    """Builder for KeywordSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: KeywordSet = KeywordSet()

    def build(self) -> KeywordSet:
        """Build and return KeywordSet object.

        Returns:
            KeywordSet instance
        """
        # TODO: Add validation
        return self._obj
