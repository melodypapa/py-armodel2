"""CompuRationalCoeffs AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 389)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_ComputationMethod.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_nominator_denominator import (
    CompuNominatorDenominator,
)


class CompuRationalCoeffs(ARObject):
    """AUTOSAR CompuRationalCoeffs."""

    def __init__(self) -> None:
        """Initialize CompuRationalCoeffs."""
        super().__init__()
        self.compu_denominator: Optional[CompuNominatorDenominator] = None
        self.compu: Optional[CompuNominatorDenominator] = None


class CompuRationalCoeffsBuilder:
    """Builder for CompuRationalCoeffs."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CompuRationalCoeffs = CompuRationalCoeffs()

    def build(self) -> CompuRationalCoeffs:
        """Build and return CompuRationalCoeffs object.

        Returns:
            CompuRationalCoeffs instance
        """
        # TODO: Add validation
        return self._obj
