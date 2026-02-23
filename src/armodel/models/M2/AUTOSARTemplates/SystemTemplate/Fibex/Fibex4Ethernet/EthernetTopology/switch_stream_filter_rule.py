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
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.stream_filter_ieee1722_tp import (
    StreamFilterIEEE1722Tp,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.stream_filter_rule_data_link_layer import (
    StreamFilterRuleDataLinkLayer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.stream_filter_rule_ip_tp import (
    StreamFilterRuleIpTp,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


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
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

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

        # Parse data_link_layer
        child = SerializationHelper.find_child_element(element, "DATA-LINK-LAYER")
        if child is not None:
            data_link_layer_value = SerializationHelper.deserialize_by_tag(child, "StreamFilterRuleDataLinkLayer")
            obj.data_link_layer = data_link_layer_value

        # Parse ieee1722_tp
        child = SerializationHelper.find_child_element(element, "IEEE1722-TP")
        if child is not None:
            ieee1722_tp_value = SerializationHelper.deserialize_by_tag(child, "StreamFilterIEEE1722Tp")
            obj.ieee1722_tp = ieee1722_tp_value

        # Parse ip_tp_rule
        child = SerializationHelper.find_child_element(element, "IP-TP-RULE")
        if child is not None:
            ip_tp_rule_value = SerializationHelper.deserialize_by_tag(child, "StreamFilterRuleIpTp")
            obj.ip_tp_rule = ip_tp_rule_value

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




    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Get type hints for the class
        try:
            type_hints_dict = get_type_hints(type(self._obj))
        except Exception:
            # Cannot resolve type hints (e.g., forward references), skip validation
            return

        for attr_name, attr_type in type_hints_dict.items():
            if attr_name.startswith("_"):
                continue

            value = getattr(self._obj, attr_name)

            # Check required fields (not Optional)
            if value is None and not self._is_optional_type(attr_type):
                if mode == BuilderValidationMode.STRICT:
                    raise ValueError(
                        f"Required attribute '{attr_name}' is None"
                    )
                elif mode == BuilderValidationMode.LENIENT:
                    import warnings
                    warnings.warn(
                        f"Required attribute '{attr_name}' is None",
                        UserWarning
                    )

    @staticmethod
    def _is_optional_type(type_hint: Any) -> bool:
        """Check if a type hint is Optional.

        Args:
            type_hint: Type hint to check

        Returns:
            True if type is Optional, False otherwise
        """
        origin = getattr(type_hint, "__origin__", None)
        return origin is Union

    @staticmethod
    def _get_expected_type(type_hint: Any) -> type:
        """Extract expected type from type hint.

        Args:
            type_hint: Type hint to extract from

        Returns:
            Expected type
        """
        if isinstance(type_hint, str):
            return object
        origin = getattr(type_hint, "__origin__", None)
        if origin is Union:
            args = getattr(type_hint, "__args__", [])
            for arg in args:
                if arg is not type(None):
                    return arg
        elif origin is list:
            args = getattr(type_hint, "__args__", [object])
            return args[0] if args else object
        return type_hint if isinstance(type_hint, type) else object


    def build(self) -> SwitchStreamFilterRule:
        """Build and return the SwitchStreamFilterRule instance with validation."""
        self._validate_instance()
        pass
        return self._obj