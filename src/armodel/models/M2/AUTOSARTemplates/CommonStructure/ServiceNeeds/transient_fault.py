"""TransientFault AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 1009)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.traced_failure import (
    TracedFailure,
)


class TransientFault(TracedFailure):
    """AUTOSAR TransientFault."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    possible_error_reactions: list[Any]
    def __init__(self) -> None:
        """Initialize TransientFault."""
        super().__init__()
        self.possible_error_reactions: list[Any] = []


class TransientFaultBuilder:
    """Builder for TransientFault."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TransientFault = TransientFault()

    def build(self) -> TransientFault:
        """Build and return TransientFault object.

        Returns:
            TransientFault instance
        """
        # TODO: Add validation
        return self._obj
