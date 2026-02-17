"""EcucIntegerParamDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 60)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 187)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_parameter_def import (
    EcucParameterDef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    UnlimitedInteger,
)


class EcucIntegerParamDef(EcucParameterDef):
    """AUTOSAR EcucIntegerParamDef."""

    def __init__(self) -> None:
        """Initialize EcucIntegerParamDef."""
        super().__init__()
        self.default_value: Optional[UnlimitedInteger] = None
        self.max: Optional[UnlimitedInteger] = None
        self.min: Optional[UnlimitedInteger] = None


class EcucIntegerParamDefBuilder:
    """Builder for EcucIntegerParamDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucIntegerParamDef = EcucIntegerParamDef()

    def build(self) -> EcucIntegerParamDef:
        """Build and return EcucIntegerParamDef object.

        Returns:
            EcucIntegerParamDef instance
        """
        # TODO: Add validation
        return self._obj
