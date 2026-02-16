"""DiagnosticEnvModeCondition AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.EnvironmentalCondition.diagnostic_env_compare_condition import (
    DiagnosticEnvCompareCondition,
)


class DiagnosticEnvModeCondition(DiagnosticEnvCompareCondition):
    """AUTOSAR DiagnosticEnvModeCondition."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("mode_element", None, False, False, any (DiagnosticEnvMode)),  # modeElement
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticEnvModeCondition."""
        super().__init__()
        self.mode_element: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticEnvModeCondition to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEnvModeCondition":
        """Create DiagnosticEnvModeCondition from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticEnvModeCondition instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticEnvModeCondition since parent returns ARObject
        return cast("DiagnosticEnvModeCondition", obj)


class DiagnosticEnvModeConditionBuilder:
    """Builder for DiagnosticEnvModeCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEnvModeCondition = DiagnosticEnvModeCondition()

    def build(self) -> DiagnosticEnvModeCondition:
        """Build and return DiagnosticEnvModeCondition object.

        Returns:
            DiagnosticEnvModeCondition instance
        """
        # TODO: Add validation
        return self._obj
