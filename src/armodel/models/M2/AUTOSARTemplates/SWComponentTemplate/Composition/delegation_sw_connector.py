"""DelegationSwConnector AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 80)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2016)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Composition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.sw_connector import (
    SwConnector,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)


class DelegationSwConnector(SwConnector):
    """AUTOSAR DelegationSwConnector."""

    inner_port_instance_ref: Optional[PortPrototype]
    outer_port: Optional[PortPrototype]
    def __init__(self) -> None:
        """Initialize DelegationSwConnector."""
        super().__init__()
        self.inner_port_instance_ref: Optional[PortPrototype] = None
        self.outer_port: Optional[PortPrototype] = None


class DelegationSwConnectorBuilder:
    """Builder for DelegationSwConnector."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DelegationSwConnector = DelegationSwConnector()

    def build(self) -> DelegationSwConnector:
        """Build and return DelegationSwConnector object.

        Returns:
            DelegationSwConnector instance
        """
        # TODO: Add validation
        return self._obj
