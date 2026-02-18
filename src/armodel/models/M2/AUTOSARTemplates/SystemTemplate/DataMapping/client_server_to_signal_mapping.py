"""ClientServerToSignalMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 242)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DataMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.data_mapping import (
    DataMapping,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.system_signal import (
    SystemSignal,
)


class ClientServerToSignalMapping(DataMapping):
    """AUTOSAR ClientServerToSignalMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    call_signal: Optional[SystemSignal]
    client_server: Optional[ClientServerOperation]
    return_signal: Optional[SystemSignal]
    def __init__(self) -> None:
        """Initialize ClientServerToSignalMapping."""
        super().__init__()
        self.call_signal: Optional[SystemSignal] = None
        self.client_server: Optional[ClientServerOperation] = None
        self.return_signal: Optional[SystemSignal] = None


class ClientServerToSignalMappingBuilder:
    """Builder for ClientServerToSignalMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ClientServerToSignalMapping = ClientServerToSignalMapping()

    def build(self) -> ClientServerToSignalMapping:
        """Build and return ClientServerToSignalMapping object.

        Returns:
            ClientServerToSignalMapping instance
        """
        # TODO: Add validation
        return self._obj
