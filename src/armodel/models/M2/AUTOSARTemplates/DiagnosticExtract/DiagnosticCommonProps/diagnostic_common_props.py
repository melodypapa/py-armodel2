"""DiagnosticCommonProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
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
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("authentication", None, True, False, None),  # authentication
        ("debounces", None, False, True, any (DiagnosticDebounce)),  # debounces
        ("default", None, False, False, ByteOrderEnum),  # default
        ("event", None, False, False, DiagnosticEvent),  # event
        ("max_number_of", None, True, False, None),  # maxNumberOf
        ("occurrence", None, False, False, DiagnosticOccurrenceCounterProcessingEnum),  # occurrence
        ("reset_confirmed", None, True, False, None),  # resetConfirmed
        ("reset_pending_bit", None, True, False, None),  # resetPendingBit
        ("response_on_all", None, True, False, None),  # responseOnAll
        ("response_on", None, True, False, None),  # responseOn
        ("type_of_event", None, False, False, DiagnosticEvent),  # typeOfEvent
    ]

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

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticCommonProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticCommonProps":
        """Create DiagnosticCommonProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticCommonProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticCommonProps since parent returns ARObject
        return cast("DiagnosticCommonProps", obj)


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
