"""CryptoKeySlot AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    String,
)


class CryptoKeySlot(Identifiable):
    """AUTOSAR CryptoKeySlot."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("allocate_shadow", None, True, False, None),  # allocateShadow
        ("crypto_alg_id", None, True, False, None),  # cryptoAlgId
        ("crypto_object_type_enum", None, False, False, any (CryptoObjectTypeEnum)),  # cryptoObjectTypeEnum
        ("key_slot_allowed", None, False, False, any (CryptoKeySlotAllowed)),  # keySlotAllowed
        ("key_slot_contents", None, False, True, any (CryptoKeySlotContent)),  # keySlotContents
        ("slot_capacity", None, True, False, None),  # slotCapacity
        ("slot_type", None, False, False, any (CryptoKeySlotType)),  # slotType
    ]

    def __init__(self) -> None:
        """Initialize CryptoKeySlot."""
        super().__init__()
        self.allocate_shadow: Optional[Boolean] = None
        self.crypto_alg_id: Optional[String] = None
        self.crypto_object_type_enum: Optional[Any] = None
        self.key_slot_allowed: Optional[Any] = None
        self.key_slot_contents: list[Any] = []
        self.slot_capacity: Optional[PositiveInteger] = None
        self.slot_type: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CryptoKeySlot to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CryptoKeySlot":
        """Create CryptoKeySlot from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CryptoKeySlot instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CryptoKeySlot since parent returns ARObject
        return cast("CryptoKeySlot", obj)


class CryptoKeySlotBuilder:
    """Builder for CryptoKeySlot."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CryptoKeySlot = CryptoKeySlot()

    def build(self) -> CryptoKeySlot:
        """Build and return CryptoKeySlot object.

        Returns:
            CryptoKeySlot instance
        """
        # TODO: Add validation
        return self._obj
