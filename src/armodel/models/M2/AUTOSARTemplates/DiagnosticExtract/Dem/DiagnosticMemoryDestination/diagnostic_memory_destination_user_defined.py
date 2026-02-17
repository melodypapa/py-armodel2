"""DiagnosticMemoryDestinationUserDefined AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 184)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticMemoryDestination.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticMemoryDestination.diagnostic_memory_destination import (
    DiagnosticMemoryDestination,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.diagnostic_auth_role import (
    DiagnosticAuthRole,
)


class DiagnosticMemoryDestinationUserDefined(DiagnosticMemoryDestination):
    """AUTOSAR DiagnosticMemoryDestinationUserDefined."""

    auth_roles: list[DiagnosticAuthRole]
    memory_id: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DiagnosticMemoryDestinationUserDefined."""
        super().__init__()
        self.auth_roles: list[DiagnosticAuthRole] = []
        self.memory_id: Optional[PositiveInteger] = None


class DiagnosticMemoryDestinationUserDefinedBuilder:
    """Builder for DiagnosticMemoryDestinationUserDefined."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticMemoryDestinationUserDefined = DiagnosticMemoryDestinationUserDefined()

    def build(self) -> DiagnosticMemoryDestinationUserDefined:
        """Build and return DiagnosticMemoryDestinationUserDefined object.

        Returns:
            DiagnosticMemoryDestinationUserDefined instance
        """
        # TODO: Add validation
        return self._obj
