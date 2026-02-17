"""EcucEnumerationLiteralDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 67)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class EcucEnumerationLiteralDef(Identifiable):
    """AUTOSAR EcucEnumerationLiteralDef."""

    def __init__(self) -> None:
        """Initialize EcucEnumerationLiteralDef."""
        super().__init__()
        self.ecuc_cond: Optional[Any] = None
        self.origin: Optional[String] = None


class EcucEnumerationLiteralDefBuilder:
    """Builder for EcucEnumerationLiteralDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucEnumerationLiteralDef = EcucEnumerationLiteralDef()

    def build(self) -> EcucEnumerationLiteralDef:
        """Build and return EcucEnumerationLiteralDef object.

        Returns:
            EcucEnumerationLiteralDef instance
        """
        # TODO: Add validation
        return self._obj
