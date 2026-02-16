"""DiagnosticFunctionIdentifierInhibit AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)


class DiagnosticFunctionIdentifierInhibit(DiagnosticCommonElement):
    """AUTOSAR DiagnosticFunctionIdentifierInhibit."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("function", None, False, False, any (DiagnosticFunction)),  # function
        ("inhibition_mask", None, False, False, DiagnosticInhibitionMaskEnum),  # inhibitionMask
        ("inhibit_sources", None, False, True, any (DiagnosticFunction)),  # inhibitSources
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticFunctionIdentifierInhibit."""
        super().__init__()
        self.function: Optional[Any] = None
        self.inhibition_mask: Optional[DiagnosticInhibitionMaskEnum] = None
        self.inhibit_sources: list[Any] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticFunctionIdentifierInhibit to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticFunctionIdentifierInhibit":
        """Create DiagnosticFunctionIdentifierInhibit from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticFunctionIdentifierInhibit instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticFunctionIdentifierInhibit since parent returns ARObject
        return cast("DiagnosticFunctionIdentifierInhibit", obj)


class DiagnosticFunctionIdentifierInhibitBuilder:
    """Builder for DiagnosticFunctionIdentifierInhibit."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticFunctionIdentifierInhibit = DiagnosticFunctionIdentifierInhibit()

    def build(self) -> DiagnosticFunctionIdentifierInhibit:
        """Build and return DiagnosticFunctionIdentifierInhibit object.

        Returns:
            DiagnosticFunctionIdentifierInhibit instance
        """
        # TODO: Add validation
        return self._obj
