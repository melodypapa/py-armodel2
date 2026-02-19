"""SwAxisCont AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 457)

JSON Source: docs/json/packages/M2_MSR_CalibrationData_CalibrationValue.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    category: Optional[CalprmAxisCategoryEnum]
    sw_arraysize_ref: Optional[ARRef]
    sw_axis_index: Optional[AxisIndexType]
    sw_values_phys: Optional[SwValues]
    unit: Optional[Unit]
    unit_display: Optional[SingleLanguageUnitNames]
    def __init__(self) -> None:
        """Initialize SwAxisCont."""
        super().__init__()
        self.category: Optional[CalprmAxisCategoryEnum] = None
        self.sw_arraysize_ref: Optional[ARRef] = None
        self.sw_axis_index: Optional[AxisIndexType] = None
        self.sw_values_phys: Optional[SwValues] = None
        self.unit: Optional[Unit] = None
        self.unit_display: Optional[SingleLanguageUnitNames] = None
    def serialize(self) -> ET.Element:
        """Serialize SwAxisCont to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize category
        if self.category is not None:
            serialized = ARObject._serialize_item(self.category, "CalprmAxisCategoryEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CATEGORY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_arraysize_ref
        if self.sw_arraysize_ref is not None:
            serialized = ARObject._serialize_item(self.sw_arraysize_ref, "ValueList")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-ARRAYSIZE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_axis_index
        if self.sw_axis_index is not None:
            serialized = ARObject._serialize_item(self.sw_axis_index, "AxisIndexType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-AXIS-INDEX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_values_phys
        if self.sw_values_phys is not None:
            serialized = ARObject._serialize_item(self.sw_values_phys, "SwValues")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-VALUES-PHYS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize unit
        if self.unit is not None:
            serialized = ARObject._serialize_item(self.unit, "Unit")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UNIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize unit_display
        if self.unit_display is not None:
            serialized = ARObject._serialize_item(self.unit_display, "SingleLanguageUnitNames")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UNIT-DISPLAY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwAxisCont":
        """Deserialize XML element to SwAxisCont object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwAxisCont object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse category
        child = ARObject._find_child_element(element, "CATEGORY")
        if child is not None:
            category_value = CalprmAxisCategoryEnum.deserialize(child)
            obj.category = category_value

        # Parse sw_arraysize_ref
        child = ARObject._find_child_element(element, "SW-ARRAYSIZE")
        if child is not None:
            sw_arraysize_ref_value = ARRef.deserialize(child)
            obj.sw_arraysize_ref = sw_arraysize_ref_value

        # Parse sw_axis_index
        child = ARObject._find_child_element(element, "SW-AXIS-INDEX")
        if child is not None:
            sw_axis_index_value = child.text
            obj.sw_axis_index = sw_axis_index_value

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
