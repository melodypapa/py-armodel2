"""CpSoftwareClusterMappingSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 285)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.port_element_to_communication_resource_mapping import (
    PortElementToCommunicationResourceMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.swc_to_application_partition_mapping import (
    SwcToApplicationPartitionMapping,
)


class CpSoftwareClusterMappingSet(ARElement):
    """AUTOSAR CpSoftwareClusterMappingSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    port_element_tos: list[PortElementToCommunicationResourceMapping]
    resource_tos: list[CpSoftwareCluster]
    software_clusters: list[Any]
    swc_tos: list[SwcToApplicationPartitionMapping]
    def __init__(self) -> None:
        """Initialize CpSoftwareClusterMappingSet."""
        super().__init__()
        self.port_element_tos: list[PortElementToCommunicationResourceMapping] = []
        self.resource_tos: list[CpSoftwareCluster] = []
        self.software_clusters: list[Any] = []
        self.swc_tos: list[SwcToApplicationPartitionMapping] = []

    def serialize(self) -> ET.Element:
        """Serialize CpSoftwareClusterMappingSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CpSoftwareClusterMappingSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize port_element_tos (list to container "PORT-ELEMENT-TOS")
        if self.port_element_tos:
            wrapper = ET.Element("PORT-ELEMENT-TOS")
            for item in self.port_element_tos:
                serialized = SerializationHelper.serialize_item(item, "PortElementToCommunicationResourceMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize resource_tos (list to container "RESOURCE-TOS")
        if self.resource_tos:
            wrapper = ET.Element("RESOURCE-TOS")
            for item in self.resource_tos:
                serialized = SerializationHelper.serialize_item(item, "CpSoftwareCluster")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize software_clusters (list to container "SOFTWARE-CLUSTERS")
        if self.software_clusters:
            wrapper = ET.Element("SOFTWARE-CLUSTERS")
            for item in self.software_clusters:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize swc_tos (list to container "SWC-TOS")
        if self.swc_tos:
            wrapper = ET.Element("SWC-TOS")
            for item in self.swc_tos:
                serialized = SerializationHelper.serialize_item(item, "SwcToApplicationPartitionMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CpSoftwareClusterMappingSet":
        """Deserialize XML element to CpSoftwareClusterMappingSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CpSoftwareClusterMappingSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CpSoftwareClusterMappingSet, cls).deserialize(element)

        # Parse port_element_tos (list from container "PORT-ELEMENT-TOS")
        obj.port_element_tos = []
        container = SerializationHelper.find_child_element(element, "PORT-ELEMENT-TOS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.port_element_tos.append(child_value)

        # Parse resource_tos (list from container "RESOURCE-TOS")
        obj.resource_tos = []
        container = SerializationHelper.find_child_element(element, "RESOURCE-TOS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.resource_tos.append(child_value)

        # Parse software_clusters (list from container "SOFTWARE-CLUSTERS")
        obj.software_clusters = []
        container = SerializationHelper.find_child_element(element, "SOFTWARE-CLUSTERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.software_clusters.append(child_value)

        # Parse swc_tos (list from container "SWC-TOS")
        obj.swc_tos = []
        container = SerializationHelper.find_child_element(element, "SWC-TOS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.swc_tos.append(child_value)

        return obj



class CpSoftwareClusterMappingSetBuilder(ARElementBuilder):
    """Builder for CpSoftwareClusterMappingSet with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CpSoftwareClusterMappingSet = CpSoftwareClusterMappingSet()


    def with_port_element_tos(self, items: list[PortElementToCommunicationResourceMapping]) -> "CpSoftwareClusterMappingSetBuilder":
        """Set port_element_tos list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.port_element_tos = list(items) if items else []
        return self

    def with_resource_tos(self, items: list[CpSoftwareCluster]) -> "CpSoftwareClusterMappingSetBuilder":
        """Set resource_tos list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.resource_tos = list(items) if items else []
        return self

    def with_software_clusters(self, items: list[any (CpSoftwareClusterTo)]) -> "CpSoftwareClusterMappingSetBuilder":
        """Set software_clusters list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.software_clusters = list(items) if items else []
        return self

    def with_swc_tos(self, items: list[SwcToApplicationPartitionMapping]) -> "CpSoftwareClusterMappingSetBuilder":
        """Set swc_tos list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.swc_tos = list(items) if items else []
        return self


    def add_port_element_to(self, item: PortElementToCommunicationResourceMapping) -> "CpSoftwareClusterMappingSetBuilder":
        """Add a single item to port_element_tos list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.port_element_tos.append(item)
        return self

    def clear_port_element_tos(self) -> "CpSoftwareClusterMappingSetBuilder":
        """Clear all items from port_element_tos list.

        Returns:
            self for method chaining
        """
        self._obj.port_element_tos = []
        return self

    def add_resource_to(self, item: CpSoftwareCluster) -> "CpSoftwareClusterMappingSetBuilder":
        """Add a single item to resource_tos list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.resource_tos.append(item)
        return self

    def clear_resource_tos(self) -> "CpSoftwareClusterMappingSetBuilder":
        """Clear all items from resource_tos list.

        Returns:
            self for method chaining
        """
        self._obj.resource_tos = []
        return self

    def add_software_cluster(self, item: any (CpSoftwareClusterTo)) -> "CpSoftwareClusterMappingSetBuilder":
        """Add a single item to software_clusters list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.software_clusters.append(item)
        return self

    def clear_software_clusters(self) -> "CpSoftwareClusterMappingSetBuilder":
        """Clear all items from software_clusters list.

        Returns:
            self for method chaining
        """
        self._obj.software_clusters = []
        return self

    def add_swc_to(self, item: SwcToApplicationPartitionMapping) -> "CpSoftwareClusterMappingSetBuilder":
        """Add a single item to swc_tos list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.swc_tos.append(item)
        return self

    def clear_swc_tos(self) -> "CpSoftwareClusterMappingSetBuilder":
        """Clear all items from swc_tos list.

        Returns:
            self for method chaining
        """
        self._obj.swc_tos = []
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


    def build(self) -> CpSoftwareClusterMappingSet:
        """Build and return the CpSoftwareClusterMappingSet instance with validation."""
        self._validate_instance()
        pass
        return self._obj