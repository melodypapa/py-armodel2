"""SwitchStreamIdentification AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 135)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port import (
    CouplingPort,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.switch_stream_filter_rule import (
    SwitchStreamFilterRule,
)


class SwitchStreamIdentification(Identifiable):
    """AUTOSAR SwitchStreamIdentification."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "egress_ports": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=CouplingPort,
        ),  # egressPorts
        "filter_action_block": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # filterActionBlock
        "filter_action_dest": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Any,
        ),  # filterActionDest
        "filter_action_drop": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # filterActionDrop
        "filter_action_vlan": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # filterActionVlan
        "ingress_ports": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=CouplingPort,
        ),  # ingressPorts
        "stream_filter": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwitchStreamFilterRule,
        ),  # streamFilter
    }

    def __init__(self) -> None:
        """Initialize SwitchStreamIdentification."""
        super().__init__()
        self.egress_ports: list[CouplingPort] = []
        self.filter_action_block: Optional[Boolean] = None
        self.filter_action_dest: Optional[Any] = None
        self.filter_action_drop: Optional[Boolean] = None
        self.filter_action_vlan: Optional[PositiveInteger] = None
        self.ingress_ports: list[CouplingPort] = []
        self.stream_filter: Optional[SwitchStreamFilterRule] = None


class SwitchStreamIdentificationBuilder:
    """Builder for SwitchStreamIdentification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwitchStreamIdentification = SwitchStreamIdentification()

    def build(self) -> SwitchStreamIdentification:
        """Build and return SwitchStreamIdentification object.

        Returns:
            SwitchStreamIdentification instance
        """
        # TODO: Add validation
        return self._obj
