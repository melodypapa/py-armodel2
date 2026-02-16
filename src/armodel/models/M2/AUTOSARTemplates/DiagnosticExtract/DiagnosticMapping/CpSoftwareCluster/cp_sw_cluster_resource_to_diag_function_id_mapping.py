"""CpSwClusterResourceToDiagFunctionIdMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)


class CpSwClusterResourceToDiagFunctionIdMapping(DiagnosticMapping):
    """AUTOSAR CpSwClusterResourceToDiagFunctionIdMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("cp_software_cluster", None, False, False, CpSoftwareCluster),  # cpSoftwareCluster
        ("function", None, False, False, any (DiagnosticFunction)),  # function
    ]

    def __init__(self) -> None:
        """Initialize CpSwClusterResourceToDiagFunctionIdMapping."""
        super().__init__()
        self.cp_software_cluster: Optional[CpSoftwareCluster] = None
        self.function: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CpSwClusterResourceToDiagFunctionIdMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CpSwClusterResourceToDiagFunctionIdMapping":
        """Create CpSwClusterResourceToDiagFunctionIdMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CpSwClusterResourceToDiagFunctionIdMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CpSwClusterResourceToDiagFunctionIdMapping since parent returns ARObject
        return cast("CpSwClusterResourceToDiagFunctionIdMapping", obj)


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
