"""IdsmSignatureSupportAp AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.CryptoDeployment.crypto_key_slot import (
    CryptoKeySlot,
)


class IdsmSignatureSupportAp(ARObject):
    """AUTOSAR IdsmSignatureSupportAp."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("crypto_primitive", None, True, False, None),  # cryptoPrimitive
        ("key_slot", None, False, False, CryptoKeySlot),  # keySlot
    ]

    def __init__(self) -> None:
        """Initialize IdsmSignatureSupportAp."""
        super().__init__()
        self.crypto_primitive: String = None
        self.key_slot: Optional[CryptoKeySlot] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert IdsmSignatureSupportAp to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IdsmSignatureSupportAp":
        """Create IdsmSignatureSupportAp from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            IdsmSignatureSupportAp instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to IdsmSignatureSupportAp since parent returns ARObject
        return cast("IdsmSignatureSupportAp", obj)


class IdsmSignatureSupportApBuilder:
    """Builder for IdsmSignatureSupportAp."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IdsmSignatureSupportAp = IdsmSignatureSupportAp()

    def build(self) -> IdsmSignatureSupportAp:
        """Build and return IdsmSignatureSupportAp object.

        Returns:
            IdsmSignatureSupportAp instance
        """
        # TODO: Add validation
        return self._obj
