"""DiagnosticOperationCyclePortMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_sw_mapping import (
    DiagnosticSwMapping,
)


class DiagnosticOperationCyclePortMapping(DiagnosticSwMapping):
    """AUTOSAR DiagnosticOperationCyclePortMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("operation_cycle", None, False, False, any (DiagnosticOperation)),  # operationCycle
        ("swc_flat_service", None, False, False, any (SwcService)),  # swcFlatService
        ("swc_service", None, False, False, any (SwcService)),  # swcService
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticOperationCyclePortMapping."""
        super().__init__()
        self.operation_cycle: Optional[Any] = None
        self.swc_flat_service: Optional[Any] = None
        self.swc_service: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticOperationCyclePortMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticOperationCyclePortMapping":
        """Create DiagnosticOperationCyclePortMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticOperationCyclePortMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticOperationCyclePortMapping since parent returns ARObject
        return cast("DiagnosticOperationCyclePortMapping", obj)


class DiagnosticOperationCyclePortMappingBuilder:
    """Builder for DiagnosticOperationCyclePortMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticOperationCyclePortMapping = DiagnosticOperationCyclePortMapping()

    def build(self) -> DiagnosticOperationCyclePortMapping:
        """Build and return DiagnosticOperationCyclePortMapping object.

        Returns:
            DiagnosticOperationCyclePortMapping instance
        """
        # TODO: Add validation
        return self._obj
