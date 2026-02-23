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
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


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
        tag = SerializationHelper.get_xml_tag(self.__class__)
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

        # Parse cp_software_cluster_ref
        child = SerializationHelper.find_child_element(element, "CP-SOFTWARE-CLUSTER-REF")
        if child is not None:
            cp_software_cluster_ref_value = ARRef.deserialize(child)
            obj.cp_software_cluster_ref = cp_software_cluster_ref_value

        # Parse meta_data_fields (list from container "META-DATA-FIELDS")
        obj.meta_data_fields = []
        container = SerializationHelper.find_child_element(element, "META-DATA-FIELDS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.meta_data_fields.append(child_value)

        # Parse provides (list from container "PROVIDES")
        obj.provides = []
        container = SerializationHelper.find_child_element(element, "PROVIDES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.provides.append(child_value)

        # Parse requires (list from container "REQUIRES")
        obj.requires = []
        container = SerializationHelper.find_child_element(element, "REQUIRES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.requires.append(child_value)

        # Parse resources (list from container "RESOURCES")
        obj.resources = []
        container = SerializationHelper.find_child_element(element, "RESOURCES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.resources.append(child_value)

        # Parse software_cluster
        child = SerializationHelper.find_child_element(element, "SOFTWARE-CLUSTER")
        if child is not None:
            software_cluster_value = child.text
            obj.software_cluster = software_cluster_value

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
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
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

    def with_resources(self, items: list[any (BinaryManifest)]) -> "CpSoftwareClusterBinaryManifestDescriptorBuilder":
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
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
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

    def add_resource(self, item: any (BinaryManifest)) -> "CpSoftwareClusterBinaryManifestDescriptorBuilder":
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



    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Get type hints for the class
        try:
            type_hints_dict = get_type_hints(type(self._obj))
        except Exception:
            # Cannot resolve type hints (e.g., forward references), skip validation
            return

        for attr_name, attr_type in type_hints_dict.items():
            if attr_name.startswith("_"):
                continue

            value = getattr(self._obj, attr_name)

            # Check required fields (not Optional)
            if value is None and not self._is_optional_type(attr_type):
                if mode == BuilderValidationMode.STRICT:
                    raise ValueError(
                        f"Required attribute '{attr_name}' is None"
                    )
                elif mode == BuilderValidationMode.LENIENT:
                    import warnings
                    warnings.warn(
                        f"Required attribute '{attr_name}' is None",
                        UserWarning
                    )

    @staticmethod
    def _is_optional_type(type_hint: Any) -> bool:
        """Check if a type hint is Optional.

        Args:
            type_hint: Type hint to check

        Returns:
            True if type is Optional, False otherwise
        """
        origin = getattr(type_hint, "__origin__", None)
        return origin is Union

    @staticmethod
    def _get_expected_type(type_hint: Any) -> type:
        """Extract expected type from type hint.

        Args:
            type_hint: Type hint to extract from

        Returns:
            Expected type
        """
        if isinstance(type_hint, str):
            return object
        origin = getattr(type_hint, "__origin__", None)
        if origin is Union:
            args = getattr(type_hint, "__args__", [])
            for arg in args:
                if arg is not type(None):
                    return arg
        elif origin is list:
            args = getattr(type_hint, "__args__", [object])
            return args[0] if args else object
        return type_hint if isinstance(type_hint, type) else object


    def build(self) -> CpSoftwareClusterBinaryManifestDescriptor:
        """Build and return the CpSoftwareClusterBinaryManifestDescriptor instance with validation."""
        self._validate_instance()
        pass
        return self._obj