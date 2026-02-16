"""DiagnosticEnvironmentalCondition AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)


class DiagnosticEnvironmentalCondition(DiagnosticCommonElement):
    """AUTOSAR DiagnosticEnvironmentalCondition."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("formula", None, False, False, any (DiagnosticEnvCondition)),  # formula
        ("mode_elements", None, False, True, any (DiagnosticEnvMode)),  # modeElements
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticEnvironmentalCondition."""
        super().__init__()
        self.formula: Optional[Any] = None
        self.mode_elements: list[Any] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticEnvironmentalCondition to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEnvironmentalCondition":
        """Create DiagnosticEnvironmentalCondition from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticEnvironmentalCondition instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticEnvironmentalCondition since parent returns ARObject
        return cast("DiagnosticEnvironmentalCondition", obj)


class DiagnosticEnvironmentalConditionBuilder:
    """Builder for DiagnosticEnvironmentalCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEnvironmentalCondition = DiagnosticEnvironmentalCondition()

    def build(self) -> DiagnosticEnvironmentalCondition:
        """Build and return DiagnosticEnvironmentalCondition object.

        Returns:
            DiagnosticEnvironmentalCondition instance
        """
        # TODO: Add validation
        return self._obj
