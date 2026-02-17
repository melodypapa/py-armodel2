"""SwCalprmAxis AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 352)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_CalibrationParameter.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.DataDictionary.CalibrationParameter import (
    CalprmAxisCategoryEnum,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import (
    SwCalibrationAccessEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    DisplayFormatString,
)
from armodel.models.M2.MSR.DataDictionary.RecordLayout import (
    AxisIndexType,
)
from armodel.models.M2.MSR.DataDictionary.CalibrationParameter.sw_calprm_axis_type_props import (
    SwCalprmAxisTypeProps,
)


class SwCalprmAxis(ARObject):
    """AUTOSAR SwCalprmAxis."""

    category: Optional[CalprmAxisCategoryEnum]
    display_format_string: Optional[DisplayFormatString]
    sw_axis_index: Optional[AxisIndexType]
    sw_calibration_access: Optional[SwCalibrationAccessEnum]
    sw_calprm_axis: Optional[SwCalprmAxisTypeProps]
    def __init__(self) -> None:
        """Initialize SwCalprmAxis."""
        super().__init__()
        self.category: Optional[CalprmAxisCategoryEnum] = None
        self.display_format_string: Optional[DisplayFormatString] = None
        self.sw_axis_index: Optional[AxisIndexType] = None
        self.sw_calibration_access: Optional[SwCalibrationAccessEnum] = None
        self.sw_calprm_axis: Optional[SwCalprmAxisTypeProps] = None


class SwCalprmAxisBuilder:
    """Builder for SwCalprmAxis."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwCalprmAxis = SwCalprmAxis()

    def build(self) -> SwCalprmAxis:
        """Build and return SwCalprmAxis object.

        Returns:
            SwCalprmAxis instance
        """
        # TODO: Add validation
        return self._obj
