"""CompuConstFormulaContent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 900)

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


class CompuConstFormulaContent(CompuConstContent):
    """AUTOSAR CompuConstFormulaContent."""

    vf: Numerical
    def __init__(self) -> None:
        """Initialize CompuConstFormulaContent."""
        super().__init__()
        self.vf: Numerical = None


class CompuConstFormulaContentBuilder:
    """Builder for CompuConstFormulaContent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CompuConstFormulaContent = CompuConstFormulaContent()

    def build(self) -> CompuConstFormulaContent:
        """Build and return CompuConstFormulaContent object.

        Returns:
            CompuConstFormulaContent instance
        """
        # TODO: Add validation
        return self._obj
