"""DiagnosticFimFunctionMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_sw_mapping import (
    DiagnosticSwMapping,
)


class DiagnosticFimFunctionMapping(DiagnosticSwMapping):
    """AUTOSAR DiagnosticFimFunctionMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("mapped_bsw", None, False, False, any (BswService)),  # mappedBsw
        ("mapped_flat_swc", None, False, False, any (SwcService)),  # mappedFlatSwc
        ("mapped", None, False, False, any (DiagnosticFunction)),  # mapped
        ("mapped_swc", None, False, False, any (SwcService)),  # mappedSwc
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticFimFunctionMapping."""
        super().__init__()
        self.mapped_bsw: Optional[Any] = None
        self.mapped_flat_swc: Optional[Any] = None
        self.mapped: Optional[Any] = None
        self.mapped_swc: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticFimFunctionMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticFimFunctionMapping":
        """Create DiagnosticFimFunctionMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticFimFunctionMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticFimFunctionMapping since parent returns ARObject
        return cast("DiagnosticFimFunctionMapping", obj)


class DiagnosticFimFunctionMappingBuilder:
    """Builder for DiagnosticFimFunctionMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticFimFunctionMapping = DiagnosticFimFunctionMapping()

    def build(self) -> DiagnosticFimFunctionMapping:
        """Build and return DiagnosticFimFunctionMapping object.

        Returns:
            DiagnosticFimFunctionMapping instance
        """
        # TODO: Add validation
        return self._obj
