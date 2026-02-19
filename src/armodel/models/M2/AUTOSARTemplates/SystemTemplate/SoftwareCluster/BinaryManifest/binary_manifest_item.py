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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class BinaryManifestItem(BinaryManifestAddressableObject):
    """AUTOSAR BinaryManifestItem."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    auxiliary_fields: list[BinaryManifestItem]
    default_value: Optional[BinaryManifestItem]
    is_unused: Optional[Boolean]
    value: Optional[BinaryManifestItem]
    def __init__(self) -> None:
        """Initialize BinaryManifestItem."""
        super().__init__()
        self.auxiliary_fields: list[BinaryManifestItem] = []
        self.default_value: Optional[BinaryManifestItem] = None
        self.is_unused: Optional[Boolean] = None
        self.value: Optional[BinaryManifestItem] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "BinaryManifestItem":
        """Deserialize XML element to BinaryManifestItem object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BinaryManifestItem object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse auxiliary_fields (list)
        obj.auxiliary_fields = []
        for child in ARObject._find_all_child_elements(element, "AUXILIARY-FIELDS"):
            auxiliary_fields_value = ARObject._deserialize_by_tag(child, "BinaryManifestItem")
            obj.auxiliary_fields.append(auxiliary_fields_value)

        # Parse default_value
        child = ARObject._find_child_element(element, "DEFAULT-VALUE")
        if child is not None:
            default_value_value = ARObject._deserialize_by_tag(child, "BinaryManifestItem")
            obj.default_value = default_value_value

        # Parse is_unused
        child = ARObject._find_child_element(element, "IS-UNUSED")
        if child is not None:
            is_unused_value = child.text
            obj.is_unused = is_unused_value

        # Parse value
        child = ARObject._find_child_element(element, "VALUE")
        if child is not None:
            value_value = ARObject._deserialize_by_tag(child, "BinaryManifestItem")
            obj.value = value_value

        return obj



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
