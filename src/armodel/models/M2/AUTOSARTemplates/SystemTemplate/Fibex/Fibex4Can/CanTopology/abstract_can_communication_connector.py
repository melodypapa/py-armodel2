"""AbstractCanCommunicationConnector AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 73)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_connector import (
    CommunicationConnector,
)
from abc import ABC, abstractmethod


class AbstractCanCommunicationConnector(CommunicationConnector, ABC):
    """AUTOSAR AbstractCanCommunicationConnector."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize AbstractCanCommunicationConnector."""
        super().__init__()


class AbstractCanCommunicationConnectorBuilder:
    """Builder for AbstractCanCommunicationConnector."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractCanCommunicationConnector = AbstractCanCommunicationConnector()

    def build(self) -> AbstractCanCommunicationConnector:
        """Build and return AbstractCanCommunicationConnector object.

        Returns:
            AbstractCanCommunicationConnector instance
        """
        # TODO: Add validation
        return self._obj
