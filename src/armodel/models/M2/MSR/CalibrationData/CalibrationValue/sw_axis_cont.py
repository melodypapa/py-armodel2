"""SwAxisCont AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 457)

JSON Source: docs/json/packages/M2_MSR_CalibrationData_CalibrationValue.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.DataDictionary.CalibrationParameter import (
    CalprmAxisCategoryEnum,
)
from armodel.models.M2.MSR.DataDictionary.RecordLayout import (
    AxisIndexType,
)
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


class SwAxisCont(ARObject):
    """AUTOSAR SwAxisCont."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "category": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CalprmAxisCategoryEnum,
        ),  # category
        "sw_arraysize": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ValueList,
        ),  # swArraysize
        "sw_axis_index": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # swAxisIndex
        "sw_values_phys": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwValues,
        ),  # swValuesPhys
        "unit": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Unit,
        ),  # unit
        "unit_display": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SingleLanguageUnitNames,
        ),  # unitDisplay
    }

    def __init__(self) -> None:
        """Initialize SwAxisCont."""
        super().__init__()
        self.category: Optional[CalprmAxisCategoryEnum] = None
        self.sw_arraysize: Optional[ValueList] = None
        self.sw_axis_index: Optional[AxisIndexType] = None
        self.sw_values_phys: Optional[SwValues] = None
        self.unit: Optional[Unit] = None
        self.unit_display: Optional[SingleLanguageUnitNames] = None


class SwAxisContBuilder:
    """Builder for SwAxisCont."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwAxisCont = SwAxisCont()

    def build(self) -> SwAxisCont:
        """Build and return SwAxisCont object.

        Returns:
            SwAxisCont instance
        """
        # TODO: Add validation
        return self._obj
