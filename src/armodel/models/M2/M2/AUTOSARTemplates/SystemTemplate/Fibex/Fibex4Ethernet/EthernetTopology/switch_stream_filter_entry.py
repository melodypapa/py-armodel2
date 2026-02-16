"""SwitchStreamFilterEntry AUTOSAR element."""

from typing import Optional
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
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.switch_flow_metering_entry import (
    SwitchFlowMeteringEntry,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.switch_stream_gate_entry import (
    SwitchStreamGateEntry,
)


class SwitchStreamFilterEntry(Identifiable):
    """AUTOSAR SwitchStreamFilterEntry."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "asynchronous": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CouplingPort,
        ),  # asynchronous
        "filter_priority": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # filterPriority
        "flow_metering": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwitchFlowMeteringEntry,
        ),  # flowMetering
        "max_sdu_size": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # maxSduSize
        "stream_gate": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwitchStreamGateEntry,
        ),  # streamGate
        "stream": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # stream
    }

    def __init__(self) -> None:
        """Initialize SwitchStreamFilterEntry."""
        super().__init__()
        self.asynchronous: Optional[CouplingPort] = None
        self.filter_priority: Optional[PositiveInteger] = None
        self.flow_metering: Optional[SwitchFlowMeteringEntry] = None
        self.max_sdu_size: Optional[PositiveInteger] = None
        self.stream_gate: Optional[SwitchStreamGateEntry] = None
        self.stream: Optional[Boolean] = None


class SwitchStreamFilterEntryBuilder:
    """Builder for SwitchStreamFilterEntry."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwitchStreamFilterEntry = SwitchStreamFilterEntry()

    def build(self) -> SwitchStreamFilterEntry:
        """Build and return SwitchStreamFilterEntry object.

        Returns:
            SwitchStreamFilterEntry instance
        """
        # TODO: Add validation
        return self._obj
