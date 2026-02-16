"""FirewallRuleProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall.firewall_rule import (
    FirewallRule,
)


class FirewallRuleProps(ARObject):
    """AUTOSAR FirewallRuleProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("action", None, False, False, any (FirewallActionEnum)),  # action
        ("matching_egresses", None, False, True, FirewallRule),  # matchingEgresses
        ("matchings", None, False, True, FirewallRule),  # matchings
    ]

    def __init__(self) -> None:
        """Initialize FirewallRuleProps."""
        super().__init__()
        self.action: Optional[Any] = None
        self.matching_egresses: list[FirewallRule] = []
        self.matchings: list[FirewallRule] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert FirewallRuleProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FirewallRuleProps":
        """Create FirewallRuleProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            FirewallRuleProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to FirewallRuleProps since parent returns ARObject
        return cast("FirewallRuleProps", obj)


class FirewallRulePropsBuilder:
    """Builder for FirewallRuleProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FirewallRuleProps = FirewallRuleProps()

    def build(self) -> FirewallRuleProps:
        """Build and return FirewallRuleProps object.

        Returns:
            FirewallRuleProps instance
        """
        # TODO: Add validation
        return self._obj
