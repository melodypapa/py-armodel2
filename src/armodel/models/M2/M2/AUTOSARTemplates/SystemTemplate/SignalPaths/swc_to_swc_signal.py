"""SwcToSwcSignal AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 253)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SignalPaths.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class SwcToSwcSignal(ARObject):
    """AUTOSAR SwcToSwcSignal."""

    def __init__(self) -> None:
        """Initialize SwcToSwcSignal."""
        super().__init__()
        self.data_elements: list[VariableDataPrototype] = []


class SwcToSwcSignalBuilder:
    """Builder for SwcToSwcSignal."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwcToSwcSignal = SwcToSwcSignal()

    def build(self) -> SwcToSwcSignal:
        """Build and return SwcToSwcSignal object.

        Returns:
            SwcToSwcSignal instance
        """
        # TODO: Add validation
        return self._obj
