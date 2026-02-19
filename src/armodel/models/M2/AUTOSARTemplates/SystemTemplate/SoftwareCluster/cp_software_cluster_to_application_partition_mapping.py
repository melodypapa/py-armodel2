"""CpSoftwareClusterToApplicationPartitionMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 287)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.application_partition import (
    ApplicationPartition,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)


class CpSoftwareClusterToApplicationPartitionMapping(Identifiable):
    """AUTOSAR CpSoftwareClusterToApplicationPartitionMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    applications: list[ApplicationPartition]
    software_cluster: Optional[CpSoftwareCluster]
    def __init__(self) -> None:
        """Initialize CpSoftwareClusterToApplicationPartitionMapping."""
        super().__init__()
        self.applications: list[ApplicationPartition] = []
        self.software_cluster: Optional[CpSoftwareCluster] = None
    def serialize(self) -> ET.Element:
        """Serialize CpSoftwareClusterToApplicationPartitionMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CpSoftwareClusterToApplicationPartitionMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize applications (list to container "APPLICATIONS")
        if self.applications:
            wrapper = ET.Element("APPLICATIONS")
            for item in self.applications:
                serialized = ARObject._serialize_item(item, "ApplicationPartition")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize software_cluster
        if self.software_cluster is not None:
            serialized = ARObject._serialize_item(self.software_cluster, "CpSoftwareCluster")
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
    def deserialize(cls, element: ET.Element) -> "CpSoftwareClusterToApplicationPartitionMapping":
        """Deserialize XML element to CpSoftwareClusterToApplicationPartitionMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CpSoftwareClusterToApplicationPartitionMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CpSoftwareClusterToApplicationPartitionMapping, cls).deserialize(element)

        # Parse applications (list from container "APPLICATIONS")
        obj.applications = []
        container = ARObject._find_child_element(element, "APPLICATIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.applications.append(child_value)

        # Parse software_cluster
        child = ARObject._find_child_element(element, "SOFTWARE-CLUSTER")
        if child is not None:
            software_cluster_value = ARObject._deserialize_by_tag(child, "CpSoftwareCluster")
            obj.software_cluster = software_cluster_value

        return obj



class CpSoftwareClusterToApplicationPartitionMappingBuilder:
    """Builder for CpSoftwareClusterToApplicationPartitionMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CpSoftwareClusterToApplicationPartitionMapping = CpSoftwareClusterToApplicationPartitionMapping()

    def build(self) -> CpSoftwareClusterToApplicationPartitionMapping:
        """Build and return CpSoftwareClusterToApplicationPartitionMapping object.

        Returns:
            CpSoftwareClusterToApplicationPartitionMapping instance
        """
        # TODO: Add validation
        return self._obj
