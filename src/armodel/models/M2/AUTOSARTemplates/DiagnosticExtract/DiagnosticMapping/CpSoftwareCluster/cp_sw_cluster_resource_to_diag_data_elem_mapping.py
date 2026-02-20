"""CpSwClusterResourceToDiagDataElemMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 273)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping_CpSoftwareCluster.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_data_element import (
    DiagnosticDataElement,
)


class CpSwClusterResourceToDiagDataElemMapping(DiagnosticMapping):
    """AUTOSAR CpSwClusterResourceToDiagDataElemMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    cp_software_cluster_ref: Optional[ARRef]
    diagnostic_data_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize CpSwClusterResourceToDiagDataElemMapping."""
        super().__init__()
        self.cp_software_cluster_ref: Optional[ARRef] = None
        self.diagnostic_data_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize CpSwClusterResourceToDiagDataElemMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CpSwClusterResourceToDiagDataElemMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

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

        # Serialize diagnostic_data_ref
        if self.diagnostic_data_ref is not None:
            serialized = ARObject._serialize_item(self.diagnostic_data_ref, "DiagnosticDataElement")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DIAGNOSTIC-DATA-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CpSwClusterResourceToDiagDataElemMapping":
        """Deserialize XML element to CpSwClusterResourceToDiagDataElemMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CpSwClusterResourceToDiagDataElemMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CpSwClusterResourceToDiagDataElemMapping, cls).deserialize(element)

        # Parse cp_software_cluster_ref
        child = ARObject._find_child_element(element, "CP-SOFTWARE-CLUSTER-REF")
        if child is not None:
            cp_software_cluster_ref_value = ARRef.deserialize(child)
            obj.cp_software_cluster_ref = cp_software_cluster_ref_value

        # Parse diagnostic_data_ref
        child = ARObject._find_child_element(element, "DIAGNOSTIC-DATA-REF")
        if child is not None:
            diagnostic_data_ref_value = ARRef.deserialize(child)
            obj.diagnostic_data_ref = diagnostic_data_ref_value

        return obj



class CpSwClusterResourceToDiagDataElemMappingBuilder:
    """Builder for CpSwClusterResourceToDiagDataElemMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CpSwClusterResourceToDiagDataElemMapping = CpSwClusterResourceToDiagDataElemMapping()

    def build(self) -> CpSwClusterResourceToDiagDataElemMapping:
        """Build and return CpSwClusterResourceToDiagDataElemMapping object.

        Returns:
            CpSwClusterResourceToDiagDataElemMapping instance
        """
        # TODO: Add validation
        return self._obj
