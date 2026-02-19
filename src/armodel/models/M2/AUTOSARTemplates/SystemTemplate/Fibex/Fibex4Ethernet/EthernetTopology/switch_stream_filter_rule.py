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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_link_layer: Optional[StreamFilterRuleDataLinkLayer]
    ieee1722_tp: Optional[StreamFilterIEEE1722Tp]
    ip_tp_rule: Optional[StreamFilterRuleIpTp]
    def __init__(self) -> None:
        """Initialize SwitchStreamFilterRule."""
        super().__init__()
        self.data_link_layer: Optional[StreamFilterRuleDataLinkLayer] = None
        self.ieee1722_tp: Optional[StreamFilterIEEE1722Tp] = None
        self.ip_tp_rule: Optional[StreamFilterRuleIpTp] = None

    def serialize(self) -> ET.Element:
        """Serialize SwitchStreamFilterRule to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwitchStreamFilterRule, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_link_layer
        if self.data_link_layer is not None:
            serialized = ARObject._serialize_item(self.data_link_layer, "StreamFilterRuleDataLinkLayer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-LINK-LAYER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ieee1722_tp
        if self.ieee1722_tp is not None:
            serialized = ARObject._serialize_item(self.ieee1722_tp, "StreamFilterIEEE1722Tp")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IEEE1722-TP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ip_tp_rule
        if self.ip_tp_rule is not None:
            serialized = ARObject._serialize_item(self.ip_tp_rule, "StreamFilterRuleIpTp")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IP-TP-RULE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwitchStreamFilterRule":
        """Deserialize XML element to SwitchStreamFilterRule object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwitchStreamFilterRule object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwitchStreamFilterRule, cls).deserialize(element)

        # Parse data_link_layer
        child = ARObject._find_child_element(element, "DATA-LINK-LAYER")
        if child is not None:
            data_link_layer_value = ARObject._deserialize_by_tag(child, "StreamFilterRuleDataLinkLayer")
            obj.data_link_layer = data_link_layer_value

        # Parse ieee1722_tp
        child = ARObject._find_child_element(element, "IEEE1722-TP")
        if child is not None:
            ieee1722_tp_value = ARObject._deserialize_by_tag(child, "StreamFilterIEEE1722Tp")
            obj.ieee1722_tp = ieee1722_tp_value

        # Parse ip_tp_rule
        child = ARObject._find_child_element(element, "IP-TP-RULE")
        if child is not None:
            ip_tp_rule_value = ARObject._deserialize_by_tag(child, "StreamFilterRuleIpTp")
            obj.ip_tp_rule = ip_tp_rule_value

        return obj



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
