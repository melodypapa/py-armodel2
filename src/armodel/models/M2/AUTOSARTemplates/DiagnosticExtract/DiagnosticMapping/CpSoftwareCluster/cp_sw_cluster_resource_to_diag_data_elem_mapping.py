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

    cp_software_cluster: Optional[CpSoftwareCluster]
    diagnostic_data: Optional[DiagnosticDataElement]
    def __init__(self) -> None:
        """Initialize CpSwClusterResourceToDiagDataElemMapping."""
        super().__init__()
        self.cp_software_cluster: Optional[CpSoftwareCluster] = None
        self.diagnostic_data: Optional[DiagnosticDataElement] = None
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

        # Parse cp_software_cluster
        child = ARObject._find_child_element(element, "CP-SOFTWARE-CLUSTER")
        if child is not None:
            cp_software_cluster_value = ARObject._deserialize_by_tag(child, "CpSoftwareCluster")
            obj.cp_software_cluster = cp_software_cluster_value

        # Parse diagnostic_data
        child = ARObject._find_child_element(element, "DIAGNOSTIC-DATA")
        if child is not None:
            diagnostic_data_value = ARObject._deserialize_by_tag(child, "DiagnosticDataElement")
            obj.diagnostic_data = diagnostic_data_value

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
