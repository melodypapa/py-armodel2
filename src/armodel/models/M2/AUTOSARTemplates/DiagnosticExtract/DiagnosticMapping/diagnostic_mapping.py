"""DiagnosticMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)


class DiagnosticMapping(DiagnosticCommonElement):
    """AUTOSAR DiagnosticMapping."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("provider", None, False, False, CpSoftwareCluster),  # provider
        ("requester", None, False, False, CpSoftwareCluster),  # requester
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticMapping."""
        super().__init__()
        self.provider: Optional[CpSoftwareCluster] = None
        self.requester: Optional[CpSoftwareCluster] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticMapping":
        """Create DiagnosticMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticMapping since parent returns ARObject
        return cast("DiagnosticMapping", obj)


class DiagnosticMappingBuilder:
    """Builder for DiagnosticMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticMapping = DiagnosticMapping()

    def build(self) -> DiagnosticMapping:
        """Build and return DiagnosticMapping object.

        Returns:
            DiagnosticMapping instance
        """
        # TODO: Add validation
        return self._obj
