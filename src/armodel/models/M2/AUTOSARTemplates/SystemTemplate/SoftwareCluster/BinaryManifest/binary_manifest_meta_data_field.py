"""BinaryManifestMetaDataField AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 923)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster_BinaryManifest.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest.binary_manifest_addressable_object import (
    BinaryManifestAddressableObject,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    VerbatimString,
)


class BinaryManifestMetaDataField(BinaryManifestAddressableObject):
    """AUTOSAR BinaryManifestMetaDataField."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    size: Optional[PositiveInteger]
    value: Optional[VerbatimString]
    def __init__(self) -> None:
        """Initialize BinaryManifestMetaDataField."""
        super().__init__()
        self.size: Optional[PositiveInteger] = None
        self.value: Optional[VerbatimString] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "BinaryManifestMetaDataField":
        """Deserialize XML element to BinaryManifestMetaDataField object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BinaryManifestMetaDataField object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BinaryManifestMetaDataField, cls).deserialize(element)

        # Parse size
        child = ARObject._find_child_element(element, "SIZE")
        if child is not None:
            size_value = child.text
            obj.size = size_value

        # Parse value
        child = ARObject._find_child_element(element, "VALUE")
        if child is not None:
            value_value = ARObject._deserialize_by_tag(child, "VerbatimString")
            obj.value = value_value

        return obj



class BinaryManifestMetaDataFieldBuilder:
    """Builder for BinaryManifestMetaDataField."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BinaryManifestMetaDataField = BinaryManifestMetaDataField()

    def build(self) -> BinaryManifestMetaDataField:
        """Build and return BinaryManifestMetaDataField object.

        Returns:
            BinaryManifestMetaDataField instance
        """
        # TODO: Add validation
        return self._obj
