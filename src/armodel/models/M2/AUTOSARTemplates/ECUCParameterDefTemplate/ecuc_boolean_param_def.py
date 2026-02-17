"""EcucBooleanParamDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 58)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 183)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_parameter_def import (
    EcucParameterDef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class EcucBooleanParamDef(EcucParameterDef):
    """AUTOSAR EcucBooleanParamDef."""

    default_value: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize EcucBooleanParamDef."""
        super().__init__()
        self.default_value: Optional[Boolean] = None


class EcucBooleanParamDefBuilder:
    """Builder for EcucBooleanParamDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucBooleanParamDef = EcucBooleanParamDef()

    def build(self) -> EcucBooleanParamDef:
        """Build and return EcucBooleanParamDef object.

        Returns:
            EcucBooleanParamDef instance
        """
        # TODO: Add validation
        return self._obj
