"""DiagnosticTestResult AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 204)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 804)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticTestResult.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_event import (
    DiagnosticEvent,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticTestResult.diagnostic_test_identifier import (
    DiagnosticTestIdentifier,
)


class DiagnosticTestResult(DiagnosticCommonElement):
    """AUTOSAR DiagnosticTestResult."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    diagnostic_event: Optional[DiagnosticEvent]
    monitored: Optional[Any]
    test_identifier: Optional[DiagnosticTestIdentifier]
    update_kind: Optional[DiagnosticTestResult]
    def __init__(self) -> None:
        """Initialize DiagnosticTestResult."""
        super().__init__()
        self.diagnostic_event: Optional[DiagnosticEvent] = None
        self.monitored: Optional[Any] = None
        self.test_identifier: Optional[DiagnosticTestIdentifier] = None
        self.update_kind: Optional[DiagnosticTestResult] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticTestResult":
        """Deserialize XML element to DiagnosticTestResult object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticTestResult object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticTestResult, cls).deserialize(element)

        # Parse diagnostic_event
        child = ARObject._find_child_element(element, "DIAGNOSTIC-EVENT")
        if child is not None:
            diagnostic_event_value = ARObject._deserialize_by_tag(child, "DiagnosticEvent")
            obj.diagnostic_event = diagnostic_event_value

        # Parse monitored
        child = ARObject._find_child_element(element, "MONITORED")
        if child is not None:
            monitored_value = child.text
            obj.monitored = monitored_value

        # Parse test_identifier
        child = ARObject._find_child_element(element, "TEST-IDENTIFIER")
        if child is not None:
            test_identifier_value = ARObject._deserialize_by_tag(child, "DiagnosticTestIdentifier")
            obj.test_identifier = test_identifier_value

        # Parse update_kind
        child = ARObject._find_child_element(element, "UPDATE-KIND")
        if child is not None:
            update_kind_value = ARObject._deserialize_by_tag(child, "DiagnosticTestResult")
            obj.update_kind = update_kind_value

        return obj



class DiagnosticTestResultBuilder:
    """Builder for DiagnosticTestResult."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticTestResult = DiagnosticTestResult()

    def build(self) -> DiagnosticTestResult:
        """Build and return DiagnosticTestResult object.

        Returns:
            DiagnosticTestResult instance
        """
        # TODO: Add validation
        return self._obj
