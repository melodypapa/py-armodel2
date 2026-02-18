"""BinaryManifestItemNumericalValue AUTOSAR element.

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
    Numerical,
)


class BinaryManifestItemNumericalValue(BinaryManifestItemValue):
    """AUTOSAR BinaryManifestItemNumericalValue."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    value: Optional[Numerical]
    def __init__(self) -> None:
        """Initialize BinaryManifestItemNumericalValue."""
        super().__init__()
        self.value: Optional[Numerical] = None


class BinaryManifestItemNumericalValueBuilder:
    """Builder for BinaryManifestItemNumericalValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BinaryManifestItemNumericalValue = BinaryManifestItemNumericalValue()

    def build(self) -> BinaryManifestItemNumericalValue:
        """Build and return BinaryManifestItemNumericalValue object.

        Returns:
            BinaryManifestItemNumericalValue instance
        """
        # TODO: Add validation
        return self._obj
