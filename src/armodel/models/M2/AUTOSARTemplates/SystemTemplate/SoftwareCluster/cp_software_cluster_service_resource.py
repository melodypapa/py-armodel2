"""CpSoftwareClusterServiceResource AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 904)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster_resource import (
    CpSoftwareClusterResource,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_container_value import (
    EcucContainerValue,
)


class CpSoftwareClusterServiceResource(CpSoftwareClusterResource):
    """AUTOSAR CpSoftwareClusterServiceResource."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    resource_needses: list[EcucContainerValue]
    def __init__(self) -> None:
        """Initialize CpSoftwareClusterServiceResource."""
        super().__init__()
        self.resource_needses: list[EcucContainerValue] = []

    def serialize(self) -> ET.Element:
        """Serialize CpSoftwareClusterServiceResource to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CpSoftwareClusterServiceResource, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize resource_needses (list to container "RESOURCE-NEEDSES")
        if self.resource_needses:
            wrapper = ET.Element("RESOURCE-NEEDSES")
            for item in self.resource_needses:
                serialized = ARObject._serialize_item(item, "EcucContainerValue")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CpSoftwareClusterServiceResource":
        """Deserialize XML element to CpSoftwareClusterServiceResource object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CpSoftwareClusterServiceResource object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CpSoftwareClusterServiceResource, cls).deserialize(element)

        # Parse resource_needses (list from container "RESOURCE-NEEDSES")
        obj.resource_needses = []
        container = ARObject._find_child_element(element, "RESOURCE-NEEDSES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.resource_needses.append(child_value)

        return obj



class CpSoftwareClusterServiceResourceBuilder:
    """Builder for CpSoftwareClusterServiceResource."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CpSoftwareClusterServiceResource = CpSoftwareClusterServiceResource()

    def build(self) -> CpSoftwareClusterServiceResource:
        """Build and return CpSoftwareClusterServiceResource object.

        Returns:
            CpSoftwareClusterServiceResource instance
        """
        # TODO: Add validation
        return self._obj
