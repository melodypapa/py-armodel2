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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_rational_coeffs import (
    CompuRationalCoeffs,
)


class CompuScaleRationalFormula(CompuScaleContents):
    """AUTOSAR CompuScaleRationalFormula."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    compu_rational_coeffs: Optional[CompuRationalCoeffs]
    def __init__(self) -> None:
        """Initialize CompuScaleRationalFormula."""
        super().__init__()
        self.compu_rational_coeffs: Optional[CompuRationalCoeffs] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "CompuScaleRationalFormula":
        """Deserialize XML element to CompuScaleRationalFormula object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CompuScaleRationalFormula object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse compu_rational_coeffs
        child = ARObject._find_child_element(element, "COMPU-RATIONAL-COEFFS")
        if child is not None:
            compu_rational_coeffs_value = ARObject._deserialize_by_tag(child, "CompuRationalCoeffs")
            obj.compu_rational_coeffs = compu_rational_coeffs_value

        return obj



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
