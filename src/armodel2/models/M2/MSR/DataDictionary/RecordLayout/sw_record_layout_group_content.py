"""SwRecordLayoutGroupContent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 424)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_RecordLayout.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel2.serialization.decorators import atp_mixed

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.MSR.DataDictionary.RecordLayout.sw_record_layout import (
    SwRecordLayout,
)
from armodel2.models.M2.MSR.DataDictionary.RecordLayout.sw_record_layout_group import (
    SwRecordLayoutGroup,
)
from armodel2.models.M2.MSR.DataDictionary.RecordLayout.sw_record_layout_v import (
    SwRecordLayoutV,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


@atp_mixed()

class SwRecordLayoutGroupContent(ARObject):
    """AUTOSAR SwRecordLayoutGroupContent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SW-RECORD-LAYOUT-GROUP-CONTENT"


    sw_record_layout_ref: Optional[ARRef]
    sw_record_layout_group: Optional[SwRecordLayoutGroup]
    sw_record_layout_v: Optional[SwRecordLayoutV]
    _DESERIALIZE_DISPATCH = {
        "SW-RECORD-LAYOUT-REF": lambda obj, elem: setattr(obj, "sw_record_layout_ref", ARRef.deserialize(elem)),
        "SW-RECORD-LAYOUT-GROUP": lambda obj, elem: setattr(obj, "sw_record_layout_group", SwRecordLayoutGroup.deserialize(elem)),
        "SW-RECORD-LAYOUT-V": lambda obj, elem: setattr(obj, "sw_record_layout_v", SwRecordLayoutV.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize SwRecordLayoutGroupContent."""
        super().__init__()
        self.sw_record_layout_ref: Optional[ARRef] = None
        self.sw_record_layout_group: Optional[SwRecordLayoutGroup] = None
        self.sw_record_layout_v: Optional[SwRecordLayoutV] = None

    def serialize(self) -> ET.Element:
        """Serialize SwRecordLayoutGroupContent to XML element (atp_mixed - no wrapping).

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwRecordLayoutGroupContent, self).serialize()

        # Copy all attributes from parent element to current element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element to current element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element to current element
        for child in parent_elem:
            elem.append(child)

        # Serialize sw_record_layout_ref (reference)
        if self.sw_record_layout_ref is not None:
            serialized = SerializationHelper.serialize_item(self.sw_record_layout_ref, "SwRecordLayout")
            if serialized is not None:
                wrapped = ET.Element("SW-RECORD-LAYOUT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_record_layout_group (complex type)
        if self.sw_record_layout_group is not None:
            serialized = SerializationHelper.serialize_item(self.sw_record_layout_group, "SwRecordLayoutGroup")
            if serialized is not None:
                wrapped = ET.Element("SW-RECORD-LAYOUT-GROUP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_record_layout_v (complex type)
        if self.sw_record_layout_v is not None:
            serialized = SerializationHelper.serialize_item(self.sw_record_layout_v, "SwRecordLayoutV")
            if serialized is not None:
                wrapped = ET.Element("SW-RECORD-LAYOUT-V")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwRecordLayoutGroupContent":
        """Deserialize XML element to SwRecordLayoutGroupContent object (atp_mixed - no unwrapping).

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwRecordLayoutGroupContent object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwRecordLayoutGroupContent, cls).deserialize(element)

        # Parse sw_record_layout_ref
        child = SerializationHelper.find_child_element(element, "SW-RECORD-LAYOUT-REF")
        if child is not None:
            sw_record_layout_ref_value = SerializationHelper.deserialize_by_tag(child, "SwRecordLayout")
            obj.sw_record_layout_ref = sw_record_layout_ref_value

        # Parse sw_record_layout_group
        child = SerializationHelper.find_child_element(element, "SW-RECORD-LAYOUT-GROUP")
        if child is not None:
            sw_record_layout_group_value = SerializationHelper.deserialize_by_tag(child, "SwRecordLayoutGroup")
            obj.sw_record_layout_group = sw_record_layout_group_value

        # Parse sw_record_layout_v
        child = SerializationHelper.find_child_element(element, "SW-RECORD-LAYOUT-V")
        if child is not None:
            sw_record_layout_v_value = SerializationHelper.deserialize_by_tag(child, "SwRecordLayoutV")
            obj.sw_record_layout_v = sw_record_layout_v_value

        return obj



class SwRecordLayoutGroupContentBuilder(BuilderBase):
    """Builder for SwRecordLayoutGroupContent with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SwRecordLayoutGroupContent = SwRecordLayoutGroupContent()


    def with_sw_record_layout(self, value: Optional[SwRecordLayout]) -> "SwRecordLayoutGroupContentBuilder":
        """Set sw_record_layout attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_record_layout = value
        return self

    def with_sw_record_layout_group(self, value: Optional[SwRecordLayoutGroup]) -> "SwRecordLayoutGroupContentBuilder":
        """Set sw_record_layout_group attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_record_layout_group = value
        return self

    def with_sw_record_layout_v(self, value: Optional[SwRecordLayoutV]) -> "SwRecordLayoutGroupContentBuilder":
        """Set sw_record_layout_v attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_record_layout_v = value
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


    def build(self) -> SwRecordLayoutGroupContent:
        """Build and return the SwRecordLayoutGroupContent instance with validation."""
        self._validate_instance()
        pass
        return self._obj