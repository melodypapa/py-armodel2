"""BinaryManifestRequireResource AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest.binary_manifest_resource import (
    BinaryManifestResource,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class BinaryManifestRequireResource(BinaryManifestResource):
    """AUTOSAR BinaryManifestRequireResource."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "connection_is": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # connectionIs
    }

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
