"""TpConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 587)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_cluster import (
    CommunicationCluster,
)
from abc import ABC, abstractmethod


class TpConfig(FibexElement, ABC):
    """AUTOSAR TpConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    communication_cluster: Optional[CommunicationCluster]
    def __init__(self) -> None:
        """Initialize TpConfig."""
        super().__init__()
        self.communication_cluster: Optional[CommunicationCluster] = None


class TpConfigBuilder:
    """Builder for TpConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TpConfig = TpConfig()

    def build(self) -> TpConfig:
        """Build and return TpConfig object.

        Returns:
            TpConfig instance
        """
        # TODO: Add validation
        return self._obj
