"""DiagnosticMemoryIdentifier AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.diagnostic_access_permission import (
    DiagnosticAccessPermission,
)


class DiagnosticMemoryIdentifier(DiagnosticCommonElement):
    """AUTOSAR DiagnosticMemoryIdentifier."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("access", None, False, False, DiagnosticAccessPermission),  # access
        ("id", None, True, False, None),  # id
        ("memory_high", None, True, False, None),  # memoryHigh
        ("memory_low", None, True, False, None),  # memoryLow
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticMemoryIdentifier."""
        super().__init__()
        self.access: Optional[DiagnosticAccessPermission] = None
        self.id: Optional[PositiveInteger] = None
        self.memory_high: Optional[String] = None
        self.memory_low: Optional[String] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticMemoryIdentifier to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticMemoryIdentifier":
        """Create DiagnosticMemoryIdentifier from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticMemoryIdentifier instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticMemoryIdentifier since parent returns ARObject
        return cast("DiagnosticMemoryIdentifier", obj)


class DiagnosticMemoryIdentifierBuilder:
    """Builder for DiagnosticMemoryIdentifier."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticMemoryIdentifier = DiagnosticMemoryIdentifier()

    def build(self) -> DiagnosticMemoryIdentifier:
        """Build and return DiagnosticMemoryIdentifier object.

        Returns:
            DiagnosticMemoryIdentifier instance
        """
        # TODO: Add validation
        return self._obj
