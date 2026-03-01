"""SwComponentDocumentation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 337)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 697)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 465)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SoftwareComponentDocumentation.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.MSR.Documentation.Chapters.chapter import (
    Chapter,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SwComponentDocumentation(ARObject):
    """AUTOSAR SwComponentDocumentation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SW-COMPONENT-DOCUMENTATION"


    chapters: list[Chapter]
    sw_calibration: Optional[Chapter]
    sw_carb_doc: Optional[Chapter]
    sw_diagnostics: Optional[Chapter]
    sw_feature_def: Optional[Chapter]
    sw_feature_desc: Optional[Chapter]
    sw_maintenance: Optional[Chapter]
    sw_test_desc: Optional[Chapter]
    _DESERIALIZE_DISPATCH = {
        "CHAPTERS": lambda obj, elem: obj.chapters.append(SerializationHelper.deserialize_by_tag(elem, "Chapter")),
        "SW-CALIBRATION": lambda obj, elem: setattr(obj, "sw_calibration", SerializationHelper.deserialize_by_tag(elem, "Chapter")),
        "SW-CARB-DOC": lambda obj, elem: setattr(obj, "sw_carb_doc", SerializationHelper.deserialize_by_tag(elem, "Chapter")),
        "SW-DIAGNOSTICS": lambda obj, elem: setattr(obj, "sw_diagnostics", SerializationHelper.deserialize_by_tag(elem, "Chapter")),
        "SW-FEATURE-DEF": lambda obj, elem: setattr(obj, "sw_feature_def", SerializationHelper.deserialize_by_tag(elem, "Chapter")),
        "SW-FEATURE-DESC": lambda obj, elem: setattr(obj, "sw_feature_desc", SerializationHelper.deserialize_by_tag(elem, "Chapter")),
        "SW-MAINTENANCE": lambda obj, elem: setattr(obj, "sw_maintenance", SerializationHelper.deserialize_by_tag(elem, "Chapter")),
        "SW-TEST-DESC": lambda obj, elem: setattr(obj, "sw_test_desc", SerializationHelper.deserialize_by_tag(elem, "Chapter")),
    }


    def __init__(self) -> None:
        """Initialize SwComponentDocumentation."""
        super().__init__()
        self.chapters: list[Chapter] = []
        self.sw_calibration: Optional[Chapter] = None
        self.sw_carb_doc: Optional[Chapter] = None
        self.sw_diagnostics: Optional[Chapter] = None
        self.sw_feature_def: Optional[Chapter] = None
        self.sw_feature_desc: Optional[Chapter] = None
        self.sw_maintenance: Optional[Chapter] = None
        self.sw_test_desc: Optional[Chapter] = None

    def serialize(self) -> ET.Element:
        """Serialize SwComponentDocumentation to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwComponentDocumentation, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize chapters (list to container "CHAPTERS")
        if self.chapters:
            wrapper = ET.Element("CHAPTERS")
            for item in self.chapters:
                serialized = SerializationHelper.serialize_item(item, "Chapter")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize sw_calibration
        if self.sw_calibration is not None:
            serialized = SerializationHelper.serialize_item(self.sw_calibration, "Chapter")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-CALIBRATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_carb_doc
        if self.sw_carb_doc is not None:
            serialized = SerializationHelper.serialize_item(self.sw_carb_doc, "Chapter")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-CARB-DOC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_diagnostics
        if self.sw_diagnostics is not None:
            serialized = SerializationHelper.serialize_item(self.sw_diagnostics, "Chapter")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-DIAGNOSTICS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_feature_def
        if self.sw_feature_def is not None:
            serialized = SerializationHelper.serialize_item(self.sw_feature_def, "Chapter")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-FEATURE-DEF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_feature_desc
        if self.sw_feature_desc is not None:
            serialized = SerializationHelper.serialize_item(self.sw_feature_desc, "Chapter")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-FEATURE-DESC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_maintenance
        if self.sw_maintenance is not None:
            serialized = SerializationHelper.serialize_item(self.sw_maintenance, "Chapter")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-MAINTENANCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_test_desc
        if self.sw_test_desc is not None:
            serialized = SerializationHelper.serialize_item(self.sw_test_desc, "Chapter")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-TEST-DESC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwComponentDocumentation":
        """Deserialize XML element to SwComponentDocumentation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwComponentDocumentation object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwComponentDocumentation, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "CHAPTERS":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.chapters.append(SerializationHelper.deserialize_by_tag(item_elem, "Chapter"))
            elif tag == "SW-CALIBRATION":
                setattr(obj, "sw_calibration", SerializationHelper.deserialize_by_tag(child, "Chapter"))
            elif tag == "SW-CARB-DOC":
                setattr(obj, "sw_carb_doc", SerializationHelper.deserialize_by_tag(child, "Chapter"))
            elif tag == "SW-DIAGNOSTICS":
                setattr(obj, "sw_diagnostics", SerializationHelper.deserialize_by_tag(child, "Chapter"))
            elif tag == "SW-FEATURE-DEF":
                setattr(obj, "sw_feature_def", SerializationHelper.deserialize_by_tag(child, "Chapter"))
            elif tag == "SW-FEATURE-DESC":
                setattr(obj, "sw_feature_desc", SerializationHelper.deserialize_by_tag(child, "Chapter"))
            elif tag == "SW-MAINTENANCE":
                setattr(obj, "sw_maintenance", SerializationHelper.deserialize_by_tag(child, "Chapter"))
            elif tag == "SW-TEST-DESC":
                setattr(obj, "sw_test_desc", SerializationHelper.deserialize_by_tag(child, "Chapter"))

        return obj



