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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class BinaryManifestRequireResource(BinaryManifestResource):
    """AUTOSAR BinaryManifestRequireResource."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    connection_is: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize BinaryManifestRequireResource."""
        super().__init__()
        self.connection_is: Optional[Boolean] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "BinaryManifestRequireResource":
        """Deserialize XML element to BinaryManifestRequireResource object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BinaryManifestRequireResource object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BinaryManifestRequireResource, cls).deserialize(element)

        # Parse connection_is
        child = ARObject._find_child_element(element, "CONNECTION-IS")
        if child is not None:
            connection_is_value = child.text
            obj.connection_is = connection_is_value

        return obj



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
