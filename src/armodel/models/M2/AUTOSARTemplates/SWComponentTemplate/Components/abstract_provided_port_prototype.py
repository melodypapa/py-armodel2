"""AbstractProvidedPortPrototype AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.p_port_com_spec import (
    PPortComSpec,
)


class AbstractProvidedPortPrototype(PortPrototype):
    """AUTOSAR AbstractProvidedPortPrototype."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("provided_coms", None, False, True, PPortComSpec),  # providedComs
    ]

    def __init__(self) -> None:
        """Initialize AbstractProvidedPortPrototype."""
        super().__init__()
        self.provided_coms: list[PPortComSpec] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert AbstractProvidedPortPrototype to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AbstractProvidedPortPrototype":
        """Create AbstractProvidedPortPrototype from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            AbstractProvidedPortPrototype instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to AbstractProvidedPortPrototype since parent returns ARObject
        return cast("AbstractProvidedPortPrototype", obj)


class AbstractProvidedPortPrototypeBuilder:
    """Builder for AbstractProvidedPortPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractProvidedPortPrototype = AbstractProvidedPortPrototype()

    def build(self) -> AbstractProvidedPortPrototype:
        """Build and return AbstractProvidedPortPrototype object.

        Returns:
            AbstractProvidedPortPrototype instance
        """
        # TODO: Add validation
        return self._obj
