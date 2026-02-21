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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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

    cp_software_cluster_ref: Optional[ARRef]
    meta_data_fields: list[BinaryManifestMetaDataField]
    provides: list[BinaryManifestProvideResource]
    requires: list[BinaryManifestRequireResource]
    resources: list[Any]
    software_cluster: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize CpSoftwareClusterBinaryManifestDescriptor."""
        super().__init__()
        self.cp_software_cluster_ref: Optional[ARRef] = None
        self.meta_data_fields: list[BinaryManifestMetaDataField] = []
        self.provides: list[BinaryManifestProvideResource] = []
        self.requires: list[BinaryManifestRequireResource] = []
        self.resources: list[Any] = []
        self.software_cluster: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize CpSoftwareClusterBinaryManifestDescriptor to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CpSoftwareClusterBinaryManifestDescriptor, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize cp_software_cluster_ref
        if self.cp_software_cluster_ref is not None:
            serialized = ARObject._serialize_item(self.cp_software_cluster_ref, "CpSoftwareCluster")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CP-SOFTWARE-CLUSTER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize meta_data_fields (list to container "META-DATA-FIELDS")
        if self.meta_data_fields:
            wrapper = ET.Element("META-DATA-FIELDS")
            for item in self.meta_data_fields:
                serialized = ARObject._serialize_item(item, "BinaryManifestMetaDataField")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize provides (list to container "PROVIDES")
        if self.provides:
            wrapper = ET.Element("PROVIDES")
            for item in self.provides:
                serialized = ARObject._serialize_item(item, "BinaryManifestProvideResource")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize requires (list to container "REQUIRES")
        if self.requires:
            wrapper = ET.Element("REQUIRES")
            for item in self.requires:
                serialized = ARObject._serialize_item(item, "BinaryManifestRequireResource")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize resources (list to container "RESOURCES")
        if self.resources:
            wrapper = ET.Element("RESOURCES")
            for item in self.resources:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize software_cluster
        if self.software_cluster is not None:
            serialized = ARObject._serialize_item(self.software_cluster, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SOFTWARE-CLUSTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CpSoftwareClusterBinaryManifestDescriptor":
        """Deserialize XML element to CpSoftwareClusterBinaryManifestDescriptor object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CpSoftwareClusterBinaryManifestDescriptor object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CpSoftwareClusterBinaryManifestDescriptor, cls).deserialize(element)

        # Parse cp_software_cluster_ref
        child = ARObject._find_child_element(element, "CP-SOFTWARE-CLUSTER-REF")
        if child is not None:
            cp_software_cluster_ref_value = ARRef.deserialize(child)
            obj.cp_software_cluster_ref = cp_software_cluster_ref_value

        # Parse meta_data_fields (list from container "META-DATA-FIELDS")
        obj.meta_data_fields = []
        container = ARObject._find_child_element(element, "META-DATA-FIELDS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.meta_data_fields.append(child_value)

        # Parse provides (list from container "PROVIDES")
        obj.provides = []
        container = ARObject._find_child_element(element, "PROVIDES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.provides.append(child_value)

        # Parse requires (list from container "REQUIRES")
        obj.requires = []
        container = ARObject._find_child_element(element, "REQUIRES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.requires.append(child_value)

        # Parse resources (list from container "RESOURCES")
        obj.resources = []
        container = ARObject._find_child_element(element, "RESOURCES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.resources.append(child_value)

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
