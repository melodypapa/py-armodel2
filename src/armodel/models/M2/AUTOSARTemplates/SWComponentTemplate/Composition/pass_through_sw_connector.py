"""PassThroughSwConnector AUTOSAR element."""

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


class PassThroughSwConnector(SwConnector):
    """AUTOSAR PassThroughSwConnector."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("provided_outer", None, False, False, AbstractProvidedPortPrototype),  # providedOuter
        ("required_outer", None, False, False, AbstractRequiredPortPrototype),  # requiredOuter
    ]

    def __init__(self) -> None:
        """Initialize PassThroughSwConnector."""
        super().__init__()
        self.provided_outer: Optional[AbstractProvidedPortPrototype] = None
        self.required_outer: Optional[AbstractRequiredPortPrototype] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert PassThroughSwConnector to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PassThroughSwConnector":
        """Create PassThroughSwConnector from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            PassThroughSwConnector instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to PassThroughSwConnector since parent returns ARObject
        return cast("PassThroughSwConnector", obj)


class PassThroughSwConnectorBuilder:
    """Builder for PassThroughSwConnector."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PassThroughSwConnector = PassThroughSwConnector()

    def build(self) -> PassThroughSwConnector:
        """Build and return PassThroughSwConnector object.

        Returns:
            PassThroughSwConnector instance
        """
        # TODO: Add validation
        return self._obj
