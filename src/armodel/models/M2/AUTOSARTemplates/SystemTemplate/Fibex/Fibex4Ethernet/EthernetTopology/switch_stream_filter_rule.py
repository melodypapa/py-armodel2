"""SwitchStreamFilterRule AUTOSAR element."""

from typing import Optional, cast
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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("data_link_layer", None, False, False, StreamFilterRuleDataLinkLayer),  # dataLinkLayer
        ("ieee1722_tp", None, False, False, StreamFilterIEEE1722Tp),  # ieee1722Tp
        ("ip_tp_rule", None, False, False, StreamFilterRuleIpTp),  # ipTpRule
    ]

    def __init__(self) -> None:
        """Initialize SwitchStreamFilterRule."""
        super().__init__()
        self.data_link_layer: Optional[StreamFilterRuleDataLinkLayer] = None
        self.ieee1722_tp: Optional[StreamFilterIEEE1722Tp] = None
        self.ip_tp_rule: Optional[StreamFilterRuleIpTp] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SwitchStreamFilterRule to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwitchStreamFilterRule":
        """Create SwitchStreamFilterRule from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SwitchStreamFilterRule instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SwitchStreamFilterRule since parent returns ARObject
        return cast("SwitchStreamFilterRule", obj)


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
