"""UserDefinedCommunicationConnector AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 179)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_CddSupport.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_connector import (
    CommunicationConnector,
)


class UserDefinedCommunicationConnector(CommunicationConnector):
    """AUTOSAR UserDefinedCommunicationConnector."""

    def __init__(self) -> None:
        """Initialize UserDefinedCommunicationConnector."""
        super().__init__()


class UserDefinedCommunicationConnectorBuilder:
    """Builder for UserDefinedCommunicationConnector."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: UserDefinedCommunicationConnector = UserDefinedCommunicationConnector()

    def build(self) -> UserDefinedCommunicationConnector:
        """Build and return UserDefinedCommunicationConnector object.

        Returns:
            UserDefinedCommunicationConnector instance
        """
        # TODO: Add validation
        return self._obj
