"""ParameterProvideComSpec AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 192)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.p_port_com_spec import (
    PPortComSpec,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.parameter_data_prototype import (
    ParameterDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
    ValueSpecification,
)


class ParameterProvideComSpec(PPortComSpec):
    """AUTOSAR ParameterProvideComSpec."""

    def __init__(self) -> None:
        """Initialize ParameterProvideComSpec."""
        super().__init__()
        self.init_value: Optional[ValueSpecification] = None
        self.parameter: Optional[ParameterDataPrototype] = None


class ParameterProvideComSpecBuilder:
    """Builder for ParameterProvideComSpec."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ParameterProvideComSpec = ParameterProvideComSpec()

    def build(self) -> ParameterProvideComSpec:
        """Build and return ParameterProvideComSpec object.

        Returns:
            ParameterProvideComSpec instance
        """
        # TODO: Add validation
        return self._obj
