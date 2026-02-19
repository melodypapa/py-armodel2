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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest.binary_manifest_item import (
    BinaryManifestItem,
)


class BinaryManifestItemDefinition(Identifiable):
    """AUTOSAR BinaryManifestItemDefinition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    auxiliary_fields: list[BinaryManifestItem]
    is_optional: Optional[Boolean]
    size: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize BinaryManifestItemDefinition."""
        super().__init__()
        self.auxiliary_fields: list[BinaryManifestItem] = []
        self.is_optional: Optional[Boolean] = None
        self.size: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "BinaryManifestItemDefinition":
        """Deserialize XML element to BinaryManifestItemDefinition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BinaryManifestItemDefinition object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse auxiliary_fields (list)
        obj.auxiliary_fields = []
        for child in ARObject._find_all_child_elements(element, "AUXILIARY-FIELDS"):
            auxiliary_fields_value = ARObject._deserialize_by_tag(child, "BinaryManifestItem")
            obj.auxiliary_fields.append(auxiliary_fields_value)

        # Parse is_optional
        child = ARObject._find_child_element(element, "IS-OPTIONAL")
        if child is not None:
            is_optional_value = child.text
            obj.is_optional = is_optional_value

        # Parse size
        child = ARObject._find_child_element(element, "SIZE")
        if child is not None:
            size_value = child.text
            obj.size = size_value

        return obj



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
