"""CpSoftwareClusterMappingSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 285)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.port_element_to_communication_resource_mapping import (
    PortElementToCommunicationResourceMapping,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.swc_to_application_partition_mapping import (
    SwcToApplicationPartitionMapping,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class CpSoftwareClusterMappingSet(ARElement):
    """AUTOSAR CpSoftwareClusterMappingSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CP-SOFTWARE-CLUSTER-MAPPING-SET"


    port_element_toes: list[PortElementToCommunicationResourceMapping]
    resource_toes: list[CpSoftwareCluster]
    software_clusters: list[Any]
    swc_toes: list[SwcToApplicationPartitionMapping]
    _DESERIALIZE_DISPATCH = {
        "PORT-ELEMENT-TOS": lambda obj, elem: obj.port_element_toes.append(SerializationHelper.deserialize_by_tag(elem, "PortElementToCommunicationResourceMapping")),
        "RESOURCE-TOS": lambda obj, elem: obj.resource_toes.append(SerializationHelper.deserialize_by_tag(elem, "CpSoftwareCluster")),
        "SOFTWARE-CLUSTERS": lambda obj, elem: obj.software_clusters.append(SerializationHelper.deserialize_by_tag(elem, "any (CpSoftwareClusterTo)")),
        "SWC-TOS": lambda obj, elem: obj.swc_toes.append(SerializationHelper.deserialize_by_tag(elem, "SwcToApplicationPartitionMapping")),
    }


    def __init__(self) -> None:
        """Initialize CpSoftwareClusterMappingSet."""
        super().__init__()
        self.port_element_toes: list[PortElementToCommunicationResourceMapping] = []
        self.resource_toes: list[CpSoftwareCluster] = []
        self.software_clusters: list[Any] = []
        self.swc_toes: list[SwcToApplicationPartitionMapping] = []

    def serialize(self) -> ET.Element:
        """Serialize CpSoftwareClusterMappingSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Serialize port_element_toes (list to container "PORT-ELEMENT-TOS")
        if self.port_element_toes:
            wrapper = ET.Element("PORT-ELEMENT-TOS")
            for item in self.port_element_toes:
                serialized = SerializationHelper.serialize_item(item, "PortElementToCommunicationResourceMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize resource_toes (list to container "RESOURCE-TOS")
        if self.resource_toes:
            wrapper = ET.Element("RESOURCE-TOS")
            for item in self.resource_toes:
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

        # Serialize swc_toes (list to container "SWC-TOS")
        if self.swc_toes:
            wrapper = ET.Element("SWC-TOS")
            for item in self.swc_toes:
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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "PORT-ELEMENT-TOS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.port_element_toes.append(SerializationHelper.deserialize_by_tag(item_elem, "PortElementToCommunicationResourceMapping"))
            elif tag == "RESOURCE-TOS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.resource_toes.append(SerializationHelper.deserialize_by_tag(item_elem, "CpSoftwareCluster"))
            elif tag == "SOFTWARE-CLUSTERS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.software_clusters.append(SerializationHelper.deserialize_by_tag(item_elem, "any (CpSoftwareClusterTo)"))
            elif tag == "SWC-TOS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.swc_toes.append(SerializationHelper.deserialize_by_tag(item_elem, "SwcToApplicationPartitionMapping"))

        return obj



class CpSoftwareClusterMappingSetBuilder(ARElementBuilder):
    """Builder for CpSoftwareClusterMappingSet with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CpSoftwareClusterMappingSet = CpSoftwareClusterMappingSet()


    def with_port_element_toes(self, items: list[PortElementToCommunicationResourceMapping]) -> "CpSoftwareClusterMappingSetBuilder":
        """Set port_element_toes list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.port_element_toes = list(items) if items else []
        return self

    def with_resource_toes(self, items: list[CpSoftwareCluster]) -> "CpSoftwareClusterMappingSetBuilder":
        """Set resource_toes list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.resource_toes = list(items) if items else []
        return self

    def with_software_clusters(self, items: list[Any]) -> "CpSoftwareClusterMappingSetBuilder":
        """Set software_clusters list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.software_clusters = list(items) if items else []
        return self

    def with_swc_toes(self, items: list[SwcToApplicationPartitionMapping]) -> "CpSoftwareClusterMappingSetBuilder":
        """Set swc_toes list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.swc_toes = list(items) if items else []
        return self


    def add_port_element_to(self, item: PortElementToCommunicationResourceMapping) -> "CpSoftwareClusterMappingSetBuilder":
        """Add a single item to port_element_toes list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.port_element_toes.append(item)
        return self

    def clear_port_element_toes(self) -> "CpSoftwareClusterMappingSetBuilder":
        """Clear all items from port_element_toes list.

        Returns:
            self for method chaining
        """
        self._obj.port_element_toes = []
        return self

    def add_resource_to(self, item: CpSoftwareCluster) -> "CpSoftwareClusterMappingSetBuilder":
        """Add a single item to resource_toes list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.resource_toes.append(item)
        return self

    def clear_resource_toes(self) -> "CpSoftwareClusterMappingSetBuilder":
        """Clear all items from resource_toes list.

        Returns:
            self for method chaining
        """
        self._obj.resource_toes = []
        return self

    def add_software_cluster(self, item: Any) -> "CpSoftwareClusterMappingSetBuilder":
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
        """Add a single item to swc_toes list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.swc_toes.append(item)
        return self

    def clear_swc_toes(self) -> "CpSoftwareClusterMappingSetBuilder":
        """Clear all items from swc_toes list.

        Returns:
            self for method chaining
        """
        self._obj.swc_toes = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "portElementTo",
        "resourceTo",
        "softwareCluster",
        "swcTo",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> CpSoftwareClusterMappingSet:
        """Build and return the CpSoftwareClusterMappingSet instance with validation."""
        self._validate_instance()
        return self._obj