"""DiagnosticFimEventGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 217)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Fim.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_event import (
    DiagnosticEvent,
)


class DiagnosticFimEventGroup(DiagnosticCommonElement):
    """AUTOSAR DiagnosticFimEventGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    events: list[DiagnosticEvent]
    def __init__(self) -> None:
        """Initialize DiagnosticFimEventGroup."""
        super().__init__()
        self.events: list[DiagnosticEvent] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticFimEventGroup":
        """Deserialize XML element to DiagnosticFimEventGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticFimEventGroup object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse events (list)
        obj.events = []
        for child in ARObject._find_all_child_elements(element, "EVENTS"):
            events_value = ARObject._deserialize_by_tag(child, "DiagnosticEvent")
            obj.events.append(events_value)

        return obj



class DiagnosticFimEventGroupBuilder:
    """Builder for DiagnosticFimEventGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticFimEventGroup = DiagnosticFimEventGroup()

    def build(self) -> DiagnosticFimEventGroup:
        """Build and return DiagnosticFimEventGroup object.

        Returns:
            DiagnosticFimEventGroup instance
        """
        # TODO: Add validation
        return self._obj
