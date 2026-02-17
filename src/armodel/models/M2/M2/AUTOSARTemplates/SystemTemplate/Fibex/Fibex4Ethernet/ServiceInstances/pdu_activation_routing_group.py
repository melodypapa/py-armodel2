"""PduActivationRoutingGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 488)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    EventGroupControlTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.so_con_i_pdu_identifier import (
    SoConIPduIdentifier,
)


class PduActivationRoutingGroup(Identifiable):
    """AUTOSAR PduActivationRoutingGroup."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "event_group": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=EventGroupControlTypeEnum,
        ),  # eventGroup
        "i_pdu_identifiers": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=SoConIPduIdentifier,
        ),  # iPduIdentifiers
    }

    def __init__(self) -> None:
        """Initialize PduActivationRoutingGroup."""
        super().__init__()
        self.event_group: Optional[EventGroupControlTypeEnum] = None
        self.i_pdu_identifiers: list[SoConIPduIdentifier] = []


class PduActivationRoutingGroupBuilder:
    """Builder for PduActivationRoutingGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PduActivationRoutingGroup = PduActivationRoutingGroup()

    def build(self) -> PduActivationRoutingGroup:
        """Build and return PduActivationRoutingGroup object.

        Returns:
            PduActivationRoutingGroup instance
        """
        # TODO: Add validation
        return self._obj
