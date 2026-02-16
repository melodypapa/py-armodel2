"""StateDependentFirewall AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall.firewall_rule_props import (
    FirewallRuleProps,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)


class StateDependentFirewall(ARElement):
    """AUTOSAR StateDependentFirewall."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("default_action", None, False, False, any (FirewallActionEnum)),  # defaultAction
        ("firewall_rule_propses", None, False, True, FirewallRuleProps),  # firewallRulePropses
        ("firewall_states", None, False, True, ModeDeclaration),  # firewallStates
    ]

    def __init__(self) -> None:
        """Initialize StateDependentFirewall."""
        super().__init__()
        self.default_action: Optional[Any] = None
        self.firewall_rule_propses: list[FirewallRuleProps] = []
        self.firewall_states: list[ModeDeclaration] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert StateDependentFirewall to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "StateDependentFirewall":
        """Create StateDependentFirewall from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            StateDependentFirewall instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to StateDependentFirewall since parent returns ARObject
        return cast("StateDependentFirewall", obj)


class StateDependentFirewallBuilder:
    """Builder for StateDependentFirewall."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: StateDependentFirewall = StateDependentFirewall()

    def build(self) -> StateDependentFirewall:
        """Build and return StateDependentFirewall object.

        Returns:
            StateDependentFirewall instance
        """
        # TODO: Add validation
        return self._obj
