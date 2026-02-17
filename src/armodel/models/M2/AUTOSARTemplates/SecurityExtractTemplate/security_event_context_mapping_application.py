"""SecurityEventContextMappingApplication AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 42)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.security_event_context_mapping import (
    SecurityEventContextMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class SecurityEventContextMappingApplication(SecurityEventContextMapping):
    """AUTOSAR SecurityEventContextMappingApplication."""

    affected: String
    def __init__(self) -> None:
        """Initialize SecurityEventContextMappingApplication."""
        super().__init__()
        self.affected: String = None


class SecurityEventContextMappingApplicationBuilder:
    """Builder for SecurityEventContextMappingApplication."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecurityEventContextMappingApplication = SecurityEventContextMappingApplication()

    def build(self) -> SecurityEventContextMappingApplication:
        """Build and return SecurityEventContextMappingApplication object.

        Returns:
            SecurityEventContextMappingApplication instance
        """
        # TODO: Add validation
        return self._obj
