"""ParameterInterface AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 41)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2042)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.data_interface import (
    DataInterface,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.parameter_data_prototype import (
    ParameterDataPrototype,
)


class ParameterInterface(DataInterface):
    """AUTOSAR ParameterInterface."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    parameters: list[ParameterDataPrototype]
    def __init__(self) -> None:
        """Initialize ParameterInterface."""
        super().__init__()
        self.parameters: list[ParameterDataPrototype] = []


class ParameterInterfaceBuilder:
    """Builder for ParameterInterface."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ParameterInterface = ParameterInterface()

    def build(self) -> ParameterInterface:
        """Build and return ParameterInterface object.

        Returns:
            ParameterInterface instance
        """
        # TODO: Add validation
        return self._obj
