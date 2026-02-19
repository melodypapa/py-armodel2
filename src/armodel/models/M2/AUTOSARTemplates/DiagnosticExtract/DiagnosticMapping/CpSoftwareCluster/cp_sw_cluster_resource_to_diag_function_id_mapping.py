"""CpSwClusterResourceToDiagFunctionIdMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 275)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping_CpSoftwareCluster.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)


class CpSwClusterResourceToDiagFunctionIdMapping(DiagnosticMapping):
    """AUTOSAR CpSwClusterResourceToDiagFunctionIdMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    cp_software_cluster: Optional[CpSoftwareCluster]
    function: Optional[Any]
    def __init__(self) -> None:
        """Initialize CpSwClusterResourceToDiagFunctionIdMapping."""
        super().__init__()
        self.cp_software_cluster: Optional[CpSoftwareCluster] = None
        self.function: Optional[Any] = None
    def serialize(self) -> ET.Element:
        """Serialize CpSwClusterResourceToDiagFunctionIdMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CpSwClusterResourceToDiagFunctionIdMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize cp_software_cluster
        if self.cp_software_cluster is not None:
            serialized = ARObject._serialize_item(self.cp_software_cluster, "CpSoftwareCluster")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CP-SOFTWARE-CLUSTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize function
        if self.function is not None:
            serialized = ARObject._serialize_item(self.function, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FUNCTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CpSwClusterResourceToDiagFunctionIdMapping":
        """Deserialize XML element to CpSwClusterResourceToDiagFunctionIdMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CpSwClusterResourceToDiagFunctionIdMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CpSwClusterResourceToDiagFunctionIdMapping, cls).deserialize(element)

        # Parse cp_software_cluster
        child = ARObject._find_child_element(element, "CP-SOFTWARE-CLUSTER")
        if child is not None:
            cp_software_cluster_value = ARObject._deserialize_by_tag(child, "CpSoftwareCluster")
            obj.cp_software_cluster = cp_software_cluster_value

        # Parse function
        child = ARObject._find_child_element(element, "FUNCTION")
        if child is not None:
            function_value = child.text
            obj.function = function_value

        return obj



class CpSwClusterResourceToDiagFunctionIdMappingBuilder:
    """Builder for CpSwClusterResourceToDiagFunctionIdMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CpSwClusterResourceToDiagFunctionIdMapping = CpSwClusterResourceToDiagFunctionIdMapping()

    def build(self) -> CpSwClusterResourceToDiagFunctionIdMapping:
        """Build and return CpSwClusterResourceToDiagFunctionIdMapping object.

        Returns:
            CpSwClusterResourceToDiagFunctionIdMapping instance
        """
        # TODO: Add validation
        return self._obj
