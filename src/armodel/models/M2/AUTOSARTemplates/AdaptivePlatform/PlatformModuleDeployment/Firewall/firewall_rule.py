"""FirewallRule AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class FirewallRule(ARElement):
    """AUTOSAR FirewallRule."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("bucket_size", None, True, False, None),  # bucketSize
        ("data_link_layer_rule", None, False, False, any (DataLinkLayerRule)),  # dataLinkLayerRule
        ("dds_rule", None, False, False, any (DdsRule)),  # ddsRule
        ("do_ip_rule", None, False, False, any (DoIpRule)),  # doIpRule
        ("network_layer_rule", None, False, False, any (NetworkLayerRule)),  # networkLayerRule
        ("payload_byte_patterns", None, False, True, any (PayloadBytePattern)),  # payloadBytePatterns
        ("refill_amount", None, True, False, None),  # refillAmount
        ("someip_rule", None, False, False, any (SomeipProtocolRule)),  # someipRule
        ("someip_sd_rule", None, False, False, any (SomeipSdRule)),  # someipSdRule
        ("transport_layer_rule", None, False, False, any (TransportLayerRule)),  # transportLayerRule
    ]

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

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert FirewallRule to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FirewallRule":
        """Create FirewallRule from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            FirewallRule instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to FirewallRule since parent returns ARObject
        return cast("FirewallRule", obj)


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
