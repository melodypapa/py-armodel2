"""StateDependentFirewall AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 583)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_AdaptivePlatform_PlatformModuleDeployment_Firewall.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "default_action": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (FirewallActionEnum),
        ),  # defaultAction
        "firewall_rule_propses": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=FirewallRuleProps,
        ),  # firewallRulePropses
        "firewall_states": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ModeDeclaration,
        ),  # firewallStates
    }

    def __init__(self) -> None:
        """Initialize StateDependentFirewall."""
        super().__init__()
        self.default_action: Optional[Any] = None
        self.firewall_rule_propses: list[FirewallRuleProps] = []
        self.firewall_states: list[ModeDeclaration] = []


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
