"""SwitchStreamIdentification AUTOSAR element."""

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
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.switch_stream_filter_rule import (
    SwitchStreamFilterRule,
)


class SwitchStreamIdentification(Identifiable):
    """AUTOSAR SwitchStreamIdentification."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("egress_ports", None, False, True, CouplingPort),  # egressPorts
        ("filter_action_block", None, True, False, None),  # filterActionBlock
        ("filter_action_dest", None, False, False, any (SwitchStreamFilter)),  # filterActionDest
        ("filter_action_drop", None, True, False, None),  # filterActionDrop
        ("filter_action_vlan", None, True, False, None),  # filterActionVlan
        ("ingress_ports", None, False, True, CouplingPort),  # ingressPorts
        ("stream_filter", None, False, False, SwitchStreamFilterRule),  # streamFilter
    ]

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

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SwitchStreamIdentification to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwitchStreamIdentification":
        """Create SwitchStreamIdentification from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SwitchStreamIdentification instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SwitchStreamIdentification since parent returns ARObject
        return cast("SwitchStreamIdentification", obj)


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
