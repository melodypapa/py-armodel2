"""BinaryManifestItemDefinition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 920)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster_BinaryManifest.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest.binary_manifest_item import (
    BinaryManifestItem,
)


class BinaryManifestItemDefinition(Identifiable):
    """AUTOSAR BinaryManifestItemDefinition."""

    auxiliary_fields: list[BinaryManifestItem]
    is_optional: Optional[Boolean]
    size: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize BinaryManifestItemDefinition."""
        super().__init__()
        self.auxiliary_fields: list[BinaryManifestItem] = []
        self.is_optional: Optional[Boolean] = None
        self.size: Optional[PositiveInteger] = None


class BinaryManifestItemDefinitionBuilder:
    """Builder for BinaryManifestItemDefinition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BinaryManifestItemDefinition = BinaryManifestItemDefinition()

    def build(self) -> BinaryManifestItemDefinition:
        """Build and return BinaryManifestItemDefinition object.

        Returns:
            BinaryManifestItemDefinition instance
        """
        # TODO: Add validation
        return self._obj
