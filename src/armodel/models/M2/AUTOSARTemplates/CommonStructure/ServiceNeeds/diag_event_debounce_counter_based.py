"""DiagEventDebounceCounterBased AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 259)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 196)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 757)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diag_event_debounce_algorithm import (
    DiagEventDebounceAlgorithm,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class DiagEventDebounceCounterBased(DiagEventDebounceAlgorithm):
    """AUTOSAR DiagEventDebounceCounterBased."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    counter_based: Optional[Integer]
    counter: Optional[Integer]
    counter_failed: Optional[Integer]
    counter_jump: Optional[Integer]
    counter_jump_up: Optional[Integer]
    counter_passed: Optional[Integer]
    def __init__(self) -> None:
        """Initialize DiagEventDebounceCounterBased."""
        super().__init__()
        self.counter_based: Optional[Integer] = None
        self.counter: Optional[Integer] = None
        self.counter_failed: Optional[Integer] = None
        self.counter_jump: Optional[Integer] = None
        self.counter_jump_up: Optional[Integer] = None
        self.counter_passed: Optional[Integer] = None


class DiagEventDebounceCounterBasedBuilder:
    """Builder for DiagEventDebounceCounterBased."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagEventDebounceCounterBased = DiagEventDebounceCounterBased()

    def build(self) -> DiagEventDebounceCounterBased:
        """Build and return DiagEventDebounceCounterBased object.

        Returns:
            DiagEventDebounceCounterBased instance
        """
        # TODO: Add validation
        return self._obj
