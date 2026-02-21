"""RuleBasedAxisCont AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 464)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
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
    unit_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize RuleBasedAxisCont."""
        super().__init__()
        self.category: Optional[CalprmAxisCategoryEnum] = None
        self.rule_based: Optional[Any] = None
        self.sw_arraysize_ref: Optional[ARRef] = None
        self.sw_axis_index: Optional[AxisIndexType] = None
        self.unit_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize RuleBasedAxisCont to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # Serialize category
        if self.category is not None:
            serialized = SerializationHelper.serialize_item(self.category, "CalprmAxisCategoryEnum")
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

        # Serialize rule_based
        if self.rule_based is not None:
            serialized = SerializationHelper.serialize_item(self.rule_based, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RULE-BASED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_arraysize_ref
        if self.sw_arraysize_ref is not None:
            serialized = SerializationHelper.serialize_item(self.sw_arraysize_ref, "ValueList")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-ARRAYSIZE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_axis_index
        if self.sw_axis_index is not None:
            serialized = SerializationHelper.serialize_item(self.sw_axis_index, "AxisIndexType")
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

        # Serialize unit_ref
        if self.unit_ref is not None:
            serialized = SerializationHelper.serialize_item(self.unit_ref, "Unit")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UNIT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

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
        child = SerializationHelper.find_child_element(element, "CATEGORY")
        if child is not None:
            category_value = CalprmAxisCategoryEnum.deserialize(child)
            obj.category = category_value

        # Parse rule_based
        child = SerializationHelper.find_child_element(element, "RULE-BASED")
        if child is not None:
            rule_based_value = child.text
            obj.rule_based = rule_based_value

        # Parse sw_arraysize_ref
        child = SerializationHelper.find_child_element(element, "SW-ARRAYSIZE-REF")
        if child is not None:
            sw_arraysize_ref_value = ARRef.deserialize(child)
            obj.sw_arraysize_ref = sw_arraysize_ref_value

        # Parse sw_axis_index
        child = SerializationHelper.find_child_element(element, "SW-AXIS-INDEX")
        if child is not None:
            sw_axis_index_value = child.text
            obj.sw_axis_index = sw_axis_index_value

        # Parse unit_ref
        child = SerializationHelper.find_child_element(element, "UNIT-REF")
        if child is not None:
            unit_ref_value = ARRef.deserialize(child)
            obj.unit_ref = unit_ref_value

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
