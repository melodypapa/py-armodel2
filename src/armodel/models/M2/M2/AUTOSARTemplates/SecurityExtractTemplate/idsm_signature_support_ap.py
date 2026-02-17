"""IdsmSignatureSupportAp AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 64)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.CryptoDeployment.crypto_key_slot import (
    CryptoKeySlot,
)


class IdsmSignatureSupportAp(ARObject):
    """AUTOSAR IdsmSignatureSupportAp."""

    def __init__(self) -> None:
        """Initialize IdsmSignatureSupportAp."""
        super().__init__()
        self.crypto_primitive: String = None
        self.key_slot: Optional[CryptoKeySlot] = None


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
