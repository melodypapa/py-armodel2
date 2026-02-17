"""SwValueCont AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 449)

JSON Source: docs/json/packages/M2_MSR_CalibrationData_CalibrationValue.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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

    sw_arraysize: Optional[ValueList]
    sw_values_phys: Optional[SwValues]
    unit: Optional[Unit]
    unit_display: Optional[SingleLanguageUnitNames]
    def __init__(self) -> None:
        """Initialize SwValueCont."""
        super().__init__()
        self.sw_arraysize: Optional[ValueList] = None
        self.sw_values_phys: Optional[SwValues] = None
        self.unit: Optional[Unit] = None
        self.unit_display: Optional[SingleLanguageUnitNames] = None


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
