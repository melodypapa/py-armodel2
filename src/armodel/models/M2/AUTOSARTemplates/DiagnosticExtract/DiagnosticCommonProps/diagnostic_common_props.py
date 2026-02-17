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
