"""FirewallRuleProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 584)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_AdaptivePlatform_PlatformModuleDeployment_Firewall.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall.firewall_rule import (
    FirewallRule,
)


class FirewallRuleProps(ARObject):
    """AUTOSAR FirewallRuleProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    action: Optional[Any]
    matching_egresses: list[FirewallRule]
    matchings: list[FirewallRule]
    def __init__(self) -> None:
        """Initialize FirewallRuleProps."""
        super().__init__()
        self.action: Optional[Any] = None
        self.matching_egresses: list[FirewallRule] = []
        self.matchings: list[FirewallRule] = []


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
