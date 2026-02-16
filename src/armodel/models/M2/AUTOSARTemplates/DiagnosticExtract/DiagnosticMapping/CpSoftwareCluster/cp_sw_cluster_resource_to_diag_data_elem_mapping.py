"""CpSwClusterResourceToDiagDataElemMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_data_element import (
    DiagnosticDataElement,
)


class CpSwClusterResourceToDiagDataElemMapping(DiagnosticMapping):
    """AUTOSAR CpSwClusterResourceToDiagDataElemMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("cp_software_cluster", None, False, False, CpSoftwareCluster),  # cpSoftwareCluster
        ("diagnostic_data", None, False, False, DiagnosticDataElement),  # diagnosticData
    ]

    def __init__(self) -> None:
        """Initialize CpSwClusterResourceToDiagDataElemMapping."""
        super().__init__()
        self.cp_software_cluster: Optional[CpSoftwareCluster] = None
        self.diagnostic_data: Optional[DiagnosticDataElement] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CpSwClusterResourceToDiagDataElemMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CpSwClusterResourceToDiagDataElemMapping":
        """Create CpSwClusterResourceToDiagDataElemMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CpSwClusterResourceToDiagDataElemMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CpSwClusterResourceToDiagDataElemMapping since parent returns ARObject
        return cast("CpSwClusterResourceToDiagDataElemMapping", obj)


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
