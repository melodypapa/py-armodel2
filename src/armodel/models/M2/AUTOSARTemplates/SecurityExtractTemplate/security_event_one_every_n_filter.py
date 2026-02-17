"""SecurityEventOneEveryNFilter AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 24)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.abstract_security_event_filter import (
    AbstractSecurityEventFilter,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class SecurityEventOneEveryNFilter(AbstractSecurityEventFilter):
    """AUTOSAR SecurityEventOneEveryNFilter."""

    n: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize SecurityEventOneEveryNFilter."""
        super().__init__()
        self.n: Optional[PositiveInteger] = None


class SecurityEventOneEveryNFilterBuilder:
    """Builder for SecurityEventOneEveryNFilter."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecurityEventOneEveryNFilter = SecurityEventOneEveryNFilter()

    def build(self) -> SecurityEventOneEveryNFilter:
        """Build and return SecurityEventOneEveryNFilter object.

        Returns:
            SecurityEventOneEveryNFilter instance
        """
        # TODO: Add validation
        return self._obj
