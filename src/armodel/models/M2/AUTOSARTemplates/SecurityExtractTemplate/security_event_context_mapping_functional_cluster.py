"""SecurityEventContextMappingFunctionalCluster AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 39)

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


class SecurityEventContextMappingFunctionalCluster(SecurityEventContextMapping):
    """AUTOSAR SecurityEventContextMappingFunctionalCluster."""

    affected: String
    def __init__(self) -> None:
        """Initialize SecurityEventContextMappingFunctionalCluster."""
        super().__init__()
        self.affected: String = None


class SecurityEventContextMappingFunctionalClusterBuilder:
    """Builder for SecurityEventContextMappingFunctionalCluster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecurityEventContextMappingFunctionalCluster = SecurityEventContextMappingFunctionalCluster()

    def build(self) -> SecurityEventContextMappingFunctionalCluster:
        """Build and return SecurityEventContextMappingFunctionalCluster object.

        Returns:
            SecurityEventContextMappingFunctionalCluster instance
        """
        # TODO: Add validation
        return self._obj
