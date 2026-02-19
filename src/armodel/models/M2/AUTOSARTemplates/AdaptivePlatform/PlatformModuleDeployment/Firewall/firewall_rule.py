"""FirewallRule AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 584)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_AdaptivePlatform_PlatformModuleDeployment_Firewall.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class FirewallRule(ARElement):
    """AUTOSAR FirewallRule."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    bucket_size: Optional[PositiveInteger]
    data_link_layer_rule: Optional[Any]
    dds_rule: Optional[Any]
    do_ip_rule: Optional[Any]
    network_layer_rule: Optional[Any]
    payload_byte_patterns: list[Any]
    refill_amount: Optional[PositiveInteger]
    someip_rule: Optional[Any]
    someip_sd_rule: Optional[Any]
    transport_layer_rule: Optional[Any]
    def __init__(self) -> None:
        """Initialize FirewallRule."""
        super().__init__()
        self.bucket_size: Optional[PositiveInteger] = None
        self.data_link_layer_rule: Optional[Any] = None
        self.dds_rule: Optional[Any] = None
        self.do_ip_rule: Optional[Any] = None
        self.network_layer_rule: Optional[Any] = None
        self.payload_byte_patterns: list[Any] = []
        self.refill_amount: Optional[PositiveInteger] = None
        self.someip_rule: Optional[Any] = None
        self.someip_sd_rule: Optional[Any] = None
        self.transport_layer_rule: Optional[Any] = None
    def serialize(self) -> ET.Element:
        """Serialize FirewallRule to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FirewallRule, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize bucket_size
        if self.bucket_size is not None:
            serialized = ARObject._serialize_item(self.bucket_size, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BUCKET-SIZE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize data_link_layer_rule
        if self.data_link_layer_rule is not None:
            serialized = ARObject._serialize_item(self.data_link_layer_rule, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-LINK-LAYER-RULE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize dds_rule
        if self.dds_rule is not None:
            serialized = ARObject._serialize_item(self.dds_rule, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DDS-RULE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize do_ip_rule
        if self.do_ip_rule is not None:
            serialized = ARObject._serialize_item(self.do_ip_rule, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DO-IP-RULE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize network_layer_rule
        if self.network_layer_rule is not None:
            serialized = ARObject._serialize_item(self.network_layer_rule, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NETWORK-LAYER-RULE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize payload_byte_patterns (list to container "PAYLOAD-BYTE-PATTERNS")
        if self.payload_byte_patterns:
            wrapper = ET.Element("PAYLOAD-BYTE-PATTERNS")
            for item in self.payload_byte_patterns:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize refill_amount
        if self.refill_amount is not None:
            serialized = ARObject._serialize_item(self.refill_amount, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REFILL-AMOUNT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize someip_rule
        if self.someip_rule is not None:
            serialized = ARObject._serialize_item(self.someip_rule, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SOMEIP-RULE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize someip_sd_rule
        if self.someip_sd_rule is not None:
            serialized = ARObject._serialize_item(self.someip_sd_rule, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SOMEIP-SD-RULE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize transport_layer_rule
        if self.transport_layer_rule is not None:
            serialized = ARObject._serialize_item(self.transport_layer_rule, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRANSPORT-LAYER-RULE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FirewallRule":
        """Deserialize XML element to FirewallRule object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FirewallRule object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FirewallRule, cls).deserialize(element)

        # Parse bucket_size
        child = ARObject._find_child_element(element, "BUCKET-SIZE")
        if child is not None:
            bucket_size_value = child.text
            obj.bucket_size = bucket_size_value

        # Parse data_link_layer_rule
        child = ARObject._find_child_element(element, "DATA-LINK-LAYER-RULE")
        if child is not None:
            data_link_layer_rule_value = child.text
            obj.data_link_layer_rule = data_link_layer_rule_value

        # Parse dds_rule
        child = ARObject._find_child_element(element, "DDS-RULE")
        if child is not None:
            dds_rule_value = child.text
            obj.dds_rule = dds_rule_value

        # Parse do_ip_rule
        child = ARObject._find_child_element(element, "DO-IP-RULE")
        if child is not None:
            do_ip_rule_value = child.text
            obj.do_ip_rule = do_ip_rule_value

        # Parse network_layer_rule
        child = ARObject._find_child_element(element, "NETWORK-LAYER-RULE")
        if child is not None:
            network_layer_rule_value = child.text
            obj.network_layer_rule = network_layer_rule_value

        # Parse payload_byte_patterns (list from container "PAYLOAD-BYTE-PATTERNS")
        obj.payload_byte_patterns = []
        container = ARObject._find_child_element(element, "PAYLOAD-BYTE-PATTERNS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.payload_byte_patterns.append(child_value)

        # Parse refill_amount
        child = ARObject._find_child_element(element, "REFILL-AMOUNT")
        if child is not None:
            refill_amount_value = child.text
            obj.refill_amount = refill_amount_value

        # Parse someip_rule
        child = ARObject._find_child_element(element, "SOMEIP-RULE")
        if child is not None:
            someip_rule_value = child.text
            obj.someip_rule = someip_rule_value

        # Parse someip_sd_rule
        child = ARObject._find_child_element(element, "SOMEIP-SD-RULE")
        if child is not None:
            someip_sd_rule_value = child.text
            obj.someip_sd_rule = someip_sd_rule_value

        # Parse transport_layer_rule
        child = ARObject._find_child_element(element, "TRANSPORT-LAYER-RULE")
        if child is not None:
            transport_layer_rule_value = child.text
            obj.transport_layer_rule = transport_layer_rule_value

        return obj



class FirewallRuleBuilder:
    """Builder for FirewallRule."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FirewallRule = FirewallRule()

    def build(self) -> FirewallRule:
        """Build and return FirewallRule object.

        Returns:
            FirewallRule instance
        """
        # TODO: Add validation
        return self._obj
