"""SecurityEventContextMappingCommConnector AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 40)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.security_event_context_mapping import (
    SecurityEventContextMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_connector import (
    CommunicationConnector,
)


class SecurityEventContextMappingCommConnector(SecurityEventContextMapping):
    """AUTOSAR SecurityEventContextMappingCommConnector."""

    comm_connectors: list[CommunicationConnector]
    def __init__(self) -> None:
        """Initialize SecurityEventContextMappingCommConnector."""
        super().__init__()
        self.comm_connectors: list[CommunicationConnector] = []


class SecurityEventContextMappingCommConnectorBuilder:
    """Builder for SecurityEventContextMappingCommConnector."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecurityEventContextMappingCommConnector = SecurityEventContextMappingCommConnector()

    def build(self) -> SecurityEventContextMappingCommConnector:
        """Build and return SecurityEventContextMappingCommConnector object.

        Returns:
            SecurityEventContextMappingCommConnector instance
        """
        # TODO: Add validation
        return self._obj
