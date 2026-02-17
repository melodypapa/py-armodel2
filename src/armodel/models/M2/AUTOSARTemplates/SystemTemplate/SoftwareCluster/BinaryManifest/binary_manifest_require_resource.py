"""BinaryManifestRequireResource AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 916)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster_BinaryManifest.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest.binary_manifest_resource import (
    BinaryManifestResource,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class BinaryManifestRequireResource(BinaryManifestResource):
    """AUTOSAR BinaryManifestRequireResource."""

    def __init__(self) -> None:
        """Initialize BinaryManifestRequireResource."""
        super().__init__()
        self.connection_is: Optional[Boolean] = None


class BinaryManifestRequireResourceBuilder:
    """Builder for BinaryManifestRequireResource."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BinaryManifestRequireResource = BinaryManifestRequireResource()

    def build(self) -> BinaryManifestRequireResource:
        """Build and return BinaryManifestRequireResource object.

        Returns:
            BinaryManifestRequireResource instance
        """
        # TODO: Add validation
        return self._obj
