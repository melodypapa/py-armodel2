"""SwRecordLayoutGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 422)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2066)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_RecordLayout.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    Integer,
    NameToken,
)
from armodel.models.M2.MSR.DataDictionary.RecordLayout import (
    AsamRecordLayoutSemantics,
    RecordLayoutIteratorPoint,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_overview_paragraph import (
    MultiLanguageOverviewParagraph,
)
from armodel.models.M2.MSR.DataDictionary.Axis.sw_generic_axis_param_type import (
    SwGenericAxisParamType,
)


class SwRecordLayoutGroup(ARObject):
    """AUTOSAR SwRecordLayoutGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    category: Optional[AsamRecordLayoutSemantics]
    desc: Optional[MultiLanguageOverviewParagraph]
    short_label: Optional[Identifier]
    sw_generic_axis_param_type_ref: Optional[ARRef]
    sw_record_layout_component: Optional[Identifier]
    sw_record_layout_group_axis: Optional[AxisIndexType ]
    sw_record_layout_group_content_type: Optional[swRecordLayoutGroupContent]
    sw_record_layout_group_index: Optional[NameToken]
    sw_record_layout_group_step: Optional[Integer]
    sw_record_layout_group_from: Optional[RecordLayoutIteratorPoint]
    sw_record_layout_group_to: Optional[RecordLayoutIteratorPoint]
    def __init__(self) -> None:
        """Initialize SwRecordLayoutGroup."""
        super().__init__()
        self.category: Optional[AsamRecordLayoutSemantics] = None
        self.desc: Optional[MultiLanguageOverviewParagraph] = None
        self.short_label: Optional[Identifier] = None
        self.sw_generic_axis_param_type_ref: Optional[ARRef] = None
        self.sw_record_layout_component: Optional[Identifier] = None
        self.sw_record_layout_group_axis: Optional[AxisIndexType ] = None
        self.sw_record_layout_group_content_type: Optional[swRecordLayoutGroupContent] = None
        self.sw_record_layout_group_index: Optional[NameToken] = None
        self.sw_record_layout_group_step: Optional[Integer] = None
        self.sw_record_layout_group_from: Optional[RecordLayoutIteratorPoint] = None
        self.sw_record_layout_group_to: Optional[RecordLayoutIteratorPoint] = None

    def serialize(self) -> ET.Element:
        """Serialize SwRecordLayoutGroup to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwRecordLayoutGroup, self).serialize()

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
            serialized = SerializationHelper.serialize_item(self.category, "AsamRecordLayoutSemantics")
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

        # Serialize sw_record_layout_component
        if self.sw_record_layout_component is not None:
            serialized = SerializationHelper.serialize_item(self.sw_record_layout_component, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-RECORD-LAYOUT-COMPONENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_record_layout_group_axis
        if self.sw_record_layout_group_axis is not None:
            serialized = SerializationHelper.serialize_item(self.sw_record_layout_group_axis, "AxisIndexType ")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-RECORD-LAYOUT-GROUP-AXIS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_record_layout_group_content_type
        if self.sw_record_layout_group_content_type is not None:
            serialized = SerializationHelper.serialize_item(self.sw_record_layout_group_content_type, "swRecordLayoutGroupContent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-RECORD-LAYOUT-GROUP-CONTENT-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_record_layout_group_index
        if self.sw_record_layout_group_index is not None:
            serialized = SerializationHelper.serialize_item(self.sw_record_layout_group_index, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-RECORD-LAYOUT-GROUP-INDEX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_record_layout_group_step
        if self.sw_record_layout_group_step is not None:
            serialized = SerializationHelper.serialize_item(self.sw_record_layout_group_step, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-RECORD-LAYOUT-GROUP-STEP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_record_layout_group_from
        if self.sw_record_layout_group_from is not None:
            serialized = SerializationHelper.serialize_item(self.sw_record_layout_group_from, "RecordLayoutIteratorPoint")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-RECORD-LAYOUT-GROUP-FROM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_record_layout_group_to
        if self.sw_record_layout_group_to is not None:
            serialized = SerializationHelper.serialize_item(self.sw_record_layout_group_to, "RecordLayoutIteratorPoint")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-RECORD-LAYOUT-GROUP-TO")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwRecordLayoutGroup":
        """Deserialize XML element to SwRecordLayoutGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwRecordLayoutGroup object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwRecordLayoutGroup, cls).deserialize(element)

        # Parse category
        child = SerializationHelper.find_child_element(element, "CATEGORY")
        if child is not None:
            category_value = child.text
            obj.category = category_value

        # Parse desc
        child = SerializationHelper.find_child_element(element, "DESC")
        if child is not None:
            desc_value = SerializationHelper.deserialize_by_tag(child, "MultiLanguageOverviewParagraph")
            obj.desc = desc_value

        # Parse short_label
        child = SerializationHelper.find_child_element(element, "SHORT-LABEL")
        if child is not None:
            short_label_value = SerializationHelper.deserialize_by_tag(child, "Identifier")
            obj.short_label = short_label_value

        # Parse sw_generic_axis_param_type_ref
        child = SerializationHelper.find_child_element(element, "SW-GENERIC-AXIS-PARAM-TYPE-REF")
        if child is not None:
            sw_generic_axis_param_type_ref_value = ARRef.deserialize(child)
            obj.sw_generic_axis_param_type_ref = sw_generic_axis_param_type_ref_value

        # Parse sw_record_layout_component
        child = SerializationHelper.find_child_element(element, "SW-RECORD-LAYOUT-COMPONENT")
        if child is not None:
            sw_record_layout_component_value = SerializationHelper.deserialize_by_tag(child, "Identifier")
            obj.sw_record_layout_component = sw_record_layout_component_value

        # Parse sw_record_layout_group_axis
        child = SerializationHelper.find_child_element(element, "SW-RECORD-LAYOUT-GROUP-AXIS")
        if child is not None:
            sw_record_layout_group_axis_value = SerializationHelper.deserialize_by_tag(child, "AxisIndexType ")
            obj.sw_record_layout_group_axis = sw_record_layout_group_axis_value

        # Parse sw_record_layout_group_content_type
        child = SerializationHelper.find_child_element(element, "SW-RECORD-LAYOUT-GROUP-CONTENT-TYPE")
        if child is not None:
            sw_record_layout_group_content_type_value = SerializationHelper.deserialize_by_tag(child, "swRecordLayoutGroupContent")
            obj.sw_record_layout_group_content_type = sw_record_layout_group_content_type_value

        # Parse sw_record_layout_group_index
        child = SerializationHelper.find_child_element(element, "SW-RECORD-LAYOUT-GROUP-INDEX")
        if child is not None:
            sw_record_layout_group_index_value = child.text
            obj.sw_record_layout_group_index = sw_record_layout_group_index_value

        # Parse sw_record_layout_group_step
        child = SerializationHelper.find_child_element(element, "SW-RECORD-LAYOUT-GROUP-STEP")
        if child is not None:
            sw_record_layout_group_step_value = child.text
            obj.sw_record_layout_group_step = sw_record_layout_group_step_value

        # Parse sw_record_layout_group_from
        child = SerializationHelper.find_child_element(element, "SW-RECORD-LAYOUT-GROUP-FROM")
        if child is not None:
            sw_record_layout_group_from_value = child.text
            obj.sw_record_layout_group_from = sw_record_layout_group_from_value

        # Parse sw_record_layout_group_to
        child = SerializationHelper.find_child_element(element, "SW-RECORD-LAYOUT-GROUP-TO")
        if child is not None:
            sw_record_layout_group_to_value = child.text
            obj.sw_record_layout_group_to = sw_record_layout_group_to_value

        return obj



