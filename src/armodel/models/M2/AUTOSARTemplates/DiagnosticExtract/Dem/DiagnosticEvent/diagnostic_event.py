"""DiagnosticEvent AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "associated": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # associated
        "clear_event": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticClearEventAllowedBehaviorEnum,
        ),  # clearEvent
        "confirmation": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # confirmation
        "connecteds": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (DiagnosticConnected),
        ),  # connecteds
        "event_clear": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticEventClearAllowedEnum,
        ),  # eventClear
        "event_kind": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticEventKindEnum,
        ),  # eventKind
        "prestorage": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # prestorage
        "prestored": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # prestored
        "recoverable_in": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # recoverableIn
    }

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
