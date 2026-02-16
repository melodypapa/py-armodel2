"""DiagnosticAging AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DiagnosticAging(DiagnosticCommonElement):
    """AUTOSAR DiagnosticAging."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("aging_cycle", None, False, False, any (DiagnosticOperation)),  # agingCycle
        ("threshold", None, True, False, None),  # threshold
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticAging."""
        super().__init__()
        self.aging_cycle: Optional[Any] = None
        self.threshold: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticAging to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticAging":
        """Create DiagnosticAging from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticAging instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticAging since parent returns ARObject
        return cast("DiagnosticAging", obj)


class DiagnosticAgingBuilder:
    """Builder for DiagnosticAging."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticAging = DiagnosticAging()

    def build(self) -> DiagnosticAging:
        """Build and return DiagnosticAging object.

        Returns:
            DiagnosticAging instance
        """
        # TODO: Add validation
        return self._obj
