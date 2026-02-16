"""CpSoftwareClusterBinaryManifestDescriptor AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
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
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("cp_software_cluster", None, False, False, CpSoftwareCluster),  # cpSoftwareCluster
        ("meta_data_fields", None, False, True, BinaryManifestMetaDataField),  # metaDataFields
        ("provides", None, False, True, BinaryManifestProvideResource),  # provides
        ("requires", None, False, True, BinaryManifestRequireResource),  # requires
        ("resources", None, False, True, any (BinaryManifest)),  # resources
        ("software_cluster", None, True, False, None),  # softwareCluster
    ]

    def __init__(self) -> None:
        """Initialize CpSoftwareClusterBinaryManifestDescriptor."""
        super().__init__()
        self.cp_software_cluster: Optional[CpSoftwareCluster] = None
        self.meta_data_fields: list[BinaryManifestMetaDataField] = []
        self.provides: list[BinaryManifestProvideResource] = []
        self.requires: list[BinaryManifestRequireResource] = []
        self.resources: list[Any] = []
        self.software_cluster: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CpSoftwareClusterBinaryManifestDescriptor to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CpSoftwareClusterBinaryManifestDescriptor":
        """Create CpSoftwareClusterBinaryManifestDescriptor from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CpSoftwareClusterBinaryManifestDescriptor instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CpSoftwareClusterBinaryManifestDescriptor since parent returns ARObject
        return cast("CpSoftwareClusterBinaryManifestDescriptor", obj)


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
