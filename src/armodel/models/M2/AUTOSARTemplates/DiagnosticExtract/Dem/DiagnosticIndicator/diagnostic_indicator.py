"""DiagnosticIndicator AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)


class DiagnosticIndicator(DiagnosticCommonElement):
    """AUTOSAR DiagnosticIndicator."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("type", None, False, False, DiagnosticIndicatorTypeEnum),  # type
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticIndicator."""
        super().__init__()
        self.type: Optional[DiagnosticIndicatorTypeEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticIndicator to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticIndicator":
        """Create DiagnosticIndicator from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticIndicator instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticIndicator since parent returns ARObject
        return cast("DiagnosticIndicator", obj)


class DiagnosticIndicatorBuilder:
    """Builder for DiagnosticIndicator."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticIndicator = DiagnosticIndicator()

    def build(self) -> DiagnosticIndicator:
        """Build and return DiagnosticIndicator object.

        Returns:
            DiagnosticIndicator instance
        """
        # TODO: Add validation
        return self._obj
