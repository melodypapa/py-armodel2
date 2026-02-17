"""CpSoftwareClusterBinaryManifestDescriptor AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 913)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster_BinaryManifest.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest.binary_manifest_meta_data_field import (
    BinaryManifestMetaDataField,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest.binary_manifest_provide_resource import (
    BinaryManifestProvideResource,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest.binary_manifest_require_resource import (
    BinaryManifestRequireResource,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)


class CpSoftwareClusterBinaryManifestDescriptor(ARElement):
    """AUTOSAR CpSoftwareClusterBinaryManifestDescriptor."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "cp_software_cluster": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CpSoftwareCluster,
        ),  # cpSoftwareCluster
        "meta_data_fields": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=BinaryManifestMetaDataField,
        ),  # metaDataFields
        "provides": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=BinaryManifestProvideResource,
        ),  # provides
        "requires": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=BinaryManifestRequireResource,
        ),  # requires
        "resources": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (BinaryManifest),
        ),  # resources
        "software_cluster": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # softwareCluster
    }

    def __init__(self) -> None:
        """Initialize CpSoftwareClusterBinaryManifestDescriptor."""
        super().__init__()
        self.cp_software_cluster: Optional[CpSoftwareCluster] = None
        self.meta_data_fields: list[BinaryManifestMetaDataField] = []
        self.provides: list[BinaryManifestProvideResource] = []
        self.requires: list[BinaryManifestRequireResource] = []
        self.resources: list[Any] = []
        self.software_cluster: Optional[PositiveInteger] = None


class CpSoftwareClusterBinaryManifestDescriptorBuilder:
    """Builder for CpSoftwareClusterBinaryManifestDescriptor."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CpSoftwareClusterBinaryManifestDescriptor = CpSoftwareClusterBinaryManifestDescriptor()

    def build(self) -> CpSoftwareClusterBinaryManifestDescriptor:
        """Build and return CpSoftwareClusterBinaryManifestDescriptor object.

        Returns:
            CpSoftwareClusterBinaryManifestDescriptor instance
        """
        # TODO: Add validation
        return self._obj
