"""Sdf AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    Numerical,
)


class Sdf(ARObject):
    """AUTOSAR Sdf."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("gid", None, True, False, None),  # gid
        ("value", None, True, False, None),  # value
    ]

    def __init__(self) -> None:
        """Initialize Sdf."""
        super().__init__()
        self.gid: NameToken = None
        self.value: Optional[Numerical] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert Sdf to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Sdf":
        """Create Sdf from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            Sdf instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to Sdf since parent returns ARObject
        return cast("Sdf", obj)


class SdfBuilder:
    """Builder for Sdf."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Sdf = Sdf()

    def build(self) -> Sdf:
        """Build and return Sdf object.

        Returns:
            Sdf instance
        """
        # TODO: Add validation
        return self._obj
