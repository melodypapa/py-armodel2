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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class FirewallRule(ARElement):
    """AUTOSAR FirewallRule."""

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
