"""CouplingPortStructuralElement AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)


class CouplingPortStructuralElement(Identifiable):
    """AUTOSAR CouplingPortStructuralElement."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize CouplingPortStructuralElement."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CouplingPortStructuralElement to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CouplingPortStructuralElement":
        """Create CouplingPortStructuralElement from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CouplingPortStructuralElement instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CouplingPortStructuralElement since parent returns ARObject
        return cast("CouplingPortStructuralElement", obj)


class CouplingPortStructuralElementBuilder:
    """Builder for CouplingPortStructuralElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CouplingPortStructuralElement = CouplingPortStructuralElement()

    def build(self) -> CouplingPortStructuralElement:
        """Build and return CouplingPortStructuralElement object.

        Returns:
            CouplingPortStructuralElement instance
        """
        # TODO: Add validation
        return self._obj
