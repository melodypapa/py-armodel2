"""SecurityEventFilterChain AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 20)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.ids_common_element import (
    IdsCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.security_event_one_every_n_filter import (
    SecurityEventOneEveryNFilter,
)
from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.security_event_state_filter import (
    SecurityEventStateFilter,
)
from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.security_event_threshold_filter import (
    SecurityEventThresholdFilter,
)


class SecurityEventFilterChain(IdsCommonElement):
    """AUTOSAR SecurityEventFilterChain."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    aggregation: Optional[Any]
    one_every_n: Optional[SecurityEventOneEveryNFilter]
    state: Optional[SecurityEventStateFilter]
    threshold: Optional[SecurityEventThresholdFilter]
    def __init__(self) -> None:
        """Initialize SecurityEventFilterChain."""
        super().__init__()
        self.aggregation: Optional[Any] = None
        self.one_every_n: Optional[SecurityEventOneEveryNFilter] = None
        self.state: Optional[SecurityEventStateFilter] = None
        self.threshold: Optional[SecurityEventThresholdFilter] = None


class SecurityEventFilterChainBuilder:
    """Builder for SecurityEventFilterChain."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecurityEventFilterChain = SecurityEventFilterChain()

    def build(self) -> SecurityEventFilterChain:
        """Build and return SecurityEventFilterChain object.

        Returns:
            SecurityEventFilterChain instance
        """
        # TODO: Add validation
        return self._obj
