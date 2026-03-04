"""SwitchStreamFilterRule AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 136)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.stream_filter_ieee1722_tp import (
    StreamFilterIEEE1722Tp,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.stream_filter_rule_data_link_layer import (
    StreamFilterRuleDataLinkLayer,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.stream_filter_rule_ip_tp import (
    StreamFilterRuleIpTp,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SwitchStreamFilterRule(Identifiable):
    """AUTOSAR SwitchStreamFilterRule."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SWITCH-STREAM-FILTER-RULE"


    data_link_layer: Optional[StreamFilterRuleDataLinkLayer]
    ieee1722_tp: Optional[StreamFilterIEEE1722Tp]
    ip_tp_rule: Optional[StreamFilterRuleIpTp]
    _DESERIALIZE_DISPATCH = {
        "DATA-LINK-LAYER": lambda obj, elem: setattr(obj, "data_link_layer", SerializationHelper.deserialize_by_tag(elem, "StreamFilterRuleDataLinkLayer")),
        "IEEE1722-TP": lambda obj, elem: setattr(obj, "ieee1722_tp", SerializationHelper.deserialize_by_tag(elem, "StreamFilterIEEE1722Tp")),
        "IP-TP-RULE": lambda obj, elem: setattr(obj, "ip_tp_rule", SerializationHelper.deserialize_by_tag(elem, "StreamFilterRuleIpTp")),
    }


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
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwitchStreamFilterRule, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_link_layer
        if self.data_link_layer is not None:
            serialized = SerializationHelper.serialize_item(self.data_link_layer, "StreamFilterRuleDataLinkLayer")
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
            serialized = SerializationHelper.serialize_item(self.ieee1722_tp, "StreamFilterIEEE1722Tp")
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
            serialized = SerializationHelper.serialize_item(self.ip_tp_rule, "StreamFilterRuleIpTp")
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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DATA-LINK-LAYER":
                setattr(obj, "data_link_layer", SerializationHelper.deserialize_by_tag(child, "StreamFilterRuleDataLinkLayer"))
            elif tag == "IEEE1722-TP":
                setattr(obj, "ieee1722_tp", SerializationHelper.deserialize_by_tag(child, "StreamFilterIEEE1722Tp"))
            elif tag == "IP-TP-RULE":
                setattr(obj, "ip_tp_rule", SerializationHelper.deserialize_by_tag(child, "StreamFilterRuleIpTp"))

        return obj



class SwitchStreamFilterRuleBuilder(IdentifiableBuilder):
    """Builder for SwitchStreamFilterRule with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SwitchStreamFilterRule = SwitchStreamFilterRule()


    def with_data_link_layer(self, value: Optional[StreamFilterRuleDataLinkLayer]) -> "SwitchStreamFilterRuleBuilder":
        """Set data_link_layer attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.data_link_layer = value
        return self

    def with_ieee1722_tp(self, value: Optional[StreamFilterIEEE1722Tp]) -> "SwitchStreamFilterRuleBuilder":
        """Set ieee1722_tp attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ieee1722_tp = value
        return self

    def with_ip_tp_rule(self, value: Optional[StreamFilterRuleIpTp]) -> "SwitchStreamFilterRuleBuilder":
        """Set ip_tp_rule attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ip_tp_rule = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "dataLinkLayer",
        "ieee1722Tp",
        "ipTpRule",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> SwitchStreamFilterRule:
        """Build and return the SwitchStreamFilterRule instance with validation."""
        self._validate_instance()
        return self._obj