"""BinaryManifestProvideResource AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 914)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster_BinaryManifest.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest.binary_manifest_resource import (
    BinaryManifestResource,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class BinaryManifestProvideResource(BinaryManifestResource):
    """AUTOSAR BinaryManifestProvideResource."""

    number_of: Optional[PositiveInteger]
    supports: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize BinaryManifestProvideResource."""
        super().__init__()
        self.number_of: Optional[PositiveInteger] = None
        self.supports: Optional[Boolean] = None


class BinaryManifestProvideResourceBuilder:
    """Builder for BinaryManifestProvideResource."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BinaryManifestProvideResource = BinaryManifestProvideResource()

    def build(self) -> BinaryManifestProvideResource:
        """Build and return BinaryManifestProvideResource object.

        Returns:
            BinaryManifestProvideResource instance
        """
        # TODO: Add validation
        return self._obj
