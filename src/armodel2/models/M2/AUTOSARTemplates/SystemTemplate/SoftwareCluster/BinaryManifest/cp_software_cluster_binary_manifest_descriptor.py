"""CpSoftwareClusterBinaryManifestDescriptor AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 913)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster_BinaryManifest.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest.binary_manifest_meta_data_field import (
    BinaryManifestMetaDataField,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest.binary_manifest_provide_resource import (
    BinaryManifestProvideResource,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.BinaryManifest.binary_manifest_require_resource import (
    BinaryManifestRequireResource,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class CpSoftwareClusterBinaryManifestDescriptor(ARElement):
    """AUTOSAR CpSoftwareClusterBinaryManifestDescriptor."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CP-SOFTWARE-CLUSTER-BINARY-MANIFEST-DESCRIPTOR"


    cp_software_cluster_ref: Optional[ARRef]
    meta_data_fields: list[BinaryManifestMetaDataField]
    provides: list[BinaryManifestProvideResource]
    requires: list[BinaryManifestRequireResource]
    resources: list[Any]
    software_cluster: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "CP-SOFTWARE-CLUSTER-REF": lambda obj, elem: setattr(obj, "cp_software_cluster_ref", ARRef.deserialize(elem)),
        "META-DATA-FIELDS": lambda obj, elem: obj.meta_data_fields.append(SerializationHelper.deserialize_by_tag(elem, "BinaryManifestMetaDataField")),
        "PROVIDES": lambda obj, elem: obj.provides.append(SerializationHelper.deserialize_by_tag(elem, "BinaryManifestProvideResource")),
        "REQUIRES": lambda obj, elem: obj.requires.append(SerializationHelper.deserialize_by_tag(elem, "BinaryManifestRequireResource")),
        "RESOURCES": lambda obj, elem: obj.resources.append(SerializationHelper.deserialize_by_tag(elem, "any (BinaryManifest)")),
        "SOFTWARE-CLUSTER": lambda obj, elem: setattr(obj, "software_cluster", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


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
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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
            serialized = SerializationHelper.serialize_item(self.cp_software_cluster_ref, "CpSoftwareCluster")
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
                serialized = SerializationHelper.serialize_item(item, "BinaryManifestMetaDataField")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize provides (list to container "PROVIDES")
        if self.provides:
            wrapper = ET.Element("PROVIDES")
            for item in self.provides:
                serialized = SerializationHelper.serialize_item(item, "BinaryManifestProvideResource")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize requires (list to container "REQUIRES")
        if self.requires:
            wrapper = ET.Element("REQUIRES")
            for item in self.requires:
                serialized = SerializationHelper.serialize_item(item, "BinaryManifestRequireResource")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize resources (list to container "RESOURCES")
        if self.resources:
            wrapper = ET.Element("RESOURCES")
            for item in self.resources:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize software_cluster
        if self.software_cluster is not None:
            serialized = SerializationHelper.serialize_item(self.software_cluster, "PositiveInteger")
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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CP-SOFTWARE-CLUSTER-REF":
                setattr(obj, "cp_software_cluster_ref", ARRef.deserialize(child))
            elif tag == "META-DATA-FIELDS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.meta_data_fields.append(SerializationHelper.deserialize_by_tag(item_elem, "BinaryManifestMetaDataField"))
            elif tag == "PROVIDES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.provides.append(SerializationHelper.deserialize_by_tag(item_elem, "BinaryManifestProvideResource"))
            elif tag == "REQUIRES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.requires.append(SerializationHelper.deserialize_by_tag(item_elem, "BinaryManifestRequireResource"))
            elif tag == "RESOURCES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.resources.append(SerializationHelper.deserialize_by_tag(item_elem, "any (BinaryManifest)"))
            elif tag == "SOFTWARE-CLUSTER":
                setattr(obj, "software_cluster", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class CpSoftwareClusterBinaryManifestDescriptorBuilder(ARElementBuilder):
    """Builder for CpSoftwareClusterBinaryManifestDescriptor with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CpSoftwareClusterBinaryManifestDescriptor = CpSoftwareClusterBinaryManifestDescriptor()


    def with_cp_software_cluster(self, value: Optional[CpSoftwareCluster]) -> "CpSoftwareClusterBinaryManifestDescriptorBuilder":
        """Set cp_software_cluster attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'cp_software_cluster' is required and cannot be None")
        self._obj.cp_software_cluster = value
        return self

    def with_meta_data_fields(self, items: list[BinaryManifestMetaDataField]) -> "CpSoftwareClusterBinaryManifestDescriptorBuilder":
        """Set meta_data_fields list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.meta_data_fields = list(items) if items else []
        return self

    def with_provides(self, items: list[BinaryManifestProvideResource]) -> "CpSoftwareClusterBinaryManifestDescriptorBuilder":
        """Set provides list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.provides = list(items) if items else []
        return self

    def with_requires(self, items: list[BinaryManifestRequireResource]) -> "CpSoftwareClusterBinaryManifestDescriptorBuilder":
        """Set requires list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.requires = list(items) if items else []
        return self

    def with_resources(self, items: list[Any]) -> "CpSoftwareClusterBinaryManifestDescriptorBuilder":
        """Set resources list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.resources = list(items) if items else []
        return self

    def with_software_cluster(self, value: Optional[PositiveInteger]) -> "CpSoftwareClusterBinaryManifestDescriptorBuilder":
        """Set software_cluster attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'software_cluster' is required and cannot be None")
        self._obj.software_cluster = value
        return self


    def add_meta_data_field(self, item: BinaryManifestMetaDataField) -> "CpSoftwareClusterBinaryManifestDescriptorBuilder":
        """Add a single item to meta_data_fields list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.meta_data_fields.append(item)
        return self

    def clear_meta_data_fields(self) -> "CpSoftwareClusterBinaryManifestDescriptorBuilder":
        """Clear all items from meta_data_fields list.

        Returns:
            self for method chaining
        """
        self._obj.meta_data_fields = []
        return self

    def add_provide(self, item: BinaryManifestProvideResource) -> "CpSoftwareClusterBinaryManifestDescriptorBuilder":
        """Add a single item to provides list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.provides.append(item)
        return self

    def clear_provides(self) -> "CpSoftwareClusterBinaryManifestDescriptorBuilder":
        """Clear all items from provides list.

        Returns:
            self for method chaining
        """
        self._obj.provides = []
        return self

    def add_require(self, item: BinaryManifestRequireResource) -> "CpSoftwareClusterBinaryManifestDescriptorBuilder":
        """Add a single item to requires list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.requires.append(item)
        return self

    def clear_requires(self) -> "CpSoftwareClusterBinaryManifestDescriptorBuilder":
        """Clear all items from requires list.

        Returns:
            self for method chaining
        """
        self._obj.requires = []
        return self

    def add_resource(self, item: Any) -> "CpSoftwareClusterBinaryManifestDescriptorBuilder":
        """Add a single item to resources list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.resources.append(item)
        return self

    def clear_resources(self) -> "CpSoftwareClusterBinaryManifestDescriptorBuilder":
        """Clear all items from resources list.

        Returns:
            self for method chaining
        """
        self._obj.resources = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "cpSoftwareCluster",
        "metaDataField",
        "provide",
        "require",
        "resource",
        "softwareCluster",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> CpSoftwareClusterBinaryManifestDescriptor:
        """Build and return the CpSoftwareClusterBinaryManifestDescriptor instance with validation."""
        self._validate_instance()
        return self._obj