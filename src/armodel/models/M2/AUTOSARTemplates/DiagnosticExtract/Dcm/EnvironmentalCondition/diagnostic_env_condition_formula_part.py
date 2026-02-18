"""DiagnosticEnvConditionFormulaPart AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 80)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_EnvironmentalCondition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from abc import ABC, abstractmethod


class DiagnosticEnvConditionFormulaPart(ARObject, ABC):
    """AUTOSAR DiagnosticEnvConditionFormulaPart."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize DiagnosticEnvConditionFormulaPart."""
        super().__init__()


class DiagnosticEnvConditionFormulaPartBuilder:
    """Builder for DiagnosticEnvConditionFormulaPart."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEnvConditionFormulaPart = DiagnosticEnvConditionFormulaPart()

    def build(self) -> DiagnosticEnvConditionFormulaPart:
        """Build and return DiagnosticEnvConditionFormulaPart object.

        Returns:
            DiagnosticEnvConditionFormulaPart instance
        """
        # TODO: Add validation
        return self._obj
