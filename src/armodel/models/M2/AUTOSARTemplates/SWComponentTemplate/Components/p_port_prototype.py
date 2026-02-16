"""PPortPrototype AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_provided_port_prototype import (
    AbstractProvidedPortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface import (
    PortInterface,
)


class PPortPrototype(AbstractProvidedPortPrototype):
    """AUTOSAR PPortPrototype."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("provided", None, False, False, PortInterface),  # provided
    ]

    def __init__(self) -> None:
        """Initialize PPortPrototype."""
        super().__init__()
        self.provided: Optional[PortInterface] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert PPortPrototype to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PPortPrototype":
        """Create PPortPrototype from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            PPortPrototype instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to PPortPrototype since parent returns ARObject
        return cast("PPortPrototype", obj)


class PPortPrototypeBuilder:
    """Builder for PPortPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PPortPrototype = PPortPrototype()

    def build(self) -> PPortPrototype:
        """Build and return PPortPrototype object.

        Returns:
            PPortPrototype instance
        """
        # TODO: Add validation
        return self._obj
