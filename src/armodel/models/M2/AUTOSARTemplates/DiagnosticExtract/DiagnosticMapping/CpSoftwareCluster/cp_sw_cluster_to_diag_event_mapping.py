"""CpSwClusterToDiagEventMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_event import (
    DiagnosticEvent,
)


class CpSwClusterToDiagEventMapping(DiagnosticMapping):
    """AUTOSAR CpSwClusterToDiagEventMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("cp_software_cluster", None, False, False, CpSoftwareCluster),  # cpSoftwareCluster
        ("diagnostic_event", None, False, False, DiagnosticEvent),  # diagnosticEvent
    ]

    def __init__(self) -> None:
        """Initialize CpSwClusterToDiagEventMapping."""
        super().__init__()
        self.cp_software_cluster: Optional[CpSoftwareCluster] = None
        self.diagnostic_event: Optional[DiagnosticEvent] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CpSwClusterToDiagEventMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CpSwClusterToDiagEventMapping":
        """Create CpSwClusterToDiagEventMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CpSwClusterToDiagEventMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CpSwClusterToDiagEventMapping since parent returns ARObject
        return cast("CpSwClusterToDiagEventMapping", obj)


class CpSwClusterToDiagEventMappingBuilder:
    """Builder for CpSwClusterToDiagEventMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CpSwClusterToDiagEventMapping = CpSwClusterToDiagEventMapping()

    def build(self) -> CpSwClusterToDiagEventMapping:
        """Build and return CpSwClusterToDiagEventMapping object.

        Returns:
            CpSwClusterToDiagEventMapping instance
        """
        # TODO: Add validation
        return self._obj
