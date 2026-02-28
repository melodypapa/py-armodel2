"""SwRecordLayoutV AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 421)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_RecordLayout.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    Integer,
    NameToken,
    NameTokens,
)
from armodel2.models.M2.MSR.DataDictionary.RecordLayout import (
    AxisIndexType,
)
from armodel2.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_overview_paragraph import (
    MultiLanguageOverviewParagraph,
)
from armodel2.models.M2.MSR.AsamHdo.BaseTypes.sw_base_type import (
    SwBaseType,
)
from armodel2.models.M2.MSR.DataDictionary.Axis.sw_generic_axis_param_type import (
    SwGenericAxisParamType,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SwRecordLayoutV(ARObject):
    """AUTOSAR SwRecordLayoutV."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SW-RECORD-LAYOUT-V"


    short_label: Optional[Identifier]
    base_type_ref: Optional[ARRef]
    desc: Optional[MultiLanguageOverviewParagraph]
    sw_generic_axis_param_type_ref: Optional[ARRef]
    sw_record_layout_v_axis: Optional[AxisIndexType]
    sw_record_layout_v_fix_value: Optional[Integer]
    sw_record_layout_v_index: Optional[NameTokens]
    sw_record_layout_v_prop: Optional[NameToken]
    _DESERIALIZE_DISPATCH = {
        "SHORT-LABEL": lambda obj, elem: setattr(obj, "short_label", elem.text),
        "BASE-TYPE-REF": lambda obj, elem: setattr(obj, "base_type_ref", ARRef.deserialize(elem)),
        "DESC": lambda obj, elem: setattr(obj, "desc", MultiLanguageOverviewParagraph.deserialize(elem)),
        "SW-GENERIC-AXIS-PARAM-TYPE-REF": lambda obj, elem: setattr(obj, "sw_generic_axis_param_type_ref", ARRef.deserialize(elem)),
        "SW-RECORD-LAYOUT-V-AXIS": lambda obj, elem: setattr(obj, "sw_record_layout_v_axis", elem.text),
        "SW-RECORD-LAYOUT-V-FIX-VALUE": lambda obj, elem: setattr(obj, "sw_record_layout_v_fix_value", elem.text),
        "SW-RECORD-LAYOUT-V-INDEX": lambda obj, elem: setattr(obj, "sw_record_layout_v_index", elem.text),
        "SW-RECORD-LAYOUT-V-PROP": lambda obj, elem: setattr(obj, "sw_record_layout_v_prop", elem.text),
    }


    def __init__(self) -> None:
        """Initialize SwRecordLayoutV."""
        super().__init__()
        self.short_label: Optional[Identifier] = None
        self.base_type_ref: Optional[ARRef] = None
        self.desc: Optional[MultiLanguageOverviewParagraph] = None
        self.sw_generic_axis_param_type_ref: Optional[ARRef] = None
        self.sw_record_layout_v_axis: Optional[AxisIndexType] = None
        self.sw_record_layout_v_fix_value: Optional[Integer] = None
        self.sw_record_layout_v_index: Optional[NameTokens] = None
        self.sw_record_layout_v_prop: Optional[NameToken] = None

    def serialize(self) -> ET.Element:
        """Serialize SwRecordLayoutV to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwRecordLayoutV, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize short_label
        if self.short_label is not None:
            serialized = SerializationHelper.serialize_item(self.short_label, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHORT-LABEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize base_type_ref
        if self.base_type_ref is not None:
            serialized = SerializationHelper.serialize_item(self.base_type_ref, "SwBaseType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BASE-TYPE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize desc
        if self.desc is not None:
            serialized = SerializationHelper.serialize_item(self.desc, "MultiLanguageOverviewParagraph")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DESC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_generic_axis_param_type_ref
        if self.sw_generic_axis_param_type_ref is not None:
            serialized = SerializationHelper.serialize_item(self.sw_generic_axis_param_type_ref, "SwGenericAxisParamType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-GENERIC-AXIS-PARAM-TYPE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_record_layout_v_axis
        if self.sw_record_layout_v_axis is not None:
            serialized = SerializationHelper.serialize_item(self.sw_record_layout_v_axis, "AxisIndexType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-RECORD-LAYOUT-V-AXIS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_record_layout_v_fix_value
        if self.sw_record_layout_v_fix_value is not None:
            serialized = SerializationHelper.serialize_item(self.sw_record_layout_v_fix_value, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-RECORD-LAYOUT-V-FIX-VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_record_layout_v_index
        if self.sw_record_layout_v_index is not None:
            serialized = SerializationHelper.serialize_item(self.sw_record_layout_v_index, "NameTokens")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-RECORD-LAYOUT-V-INDEX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_record_layout_v_prop
        if self.sw_record_layout_v_prop is not None:
            serialized = SerializationHelper.serialize_item(self.sw_record_layout_v_prop, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-RECORD-LAYOUT-V-PROP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwRecordLayoutV":
        """Deserialize XML element to SwRecordLayoutV object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwRecordLayoutV object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwRecordLayoutV, cls).deserialize(element)

        # Parse short_label
        child = SerializationHelper.find_child_element(element, "SHORT-LABEL")
        if child is not None:
            short_label_value = SerializationHelper.deserialize_by_tag(child, "Identifier")
            obj.short_label = short_label_value

        # Parse base_type_ref
        child = SerializationHelper.find_child_element(element, "BASE-TYPE-REF")
        if child is not None:
            base_type_ref_value = ARRef.deserialize(child)
            obj.base_type_ref = base_type_ref_value

        # Parse desc
        child = SerializationHelper.find_child_element(element, "DESC")
        if child is not None:
            desc_value = SerializationHelper.deserialize_by_tag(child, "MultiLanguageOverviewParagraph")
            obj.desc = desc_value

        # Parse sw_generic_axis_param_type_ref
        child = SerializationHelper.find_child_element(element, "SW-GENERIC-AXIS-PARAM-TYPE-REF")
        if child is not None:
            sw_generic_axis_param_type_ref_value = ARRef.deserialize(child)
            obj.sw_generic_axis_param_type_ref = sw_generic_axis_param_type_ref_value

        # Parse sw_record_layout_v_axis
        child = SerializationHelper.find_child_element(element, "SW-RECORD-LAYOUT-V-AXIS")
        if child is not None:
            sw_record_layout_v_axis_value = child.text
            obj.sw_record_layout_v_axis = sw_record_layout_v_axis_value

        # Parse sw_record_layout_v_fix_value
        child = SerializationHelper.find_child_element(element, "SW-RECORD-LAYOUT-V-FIX-VALUE")
        if child is not None:
            sw_record_layout_v_fix_value_value = child.text
            obj.sw_record_layout_v_fix_value = sw_record_layout_v_fix_value_value

        # Parse sw_record_layout_v_index
        child = SerializationHelper.find_child_element(element, "SW-RECORD-LAYOUT-V-INDEX")
        if child is not None:
            sw_record_layout_v_index_value = child.text
            obj.sw_record_layout_v_index = sw_record_layout_v_index_value

        # Parse sw_record_layout_v_prop
        child = SerializationHelper.find_child_element(element, "SW-RECORD-LAYOUT-V-PROP")
        if child is not None:
            sw_record_layout_v_prop_value = child.text
            obj.sw_record_layout_v_prop = sw_record_layout_v_prop_value

        return obj



