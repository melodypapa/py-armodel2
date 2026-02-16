"""DoIpRoutingActivationAuthenticationNeeds AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.do_ip_service_needs import (
    DoIpServiceNeeds,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    PositiveInteger,
)


class DoIpRoutingActivationAuthenticationNeeds(DoIpServiceNeeds):
    """AUTOSAR DoIpRoutingActivationAuthenticationNeeds."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("data_length", None, True, False, None),  # dataLength
        ("routing", None, True, False, None),  # routing
    ]

    def __init__(self) -> None:
        """Initialize DoIpRoutingActivationAuthenticationNeeds."""
        super().__init__()
        self.data_length: Optional[PositiveInteger] = None
        self.routing: Optional[NameToken] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DoIpRoutingActivationAuthenticationNeeds to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DoIpRoutingActivationAuthenticationNeeds":
        """Create DoIpRoutingActivationAuthenticationNeeds from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DoIpRoutingActivationAuthenticationNeeds instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DoIpRoutingActivationAuthenticationNeeds since parent returns ARObject
        return cast("DoIpRoutingActivationAuthenticationNeeds", obj)


class DoIpRoutingActivationAuthenticationNeedsBuilder:
    """Builder for DoIpRoutingActivationAuthenticationNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DoIpRoutingActivationAuthenticationNeeds = DoIpRoutingActivationAuthenticationNeeds()

    def build(self) -> DoIpRoutingActivationAuthenticationNeeds:
        """Build and return DoIpRoutingActivationAuthenticationNeeds object.

        Returns:
            DoIpRoutingActivationAuthenticationNeeds instance
        """
        # TODO: Add validation
        return self._obj
