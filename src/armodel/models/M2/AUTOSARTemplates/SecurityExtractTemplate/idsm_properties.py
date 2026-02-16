"""IdsmProperties AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.ids_common_element import (
    IdsCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.idsm_rate_limitation import (
    IdsmRateLimitation,
)
from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.idsm_traffic_limitation import (
    IdsmTrafficLimitation,
)


class IdsmProperties(IdsCommonElement):
    """AUTOSAR IdsmProperties."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("rate_limitations", None, False, True, IdsmRateLimitation),  # rateLimitations
        ("traffic_limitations", None, False, True, IdsmTrafficLimitation),  # trafficLimitations
    ]

    def __init__(self) -> None:
        """Initialize IdsmProperties."""
        super().__init__()
        self.rate_limitations: list[IdsmRateLimitation] = []
        self.traffic_limitations: list[IdsmTrafficLimitation] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert IdsmProperties to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IdsmProperties":
        """Create IdsmProperties from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            IdsmProperties instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to IdsmProperties since parent returns ARObject
        return cast("IdsmProperties", obj)


class IdsmPropertiesBuilder:
    """Builder for IdsmProperties."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IdsmProperties = IdsmProperties()

    def build(self) -> IdsmProperties:
        """Build and return IdsmProperties object.

        Returns:
            IdsmProperties instance
        """
        # TODO: Add validation
        return self._obj
