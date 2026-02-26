"""Firewall module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall.state_dependent_firewall import (
        StateDependentFirewall,
    )
    from armodel2.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall.firewall_rule_props import (
        FirewallRuleProps,
    )
    from armodel2.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall.firewall_rule import (
        FirewallRule,
    )

__all__ = [
    "FirewallRule",
    "FirewallRuleProps",
    "StateDependentFirewall",
]
