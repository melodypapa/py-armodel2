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
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CpSoftwareClusterMappingSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize port_element_tos (list to container "PORT-ELEMENT-TOS")
        if self.port_element_tos:
            wrapper = ET.Element("PORT-ELEMENT-TOS")
            for item in self.port_element_tos:
                serialized = ARObject._serialize_item(item, "PortElementToCommunicationResourceMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize resource_tos (list to container "RESOURCE-TOS")
        if self.resource_tos:
            wrapper = ET.Element("RESOURCE-TOS")
            for item in self.resource_tos:
                serialized = ARObject._serialize_item(item, "CpSoftwareCluster")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize software_clusters (list to container "SOFTWARE-CLUSTERS")
        if self.software_clusters:
            wrapper = ET.Element("SOFTWARE-CLUSTERS")
            for item in self.software_clusters:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize swc_tos (list to container "SWC-TOS")
        if self.swc_tos:
            wrapper = ET.Element("SWC-TOS")
            for item in self.swc_tos:
                serialized = ARObject._serialize_item(item, "SwcToApplicationPartitionMapping")
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
        container = ARObject._find_child_element(element, "PORT-ELEMENT-TOS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.port_element_tos.append(child_value)

        # Parse resource_tos (list from container "RESOURCE-TOS")
        obj.resource_tos = []
        container = ARObject._find_child_element(element, "RESOURCE-TOS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.resource_tos.append(child_value)

        # Parse software_clusters (list from container "SOFTWARE-CLUSTERS")
        obj.software_clusters = []
        container = ARObject._find_child_element(element, "SOFTWARE-CLUSTERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.software_clusters.append(child_value)

        # Parse swc_tos (list from container "SWC-TOS")
        obj.swc_tos = []
        container = ARObject._find_child_element(element, "SWC-TOS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.swc_tos.append(child_value)

        return obj



class CpSoftwareClusterMappingSetBuilder:
    """Builder for CpSoftwareClusterMappingSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CpSoftwareClusterMappingSet = CpSoftwareClusterMappingSet()

    def build(self) -> CpSoftwareClusterMappingSet:
        """Build and return CpSoftwareClusterMappingSet object.

        Returns:
            CpSoftwareClusterMappingSet instance
        """
        # TODO: Add validation
        return self._obj
