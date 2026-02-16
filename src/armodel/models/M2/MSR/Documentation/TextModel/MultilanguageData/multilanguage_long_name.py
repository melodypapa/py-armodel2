"""MultilanguageLongName AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel.l_long_name import (
    LLongName,
)


class MultilanguageLongName(ARObject):
    """AUTOSAR MultilanguageLongName."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("l4", None, False, False, LLongName),  # l4
    ]

    def __init__(self) -> None:
        """Initialize MultilanguageLongName."""
        super().__init__()
        self.l4: LLongName = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert MultilanguageLongName to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MultilanguageLongName":
        """Create MultilanguageLongName from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            MultilanguageLongName instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to MultilanguageLongName since parent returns ARObject
        return cast("MultilanguageLongName", obj)


class MultilanguageLongNameBuilder:
    """Builder for MultilanguageLongName."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MultilanguageLongName = MultilanguageLongName()

    def build(self) -> MultilanguageLongName:
        """Build and return MultilanguageLongName object.

        Returns:
            MultilanguageLongName instance
        """
        # TODO: Add validation
        return self._obj
