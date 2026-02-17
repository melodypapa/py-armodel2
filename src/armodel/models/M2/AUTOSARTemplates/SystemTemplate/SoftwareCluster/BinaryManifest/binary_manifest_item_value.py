"""BinaryManifestItemValue AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 922)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster_BinaryManifest.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class BinaryManifestItemValue(ARObject):
    """AUTOSAR BinaryManifestItemValue."""
    """Abstract base class - do not instantiate directly."""

    def __init__(self) -> None:
        """Initialize BinaryManifestItemValue."""
        super().__init__()


class BinaryManifestItemValueBuilder:
    """Builder for BinaryManifestItemValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BinaryManifestItemValue = BinaryManifestItemValue()

    def build(self) -> BinaryManifestItemValue:
        """Build and return BinaryManifestItemValue object.

        Returns:
            BinaryManifestItemValue instance
        """
        # TODO: Add validation
        return self._obj
