"""J1939NmNode AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 322)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 691)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_node import (
    NmNode,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import (
    J1939NmAddressConfigurationCapabilityEnum,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.j1939_node_name import (
    J1939NodeName,
)


class J1939NmNode(NmNode):
    """AUTOSAR J1939NmNode."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    address: Optional[J1939NmAddressConfigurationCapabilityEnum]
    node_name: Optional[J1939NodeName]
    def __init__(self) -> None:
        """Initialize J1939NmNode."""
        super().__init__()
        self.address: Optional[J1939NmAddressConfigurationCapabilityEnum] = None
        self.node_name: Optional[J1939NodeName] = None


class J1939NmNodeBuilder:
    """Builder for J1939NmNode."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: J1939NmNode = J1939NmNode()

    def build(self) -> J1939NmNode:
        """Build and return J1939NmNode object.

        Returns:
            J1939NmNode instance
        """
        # TODO: Add validation
        return self._obj
