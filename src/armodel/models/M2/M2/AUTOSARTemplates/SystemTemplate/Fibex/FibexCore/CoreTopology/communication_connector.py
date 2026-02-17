"""CommunicationConnector AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 54)
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 57)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import (
    PncGatewayTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.comm_connector_port import (
    CommConnectorPort,
)


class CommunicationConnector(Identifiable):
    """AUTOSAR CommunicationConnector."""
    """Abstract base class - do not instantiate directly."""

    def __init__(self) -> None:
        """Initialize CommunicationConnector."""
        super().__init__()
        self.comm_controller: Optional[Any] = None
        self.create_ecu: Optional[Boolean] = None
        self.dynamic_pnc_to: Optional[Boolean] = None
        self.ecu_comm_ports: list[CommConnectorPort] = []
        self.pnc_filter_arrays: list[PositiveInteger] = []
        self.pnc_gateway_type_enum: Optional[PncGatewayTypeEnum] = None


class CommunicationConnectorBuilder:
    """Builder for CommunicationConnector."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CommunicationConnector = CommunicationConnector()

    def build(self) -> CommunicationConnector:
        """Build and return CommunicationConnector object.

        Returns:
            CommunicationConnector instance
        """
        # TODO: Add validation
        return self._obj
