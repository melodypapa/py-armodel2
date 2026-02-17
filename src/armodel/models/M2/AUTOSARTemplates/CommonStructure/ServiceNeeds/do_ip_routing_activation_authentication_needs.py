"""DoIpRoutingActivationAuthenticationNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 806)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.do_ip_service_needs import (
    DoIpServiceNeeds,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    PositiveInteger,
)


class DoIpRoutingActivationAuthenticationNeeds(DoIpServiceNeeds):
    """AUTOSAR DoIpRoutingActivationAuthenticationNeeds."""

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
        """Initialize DoIpRoutingActivationAuthenticationNeeds."""
        super().__init__()
        self.data_length: Optional[PositiveInteger] = None
        self.routing: Optional[NameToken] = None


class DoIpRoutingActivationAuthenticationNeedsBuilder:
    """Builder for DoIpRoutingActivationAuthenticationNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DoIpRoutingActivationAuthenticationNeeds = DoIpRoutingActivationAuthenticationNeeds()

    def build(self) -> DoIpRoutingActivationAuthenticationNeeds:
        """Build and return DoIpRoutingActivationAuthenticationNeeds object.

        Returns:
            DoIpRoutingActivationAuthenticationNeeds instance
        """
        # TODO: Add validation
        return self._obj
