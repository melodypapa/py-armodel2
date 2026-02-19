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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "PhysicalDimension":
        """Deserialize XML element to PhysicalDimension object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PhysicalDimension object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PhysicalDimension, cls).deserialize(element)

        # Parse current_exp
        child = ARObject._find_child_element(element, "CURRENT-EXP")
        if child is not None:
            current_exp_value = child.text
            obj.current_exp = current_exp_value

        # Parse length_exp
        child = ARObject._find_child_element(element, "LENGTH-EXP")
        if child is not None:
            length_exp_value = child.text
            obj.length_exp = length_exp_value

        # Parse luminous
        child = ARObject._find_child_element(element, "LUMINOUS")
        if child is not None:
            luminous_value = child.text
            obj.luminous = luminous_value

        # Parse mass_exp
        child = ARObject._find_child_element(element, "MASS-EXP")
        if child is not None:
            mass_exp_value = child.text
            obj.mass_exp = mass_exp_value

        # Parse molar_amount
        child = ARObject._find_child_element(element, "MOLAR-AMOUNT")
        if child is not None:
            molar_amount_value = child.text
            obj.molar_amount = molar_amount_value

        # Parse temperature_exp
        child = ARObject._find_child_element(element, "TEMPERATURE-EXP")
        if child is not None:
            temperature_exp_value = child.text
            obj.temperature_exp = temperature_exp_value

        # Parse time_exp
        child = ARObject._find_child_element(element, "TIME-EXP")
        if child is not None:
            time_exp_value = child.text
            obj.time_exp = time_exp_value

        return obj



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
