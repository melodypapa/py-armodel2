"""RuleBasedAxisCont AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 464)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.MSR.DataDictionary.CalibrationParameter import (
    CalprmAxisCategoryEnum,
)
from armodel.models.M2.MSR.DataDictionary.RecordLayout import (
    AxisIndexType,
)
from armodel.models.M2.MSR.AsamHdo.Units.unit import (
    Unit,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties.value_list import (
    ValueList,
)


class RuleBasedAxisCont(ARObject):
    """AUTOSAR RuleBasedAxisCont."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    category: Optional[CalprmAxisCategoryEnum]
    rule_based: Optional[Any]
    sw_arraysize_ref: Optional[ARRef]
    sw_axis_index: Optional[AxisIndexType]
    unit: Optional[Unit]
    def __init__(self) -> None:
        """Initialize RuleBasedAxisCont."""
        super().__init__()
        self.category: Optional[CalprmAxisCategoryEnum] = None
        self.rule_based: Optional[Any] = None
        self.sw_arraysize_ref: Optional[ARRef] = None
        self.sw_axis_index: Optional[AxisIndexType] = None
        self.unit: Optional[Unit] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "RuleBasedAxisCont":
        """Deserialize XML element to RuleBasedAxisCont object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RuleBasedAxisCont object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse category
        child = ARObject._find_child_element(element, "CATEGORY")
        if child is not None:
            category_value = child.text
            obj.category = category_value

        # Parse rule_based
        child = ARObject._find_child_element(element, "RULE-BASED")
        if child is not None:
            rule_based_value = child.text
            obj.rule_based = rule_based_value

        # Parse sw_arraysize_ref
        child = ARObject._find_child_element(element, "SW-ARRAYSIZE")
        if child is not None:
            sw_arraysize_ref_value = ARObject._deserialize_by_tag(child, "ValueList")
            obj.sw_arraysize_ref = sw_arraysize_ref_value

        # Parse sw_axis_index
        child = ARObject._find_child_element(element, "SW-AXIS-INDEX")
        if child is not None:
            sw_axis_index_value = child.text
            obj.sw_axis_index = sw_axis_index_value

        # Parse unit
        child = ARObject._find_child_element(element, "UNIT")
        if child is not None:
            unit_value = ARObject._deserialize_by_tag(child, "Unit")
            obj.unit = unit_value

        return obj



class RuleBasedAxisContBuilder:
    """Builder for RuleBasedAxisCont."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RuleBasedAxisCont = RuleBasedAxisCont()

    def build(self) -> RuleBasedAxisCont:
        """Build and return RuleBasedAxisCont object.

        Returns:
            RuleBasedAxisCont instance
        """
        # TODO: Add validation
        return self._obj
