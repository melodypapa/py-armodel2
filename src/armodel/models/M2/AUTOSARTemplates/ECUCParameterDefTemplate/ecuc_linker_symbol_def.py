"""EcucLinkerSymbolDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 65)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class EcucLinkerSymbolDef(ARObject):
    """AUTOSAR EcucLinkerSymbolDef."""

    def __init__(self) -> None:
        """Initialize EcucLinkerSymbolDef."""
        super().__init__()


class EcucLinkerSymbolDefBuilder:
    """Builder for EcucLinkerSymbolDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucLinkerSymbolDef = EcucLinkerSymbolDef()

    def build(self) -> EcucLinkerSymbolDef:
        """Build and return EcucLinkerSymbolDef object.

        Returns:
            EcucLinkerSymbolDef instance
        """
        # TODO: Add validation
        return self._obj
