"""BinaryManifestItem AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 919)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster_BinaryManifest.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest.binary_manifest_addressable_object import (
    BinaryManifestAddressableObject,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class BinaryManifestItem(BinaryManifestAddressableObject):
    """AUTOSAR BinaryManifestItem."""

    def __init__(self) -> None:
        """Initialize BinaryManifestItem."""
        super().__init__()
        self.auxiliary_fields: list[BinaryManifestItem] = []
        self.default_value: Optional[BinaryManifestItem] = None
        self.is_unused: Optional[Boolean] = None
        self.value: Optional[BinaryManifestItem] = None


class BinaryManifestItemBuilder:
    """Builder for BinaryManifestItem."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BinaryManifestItem = BinaryManifestItem()

    def build(self) -> BinaryManifestItem:
        """Build and return BinaryManifestItem object.

        Returns:
            BinaryManifestItem instance
        """
        # TODO: Add validation
        return self._obj
