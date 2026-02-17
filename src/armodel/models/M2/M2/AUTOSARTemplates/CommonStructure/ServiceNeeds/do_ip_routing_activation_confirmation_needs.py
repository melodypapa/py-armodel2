"""DoIpRoutingActivationConfirmationNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 807)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.do_ip_service_needs import (
    DoIpServiceNeeds,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    PositiveInteger,
)


class DoIpRoutingActivationConfirmationNeeds(DoIpServiceNeeds):
    """AUTOSAR DoIpRoutingActivationConfirmationNeeds."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "data_length": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # dataLength
        "routing": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # routing
    }

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
