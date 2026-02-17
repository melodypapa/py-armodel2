"""CompuScaleRationalFormula AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 390)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_ComputationMethod.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_scale_contents import (
    CompuScaleContents,
)
from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_rational_coeffs import (
    CompuRationalCoeffs,
)


class CompuScaleRationalFormula(CompuScaleContents):
    """AUTOSAR CompuScaleRationalFormula."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "compu_rational_coeffs": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CompuRationalCoeffs,
        ),  # compuRationalCoeffs
    }

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
