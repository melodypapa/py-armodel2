"""ClientServerInterface AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 308)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 235)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 101)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2007)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 432)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface import (
    PortInterface,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.application_error import (
    ApplicationError,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)


class ClientServerInterface(PortInterface):
    """AUTOSAR ClientServerInterface."""

    operations: list[ClientServerOperation]
    possible_errors: list[ApplicationError]
    def __init__(self) -> None:
        """Initialize ClientServerInterface."""
        super().__init__()
        self.operations: list[ClientServerOperation] = []
        self.possible_errors: list[ApplicationError] = []


class ClientServerInterfaceBuilder:
    """Builder for ClientServerInterface."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ClientServerInterface = ClientServerInterface()

    def build(self) -> ClientServerInterface:
        """Build and return ClientServerInterface object.

        Returns:
            ClientServerInterface instance
        """
        # TODO: Add validation
        return self._obj
