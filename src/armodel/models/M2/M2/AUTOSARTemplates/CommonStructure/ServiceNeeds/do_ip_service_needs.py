"""DoIpServiceNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 237)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 805)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2020)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)


class DoIpServiceNeeds(ServiceNeeds):
    """AUTOSAR DoIpServiceNeeds."""
    """Abstract base class - do not instantiate directly."""

    def __init__(self) -> None:
        """Initialize DoIpServiceNeeds."""
        super().__init__()


class DoIpServiceNeedsBuilder:
    """Builder for DoIpServiceNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DoIpServiceNeeds = DoIpServiceNeeds()

    def build(self) -> DoIpServiceNeeds:
        """Build and return DoIpServiceNeeds object.

        Returns:
            DoIpServiceNeeds instance
        """
        # TODO: Add validation
        return self._obj
