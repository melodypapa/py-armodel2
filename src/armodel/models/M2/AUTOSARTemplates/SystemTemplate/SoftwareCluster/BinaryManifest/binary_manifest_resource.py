"""BinaryManifestResource AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 915)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster_BinaryManifest.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)


class BinaryManifestResource(Identifiable):
    """AUTOSAR BinaryManifestResource."""
    """Abstract base class - do not instantiate directly."""

    def __init__(self) -> None:
        """Initialize BinaryManifestResource."""
        super().__init__()
        self.global_resource: Optional[PositiveInteger] = None
        self.resource: Optional[Any] = None
        self.resource_guard: Optional[String] = None


class BinaryManifestResourceBuilder:
    """Builder for BinaryManifestResource."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BinaryManifestResource = BinaryManifestResource()

    def build(self) -> BinaryManifestResource:
        """Build and return BinaryManifestResource object.

        Returns:
            BinaryManifestResource instance
        """
        # TODO: Add validation
        return self._obj
