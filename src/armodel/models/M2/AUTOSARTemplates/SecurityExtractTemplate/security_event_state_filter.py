"""SecurityEventStateFilter AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 22)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.abstract_security_event_filter import (
    AbstractSecurityEventFilter,
)
from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.block_state import (
    BlockState,
)


class SecurityEventStateFilter(AbstractSecurityEventFilter):
    """AUTOSAR SecurityEventStateFilter."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    block_if_states: list[BlockState]
    def __init__(self) -> None:
        """Initialize SecurityEventStateFilter."""
        super().__init__()
        self.block_if_states: list[BlockState] = []


class SecurityEventStateFilterBuilder:
    """Builder for SecurityEventStateFilter."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecurityEventStateFilter = SecurityEventStateFilter()

    def build(self) -> SecurityEventStateFilter:
        """Build and return SecurityEventStateFilter object.

        Returns:
            SecurityEventStateFilter instance
        """
        # TODO: Add validation
        return self._obj
