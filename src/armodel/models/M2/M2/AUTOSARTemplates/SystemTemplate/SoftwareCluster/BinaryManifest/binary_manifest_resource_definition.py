"""BinaryManifestResourceDefinition AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest.binary_manifest_item import (
    BinaryManifestItem,
)


class BinaryManifestResourceDefinition(Identifiable):
    """AUTOSAR BinaryManifestResourceDefinition."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "item_definitions": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=BinaryManifestItem,
        ),  # itemDefinitions
    }

    def __init__(self) -> None:
        """Initialize BinaryManifestResourceDefinition."""
        super().__init__()
        self.item_definitions: list[BinaryManifestItem] = []


class BinaryManifestResourceDefinitionBuilder:
    """Builder for BinaryManifestResourceDefinition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BinaryManifestResourceDefinition = BinaryManifestResourceDefinition()

    def build(self) -> BinaryManifestResourceDefinition:
        """Build and return BinaryManifestResourceDefinition object.

        Returns:
            BinaryManifestResourceDefinition instance
        """
        # TODO: Add validation
        return self._obj
