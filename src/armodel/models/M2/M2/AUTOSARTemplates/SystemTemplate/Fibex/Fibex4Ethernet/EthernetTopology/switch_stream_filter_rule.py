"""SwitchStreamFilterRule AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 136)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.stream_filter_ieee1722_tp import (
    StreamFilterIEEE1722Tp,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.stream_filter_rule_data_link_layer import (
    StreamFilterRuleDataLinkLayer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.stream_filter_rule_ip_tp import (
    StreamFilterRuleIpTp,
)


class SwitchStreamFilterRule(Identifiable):
    """AUTOSAR SwitchStreamFilterRule."""

    def __init__(self) -> None:
        """Initialize SwitchStreamFilterRule."""
        super().__init__()
        self.data_link_layer: Optional[StreamFilterRuleDataLinkLayer] = None
        self.ieee1722_tp: Optional[StreamFilterIEEE1722Tp] = None
        self.ip_tp_rule: Optional[StreamFilterRuleIpTp] = None


class SwitchStreamFilterRuleBuilder:
    """Builder for SwitchStreamFilterRule."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwitchStreamFilterRule = SwitchStreamFilterRule()

    def build(self) -> SwitchStreamFilterRule:
        """Build and return SwitchStreamFilterRule object.

        Returns:
            SwitchStreamFilterRule instance
        """
        # TODO: Add validation
        return self._obj
