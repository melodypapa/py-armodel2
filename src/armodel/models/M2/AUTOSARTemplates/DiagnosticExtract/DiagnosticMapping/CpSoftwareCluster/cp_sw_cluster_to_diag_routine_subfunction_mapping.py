"""CpSwClusterToDiagRoutineSubfunctionMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_routine import (
    DiagnosticRoutine,
)


class CpSwClusterToDiagRoutineSubfunctionMapping(DiagnosticMapping):
    """AUTOSAR CpSwClusterToDiagRoutineSubfunctionMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("cp_software_cluster", None, False, False, CpSoftwareCluster),  # cpSoftwareCluster
        ("routine", None, False, False, DiagnosticRoutine),  # routine
    ]

    def __init__(self) -> None:
        """Initialize CpSwClusterToDiagRoutineSubfunctionMapping."""
        super().__init__()
        self.cp_software_cluster: Optional[CpSoftwareCluster] = None
        self.routine: Optional[DiagnosticRoutine] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CpSwClusterToDiagRoutineSubfunctionMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CpSwClusterToDiagRoutineSubfunctionMapping":
        """Create CpSwClusterToDiagRoutineSubfunctionMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CpSwClusterToDiagRoutineSubfunctionMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CpSwClusterToDiagRoutineSubfunctionMapping since parent returns ARObject
        return cast("CpSwClusterToDiagRoutineSubfunctionMapping", obj)


class CpSwClusterToDiagRoutineSubfunctionMappingBuilder:
    """Builder for CpSwClusterToDiagRoutineSubfunctionMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CpSwClusterToDiagRoutineSubfunctionMapping = CpSwClusterToDiagRoutineSubfunctionMapping()

    def build(self) -> CpSwClusterToDiagRoutineSubfunctionMapping:
        """Build and return CpSwClusterToDiagRoutineSubfunctionMapping object.

        Returns:
            CpSwClusterToDiagRoutineSubfunctionMapping instance
        """
        # TODO: Add validation
        return self._obj
