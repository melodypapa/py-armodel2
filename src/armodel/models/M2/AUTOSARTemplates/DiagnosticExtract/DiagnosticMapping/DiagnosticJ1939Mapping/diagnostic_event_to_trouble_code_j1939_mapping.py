"""DiagnosticEventToTroubleCodeJ1939Mapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 269)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping_DiagnosticJ1939Mapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_event import (
    DiagnosticEvent,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTroubleCode.diagnostic_trouble_code import (
    DiagnosticTroubleCode,
)


class DiagnosticEventToTroubleCodeJ1939Mapping(DiagnosticMapping):
    """AUTOSAR DiagnosticEventToTroubleCodeJ1939Mapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    diagnostic_event: Optional[DiagnosticEvent]
    trouble_code: Optional[DiagnosticTroubleCode]
    def __init__(self) -> None:
        """Initialize DiagnosticEventToTroubleCodeJ1939Mapping."""
        super().__init__()
        self.diagnostic_event: Optional[DiagnosticEvent] = None
        self.trouble_code: Optional[DiagnosticTroubleCode] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEventToTroubleCodeJ1939Mapping":
        """Deserialize XML element to DiagnosticEventToTroubleCodeJ1939Mapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticEventToTroubleCodeJ1939Mapping object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse diagnostic_event
        child = ARObject._find_child_element(element, "DIAGNOSTIC-EVENT")
        if child is not None:
            diagnostic_event_value = ARObject._deserialize_by_tag(child, "DiagnosticEvent")
            obj.diagnostic_event = diagnostic_event_value

        # Parse trouble_code
        child = ARObject._find_child_element(element, "TROUBLE-CODE")
        if child is not None:
            trouble_code_value = ARObject._deserialize_by_tag(child, "DiagnosticTroubleCode")
            obj.trouble_code = trouble_code_value

        return obj



class DiagnosticEventToTroubleCodeJ1939MappingBuilder:
    """Builder for DiagnosticEventToTroubleCodeJ1939Mapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEventToTroubleCodeJ1939Mapping = DiagnosticEventToTroubleCodeJ1939Mapping()

    def build(self) -> DiagnosticEventToTroubleCodeJ1939Mapping:
        """Build and return DiagnosticEventToTroubleCodeJ1939Mapping object.

        Returns:
            DiagnosticEventToTroubleCodeJ1939Mapping instance
        """
        # TODO: Add validation
        return self._obj
