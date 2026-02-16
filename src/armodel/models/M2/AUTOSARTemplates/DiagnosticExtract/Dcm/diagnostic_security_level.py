"""DiagnosticSecurityLevel AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)


class DiagnosticSecurityLevel(DiagnosticCommonElement):
    """AUTOSAR DiagnosticSecurityLevel."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("access_data", None, True, False, None),  # accessData
        ("key_size", None, True, False, None),  # keySize
        ("num_failed", None, True, False, None),  # numFailed
        ("security_delay", None, True, False, None),  # securityDelay
        ("seed_size", None, True, False, None),  # seedSize
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticSecurityLevel."""
        super().__init__()
        self.access_data: Optional[PositiveInteger] = None
        self.key_size: Optional[PositiveInteger] = None
        self.num_failed: Optional[PositiveInteger] = None
        self.security_delay: Optional[TimeValue] = None
        self.seed_size: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticSecurityLevel to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticSecurityLevel":
        """Create DiagnosticSecurityLevel from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticSecurityLevel instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticSecurityLevel since parent returns ARObject
        return cast("DiagnosticSecurityLevel", obj)


class DiagnosticSecurityLevelBuilder:
    """Builder for DiagnosticSecurityLevel."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticSecurityLevel = DiagnosticSecurityLevel()

    def build(self) -> DiagnosticSecurityLevel:
        """Build and return DiagnosticSecurityLevel object.

        Returns:
            DiagnosticSecurityLevel instance
        """
        # TODO: Add validation
        return self._obj
