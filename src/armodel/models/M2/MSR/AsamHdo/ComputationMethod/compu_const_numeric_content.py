"""CompuConstNumericContent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 389)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_ComputationMethod.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_const_content import (
    CompuConstContent,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
)


class CompuConstNumericContent(CompuConstContent):
    """AUTOSAR CompuConstNumericContent."""

    v: Optional[Numerical]
    def __init__(self) -> None:
        """Initialize CompuConstNumericContent."""
        super().__init__()
        self.v: Optional[Numerical] = None


class CompuConstNumericContentBuilder:
    """Builder for CompuConstNumericContent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CompuConstNumericContent = CompuConstNumericContent()

    def build(self) -> CompuConstNumericContent:
        """Build and return CompuConstNumericContent object.

        Returns:
            CompuConstNumericContent instance
        """
        # TODO: Add validation
        return self._obj
