"""CanCommunicationConnector AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 74)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology.abstract_can_communication_connector import (
    AbstractCanCommunicationConnector,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    PositiveUnlimitedInteger,
)


class CanCommunicationConnector(AbstractCanCommunicationConnector):
    """AUTOSAR CanCommunicationConnector."""

    pnc_wakeup_can: Optional[PositiveInteger]
    pnc_wakeup: Optional[PositiveUnlimitedInteger]
    pnc_wakeup_dlc: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize CanCommunicationConnector."""
        super().__init__()
        self.pnc_wakeup_can: Optional[PositiveInteger] = None
        self.pnc_wakeup: Optional[PositiveUnlimitedInteger] = None
        self.pnc_wakeup_dlc: Optional[PositiveInteger] = None


class CanCommunicationConnectorBuilder:
    """Builder for CanCommunicationConnector."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanCommunicationConnector = CanCommunicationConnector()

    def build(self) -> CanCommunicationConnector:
        """Build and return CanCommunicationConnector object.

        Returns:
            CanCommunicationConnector instance
        """
        # TODO: Add validation
        return self._obj
