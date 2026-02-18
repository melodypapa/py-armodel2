"""ObdInfoServiceNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 324)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 233)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 797)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)


class ObdInfoServiceNeeds(DiagnosticCapabilityElement):
    """AUTOSAR ObdInfoServiceNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize ObdInfoServiceNeeds."""
        super().__init__()


class ObdInfoServiceNeedsBuilder:
    """Builder for ObdInfoServiceNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ObdInfoServiceNeeds = ObdInfoServiceNeeds()

    def build(self) -> ObdInfoServiceNeeds:
        """Build and return ObdInfoServiceNeeds object.

        Returns:
            ObdInfoServiceNeeds instance
        """
        # TODO: Add validation
        return self._obj
