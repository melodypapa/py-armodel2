"""IPduPort AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 304)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.comm_connector_port import (
    CommConnectorPort,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    IPduSignalProcessingEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    TimeValue,
)


class IPduPort(CommConnectorPort):
    """AUTOSAR IPduPort."""

    def __init__(self) -> None:
        """Initialize IPduPort."""
        super().__init__()
        self.i_pdu_signal: Optional[IPduSignalProcessingEnum] = None
        self.rx_security: Optional[Boolean] = None
        self.timestamp_rx: Optional[TimeValue] = None
        self.use_auth_data: Optional[Boolean] = None


class IPduPortBuilder:
    """Builder for IPduPort."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IPduPort = IPduPort()

    def build(self) -> IPduPort:
        """Build and return IPduPort object.

        Returns:
            IPduPort instance
        """
        # TODO: Add validation
        return self._obj
