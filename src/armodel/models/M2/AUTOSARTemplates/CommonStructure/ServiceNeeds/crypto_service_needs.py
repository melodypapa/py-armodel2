"""CryptoServiceNeeds AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)


class CryptoServiceNeeds(ServiceNeeds):
    """AUTOSAR CryptoServiceNeeds."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("algorithm_family", None, True, False, None),  # algorithmFamily
        ("algorithm_mode", None, True, False, None),  # algorithmMode
        ("crypto_key", None, True, False, None),  # cryptoKey
        ("maximum_key", None, True, False, None),  # maximumKey
    ]

    def __init__(self) -> None:
        """Initialize CryptoServiceNeeds."""
        super().__init__()
        self.algorithm_family: Optional[String] = None
        self.algorithm_mode: Optional[String] = None
        self.crypto_key: Optional[String] = None
        self.maximum_key: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CryptoServiceNeeds to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CryptoServiceNeeds":
        """Create CryptoServiceNeeds from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CryptoServiceNeeds instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CryptoServiceNeeds since parent returns ARObject
        return cast("CryptoServiceNeeds", obj)


class CryptoServiceNeedsBuilder:
    """Builder for CryptoServiceNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CryptoServiceNeeds = CryptoServiceNeeds()

    def build(self) -> CryptoServiceNeeds:
        """Build and return CryptoServiceNeeds object.

        Returns:
            CryptoServiceNeeds instance
        """
        # TODO: Add validation
        return self._obj
