"""CryptoKeySlot AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 57)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_AdaptivePlatform_PlatformModuleDeployment_CryptoDeployment.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "allocate_shadow": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # allocateShadow
        "crypto_alg_id": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # cryptoAlgId
        "crypto_object_type_enum": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (CryptoObjectTypeEnum),
        ),  # cryptoObjectTypeEnum
        "key_slot_allowed": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (CryptoKeySlotAllowed),
        ),  # keySlotAllowed
        "key_slot_contents": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (CryptoKeySlotContent),
        ),  # keySlotContents
        "slot_capacity": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # slotCapacity
        "slot_type": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (CryptoKeySlotType),
        ),  # slotType
    }

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
