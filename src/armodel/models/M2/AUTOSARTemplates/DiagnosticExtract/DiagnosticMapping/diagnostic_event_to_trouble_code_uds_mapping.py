"""DiagnosticEventToTroubleCodeUdsMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 245)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping.classes.json"""

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


class DiagnosticEventToTroubleCodeUdsMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticEventToTroubleCodeUdsMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    diagnostic_event: Optional[DiagnosticEvent]
    trouble_code_uds: Optional[DiagnosticTroubleCode]
    def __init__(self) -> None:
        """Initialize DiagnosticEventToTroubleCodeUdsMapping."""
        super().__init__()
        self.diagnostic_event: Optional[DiagnosticEvent] = None
        self.trouble_code_uds: Optional[DiagnosticTroubleCode] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEventToTroubleCodeUdsMapping":
        """Deserialize XML element to DiagnosticEventToTroubleCodeUdsMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticEventToTroubleCodeUdsMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticEventToTroubleCodeUdsMapping, cls).deserialize(element)

        # Parse diagnostic_event
        child = ARObject._find_child_element(element, "DIAGNOSTIC-EVENT")
        if child is not None:
            diagnostic_event_value = ARObject._deserialize_by_tag(child, "DiagnosticEvent")
            obj.diagnostic_event = diagnostic_event_value

        # Parse trouble_code_uds
        child = ARObject._find_child_element(element, "TROUBLE-CODE-UDS")
        if child is not None:
            trouble_code_uds_value = ARObject._deserialize_by_tag(child, "DiagnosticTroubleCode")
            obj.trouble_code_uds = trouble_code_uds_value

        return obj



class DiagnosticEventToTroubleCodeUdsMappingBuilder:
    """Builder for DiagnosticEventToTroubleCodeUdsMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEventToTroubleCodeUdsMapping = DiagnosticEventToTroubleCodeUdsMapping()

    def build(self) -> DiagnosticEventToTroubleCodeUdsMapping:
        """Build and return DiagnosticEventToTroubleCodeUdsMapping object.

        Returns:
            DiagnosticEventToTroubleCodeUdsMapping instance
        """
        # TODO: Add validation
        return self._obj
