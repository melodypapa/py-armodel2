"""DoIpRoutingActivationConfirmationNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 807)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.do_ip_service_needs import (
    DoIpServiceNeeds,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    PositiveInteger,
)


class DoIpRoutingActivationConfirmationNeeds(DoIpServiceNeeds):
    """AUTOSAR DoIpRoutingActivationConfirmationNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_length: Optional[PositiveInteger]
    routing: Optional[NameToken]
    def __init__(self) -> None:
        """Initialize DoIpRoutingActivationConfirmationNeeds."""
        super().__init__()
        self.data_length: Optional[PositiveInteger] = None
        self.routing: Optional[NameToken] = None


class DoIpRoutingActivationConfirmationNeedsBuilder:
    """Builder for DoIpRoutingActivationConfirmationNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DoIpRoutingActivationConfirmationNeeds = DoIpRoutingActivationConfirmationNeeds()

    def build(self) -> DoIpRoutingActivationConfirmationNeeds:
        """Build and return DoIpRoutingActivationConfirmationNeeds object.

        Returns:
            DoIpRoutingActivationConfirmationNeeds instance
        """
        # TODO: Add validation
        return self._obj
