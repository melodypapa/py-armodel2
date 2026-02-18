"""DoIpRoutingActivation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 553)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DoIP.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DoIP.do_ip_logic_target_address_props import (
    DoIpLogicTargetAddressProps,
)


class DoIpRoutingActivation(Identifiable):
    """AUTOSAR DoIpRoutingActivation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    do_ip_targets: list[DoIpLogicTargetAddressProps]
    def __init__(self) -> None:
        """Initialize DoIpRoutingActivation."""
        super().__init__()
        self.do_ip_targets: list[DoIpLogicTargetAddressProps] = []


class DoIpRoutingActivationBuilder:
    """Builder for DoIpRoutingActivation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DoIpRoutingActivation = DoIpRoutingActivation()

    def build(self) -> DoIpRoutingActivation:
        """Build and return DoIpRoutingActivation object.

        Returns:
            DoIpRoutingActivation instance
        """
        # TODO: Add validation
        return self._obj
