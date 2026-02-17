"""SecurityEventAggregationFilter AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 24)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.abstract_security_event_filter import (
    AbstractSecurityEventFilter,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class SecurityEventAggregationFilter(AbstractSecurityEventFilter):
    """AUTOSAR SecurityEventAggregationFilter."""

    context_data: Optional[Any]
    minimum: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize SecurityEventAggregationFilter."""
        super().__init__()
        self.context_data: Optional[Any] = None
        self.minimum: Optional[TimeValue] = None


class SecurityEventAggregationFilterBuilder:
    """Builder for SecurityEventAggregationFilter."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecurityEventAggregationFilter = SecurityEventAggregationFilter()

    def build(self) -> SecurityEventAggregationFilter:
        """Build and return SecurityEventAggregationFilter object.

        Returns:
            SecurityEventAggregationFilter instance
        """
        # TODO: Add validation
        return self._obj
