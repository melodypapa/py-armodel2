"""DiagnosticMemoryDestination AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 181)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticMemoryDestination.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticMemoryDestination import (
    DiagnosticMemoryEntryStorageTriggerEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_event import (
    DiagnosticEvent,
)
from abc import ABC, abstractmethod


class DiagnosticMemoryDestination(DiagnosticCommonElement, ABC):
    """AUTOSAR DiagnosticMemoryDestination."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    aging_requires: Optional[Boolean]
    clear_dtc: Optional[Any]
    dtc_status: Optional[PositiveInteger]
    event: Optional[DiagnosticEvent]
    max_number_of: Optional[PositiveInteger]
    memory_entry: Optional[DiagnosticMemoryEntryStorageTriggerEnum]
    status_bit: Optional[Boolean]
    type_of_freeze: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticMemoryDestination."""
        super().__init__()
        self.aging_requires: Optional[Boolean] = None
        self.clear_dtc: Optional[Any] = None
        self.dtc_status: Optional[PositiveInteger] = None
        self.event: Optional[DiagnosticEvent] = None
        self.max_number_of: Optional[PositiveInteger] = None
        self.memory_entry: Optional[DiagnosticMemoryEntryStorageTriggerEnum] = None
        self.status_bit: Optional[Boolean] = None
        self.type_of_freeze: Optional[Any] = None


class DiagnosticMemoryDestinationBuilder:
    """Builder for DiagnosticMemoryDestination."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticMemoryDestination = DiagnosticMemoryDestination()

    def build(self) -> DiagnosticMemoryDestination:
        """Build and return DiagnosticMemoryDestination object.

        Returns:
            DiagnosticMemoryDestination instance
        """
        # TODO: Add validation
        return self._obj
