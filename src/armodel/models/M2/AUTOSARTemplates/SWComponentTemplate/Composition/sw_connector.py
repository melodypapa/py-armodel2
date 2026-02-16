"""SwConnector AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface_mapping import (
    PortInterfaceMapping,
)


class SwConnector(Identifiable):
    """AUTOSAR SwConnector."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("mapping", None, False, False, PortInterfaceMapping),  # mapping
    ]

    def __init__(self) -> None:
        """Initialize SwConnector."""
        super().__init__()
        self.mapping: Optional[PortInterfaceMapping] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SwConnector to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwConnector":
        """Create SwConnector from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SwConnector instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SwConnector since parent returns ARObject
        return cast("SwConnector", obj)


class SwConnectorBuilder:
    """Builder for SwConnector."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwConnector = SwConnector()

    def build(self) -> SwConnector:
        """Build and return SwConnector object.

        Returns:
            SwConnector instance
        """
        # TODO: Add validation
        return self._obj
