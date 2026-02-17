"""EcucForeignReferenceDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 75)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_abstract_external_reference_def import (
    EcucAbstractExternalReferenceDef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class EcucForeignReferenceDef(EcucAbstractExternalReferenceDef):
    """AUTOSAR EcucForeignReferenceDef."""

    def __init__(self) -> None:
        """Initialize EcucForeignReferenceDef."""
        super().__init__()
        self.destination_type: Optional[String] = None


class EcucForeignReferenceDefBuilder:
    """Builder for EcucForeignReferenceDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucForeignReferenceDef = EcucForeignReferenceDef()

    def build(self) -> EcucForeignReferenceDef:
        """Build and return EcucForeignReferenceDef object.

        Returns:
            EcucForeignReferenceDef instance
        """
        # TODO: Add validation
        return self._obj
