"""SubElementMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 137)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.sub_element_ref import (
    SubElementRef,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.text_table_mapping import (
    TextTableMapping,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SubElementMapping(ARObject):
    """AUTOSAR SubElementMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SUB-ELEMENT-MAPPING"


    first_element_ref: Optional[ARRef]
    second_element_ref: Optional[ARRef]
    text_table_ref: ARRef
    _DESERIALIZE_DISPATCH = {
        "FIRST-ELEMENT-REF": ("_POLYMORPHIC", "first_element_ref", ["ApplicationCompositeDataTypeSubElementRef", "ImplementationDataTypeSubElementRef"]),
        "SECOND-ELEMENT-REF": ("_POLYMORPHIC", "second_element_ref", ["ApplicationCompositeDataTypeSubElementRef", "ImplementationDataTypeSubElementRef"]),
        "TEXT-TABLE-REF": lambda obj, elem: setattr(obj, "text_table_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize SubElementMapping."""
        super().__init__()
        self.first_element_ref: Optional[ARRef] = None
        self.second_element_ref: Optional[ARRef] = None
        self.text_table_ref: ARRef = None

    def serialize(self) -> ET.Element:
        """Serialize SubElementMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SubElementMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize first_element_ref
        if self.first_element_ref is not None:
            serialized = SerializationHelper.serialize_item(self.first_element_ref, "SubElementRef")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FIRST-ELEMENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize second_element_ref
        if self.second_element_ref is not None:
            serialized = SerializationHelper.serialize_item(self.second_element_ref, "SubElementRef")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SECOND-ELEMENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize text_table_ref
        if self.text_table_ref is not None:
            serialized = SerializationHelper.serialize_item(self.text_table_ref, "TextTableMapping")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TEXT-TABLE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SubElementMapping":
        """Deserialize XML element to SubElementMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SubElementMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SubElementMapping, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "FIRST-ELEMENT-REF":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "APPLICATION-COMPOSITE-DATA-TYPE-SUB-ELEMENT-REF":
                        setattr(obj, "first_element_ref", SerializationHelper.deserialize_by_tag(child[0], "ApplicationCompositeDataTypeSubElementRef"))
                    elif concrete_tag == "IMPLEMENTATION-DATA-TYPE-SUB-ELEMENT-REF":
                        setattr(obj, "first_element_ref", SerializationHelper.deserialize_by_tag(child[0], "ImplementationDataTypeSubElementRef"))
            elif tag == "SECOND-ELEMENT-REF":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "APPLICATION-COMPOSITE-DATA-TYPE-SUB-ELEMENT-REF":
                        setattr(obj, "second_element_ref", SerializationHelper.deserialize_by_tag(child[0], "ApplicationCompositeDataTypeSubElementRef"))
                    elif concrete_tag == "IMPLEMENTATION-DATA-TYPE-SUB-ELEMENT-REF":
                        setattr(obj, "second_element_ref", SerializationHelper.deserialize_by_tag(child[0], "ImplementationDataTypeSubElementRef"))
            elif tag == "TEXT-TABLE-REF":
                setattr(obj, "text_table_ref", ARRef.deserialize(child))

        return obj



class SubElementMappingBuilder(BuilderBase):
    """Builder for SubElementMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SubElementMapping = SubElementMapping()


    def with_first_element(self, value: Optional[SubElementRef]) -> "SubElementMappingBuilder":
        """Set first_element attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.first_element = value
        return self

    def with_second_element(self, value: Optional[SubElementRef]) -> "SubElementMappingBuilder":
        """Set second_element attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.second_element = value
        return self

    def with_text_table(self, value: TextTableMapping) -> "SubElementMappingBuilder":
        """Set text_table attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.text_table = value
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


    def build(self) -> SubElementMapping:
        """Build and return the SubElementMapping instance with validation."""
        self._validate_instance()
        pass
        return self._obj