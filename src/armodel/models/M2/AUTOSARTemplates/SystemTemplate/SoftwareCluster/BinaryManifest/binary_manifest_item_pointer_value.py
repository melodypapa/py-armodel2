"""BinaryManifestItemPointerValue AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 922)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster_BinaryManifest.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest.binary_manifest_item_value import (
    BinaryManifestItemValue,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Address,
    SymbolString,
)


class BinaryManifestItemPointerValue(BinaryManifestItemValue):
    """AUTOSAR BinaryManifestItemPointerValue."""

    address: Optional[Address]
    symbol: Optional[SymbolString]
    def __init__(self) -> None:
        """Initialize BinaryManifestItemPointerValue."""
        super().__init__()
        self.address: Optional[Address] = None
        self.symbol: Optional[SymbolString] = None


class BinaryManifestItemPointerValueBuilder:
    """Builder for BinaryManifestItemPointerValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BinaryManifestItemPointerValue = BinaryManifestItemPointerValue()

    def build(self) -> BinaryManifestItemPointerValue:
        """Build and return BinaryManifestItemPointerValue object.

        Returns:
            BinaryManifestItemPointerValue instance
        """
        # TODO: Add validation
        return self._obj
