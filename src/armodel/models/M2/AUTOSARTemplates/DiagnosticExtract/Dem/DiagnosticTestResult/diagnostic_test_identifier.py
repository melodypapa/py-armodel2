"""DiagnosticTestIdentifier AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 205)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticTestResult.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DiagnosticTestIdentifier(ARObject):
    """AUTOSAR DiagnosticTestIdentifier."""

    id: Optional[PositiveInteger]
    uas_id: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DiagnosticTestIdentifier."""
        super().__init__()
        self.id: Optional[PositiveInteger] = None
        self.uas_id: Optional[PositiveInteger] = None


class DiagnosticTestIdentifierBuilder:
    """Builder for DiagnosticTestIdentifier."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticTestIdentifier = DiagnosticTestIdentifier()

    def build(self) -> DiagnosticTestIdentifier:
        """Build and return DiagnosticTestIdentifier object.

        Returns:
            DiagnosticTestIdentifier instance
        """
        # TODO: Add validation
        return self._obj
