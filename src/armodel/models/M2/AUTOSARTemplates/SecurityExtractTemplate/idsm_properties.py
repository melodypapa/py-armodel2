"""IdsmProperties AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 63)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.ids_common_element import (
    IdsCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.idsm_rate_limitation import (
    IdsmRateLimitation,
)
from armodel.models.M2.AUTOSARTemplates.SecurityExtractTemplate.idsm_traffic_limitation import (
    IdsmTrafficLimitation,
)


class IdsmProperties(IdsCommonElement):
    """AUTOSAR IdsmProperties."""

    rate_limitations: list[IdsmRateLimitation]
    traffic_limitations: list[IdsmTrafficLimitation]
    def __init__(self) -> None:
        """Initialize IdsmProperties."""
        super().__init__()
        self.rate_limitations: list[IdsmRateLimitation] = []
        self.traffic_limitations: list[IdsmTrafficLimitation] = []


class IdsmPropertiesBuilder:
    """Builder for IdsmProperties."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IdsmProperties = IdsmProperties()

    def build(self) -> IdsmProperties:
        """Build and return IdsmProperties object.

        Returns:
            IdsmProperties instance
        """
        # TODO: Add validation
        return self._obj
