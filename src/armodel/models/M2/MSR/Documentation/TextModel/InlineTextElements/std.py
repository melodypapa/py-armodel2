"""Std AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.single_language_referrable import (
    SingleLanguageReferrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    DateTime,
    String,
)


class Std(SingleLanguageReferrable):
    """AUTOSAR Std."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("date", None, True, False, None),  # date
        ("position", None, True, False, None),  # position
        ("state", None, True, False, None),  # state
        ("subtitle", None, True, False, None),  # subtitle
        ("url", None, False, False, any (Url)),  # url
    ]

    def __init__(self) -> None:
        """Initialize Std."""
        super().__init__()
        self.date: Optional[DateTime] = None
        self.position: Optional[String] = None
        self.state: Optional[String] = None
        self.subtitle: Optional[String] = None
        self.url: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert Std to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Std":
        """Create Std from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            Std instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to Std since parent returns ARObject
        return cast("Std", obj)


class StdBuilder:
    """Builder for Std."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Std = Std()

    def build(self) -> Std:
        """Build and return Std object.

        Returns:
            Std instance
        """
        # TODO: Add validation
        return self._obj
