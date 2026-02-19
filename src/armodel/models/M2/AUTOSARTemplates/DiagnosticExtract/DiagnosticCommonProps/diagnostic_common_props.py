"""DiagnosticCommonProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 64)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticCommonProps.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticCommonProps import (
    DiagnosticOccurrenceCounterProcessingEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ByteOrderEnum,
)
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    authentication: Optional[TimeValue]
    debounces: list[Any]
    default: Optional[ByteOrderEnum]
    event: Optional[DiagnosticEvent]
    max_number_of: Optional[PositiveInteger]
    occurrence: Optional[DiagnosticOccurrenceCounterProcessingEnum]
    reset_confirmed: Optional[Boolean]
    reset_pending_bit: Optional[Boolean]
    response_on_all: Optional[Boolean]
    response_on: Optional[Boolean]
    type_of_event: Optional[DiagnosticEvent]
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticCommonProps":
        """Deserialize XML element to DiagnosticCommonProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticCommonProps object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse authentication
        child = ARObject._find_child_element(element, "AUTHENTICATION")
        if child is not None:
            authentication_value = child.text
            obj.authentication = authentication_value

        # Parse debounces (list from container "DEBOUNCES")
        obj.debounces = []
        container = ARObject._find_child_element(element, "DEBOUNCES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.debounces.append(child_value)

        # Parse default
        child = ARObject._find_child_element(element, "DEFAULT")
        if child is not None:
            default_value = ByteOrderEnum.deserialize(child)
            obj.default = default_value

        # Parse event
        child = ARObject._find_child_element(element, "EVENT")
        if child is not None:
            event_value = ARObject._deserialize_by_tag(child, "DiagnosticEvent")
            obj.event = event_value

        # Parse max_number_of
        child = ARObject._find_child_element(element, "MAX-NUMBER-OF")
        if child is not None:
            max_number_of_value = child.text
            obj.max_number_of = max_number_of_value

        # Parse occurrence
        child = ARObject._find_child_element(element, "OCCURRENCE")
        if child is not None:
            occurrence_value = DiagnosticOccurrenceCounterProcessingEnum.deserialize(child)
            obj.occurrence = occurrence_value

        # Parse reset_confirmed
        child = ARObject._find_child_element(element, "RESET-CONFIRMED")
        if child is not None:
            reset_confirmed_value = child.text
            obj.reset_confirmed = reset_confirmed_value

        # Parse reset_pending_bit
        child = ARObject._find_child_element(element, "RESET-PENDING-BIT")
        if child is not None:
            reset_pending_bit_value = child.text
            obj.reset_pending_bit = reset_pending_bit_value

        # Parse response_on_all
        child = ARObject._find_child_element(element, "RESPONSE-ON-ALL")
        if child is not None:
            response_on_all_value = child.text
            obj.response_on_all = response_on_all_value

        # Parse response_on
        child = ARObject._find_child_element(element, "RESPONSE-ON")
        if child is not None:
            response_on_value = child.text
            obj.response_on = response_on_value

        # Parse type_of_event
        child = ARObject._find_child_element(element, "TYPE-OF-EVENT")
        if child is not None:
            type_of_event_value = ARObject._deserialize_by_tag(child, "DiagnosticEvent")
            obj.type_of_event = type_of_event_value

        return obj



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
