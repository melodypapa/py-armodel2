"""DdsDurability AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject


class DdsDurability(ARObject):
    """AUTOSAR DdsDurability."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("durability_kind", None, False, False, DdsDurabilityKindEnum),  # durabilityKind
    ]

    def __init__(self) -> None:
        """Initialize DdsDurability."""
        super().__init__()
        self.durability_kind: Optional[DdsDurabilityKindEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DdsDurability to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsDurability":
        """Create DdsDurability from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DdsDurability instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DdsDurability since parent returns ARObject
        return cast("DdsDurability", obj)


class DdsDurabilityBuilder:
    """Builder for DdsDurability."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsDurability = DdsDurability()

    def build(self) -> DdsDurability:
        """Build and return DdsDurability object.

        Returns:
            DdsDurability instance
        """
        # TODO: Add validation
        return self._obj
