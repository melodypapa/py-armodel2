"""CanTpChannel AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 608)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class CanTpChannel(Identifiable):
    """AUTOSAR CanTpChannel."""

    channel_id: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize CanTpChannel."""
        super().__init__()
        self.channel_id: Optional[PositiveInteger] = None


class CanTpChannelBuilder:
    """Builder for CanTpChannel."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanTpChannel = CanTpChannel()

    def build(self) -> CanTpChannel:
        """Build and return CanTpChannel object.

        Returns:
            CanTpChannel instance
        """
        # TODO: Add validation
        return self._obj
