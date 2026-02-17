"""ClientComSpec AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 187)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.r_port_com_spec import (
    RPortComSpec,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)


class ClientComSpec(RPortComSpec):
    """AUTOSAR ClientComSpec."""

    end_to_end_call: Optional[TimeValue]
    operation: Optional[ClientServerOperation]
    transformation_coms: list[Any]
    def __init__(self) -> None:
        """Initialize ClientComSpec."""
        super().__init__()
        self.end_to_end_call: Optional[TimeValue] = None
        self.operation: Optional[ClientServerOperation] = None
        self.transformation_coms: list[Any] = []


class ClientComSpecBuilder:
    """Builder for ClientComSpec."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ClientComSpec = ClientComSpec()

    def build(self) -> ClientComSpec:
        """Build and return ClientComSpec object.

        Returns:
            ClientComSpec instance
        """
        # TODO: Add validation
        return self._obj
