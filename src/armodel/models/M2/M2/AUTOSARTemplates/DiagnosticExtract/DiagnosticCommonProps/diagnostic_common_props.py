"""DiagnosticCommonProps AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_event import (
    DiagnosticEvent,
)


class DiagnosticCommonProps(ARObject):
    """AUTOSAR DiagnosticCommonProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "authentication": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # authentication
        "debounces": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (DiagnosticDebounce),
        ),  # debounces
        "default": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ByteOrderEnum,
        ),  # default
        "event": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticEvent,
        ),  # event
        "max_number_of": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # maxNumberOf
        "occurrence": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticOccurrenceCounterProcessingEnum,
        ),  # occurrence
        "reset_confirmed": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # resetConfirmed
        "reset_pending_bit": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # resetPendingBit
        "response_on_all": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # responseOnAll
        "response_on": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # responseOn
        "type_of_event": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticEvent,
        ),  # typeOfEvent
    }

    def __init__(self) -> None:
        """Initialize DiagnosticCommonProps."""
        super().__init__()
        self.authentication: Optional[TimeValue] = None
        self.debounces: list[Any] = []
        self.default: Optional[ByteOrderEnum] = None
        self.event: Optional[DiagnosticEvent] = None
        self.max_number_of: Optional[PositiveInteger] = None
        self.occurrence: Optional[DiagnosticOccurrenceCounterProcessingEnum] = None
        self.reset_confirmed: Optional[Boolean] = None
        self.reset_pending_bit: Optional[Boolean] = None
        self.response_on_all: Optional[Boolean] = None
        self.response_on: Optional[Boolean] = None
        self.type_of_event: Optional[DiagnosticEvent] = None


class DiagnosticCommonPropsBuilder:
    """Builder for DiagnosticCommonProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticCommonProps = DiagnosticCommonProps()

    def build(self) -> DiagnosticCommonProps:
        """Build and return DiagnosticCommonProps object.

        Returns:
            DiagnosticCommonProps instance
        """
        # TODO: Add validation
        return self._obj
