"""SwitchStreamIdentification AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 135)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    egress_ports: list[CouplingPort]
    filter_action_block: Optional[Boolean]
    filter_action_dest: Optional[Any]
    filter_action_drop: Optional[Boolean]
    filter_action_vlan: Optional[PositiveInteger]
    ingress_ports: list[CouplingPort]
    stream_filter: Optional[SwitchStreamFilterRule]
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwitchStreamIdentification":
        """Deserialize XML element to SwitchStreamIdentification object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwitchStreamIdentification object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwitchStreamIdentification, cls).deserialize(element)

        # Parse egress_ports (list from container "EGRESS-PORTS")
        obj.egress_ports = []
        container = ARObject._find_child_element(element, "EGRESS-PORTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.egress_ports.append(child_value)

        # Parse filter_action_block
        child = ARObject._find_child_element(element, "FILTER-ACTION-BLOCK")
        if child is not None:
            filter_action_block_value = child.text
            obj.filter_action_block = filter_action_block_value

        # Parse filter_action_dest
        child = ARObject._find_child_element(element, "FILTER-ACTION-DEST")
        if child is not None:
            filter_action_dest_value = child.text
            obj.filter_action_dest = filter_action_dest_value

        # Parse filter_action_drop
        child = ARObject._find_child_element(element, "FILTER-ACTION-DROP")
        if child is not None:
            filter_action_drop_value = child.text
            obj.filter_action_drop = filter_action_drop_value

        # Parse filter_action_vlan
        child = ARObject._find_child_element(element, "FILTER-ACTION-VLAN")
        if child is not None:
            filter_action_vlan_value = child.text
            obj.filter_action_vlan = filter_action_vlan_value

        # Parse ingress_ports (list from container "INGRESS-PORTS")
        obj.ingress_ports = []
        container = ARObject._find_child_element(element, "INGRESS-PORTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.ingress_ports.append(child_value)

        # Parse stream_filter
        child = ARObject._find_child_element(element, "STREAM-FILTER")
        if child is not None:
            stream_filter_value = ARObject._deserialize_by_tag(child, "SwitchStreamFilterRule")
            obj.stream_filter = stream_filter_value

        return obj



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
