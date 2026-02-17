"""DiagnosticDeAuthentication AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 100)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_Authentication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.Authentication.diagnostic_authentication import (
    DiagnosticAuthentication,
)


class DiagnosticDeAuthentication(DiagnosticAuthentication):
    """AUTOSAR DiagnosticDeAuthentication."""

    def __init__(self) -> None:
        """Initialize DiagnosticDeAuthentication."""
        super().__init__()


class DiagnosticDeAuthenticationBuilder:
    """Builder for DiagnosticDeAuthentication."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticDeAuthentication = DiagnosticDeAuthentication()

    def build(self) -> DiagnosticDeAuthentication:
        """Build and return DiagnosticDeAuthentication object.

        Returns:
            DiagnosticDeAuthentication instance
        """
        # TODO: Add validation
        return self._obj
