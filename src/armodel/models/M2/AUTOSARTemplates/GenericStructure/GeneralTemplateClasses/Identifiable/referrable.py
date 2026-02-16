"""Referrable AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.short_name_fragment import (
    ShortNameFragment,
)


class Referrable(ARObject):
    """AUTOSAR Referrable."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("short_name", None, True, False, None),  # shortName
        ("short_name_fragments", None, False, True, ShortNameFragment),  # shortNameFragments
    ]

    def __init__(self) -> None:
        """Initialize Referrable."""
        super().__init__()
        self.short_name: Identifier = None
        self.short_name_fragments: list[ShortNameFragment] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert Referrable to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Referrable":
        """Create Referrable from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            Referrable instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to Referrable since parent returns ARObject
        return cast("Referrable", obj)


class ReferrableBuilder:
    """Builder for Referrable."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Referrable = Referrable()

    def build(self) -> Referrable:
        """Build and return Referrable object.

        Returns:
            Referrable instance
        """
        # TODO: Add validation
        return self._obj
