"""ShortNameFragment AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    String,
)


class ShortNameFragment(ARObject):
    """AUTOSAR ShortNameFragment."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("fragment", None, True, False, None),  # fragment
        ("role", None, True, False, None),  # role
    ]

    def __init__(self) -> None:
        """Initialize ShortNameFragment."""
        super().__init__()
        self.fragment: Identifier = None
        self.role: String = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ShortNameFragment to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ShortNameFragment":
        """Create ShortNameFragment from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ShortNameFragment instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ShortNameFragment since parent returns ARObject
        return cast("ShortNameFragment", obj)


class ShortNameFragmentBuilder:
    """Builder for ShortNameFragment."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ShortNameFragment = ShortNameFragment()

    def build(self) -> ShortNameFragment:
        """Build and return ShortNameFragment object.

        Returns:
            ShortNameFragment instance
        """
        # TODO: Add validation
        return self._obj
