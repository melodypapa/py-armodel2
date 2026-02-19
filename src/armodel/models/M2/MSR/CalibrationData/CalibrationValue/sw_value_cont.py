"""SwValueCont AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 449)

JSON Source: docs/json/packages/M2_MSR_CalibrationData_CalibrationValue.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.MSR.Documentation.TextModel.SingleLanguageData.single_language_unit_names import (
    SingleLanguageUnitNames,
)
from armodel.models.M2.MSR.CalibrationData.CalibrationValue.sw_values import (
    SwValues,
)
from armodel.models.M2.MSR.AsamHdo.Units.unit import (
    Unit,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties.value_list import (
    ValueList,
)


class SwValueCont(ARObject):
    """AUTOSAR SwValueCont."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    sw_arraysize_ref: Optional[ARRef]
    sw_values_phys: Optional[SwValues]
    unit: Optional[Unit]
    unit_display: Optional[SingleLanguageUnitNames]
    def __init__(self) -> None:
        """Initialize SwValueCont."""
        super().__init__()
        self.sw_arraysize_ref: Optional[ARRef] = None
        self.sw_values_phys: Optional[SwValues] = None
        self.unit: Optional[Unit] = None
        self.unit_display: Optional[SingleLanguageUnitNames] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwValueCont":
        """Deserialize XML element to SwValueCont object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwValueCont object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse sw_arraysize_ref
        child = ARObject._find_child_element(element, "SW-ARRAYSIZE")
        if child is not None:
            sw_arraysize_ref_value = ARObject._deserialize_by_tag(child, "ValueList")
            obj.sw_arraysize_ref = sw_arraysize_ref_value

        # Parse sw_values_phys
        child = ARObject._find_child_element(element, "SW-VALUES-PHYS")
        if child is not None:
            sw_values_phys_value = ARObject._deserialize_by_tag(child, "SwValues")
            obj.sw_values_phys = sw_values_phys_value

        # Parse unit
        child = ARObject._find_child_element(element, "UNIT")
        if child is not None:
            unit_value = ARObject._deserialize_by_tag(child, "Unit")
            obj.unit = unit_value

        # Parse unit_display
        child = ARObject._find_child_element(element, "UNIT-DISPLAY")
        if child is not None:
            unit_display_value = ARObject._deserialize_by_tag(child, "SingleLanguageUnitNames")
            obj.unit_display = unit_display_value

        return obj



class SwValueContBuilder:
    """Builder for SwValueCont."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwValueCont = SwValueCont()

    def build(self) -> SwValueCont:
        """Build and return SwValueCont object.

        Returns:
            SwValueCont instance
        """
        # TODO: Add validation
        return self._obj
