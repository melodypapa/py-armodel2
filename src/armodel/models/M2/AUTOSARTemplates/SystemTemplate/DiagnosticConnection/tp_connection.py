"""TpConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 633)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DiagnosticConnection.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection.tp_connection_ident import (
    TpConnectionIdent,
)


class TpConnection(ARObject):
    """AUTOSAR TpConnection."""
    """Abstract base class - do not instantiate directly."""

    def __init__(self) -> None:
        """Initialize TpConnection."""
        super().__init__()
        self.ident: Optional[TpConnectionIdent] = None


class TpConnectionBuilder:
    """Builder for TpConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TpConnection = TpConnection()

    def build(self) -> TpConnection:
        """Build and return TpConnection object.

        Returns:
            TpConnection instance
        """
        # TODO: Add validation
        return self._obj
