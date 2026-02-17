"""CompuScaleRationalFormula AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 390)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_ComputationMethod.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_scale_contents import (
    CompuScaleContents,
)
from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_rational_coeffs import (
    CompuRationalCoeffs,
)


class CompuScaleRationalFormula(CompuScaleContents):
    """AUTOSAR CompuScaleRationalFormula."""

    def __init__(self) -> None:
        """Initialize CompuScaleRationalFormula."""
        super().__init__()
        self.compu_rational_coeffs: Optional[CompuRationalCoeffs] = None


class CompuScaleRationalFormulaBuilder:
    """Builder for CompuScaleRationalFormula."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CompuScaleRationalFormula = CompuScaleRationalFormula()

    def build(self) -> CompuScaleRationalFormula:
        """Build and return CompuScaleRationalFormula object.

        Returns:
            CompuScaleRationalFormula instance
        """
        # TODO: Add validation
        return self._obj
