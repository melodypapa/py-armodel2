"""RuleBasedAxisCont AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 464)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.MSR.DataDictionary.CalibrationParameter import (
    CalprmAxisCategoryEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
)
from armodel2.models.M2.MSR.DataDictionary.RecordLayout import (
    AxisIndexType,
)
from armodel2.models.M2.MSR.AsamHdo.Units.unit import (
    Unit,
)
from armodel2.models.M2.MSR.DataDictionary.DataDefProperties.value_list import (
    ValueList,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class RuleBasedAxisCont(ARObject):
    """AUTOSAR RuleBasedAxisCont."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "RULE-BASED-AXIS-CONT"


    category: Optional[CalprmAxisCategoryEnum]
    rule_based: Optional[Any]
    sw_arraysize_ref: Optional[ARRef]
    v: Optional[Numerical]
    vts: list[Numerical]
    sw_axis_index: Optional[AxisIndexType]
    unit_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "CATEGORY": lambda obj, elem: setattr(obj, "category", CalprmAxisCategoryEnum.deserialize(elem)),
        "RULE-BASED": lambda obj, elem: setattr(obj, "rule_based", SerializationHelper.deserialize_by_tag(elem, "any (RuleBasedValue)")),
        "SW-ARRAYSIZE-REF": lambda obj, elem: setattr(obj, "sw_arraysize_ref", ARRef.deserialize(elem)),
        "V": lambda obj, elem: setattr(obj, "v", SerializationHelper.deserialize_by_tag(elem, "Numerical")),
        "VTS": lambda obj, elem: obj.vts.append(SerializationHelper.deserialize_by_tag(elem, "Numerical")),
        "SW-AXIS-INDEX": lambda obj, elem: setattr(obj, "sw_axis_index", SerializationHelper.deserialize_by_tag(elem, "AxisIndexType")),
        "UNIT-REF": lambda obj, elem: setattr(obj, "unit_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize RuleBasedAxisCont."""
        super().__init__()
        self.category: Optional[CalprmAxisCategoryEnum] = None
        self.rule_based: Optional[Any] = None
        self.sw_arraysize_ref: Optional[ARRef] = None
        self.v: Optional[Numerical] = None
        self.vts: list[Numerical] = []
        self.sw_axis_index: Optional[AxisIndexType] = None
        self.unit_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize RuleBasedAxisCont to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RuleBasedAxisCont, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

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

        # Serialize sw_arraysize_ref (atp_mixed - append children directly)
        if self.sw_arraysize_ref is not None:
            serialized = SerializationHelper.serialize_item(self.sw_arraysize_ref, "ValueList")
            if serialized is not None:
                # atpMixed type: append children directly without wrapper
                if hasattr(serialized, 'attrib'):
                    elem.attrib.update(serialized.attrib)
                # Only copy text if it's a non-empty string (not None or whitespace)
                if serialized.text and serialized.text.strip():
                    elem.text = serialized.text
                for child in serialized:
                    elem.append(child)

        # Serialize v
        if self.v is not None:
            serialized = SerializationHelper.serialize_item(self.v, "Numerical")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("V")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize vts (list to container "VTS")
        if self.vts:
            wrapper = ET.Element("VTS")
            for item in self.vts:
                serialized = SerializationHelper.serialize_item(item, "Numerical")
                if serialized is not None:
                    child_elem = ET.Element("VT")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

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
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RuleBasedAxisCont, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CATEGORY":
                setattr(obj, "category", CalprmAxisCategoryEnum.deserialize(child))
            elif tag == "RULE-BASED":
                setattr(obj, "rule_based", SerializationHelper.deserialize_by_tag(child, "any (RuleBasedValue)"))
            elif tag == "SW-ARRAYSIZE-REF":
                setattr(obj, "sw_arraysize_ref", ARRef.deserialize(child))
            elif tag == "V":
                setattr(obj, "v", SerializationHelper.deserialize_by_tag(child, "Numerical"))
            elif tag == "VTS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.vts.append(SerializationHelper.deserialize_by_tag(item_elem, "Numerical"))
            elif tag == "SW-AXIS-INDEX":
                setattr(obj, "sw_axis_index", SerializationHelper.deserialize_by_tag(child, "AxisIndexType"))
            elif tag == "UNIT-REF":
                setattr(obj, "unit_ref", ARRef.deserialize(child))

        return obj



class RuleBasedAxisContBuilder(BuilderBase):
    """Builder for RuleBasedAxisCont with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: RuleBasedAxisCont = RuleBasedAxisCont()


    def with_category(self, value: Optional[CalprmAxisCategoryEnum]) -> "RuleBasedAxisContBuilder":
        """Set category attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'category' is required and cannot be None")
        self._obj.category = value
        return self

    def with_rule_based(self, value: Optional[Any]) -> "RuleBasedAxisContBuilder":
        """Set rule_based attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'rule_based' is required and cannot be None")
        self._obj.rule_based = value
        return self

    def with_sw_arraysize(self, value: Optional[ValueList]) -> "RuleBasedAxisContBuilder":
        """Set sw_arraysize attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'sw_arraysize' is required and cannot be None")
        self._obj.sw_arraysize = value
        return self

    def with_v(self, value: Optional[Numerical]) -> "RuleBasedAxisContBuilder":
        """Set v attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'v' is required and cannot be None")
        self._obj.v = value
        return self

    def with_vts(self, items: list[Numerical]) -> "RuleBasedAxisContBuilder":
        """Set vts list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.vts = list(items) if items else []
        return self

    def with_sw_axis_index(self, value: Optional[AxisIndexType]) -> "RuleBasedAxisContBuilder":
        """Set sw_axis_index attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'sw_axis_index' is required and cannot be None")
        self._obj.sw_axis_index = value
        return self

    def with_unit(self, value: Optional[Unit]) -> "RuleBasedAxisContBuilder":
        """Set unit attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'unit' is required and cannot be None")
        self._obj.unit = value
        return self


    def add_vt(self, item: Numerical) -> "RuleBasedAxisContBuilder":
        """Add a single item to vts list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.vts.append(item)
        return self

    def clear_vts(self) -> "RuleBasedAxisContBuilder":
        """Clear all items from vts list.

        Returns:
            self for method chaining
        """
        self._obj.vts = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "category",
        "ruleBased",
        "swArraysize",
        "swAxisIndex",
        "unit",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> RuleBasedAxisCont:
        """Build and return the RuleBasedAxisCont instance with validation."""
        self._validate_instance()
        return self._obj