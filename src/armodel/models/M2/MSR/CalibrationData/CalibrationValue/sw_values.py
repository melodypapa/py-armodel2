"""SwValues AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 458)

JSON Source: docs/json/packages/M2_MSR_CalibrationData_CalibrationValue.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
    VerbatimString,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.numerical_or_text import (
    NumericalOrText,
)

if TYPE_CHECKING:
    from armodel.models.M2.MSR.CalibrationData.CalibrationValue.value_group import (
        ValueGroup,
    )



class SwValues(ARObject):
    """AUTOSAR SwValues."""

    v: Optional[Numerical]
    vf: Optional[Numerical]
    vg: Optional[ValueGroup]
    vt: Optional[VerbatimString]
    vtf: Optional[NumericalOrText]
    def __init__(self) -> None:
        """Initialize SwValues."""
        super().__init__()
        self.v: Optional[Numerical] = None
        self.vf: Optional[Numerical] = None
        self.vg: Optional[ValueGroup] = None
        self.vt: Optional[VerbatimString] = None
        self.vtf: Optional[NumericalOrText] = None


class SwValuesBuilder:
    """Builder for SwValues."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwValues = SwValues()

    def build(self) -> SwValues:
        """Build and return SwValues object.

        Returns:
            SwValues instance
        """
        # TODO: Add validation
        return self._obj
