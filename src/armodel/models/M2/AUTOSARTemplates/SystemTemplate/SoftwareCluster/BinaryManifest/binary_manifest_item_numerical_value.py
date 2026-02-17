"""BinaryManifestItemNumericalValue AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 922)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster_BinaryManifest.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest.binary_manifest_item_value import (
    BinaryManifestItemValue,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
)


class BinaryManifestItemNumericalValue(BinaryManifestItemValue):
    """AUTOSAR BinaryManifestItemNumericalValue."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "value": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # value
    }

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
