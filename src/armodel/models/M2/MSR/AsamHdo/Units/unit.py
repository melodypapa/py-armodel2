"""Unit AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 333)
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 64)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 400)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 479)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_Units.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Float,
)
from armodel.models.M2.MSR.AsamHdo.Units.physical_dimension import (
    PhysicalDimension,
)
from armodel.models.M2.MSR.Documentation.TextModel.SingleLanguageData.single_language_unit_names import (
    SingleLanguageUnitNames,
)


class Unit(ARElement):
    """AUTOSAR Unit."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    display_name: Optional[SingleLanguageUnitNames]
    factor_si_to_unit: Optional[Float]
    offset_si_to_unit: Optional[Float]
    physical: Optional[PhysicalDimension]
    def __init__(self) -> None:
        """Initialize Unit."""
        super().__init__()
        self.display_name: Optional[SingleLanguageUnitNames] = None
        self.factor_si_to_unit: Optional[Float] = None
        self.offset_si_to_unit: Optional[Float] = None
        self.physical: Optional[PhysicalDimension] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "Unit":
        """Deserialize XML element to Unit object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Unit object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse display_name
        child = ARObject._find_child_element(element, "DISPLAY-NAME")
        if child is not None:
            display_name_value = ARObject._deserialize_by_tag(child, "SingleLanguageUnitNames")
            obj.display_name = display_name_value

        # Parse factor_si_to_unit
        child = ARObject._find_child_element(element, "FACTOR-SI-TO-UNIT")
        if child is not None:
            factor_si_to_unit_value = child.text
            obj.factor_si_to_unit = factor_si_to_unit_value

        # Parse offset_si_to_unit
        child = ARObject._find_child_element(element, "OFFSET-SI-TO-UNIT")
        if child is not None:
            offset_si_to_unit_value = child.text
            obj.offset_si_to_unit = offset_si_to_unit_value

        # Parse physical
        child = ARObject._find_child_element(element, "PHYSICAL")
        if child is not None:
            physical_value = ARObject._deserialize_by_tag(child, "PhysicalDimension")
            obj.physical = physical_value

        return obj



class UnitBuilder:
    """Builder for Unit."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Unit = Unit()

    def build(self) -> Unit:
        """Build and return Unit object.

        Returns:
            Unit instance
        """
        # TODO: Add validation
        return self._obj
