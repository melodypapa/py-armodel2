"""DiagnosticEvent AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class DiagnosticEvent(DiagnosticCommonElement):
    """AUTOSAR DiagnosticEvent."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("associated", None, True, False, None),  # associated
        ("clear_event", None, False, False, DiagnosticClearEventAllowedBehaviorEnum),  # clearEvent
        ("confirmation", None, True, False, None),  # confirmation
        ("connecteds", None, False, True, any (DiagnosticConnected)),  # connecteds
        ("event_clear", None, False, False, DiagnosticEventClearAllowedEnum),  # eventClear
        ("event_kind", None, False, False, DiagnosticEventKindEnum),  # eventKind
        ("prestorage", None, True, False, None),  # prestorage
        ("prestored", None, True, False, None),  # prestored
        ("recoverable_in", None, True, False, None),  # recoverableIn
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticEvent."""
        super().__init__()
        self.associated: Optional[PositiveInteger] = None
        self.clear_event: Optional[DiagnosticClearEventAllowedBehaviorEnum] = None
        self.confirmation: Optional[PositiveInteger] = None
        self.connecteds: list[Any] = []
        self.event_clear: Optional[DiagnosticEventClearAllowedEnum] = None
        self.event_kind: Optional[DiagnosticEventKindEnum] = None
        self.prestorage: Optional[Boolean] = None
        self.prestored: Optional[Boolean] = None
        self.recoverable_in: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticEvent to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEvent":
        """Create DiagnosticEvent from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticEvent instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticEvent since parent returns ARObject
        return cast("DiagnosticEvent", obj)


class DiagnosticEventBuilder:
    """Builder for DiagnosticEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEvent = DiagnosticEvent()

    def build(self) -> DiagnosticEvent:
        """Build and return DiagnosticEvent object.

        Returns:
            DiagnosticEvent instance
        """
        # TODO: Add validation
        return self._obj
