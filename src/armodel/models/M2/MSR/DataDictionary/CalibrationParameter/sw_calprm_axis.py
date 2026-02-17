"""SwCalprmAxis AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 352)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_CalibrationParameter.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "category": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CalprmAxisCategoryEnum,
        ),  # category
        "display_format_string": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # displayFormatString
        "sw_axis_index": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # swAxisIndex
        "sw_calibration_access": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwCalibrationAccessEnum,
        ),  # swCalibrationAccess
        "sw_calprm_axis": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwCalprmAxisTypeProps,
        ),  # swCalprmAxis
    }

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
