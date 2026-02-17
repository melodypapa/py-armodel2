"""CompuRationalCoeffs AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 389)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_ComputationMethod.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_nominator_denominator import (
    CompuNominatorDenominator,
)


class CompuRationalCoeffs(ARObject):
    """AUTOSAR CompuRationalCoeffs."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "compu_denominator": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CompuNominatorDenominator,
        ),  # compuDenominator
        "compu": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CompuNominatorDenominator,
        ),  # compu
    }

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
