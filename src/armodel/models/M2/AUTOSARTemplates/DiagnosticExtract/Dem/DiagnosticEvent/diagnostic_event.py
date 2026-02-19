"""DiagnosticEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 164)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticEvent.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent import (
    DiagnosticClearEventAllowedBehaviorEnum,
    DiagnosticEventClearAllowedEnum,
    DiagnosticEventKindEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class DiagnosticEvent(DiagnosticCommonElement):
    """AUTOSAR DiagnosticEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    associated: Optional[PositiveInteger]
    clear_event: Optional[DiagnosticClearEventAllowedBehaviorEnum]
    confirmation: Optional[PositiveInteger]
    connecteds: list[Any]
    event_clear: Optional[DiagnosticEventClearAllowedEnum]
    event_kind: Optional[DiagnosticEventKindEnum]
    prestorage: Optional[Boolean]
    prestored: Optional[Boolean]
    recoverable_in: Optional[Boolean]
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEvent":
        """Deserialize XML element to DiagnosticEvent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticEvent object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse associated
        child = ARObject._find_child_element(element, "ASSOCIATED")
        if child is not None:
            associated_value = child.text
            obj.associated = associated_value

        # Parse clear_event
        child = ARObject._find_child_element(element, "CLEAR-EVENT")
        if child is not None:
            clear_event_value = child.text
            obj.clear_event = clear_event_value

        # Parse confirmation
        child = ARObject._find_child_element(element, "CONFIRMATION")
        if child is not None:
            confirmation_value = child.text
            obj.confirmation = confirmation_value

        # Parse connecteds (list)
        obj.connecteds = []
        for child in ARObject._find_all_child_elements(element, "CONNECTEDS"):
            connecteds_value = child.text
            obj.connecteds.append(connecteds_value)

        # Parse event_clear
        child = ARObject._find_child_element(element, "EVENT-CLEAR")
        if child is not None:
            event_clear_value = child.text
            obj.event_clear = event_clear_value

        # Parse event_kind
        child = ARObject._find_child_element(element, "EVENT-KIND")
        if child is not None:
            event_kind_value = child.text
            obj.event_kind = event_kind_value

        # Parse prestorage
        child = ARObject._find_child_element(element, "PRESTORAGE")
        if child is not None:
            prestorage_value = child.text
            obj.prestorage = prestorage_value

        # Parse prestored
        child = ARObject._find_child_element(element, "PRESTORED")
        if child is not None:
            prestored_value = child.text
            obj.prestored = prestored_value

        # Parse recoverable_in
        child = ARObject._find_child_element(element, "RECOVERABLE-IN")
        if child is not None:
            recoverable_in_value = child.text
            obj.recoverable_in = recoverable_in_value

        return obj



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
