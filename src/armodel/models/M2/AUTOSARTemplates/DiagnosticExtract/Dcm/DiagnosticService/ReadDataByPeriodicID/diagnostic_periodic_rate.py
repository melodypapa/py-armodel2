"""DiagnosticPeriodicRate AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 131)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_ReadDataByPeriodicID.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class DiagnosticPeriodicRate(ARObject):
    """AUTOSAR DiagnosticPeriodicRate."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    period: Optional[TimeValue]
    periodic_rate: Optional[DiagnosticPeriodicRate]
    def __init__(self) -> None:
        """Initialize DiagnosticPeriodicRate."""
        super().__init__()
        self.period: Optional[TimeValue] = None
        self.periodic_rate: Optional[DiagnosticPeriodicRate] = None


class DiagnosticPeriodicRateBuilder:
    """Builder for DiagnosticPeriodicRate."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticPeriodicRate = DiagnosticPeriodicRate()

    def build(self) -> DiagnosticPeriodicRate:
        """Build and return DiagnosticPeriodicRate object.

        Returns:
            DiagnosticPeriodicRate instance
        """
        # TODO: Add validation
        return self._obj
