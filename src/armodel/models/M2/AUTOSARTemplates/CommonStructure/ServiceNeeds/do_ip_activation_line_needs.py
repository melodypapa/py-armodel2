"""DoIpActivationLineNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 807)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2019)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.do_ip_service_needs import (
    DoIpServiceNeeds,
)


class DoIpActivationLineNeeds(DoIpServiceNeeds):
    """AUTOSAR DoIpActivationLineNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize DoIpActivationLineNeeds."""
        super().__init__()


class DoIpActivationLineNeedsBuilder:
    """Builder for DoIpActivationLineNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DoIpActivationLineNeeds = DoIpActivationLineNeeds()

    def build(self) -> DoIpActivationLineNeeds:
        """Build and return DoIpActivationLineNeeds object.

        Returns:
            DoIpActivationLineNeeds instance
        """
        # TODO: Add validation
        return self._obj
