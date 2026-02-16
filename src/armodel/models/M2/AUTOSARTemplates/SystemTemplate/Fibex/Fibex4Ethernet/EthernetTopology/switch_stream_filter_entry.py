"""SwitchStreamFilterEntry AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
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
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("asynchronous", None, False, False, CouplingPort),  # asynchronous
        ("filter_priority", None, True, False, None),  # filterPriority
        ("flow_metering", None, False, False, SwitchFlowMeteringEntry),  # flowMetering
        ("max_sdu_size", None, True, False, None),  # maxSduSize
        ("stream_gate", None, False, False, SwitchStreamGateEntry),  # streamGate
        ("stream", None, True, False, None),  # stream
    ]

    def __init__(self) -> None:
        """Initialize SwitchStreamFilterEntry."""
        super().__init__()
        self.asynchronous: Optional[CouplingPort] = None
        self.filter_priority: Optional[PositiveInteger] = None
        self.flow_metering: Optional[SwitchFlowMeteringEntry] = None
        self.max_sdu_size: Optional[PositiveInteger] = None
        self.stream_gate: Optional[SwitchStreamGateEntry] = None
        self.stream: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SwitchStreamFilterEntry to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwitchStreamFilterEntry":
        """Create SwitchStreamFilterEntry from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SwitchStreamFilterEntry instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SwitchStreamFilterEntry since parent returns ARObject
        return cast("SwitchStreamFilterEntry", obj)


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
