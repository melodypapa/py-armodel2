"""TpConnectionIdent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 61)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 633)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DiagnosticConnection.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)


class TpConnectionIdent(Referrable):
    """AUTOSAR TpConnectionIdent."""

    def __init__(self) -> None:
        """Initialize TpConnectionIdent."""
        super().__init__()


class TpConnectionIdentBuilder:
    """Builder for TpConnectionIdent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TpConnectionIdent = TpConnectionIdent()

    def build(self) -> TpConnectionIdent:
        """Build and return TpConnectionIdent object.

        Returns:
            TpConnectionIdent instance
        """
        # TODO: Add validation
        return self._obj
