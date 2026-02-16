"""DiagnosticStorageCondition AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticCondition.diagnostic_condition import (
    DiagnosticCondition,
)


class DiagnosticStorageCondition(DiagnosticCondition):
    """AUTOSAR DiagnosticStorageCondition."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticStorageCondition."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticStorageCondition to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticStorageCondition":
        """Create DiagnosticStorageCondition from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticStorageCondition instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticStorageCondition since parent returns ARObject
        return cast("DiagnosticStorageCondition", obj)


class DiagnosticStorageConditionBuilder:
    """Builder for DiagnosticStorageCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticStorageCondition = DiagnosticStorageCondition()

    def build(self) -> DiagnosticStorageCondition:
        """Build and return DiagnosticStorageCondition object.

        Returns:
            DiagnosticStorageCondition instance
        """
        # TODO: Add validation
        return self._obj
