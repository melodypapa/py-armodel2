"""IdsmSignatureSupportCp AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.crypto_service_key import (
    CryptoServiceKey,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.crypto_service_primitive import (
    CryptoServicePrimitive,
)


class IdsmSignatureSupportCp(ARObject):
    """AUTOSAR IdsmSignatureSupportCp."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("authentication", None, False, False, CryptoServicePrimitive),  # authentication
        ("crypto_service_key", None, False, False, CryptoServiceKey),  # cryptoServiceKey
    ]

    def __init__(self) -> None:
        """Initialize IdsmSignatureSupportCp."""
        super().__init__()
        self.authentication: Optional[CryptoServicePrimitive] = None
        self.crypto_service_key: Optional[CryptoServiceKey] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert IdsmSignatureSupportCp to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IdsmSignatureSupportCp":
        """Create IdsmSignatureSupportCp from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            IdsmSignatureSupportCp instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to IdsmSignatureSupportCp since parent returns ARObject
        return cast("IdsmSignatureSupportCp", obj)


class IdsmSignatureSupportCpBuilder:
    """Builder for IdsmSignatureSupportCp."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IdsmSignatureSupportCp = IdsmSignatureSupportCp()

    def build(self) -> IdsmSignatureSupportCp:
        """Build and return IdsmSignatureSupportCp object.

        Returns:
            IdsmSignatureSupportCp instance
        """
        # TODO: Add validation
        return self._obj
