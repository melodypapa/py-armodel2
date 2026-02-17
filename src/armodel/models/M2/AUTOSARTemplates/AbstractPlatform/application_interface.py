"""ApplicationInterface AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 28)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_AbstractPlatform.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface import (
    PortInterface,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.ApplicationDesign.PortInterface.field import (
    Field,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class ApplicationInterface(PortInterface):
    """AUTOSAR ApplicationInterface."""

    def __init__(self) -> None:
        """Initialize ApplicationInterface."""
        super().__init__()
        self.attributes: list[Field] = []
        self.commands: list[ClientServerOperation] = []
        self.indications: list[VariableDataPrototype] = []


class ApplicationInterfaceBuilder:
    """Builder for ApplicationInterface."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ApplicationInterface = ApplicationInterface()

    def build(self) -> ApplicationInterface:
        """Build and return ApplicationInterface object.

        Returns:
            ApplicationInterface instance
        """
        # TODO: Add validation
        return self._obj