class SwRecordLayoutGroupBuilder:
    """Builder for SwRecordLayoutGroup with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: SwRecordLayoutGroup = SwRecordLayoutGroup()


    def with_category(self, value: Optional[AsamRecordLayoutSemantics]) -> "SwRecordLayoutGroupBuilder":
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

    def with_desc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "SwRecordLayoutGroupBuilder":
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

    def with_short_label(self, value: Optional[Identifier]) -> "SwRecordLayoutGroupBuilder":
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

    def with_sw_generic_axis_param_type(self, value: Optional[SwGenericAxisParamType]) -> "SwRecordLayoutGroupBuilder":
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

    def with_sw_record_layout_component(self, value: Optional[Identifier]) -> "SwRecordLayoutGroupBuilder":
        """Set sw_record_layout_component attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_record_layout_component = value
        return self

    def with_sw_record_layout_group_axis(self, value: Optional[AxisIndexType ]) -> "SwRecordLayoutGroupBuilder":
        """Set sw_record_layout_group_axis attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_record_layout_group_axis = value
        return self

    def with_sw_record_layout_group_content_type(self, value: Optional[swRecordLayoutGroupContent]) -> "SwRecordLayoutGroupBuilder":
        """Set sw_record_layout_group_content_type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_record_layout_group_content_type = value
        return self

    def with_sw_record_layout_group_index(self, value: Optional[NameToken]) -> "SwRecordLayoutGroupBuilder":
        """Set sw_record_layout_group_index attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_record_layout_group_index = value
        return self

    def with_sw_record_layout_group_step(self, value: Optional[Integer]) -> "SwRecordLayoutGroupBuilder":
        """Set sw_record_layout_group_step attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_record_layout_group_step = value
        return self

    def with_sw_record_layout_group_from(self, value: Optional[RecordLayoutIteratorPoint]) -> "SwRecordLayoutGroupBuilder":
        """Set sw_record_layout_group_from attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_record_layout_group_from = value
        return self

    def with_sw_record_layout_group_to(self, value: Optional[RecordLayoutIteratorPoint]) -> "SwRecordLayoutGroupBuilder":
        """Set sw_record_layout_group_to attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_record_layout_group_to = value
        return self



    @staticmethod
    def _coerce_to_int(value: Any) -> int:
        """Coerce value to int.

        Args:
            value: Value to coerce

        Returns:
            Integer value

        Raises:
            ValueError: If value cannot be coerced to int
        """
        if isinstance(value, int):
            return value
        if isinstance(value, str) and value.isdigit():
            return int(value)
        if isinstance(value, float):
            return int(value)
        if isinstance(value, bool):
            return int(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to int: {value}")

    @staticmethod
    def _coerce_to_float(value: Any) -> float:
        """Coerce value to float.

        Args:
            value: Value to coerce

        Returns:
            Float value

        Raises:
            ValueError: If value cannot be coerced to float
        """
        if isinstance(value, float):
            return value
        if isinstance(value, int):
            return float(value)
        if isinstance(value, str):
            try:
                return float(value)
            except ValueError:
                pass
        raise ValueError(f"Cannot coerce {type(value).__name__} to float: {value}")

    @staticmethod
    def _coerce_to_bool(value: Any) -> bool:
        """Coerce value to bool.

        Args:
            value: Value to coerce

        Returns:
            Boolean value

        Raises:
            ValueError: If value cannot be coerced to bool
        """
        if isinstance(value, bool):
            return value
        if isinstance(value, int):
            return bool(value)
        if isinstance(value, str):
            if value.lower() in ("true", "1", "yes"):
                return True
            if value.lower() in ("false", "0", "no"):
                return False
        raise ValueError(f"Cannot coerce {type(value).__name__} to bool: {value}")

    @staticmethod
    def _coerce_to_str(value: Any) -> str:
        """Coerce value to str.

        Args:
            value: Value to coerce

        Returns:
            String value
        """
        return str(value)


    @staticmethod
    def _coerce_to_list(value: Any, item_type: str) -> list:
        """Coerce value to list.

        Args:
            value: Value to coerce
            item_type: Expected item type (for error messages)

        Returns:
            List value

        Raises:
            ValueError: If value cannot be coerced to list
        """
        if isinstance(value, list):
            return value
        if isinstance(value, tuple):
            return list(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to list[{item_type}]: {value}")


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel.core import GlobalSettingsManager, BuilderValidationMode

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


    def build(self) -> SwRecordLayoutGroup:
        """Build and return the SwRecordLayoutGroup instance with validation."""
        self._validate_instance()
        pass
        return self._obj