class SwComponentDocumentationBuilder(BuilderBase):
    """Builder for SwComponentDocumentation with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SwComponentDocumentation = SwComponentDocumentation()


    def with_chapters(self, items: list[Chapter]) -> "SwComponentDocumentationBuilder":
        """Set chapters list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.chapters = list(items) if items else []
        return self

    def with_sw_calibration(self, value: Optional[Chapter]) -> "SwComponentDocumentationBuilder":
        """Set sw_calibration attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_calibration = value
        return self

    def with_sw_carb_doc(self, value: Optional[Chapter]) -> "SwComponentDocumentationBuilder":
        """Set sw_carb_doc attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_carb_doc = value
        return self

    def with_sw_diagnostics(self, value: Optional[Chapter]) -> "SwComponentDocumentationBuilder":
        """Set sw_diagnostics attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_diagnostics = value
        return self

    def with_sw_feature_def(self, value: Optional[Chapter]) -> "SwComponentDocumentationBuilder":
        """Set sw_feature_def attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_feature_def = value
        return self

    def with_sw_feature_desc(self, value: Optional[Chapter]) -> "SwComponentDocumentationBuilder":
        """Set sw_feature_desc attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_feature_desc = value
        return self

    def with_sw_maintenance(self, value: Optional[Chapter]) -> "SwComponentDocumentationBuilder":
        """Set sw_maintenance attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_maintenance = value
        return self

    def with_sw_test_desc(self, value: Optional[Chapter]) -> "SwComponentDocumentationBuilder":
        """Set sw_test_desc attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_test_desc = value
        return self


    def add_chapter(self, item: Chapter) -> "SwComponentDocumentationBuilder":
        """Add a single item to chapters list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.chapters.append(item)
        return self

    def clear_chapters(self) -> "SwComponentDocumentationBuilder":
        """Clear all items from chapters list.

        Returns:
            self for method chaining
        """
        self._obj.chapters = []
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


    def build(self) -> SwComponentDocumentation:
        """Build and return the SwComponentDocumentation instance with validation."""
        self._validate_instance()
        pass
        return self._obj