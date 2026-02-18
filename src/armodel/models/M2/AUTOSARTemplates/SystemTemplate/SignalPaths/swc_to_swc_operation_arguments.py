"""SwcToSwcOperationArguments AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 253)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SignalPaths.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)


class SwcToSwcOperationArguments(ARObject):
    """AUTOSAR SwcToSwcOperationArguments."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    direction: Optional[Any]
    operations: list[ClientServerOperation]
    def __init__(self) -> None:
        """Initialize SwcToSwcOperationArguments."""
        super().__init__()
        self.direction: Optional[Any] = None
        self.operations: list[ClientServerOperation] = []


class SwcToSwcOperationArgumentsBuilder:
    """Builder for SwcToSwcOperationArguments."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwcToSwcOperationArguments = SwcToSwcOperationArguments()

    def build(self) -> SwcToSwcOperationArguments:
        """Build and return SwcToSwcOperationArguments object.

        Returns:
            SwcToSwcOperationArguments instance
        """
        # TODO: Add validation
        return self._obj
