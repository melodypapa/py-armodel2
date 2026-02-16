"""DiagnosticEventToEnableConditionGroupMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_event import (
    DiagnosticEvent,
)


class DiagnosticEventToEnableConditionGroupMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticEventToEnableConditionGroupMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("diagnostic_event", None, False, False, DiagnosticEvent),  # diagnosticEvent
        ("enable_condition", None, False, False, any (DiagnosticEnable)),  # enableCondition
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticEventToEnableConditionGroupMapping."""
        super().__init__()
        self.diagnostic_event: Optional[DiagnosticEvent] = None
        self.enable_condition: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticEventToEnableConditionGroupMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEventToEnableConditionGroupMapping":
        """Create DiagnosticEventToEnableConditionGroupMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticEventToEnableConditionGroupMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticEventToEnableConditionGroupMapping since parent returns ARObject
        return cast("DiagnosticEventToEnableConditionGroupMapping", obj)


class DiagnosticEventToEnableConditionGroupMappingBuilder:
    """Builder for DiagnosticEventToEnableConditionGroupMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEventToEnableConditionGroupMapping = DiagnosticEventToEnableConditionGroupMapping()

    def build(self) -> DiagnosticEventToEnableConditionGroupMapping:
        """Build and return DiagnosticEventToEnableConditionGroupMapping object.

        Returns:
            DiagnosticEventToEnableConditionGroupMapping instance
        """
        # TODO: Add validation
        return self._obj
