"""CpSoftwareClusterToEcuInstanceMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 283)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)


class CpSoftwareClusterToEcuInstanceMapping(Identifiable):
    """AUTOSAR CpSoftwareClusterToEcuInstanceMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ecu_instance: Optional[EcuInstance]
    machine_id: Optional[PositiveInteger]
    sw_clusters: list[CpSoftwareCluster]
    def __init__(self) -> None:
        """Initialize CpSoftwareClusterToEcuInstanceMapping."""
        super().__init__()
        self.ecu_instance: Optional[EcuInstance] = None
        self.machine_id: Optional[PositiveInteger] = None
        self.sw_clusters: list[CpSoftwareCluster] = []
    def serialize(self) -> ET.Element:
        """Serialize CpSoftwareClusterToEcuInstanceMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CpSoftwareClusterToEcuInstanceMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ecu_instance
        if self.ecu_instance is not None:
            serialized = ARObject._serialize_item(self.ecu_instance, "EcuInstance")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ECU-INSTANCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize machine_id
        if self.machine_id is not None:
            serialized = ARObject._serialize_item(self.machine_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MACHINE-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_clusters (list to container "SW-CLUSTERS")
        if self.sw_clusters:
            wrapper = ET.Element("SW-CLUSTERS")
            for item in self.sw_clusters:
                serialized = ARObject._serialize_item(item, "CpSoftwareCluster")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CpSoftwareClusterToEcuInstanceMapping":
        """Deserialize XML element to CpSoftwareClusterToEcuInstanceMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CpSoftwareClusterToEcuInstanceMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CpSoftwareClusterToEcuInstanceMapping, cls).deserialize(element)

        # Parse ecu_instance
        child = ARObject._find_child_element(element, "ECU-INSTANCE")
        if child is not None:
            ecu_instance_value = ARObject._deserialize_by_tag(child, "EcuInstance")
            obj.ecu_instance = ecu_instance_value

        # Parse machine_id
        child = ARObject._find_child_element(element, "MACHINE-ID")
        if child is not None:
            machine_id_value = child.text
            obj.machine_id = machine_id_value

        # Parse sw_clusters (list from container "SW-CLUSTERS")
        obj.sw_clusters = []
        container = ARObject._find_child_element(element, "SW-CLUSTERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sw_clusters.append(child_value)

        return obj



class CpSoftwareClusterToEcuInstanceMappingBuilder:
    """Builder for CpSoftwareClusterToEcuInstanceMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CpSoftwareClusterToEcuInstanceMapping = CpSoftwareClusterToEcuInstanceMapping()

    def build(self) -> CpSoftwareClusterToEcuInstanceMapping:
        """Build and return CpSoftwareClusterToEcuInstanceMapping object.

        Returns:
            CpSoftwareClusterToEcuInstanceMapping instance
        """
        # TODO: Add validation
        return self._obj
