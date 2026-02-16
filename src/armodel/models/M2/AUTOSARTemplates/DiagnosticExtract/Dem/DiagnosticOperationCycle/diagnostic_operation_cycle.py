"""DiagnosticOperationCycle AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)


class DiagnosticOperationCycle(DiagnosticCommonElement):
    """AUTOSAR DiagnosticOperationCycle."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("type_cycle_type_enum", None, False, False, any (DiagnosticOperation)),  # typeCycleTypeEnum
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticOperationCycle."""
        super().__init__()
        self.type_cycle_type_enum: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticOperationCycle to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticOperationCycle":
        """Create DiagnosticOperationCycle from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticOperationCycle instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticOperationCycle since parent returns ARObject
        return cast("DiagnosticOperationCycle", obj)


class DiagnosticOperationCycleBuilder:
    """Builder for DiagnosticOperationCycle."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticOperationCycle = DiagnosticOperationCycle()

    def build(self) -> DiagnosticOperationCycle:
        """Build and return DiagnosticOperationCycle object.

        Returns:
            DiagnosticOperationCycle instance
        """
        # TODO: Add validation
        return self._obj
