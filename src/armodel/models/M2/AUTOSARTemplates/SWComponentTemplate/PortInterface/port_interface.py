"""PortInterface AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class PortInterface(ARElement):
    """AUTOSAR PortInterface."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("is_service", None, True, False, None),  # isService
        ("service_kind", None, False, False, ServiceProviderEnum),  # serviceKind
    ]

    def __init__(self) -> None:
        """Initialize PortInterface."""
        super().__init__()
        self.is_service: Optional[Boolean] = None
        self.service_kind: Optional[ServiceProviderEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert PortInterface to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PortInterface":
        """Create PortInterface from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            PortInterface instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to PortInterface since parent returns ARObject
        return cast("PortInterface", obj)


class PortInterfaceBuilder:
    """Builder for PortInterface."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PortInterface = PortInterface()

    def build(self) -> PortInterface:
        """Build and return PortInterface object.

        Returns:
            PortInterface instance
        """
        # TODO: Add validation
        return self._obj
