"""CpSoftwareClusterBinaryManifestDescriptor AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 913)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster_BinaryManifest.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    cp_software_cluster: Optional[CpSoftwareCluster]
    meta_data_fields: list[BinaryManifestMetaDataField]
    provides: list[BinaryManifestProvideResource]
    requires: list[BinaryManifestRequireResource]
    resources: list[Any]
    software_cluster: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize CpSoftwareClusterBinaryManifestDescriptor."""
        super().__init__()
        self.cp_software_cluster: Optional[CpSoftwareCluster] = None
        self.meta_data_fields: list[BinaryManifestMetaDataField] = []
        self.provides: list[BinaryManifestProvideResource] = []
        self.requires: list[BinaryManifestRequireResource] = []
        self.resources: list[Any] = []
        self.software_cluster: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "CpSoftwareClusterBinaryManifestDescriptor":
        """Deserialize XML element to CpSoftwareClusterBinaryManifestDescriptor object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CpSoftwareClusterBinaryManifestDescriptor object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse cp_software_cluster
        child = ARObject._find_child_element(element, "CP-SOFTWARE-CLUSTER")
        if child is not None:
            cp_software_cluster_value = ARObject._deserialize_by_tag(child, "CpSoftwareCluster")
            obj.cp_software_cluster = cp_software_cluster_value

        # Parse meta_data_fields (list)
        obj.meta_data_fields = []
        for child in ARObject._find_all_child_elements(element, "META-DATA-FIELDS"):
            meta_data_fields_value = ARObject._deserialize_by_tag(child, "BinaryManifestMetaDataField")
            obj.meta_data_fields.append(meta_data_fields_value)

        # Parse provides (list)
        obj.provides = []
        for child in ARObject._find_all_child_elements(element, "PROVIDES"):
            provides_value = ARObject._deserialize_by_tag(child, "BinaryManifestProvideResource")
            obj.provides.append(provides_value)

        # Parse requires (list)
        obj.requires = []
        for child in ARObject._find_all_child_elements(element, "REQUIRES"):
            requires_value = ARObject._deserialize_by_tag(child, "BinaryManifestRequireResource")
            obj.requires.append(requires_value)

        # Parse resources (list)
        obj.resources = []
        for child in ARObject._find_all_child_elements(element, "RESOURCES"):
            resources_value = child.text
            obj.resources.append(resources_value)

        # Parse software_cluster
        child = ARObject._find_child_element(element, "SOFTWARE-CLUSTER")
        if child is not None:
            software_cluster_value = child.text
            obj.software_cluster = software_cluster_value

        return obj



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
