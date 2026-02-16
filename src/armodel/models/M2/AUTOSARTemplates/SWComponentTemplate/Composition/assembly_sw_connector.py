"""AssemblySwConnector AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.sw_connector import (
    SwConnector,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_provided_port_prototype import (
    AbstractProvidedPortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_required_port_prototype import (
    AbstractRequiredPortPrototype,
)


class AssemblySwConnector(SwConnector):
    """AUTOSAR AssemblySwConnector."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("provider_instance_ref", None, False, False, AbstractProvidedPortPrototype),  # providerInstanceRef
        ("requester_instance_ref", None, False, False, AbstractRequiredPortPrototype),  # requesterInstanceRef
    ]

    def __init__(self) -> None:
        """Initialize AssemblySwConnector."""
        super().__init__()
        self.provider_instance_ref: Optional[AbstractProvidedPortPrototype] = None
        self.requester_instance_ref: Optional[AbstractRequiredPortPrototype] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert AssemblySwConnector to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AssemblySwConnector":
        """Create AssemblySwConnector from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            AssemblySwConnector instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to AssemblySwConnector since parent returns ARObject
        return cast("AssemblySwConnector", obj)


class AssemblySwConnectorBuilder:
    """Builder for AssemblySwConnector."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AssemblySwConnector = AssemblySwConnector()

    def build(self) -> AssemblySwConnector:
        """Build and return AssemblySwConnector object.

        Returns:
            AssemblySwConnector instance
        """
        # TODO: Add validation
        return self._obj
