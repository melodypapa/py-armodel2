"""SwAxisCont AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 457)

JSON Source: docs/json/packages/M2_MSR_CalibrationData_CalibrationValue.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.MSR.DataDictionary.CalibrationParameter import (
    CalprmAxisCategoryEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
    VerbatimString,
)
from armodel2.models.M2.MSR.DataDictionary.RecordLayout import (
    AxisIndexType,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Constants.numerical_or_text import (
    NumericalOrText,
)
from armodel2.models.M2.MSR.Documentation.TextModel.SingleLanguageData.single_language_unit_names import (
    SingleLanguageUnitNames,
)
from armodel2.models.M2.MSR.AsamHdo.Units.unit import (
    Unit,
)
from armodel2.models.M2.MSR.CalibrationData.CalibrationValue.value_group import (
    ValueGroup,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SwAxisCont(ARObject):
    """AUTOSAR SwAxisCont."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SW-AXIS-CONT"


    category: Optional[CalprmAxisCategoryEnum]
    v: Optional[Numerical]
    sw_axis_index: Optional[AxisIndexType]
    vf: Optional[Numerical]
    vg: Optional[ValueGroup]
    vt: Optional[VerbatimString]
    vtf: Optional[NumericalOrText]
    unit_ref: Optional[ARRef]
    unit_display: Optional[SingleLanguageUnitNames]
    _DESERIALIZE_DISPATCH = {
        "CATEGORY": lambda obj, elem: setattr(obj, "category", CalprmAxisCategoryEnum.deserialize(elem)),
        "V": lambda obj, elem: setattr(obj, "v", SerializationHelper.deserialize_by_tag(elem, "Numerical")),
        "SW-AXIS-INDEX": lambda obj, elem: setattr(obj, "sw_axis_index", SerializationHelper.deserialize_by_tag(elem, "AxisIndexType")),
        "VF": lambda obj, elem: setattr(obj, "vf", SerializationHelper.deserialize_by_tag(elem, "Numerical")),
        "VG": lambda obj, elem: setattr(obj, "vg", SerializationHelper.deserialize_by_tag(elem, "ValueGroup")),
        "VT": lambda obj, elem: setattr(obj, "vt", SerializationHelper.deserialize_by_tag(elem, "VerbatimString")),
        "VTF": lambda obj, elem: setattr(obj, "vtf", SerializationHelper.deserialize_by_tag(elem, "NumericalOrText")),
        "UNIT-REF": lambda obj, elem: setattr(obj, "unit_ref", ARRef.deserialize(elem)),
        "UNIT-DISPLAY": lambda obj, elem: setattr(obj, "unit_display", SerializationHelper.deserialize_by_tag(elem, "SingleLanguageUnitNames")),
    }


    def __init__(self) -> None:
        """Initialize SwAxisCont."""
        super().__init__()
        self.category: Optional[CalprmAxisCategoryEnum] = None
        self.v: Optional[Numerical] = None
        self.sw_axis_index: Optional[AxisIndexType] = None
        self.vf: Optional[Numerical] = None
        self.vg: Optional[ValueGroup] = None
        self.vt: Optional[VerbatimString] = None
        self.vtf: Optional[NumericalOrText] = None
        self.unit_ref: Optional[ARRef] = None
        self.unit_display: Optional[SingleLanguageUnitNames] = None

    def serialize(self) -> ET.Element:
        """Serialize SwAxisCont to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwAxisCont, self).serialize()

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

        # Serialize vf
        if self.vf is not None:
            serialized = SerializationHelper.serialize_item(self.vf, "Numerical")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize vg
        if self.vg is not None:
            serialized = SerializationHelper.serialize_item(self.vg, "ValueGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VG")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize vt
        if self.vt is not None:
            serialized = SerializationHelper.serialize_item(self.vt, "VerbatimString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize vtf
        if self.vtf is not None:
            serialized = SerializationHelper.serialize_item(self.vtf, "NumericalOrText")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VTF")
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

        # Serialize unit_display
        if self.unit_display is not None:
            serialized = SerializationHelper.serialize_item(self.unit_display, "SingleLanguageUnitNames")
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
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwAxisCont, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CATEGORY":
                setattr(obj, "category", CalprmAxisCategoryEnum.deserialize(child))
            elif tag == "V":
                setattr(obj, "v", SerializationHelper.deserialize_by_tag(child, "Numerical"))
            elif tag == "SW-AXIS-INDEX":
                setattr(obj, "sw_axis_index", SerializationHelper.deserialize_by_tag(child, "AxisIndexType"))
            elif tag == "VF":
                setattr(obj, "vf", SerializationHelper.deserialize_by_tag(child, "Numerical"))
            elif tag == "VG":
                setattr(obj, "vg", SerializationHelper.deserialize_by_tag(child, "ValueGroup"))
            elif tag == "VT":
                setattr(obj, "vt", SerializationHelper.deserialize_by_tag(child, "VerbatimString"))
            elif tag == "VTF":
                setattr(obj, "vtf", SerializationHelper.deserialize_by_tag(child, "NumericalOrText"))
            elif tag == "UNIT-REF":
                setattr(obj, "unit_ref", ARRef.deserialize(child))
            elif tag == "UNIT-DISPLAY":
                setattr(obj, "unit_display", SerializationHelper.deserialize_by_tag(child, "SingleLanguageUnitNames"))

        return obj



class SwAxisContBuilder(BuilderBase):
    """Builder for SwAxisCont with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SwAxisCont = SwAxisCont()


    def with_category(self, value: Optional[CalprmAxisCategoryEnum]) -> "SwAxisContBuilder":
        """Set category attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.category = value
        return self

    def with_v(self, value: Optional[Numerical]) -> "SwAxisContBuilder":
        """Set v attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.v = value
        return self

    def with_sw_axis_index(self, value: Optional[AxisIndexType]) -> "SwAxisContBuilder":
        """Set sw_axis_index attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_axis_index = value
        return self

    def with_vf(self, value: Optional[Numerical]) -> "SwAxisContBuilder":
        """Set vf attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.vf = value
        return self

    def with_vg(self, value: Optional[ValueGroup]) -> "SwAxisContBuilder":
        """Set vg attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.vg = value
        return self

    def with_vt(self, value: Optional[VerbatimString]) -> "SwAxisContBuilder":
        """Set vt attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.vt = value
        return self

    def with_vtf(self, value: Optional[NumericalOrText]) -> "SwAxisContBuilder":
        """Set vtf attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.vtf = value
        return self

    def with_unit(self, value: Optional[Unit]) -> "SwAxisContBuilder":
        """Set unit attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.unit = value
        return self

    def with_unit_display(self, value: Optional[SingleLanguageUnitNames]) -> "SwAxisContBuilder":
        """Set unit_display attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.unit_display = value
        return self




    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Get type hints for the class
        try:
            type_hints_dict = get_type_hints(type(self._obj))
        except Exception:
            # Cannot resolve type hints (e.g., forward references), skip validation
            return

        for attr_name, attr_type in type_hints_dict.items():
            if attr_name.startswith("_"):
                continue

            value = getattr(self._obj, attr_name)

            # Check required fields (not Optional)
            if value is None and not self._is_optional_type(attr_type):
                if mode == BuilderValidationMode.STRICT:
                    raise ValueError(
                        f"Required attribute '{attr_name}' is None"
                    )
                elif mode == BuilderValidationMode.LENIENT:
                    import warnings
                    warnings.warn(
                        f"Required attribute '{attr_name}' is None",
                        UserWarning
                    )

    @staticmethod
    def _is_optional_type(type_hint: Any) -> bool:
        """Check if a type hint is Optional.

        Args:
            type_hint: Type hint to check

        Returns:
            True if type is Optional, False otherwise
        """
        origin = getattr(type_hint, "__origin__", None)
        return origin is Union

    @staticmethod
    def _get_expected_type(type_hint: Any) -> type:
        """Extract expected type from type hint.

        Args:
            type_hint: Type hint to extract from

        Returns:
            Expected type
        """
        if isinstance(type_hint, str):
            return object
        origin = getattr(type_hint, "__origin__", None)
        if origin is Union:
            args = getattr(type_hint, "__args__", [])
            for arg in args:
                if arg is not type(None):
                    return arg
        elif origin is list:
            args = getattr(type_hint, "__args__", [object])
            return args[0] if args else object
        return type_hint if isinstance(type_hint, type) else object


    def build(self) -> SwAxisCont:
        """Build and return the SwAxisCont instance with validation."""
        self._validate_instance()
        pass
        return self._obj