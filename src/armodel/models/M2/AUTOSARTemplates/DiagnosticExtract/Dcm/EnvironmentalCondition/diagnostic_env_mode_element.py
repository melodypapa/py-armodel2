"""DiagnosticEnvModeElement AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 89)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_EnvironmentalCondition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from abc import ABC, abstractmethod


class DiagnosticEnvModeElement(Referrable, ABC):
    """AUTOSAR DiagnosticEnvModeElement."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize DiagnosticEnvModeElement."""
        super().__init__()


class DiagnosticEnvModeElementBuilder:
    """Builder for DiagnosticEnvModeElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEnvModeElement = DiagnosticEnvModeElement()

    def build(self) -> DiagnosticEnvModeElement:
        """Build and return DiagnosticEnvModeElement object.

        Returns:
            DiagnosticEnvModeElement instance
        """
        # TODO: Add validation
        return self._obj