class SwRecordLayoutVBuilder(BuilderBase):
    """Builder for SwRecordLayoutV with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SwRecordLayoutV = SwRecordLayoutV()


    def with_short_label(self, value: Optional[Identifier]) -> "SwRecordLayoutVBuilder":
        """Set short_label attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.short_label = value
        return self

    def with_base_type(self, value: Optional[SwBaseType]) -> "SwRecordLayoutVBuilder":
        """Set base_type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.base_type = value
        return self

    def with_desc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "SwRecordLayoutVBuilder":
        """Set desc attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.desc = value
        return self

    def with_sw_generic_axis_param_type(self, value: Optional[SwGenericAxisParamType]) -> "SwRecordLayoutVBuilder":
        """Set sw_generic_axis_param_type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_generic_axis_param_type = value
        return self

    def with_sw_record_layout_v_axis(self, value: Optional[AxisIndexType]) -> "SwRecordLayoutVBuilder":
        """Set sw_record_layout_v_axis attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_record_layout_v_axis = value
        return self

    def with_sw_record_layout_v_fix_value(self, value: Optional[Integer]) -> "SwRecordLayoutVBuilder":
        """Set sw_record_layout_v_fix_value attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_record_layout_v_fix_value = value
        return self

    def with_sw_record_layout_v_index(self, value: Optional[NameTokens]) -> "SwRecordLayoutVBuilder":
        """Set sw_record_layout_v_index attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_record_layout_v_index = value
        return self

    def with_sw_record_layout_v_prop(self, value: Optional[NameToken]) -> "SwRecordLayoutVBuilder":
        """Set sw_record_layout_v_prop attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_record_layout_v_prop = value
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


    def build(self) -> SwRecordLayoutV:
        """Build and return the SwRecordLayoutV instance with validation."""
        self._validate_instance()
        pass
        return self._obj