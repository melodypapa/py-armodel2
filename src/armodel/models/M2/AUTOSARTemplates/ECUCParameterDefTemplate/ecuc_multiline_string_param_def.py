"""EcucMultilineStringParamDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 64)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization.decorators import atp_variant

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


@atp_variant()

class EcucMultilineStringParamDef(ARObject):
    """AUTOSAR EcucMultilineStringParamDef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize EcucMultilineStringParamDef."""
        super().__init__()



class EcucMultilineStringParamDefBuilder:
    """Builder for EcucMultilineStringParamDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucMultilineStringParamDef = EcucMultilineStringParamDef()

    def build(self) -> EcucMultilineStringParamDef:
        """Build and return EcucMultilineStringParamDef object.

        Returns:
            EcucMultilineStringParamDef instance
        """
        # TODO: Add validation
        return self._obj
