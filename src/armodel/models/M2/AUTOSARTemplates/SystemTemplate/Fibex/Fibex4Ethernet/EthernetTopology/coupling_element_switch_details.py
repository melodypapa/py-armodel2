"""CouplingElementSwitchDetails AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 133)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_element_abstract_details import (
    CouplingElementAbstractDetails,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.switch_asynchronous_traffic_shaper_group_entry import (
    SwitchAsynchronousTrafficShaperGroupEntry,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.switch_flow_metering_entry import (
    SwitchFlowMeteringEntry,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.switch_stream_filter_entry import (
    SwitchStreamFilterEntry,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.switch_stream_gate_entry import (
    SwitchStreamGateEntry,
)


class CouplingElementSwitchDetails(CouplingElementAbstractDetails):
    """AUTOSAR CouplingElementSwitchDetails."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "flow_meterings": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=SwitchFlowMeteringEntry,
        ),  # flowMeterings
        "stream_filters": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=SwitchStreamFilterEntry,
        ),  # streamFilters
        "stream_gates": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=SwitchStreamGateEntry,
        ),  # streamGates
        "switch_streams": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (SwitchStream),
        ),  # switchStreams
        "traffic_shapers": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=SwitchAsynchronousTrafficShaperGroupEntry,
        ),  # trafficShapers
    }

    def __init__(self) -> None:
        """Initialize CouplingElementSwitchDetails."""
        super().__init__()
        self.flow_meterings: list[SwitchFlowMeteringEntry] = []
        self.stream_filters: list[SwitchStreamFilterEntry] = []
        self.stream_gates: list[SwitchStreamGateEntry] = []
        self.switch_streams: list[Any] = []
        self.traffic_shapers: list[SwitchAsynchronousTrafficShaperGroupEntry] = []


class CouplingElementSwitchDetailsBuilder:
    """Builder for CouplingElementSwitchDetails."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CouplingElementSwitchDetails = CouplingElementSwitchDetails()

    def build(self) -> CouplingElementSwitchDetails:
        """Build and return CouplingElementSwitchDetails object.

        Returns:
            CouplingElementSwitchDetails instance
        """
        # TODO: Add validation
        return self._obj
