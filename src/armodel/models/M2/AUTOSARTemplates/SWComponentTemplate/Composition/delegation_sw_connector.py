"""DelegationSwConnector AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.sw_connector import (
    SwConnector,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)


class DelegationSwConnector(SwConnector):
    """AUTOSAR DelegationSwConnector."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("inner_port_instance_ref", None, False, False, PortPrototype),  # innerPortInstanceRef
        ("outer_port", None, False, False, PortPrototype),  # outerPort
    ]

    def __init__(self) -> None:
        """Initialize DelegationSwConnector."""
        super().__init__()
        self.inner_port_instance_ref: Optional[PortPrototype] = None
        self.outer_port: Optional[PortPrototype] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DelegationSwConnector to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DelegationSwConnector":
        """Create DelegationSwConnector from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DelegationSwConnector instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DelegationSwConnector since parent returns ARObject
        return cast("DelegationSwConnector", obj)


class DelegationSwConnectorBuilder:
    """Builder for DelegationSwConnector."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DelegationSwConnector = DelegationSwConnector()

    def build(self) -> DelegationSwConnector:
        """Build and return DelegationSwConnector object.

        Returns:
            DelegationSwConnector instance
        """
        # TODO: Add validation
        return self._obj
