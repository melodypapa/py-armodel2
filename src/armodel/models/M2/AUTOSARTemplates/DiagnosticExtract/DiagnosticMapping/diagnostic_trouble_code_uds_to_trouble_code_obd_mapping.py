"""DiagnosticTroubleCodeUdsToTroubleCodeObdMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode.diagnostic_trouble_code import (
    DiagnosticTroubleCode,
)


class DiagnosticTroubleCodeUdsToTroubleCodeObdMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticTroubleCodeUdsToTroubleCodeObdMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("trouble_code", None, False, False, DiagnosticTroubleCode),  # troubleCode
        ("trouble_code_uds", None, False, False, DiagnosticTroubleCode),  # troubleCodeUds
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticTroubleCodeUdsToTroubleCodeObdMapping."""
        super().__init__()
        self.trouble_code: Optional[DiagnosticTroubleCode] = None
        self.trouble_code_uds: Optional[DiagnosticTroubleCode] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticTroubleCodeUdsToTroubleCodeObdMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticTroubleCodeUdsToTroubleCodeObdMapping":
        """Create DiagnosticTroubleCodeUdsToTroubleCodeObdMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticTroubleCodeUdsToTroubleCodeObdMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticTroubleCodeUdsToTroubleCodeObdMapping since parent returns ARObject
        return cast("DiagnosticTroubleCodeUdsToTroubleCodeObdMapping", obj)


class DiagnosticTroubleCodeUdsToTroubleCodeObdMappingBuilder:
    """Builder for DiagnosticTroubleCodeUdsToTroubleCodeObdMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticTroubleCodeUdsToTroubleCodeObdMapping = DiagnosticTroubleCodeUdsToTroubleCodeObdMapping()

    def build(self) -> DiagnosticTroubleCodeUdsToTroubleCodeObdMapping:
        """Build and return DiagnosticTroubleCodeUdsToTroubleCodeObdMapping object.

        Returns:
            DiagnosticTroubleCodeUdsToTroubleCodeObdMapping instance
        """
        # TODO: Add validation
        return self._obj
