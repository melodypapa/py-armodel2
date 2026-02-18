"""PhysicalDimension AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 398)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_Units.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
)


class PhysicalDimension(ARElement):
    """AUTOSAR PhysicalDimension."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    current_exp: Optional[Numerical]
    length_exp: Optional[Numerical]
    luminous: Optional[Numerical]
    mass_exp: Optional[Numerical]
    molar_amount: Optional[Numerical]
    temperature_exp: Optional[Numerical]
    time_exp: Optional[Numerical]
    def __init__(self) -> None:
        """Initialize PhysicalDimension."""
        super().__init__()
        self.current_exp: Optional[Numerical] = None
        self.length_exp: Optional[Numerical] = None
        self.luminous: Optional[Numerical] = None
        self.mass_exp: Optional[Numerical] = None
        self.molar_amount: Optional[Numerical] = None
        self.temperature_exp: Optional[Numerical] = None
        self.time_exp: Optional[Numerical] = None


class PhysicalDimensionBuilder:
    """Builder for PhysicalDimension."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PhysicalDimension = PhysicalDimension()

    def build(self) -> PhysicalDimension:
        """Build and return PhysicalDimension object.

        Returns:
            PhysicalDimension instance
        """
        # TODO: Add validation
        return self._obj
