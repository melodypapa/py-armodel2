"""DiagnosticServiceMappingDiagTarget AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 234)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping_ServiceMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from abc import ABC, abstractmethod


class DiagnosticServiceMappingDiagTarget(ARObject, ABC):
    """AUTOSAR DiagnosticServiceMappingDiagTarget."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize DiagnosticServiceMappingDiagTarget."""
        super().__init__()


class DiagnosticServiceMappingDiagTargetBuilder:
    """Builder for DiagnosticServiceMappingDiagTarget."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticServiceMappingDiagTarget = DiagnosticServiceMappingDiagTarget()

    def build(self) -> DiagnosticServiceMappingDiagTarget:
        """Build and return DiagnosticServiceMappingDiagTarget object.

        Returns:
            DiagnosticServiceMappingDiagTarget instance
        """
        # TODO: Add validation
        return self._obj
