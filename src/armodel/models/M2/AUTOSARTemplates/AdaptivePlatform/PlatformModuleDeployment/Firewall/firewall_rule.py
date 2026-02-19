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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "FirewallRule":
        """Deserialize XML element to FirewallRule object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FirewallRule object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

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

        # Parse payload_byte_patterns (list)
        obj.payload_byte_patterns = []
        for child in ARObject._find_all_child_elements(element, "PAYLOAD-BYTE-PATTERNS"):
            payload_byte_patterns_value = child.text
            obj.payload_byte_patterns.append(payload_byte_patterns_value)

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
