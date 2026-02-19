"""UnitGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 314)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 402)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_Units.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.AsamHdo.Units.unit import (
    Unit,
)


class UnitGroup(ARElement):
    """AUTOSAR UnitGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    units: list[Unit]
    def __init__(self) -> None:
        """Initialize UnitGroup."""
        super().__init__()
        self.units: list[Unit] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "UnitGroup":
        """Deserialize XML element to UnitGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized UnitGroup object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse units (list)
        obj.units = []
        for child in ARObject._find_all_child_elements(element, "UNITS"):
            units_value = ARObject._deserialize_by_tag(child, "Unit")
            obj.units.append(units_value)

        return obj



class UnitGroupBuilder:
    """Builder for UnitGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: UnitGroup = UnitGroup()

    def build(self) -> UnitGroup:
        """Build and return UnitGroup object.

        Returns:
            UnitGroup instance
        """
        # TODO: Add validation
        return self._obj
