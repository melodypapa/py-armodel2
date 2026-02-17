"""DiagnosticIumprGroupIdentifier AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 211)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticEvent.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
)


class DiagnosticIumprGroupIdentifier(ARObject):
    """AUTOSAR DiagnosticIumprGroupIdentifier."""

    def __init__(self) -> None:
        """Initialize DiagnosticIumprGroupIdentifier."""
        super().__init__()
        self.group_id: Optional[NameToken] = None


class DiagnosticIumprGroupIdentifierBuilder:
    """Builder for DiagnosticIumprGroupIdentifier."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticIumprGroupIdentifier = DiagnosticIumprGroupIdentifier()

    def build(self) -> DiagnosticIumprGroupIdentifier:
        """Build and return DiagnosticIumprGroupIdentifier object.

        Returns:
            DiagnosticIumprGroupIdentifier instance
        """
        # TODO: Add validation
        return self._obj
