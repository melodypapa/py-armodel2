"""CryptoKeySlot AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 57)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_AdaptivePlatform_PlatformModuleDeployment_CryptoDeployment.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    allocate_shadow: Optional[Boolean]
    crypto_alg_id: Optional[String]
    crypto_object_type_enum: Optional[Any]
    key_slot_allowed: Optional[Any]
    key_slot_contents: list[Any]
    slot_capacity: Optional[PositiveInteger]
    slot_type: Optional[Any]
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
