"""SwTextProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 343)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 313)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 249)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 216)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_DataDefProperties.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import (
    ArraySizeSemanticsEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel2.models.M2.MSR.AsamHdo.BaseTypes.sw_base_type import (
    SwBaseType,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SwTextProps(ARObject):
    """AUTOSAR SwTextProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SW-TEXT-PROPS"


    array_size: Optional[ArraySizeSemanticsEnum]
    base_type_ref: Optional[ARRef]
    sw_fill_character: Optional[Integer]
    sw_max_text_size: Optional[Integer]
    _DESERIALIZE_DISPATCH = {
        "ARRAY-SIZE": lambda obj, elem: setattr(obj, "array_size", ArraySizeSemanticsEnum.deserialize(elem)),
        "BASE-TYPE-REF": lambda obj, elem: setattr(obj, "base_type_ref", ARRef.deserialize(elem)),
        "SW-FILL-CHARACTER": lambda obj, elem: setattr(obj, "sw_fill_character", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "SW-MAX-TEXT-SIZE": lambda obj, elem: setattr(obj, "sw_max_text_size", SerializationHelper.deserialize_by_tag(elem, "Integer")),
    }


    def __init__(self) -> None:
        """Initialize SwTextProps."""
        super().__init__()
        self.array_size: Optional[ArraySizeSemanticsEnum] = None
        self.base_type_ref: Optional[ARRef] = None
        self.sw_fill_character: Optional[Integer] = None
        self.sw_max_text_size: Optional[Integer] = None

    def serialize(self) -> ET.Element:
        """Serialize SwTextProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwTextProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize array_size
        if self.array_size is not None:
            serialized = SerializationHelper.serialize_item(self.array_size, "ArraySizeSemanticsEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ARRAY-SIZE")
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

        # Serialize sw_fill_character
        if self.sw_fill_character is not None:
            serialized = SerializationHelper.serialize_item(self.sw_fill_character, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-FILL-CHARACTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_max_text_size
        if self.sw_max_text_size is not None:
            serialized = SerializationHelper.serialize_item(self.sw_max_text_size, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-MAX-TEXT-SIZE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwTextProps":
        """Deserialize XML element to SwTextProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwTextProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwTextProps, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ARRAY-SIZE":
                setattr(obj, "array_size", ArraySizeSemanticsEnum.deserialize(child))
            elif tag == "BASE-TYPE-REF":
                setattr(obj, "base_type_ref", ARRef.deserialize(child))
            elif tag == "SW-FILL-CHARACTER":
                setattr(obj, "sw_fill_character", SerializationHelper.deserialize_by_tag(child, "Integer"))
            elif tag == "SW-MAX-TEXT-SIZE":
                setattr(obj, "sw_max_text_size", SerializationHelper.deserialize_by_tag(child, "Integer"))

        return obj



class SwTextPropsBuilder(BuilderBase):
    """Builder for SwTextProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SwTextProps = SwTextProps()


    def with_array_size(self, value: Optional[ArraySizeSemanticsEnum]) -> "SwTextPropsBuilder":
        """Set array_size attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'array_size' is required and cannot be None")
        self._obj.array_size = value
        return self

    def with_base_type(self, value: Optional[SwBaseType]) -> "SwTextPropsBuilder":
        """Set base_type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'base_type' is required and cannot be None")
        self._obj.base_type = value
        return self

    def with_sw_fill_character(self, value: Optional[Integer]) -> "SwTextPropsBuilder":
        """Set sw_fill_character attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'sw_fill_character' is required and cannot be None")
        self._obj.sw_fill_character = value
        return self

    def with_sw_max_text_size(self, value: Optional[Integer]) -> "SwTextPropsBuilder":
        """Set sw_max_text_size attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'sw_max_text_size' is required and cannot be None")
        self._obj.sw_max_text_size = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "arraySize",
        "baseType",
        "swFillCharacter",
        "swMaxTextSize",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> SwTextProps:
        """Build and return the SwTextProps instance with validation."""
        self._validate_instance()
        return self._obj