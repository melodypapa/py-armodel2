"""ImplementationDataTypeElement AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 321)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 269)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2032)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 452)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ImplementationDataTypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes.abstract_implementation_data_type_element import (
    AbstractImplementationDataTypeElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes.abstract_implementation_data_type_element import AbstractImplementationDataTypeElementBuilder
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import (
    ArrayImplPolicyEnum,
    ArraySizeSemanticsEnum,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes import (
    ArraySizeHandlingEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)

if TYPE_CHECKING:
    from armodel2.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
        SwDataDefProps,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class ImplementationDataTypeElement(AbstractImplementationDataTypeElement):
    """AUTOSAR ImplementationDataTypeElement."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "IMPLEMENTATION-DATA-TYPE-ELEMENT"


    array_impl_policy: Optional[ArrayImplPolicyEnum]
    array_size: Optional[PositiveInteger]
    array_size_handling: Optional[ArraySizeHandlingEnum]
    array_size_semantics: Optional[ArraySizeSemanticsEnum]
    is_optional: Optional[Boolean]
    sub_elements: list[ImplementationDataTypeElement]
    sw_data_def_props: Optional[SwDataDefProps]
    _DESERIALIZE_DISPATCH = {
        "ARRAY-IMPL-POLICY": lambda obj, elem: setattr(obj, "array_impl_policy", ArrayImplPolicyEnum.deserialize(elem)),
        "ARRAY-SIZE": lambda obj, elem: setattr(obj, "array_size", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "ARRAY-SIZE-HANDLING": lambda obj, elem: setattr(obj, "array_size_handling", ArraySizeHandlingEnum.deserialize(elem)),
        "ARRAY-SIZE-SEMANTICS": lambda obj, elem: setattr(obj, "array_size_semantics", ArraySizeSemanticsEnum.deserialize(elem)),
        "IS-OPTIONAL": lambda obj, elem: setattr(obj, "is_optional", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "SUB-ELEMENTS": lambda obj, elem: obj.sub_elements.append(SerializationHelper.deserialize_by_tag(elem, "ImplementationDataTypeElement")),
        "SW-DATA-DEF-PROPS": lambda obj, elem: setattr(obj, "sw_data_def_props", SerializationHelper.deserialize_by_tag(elem, "SwDataDefProps")),
    }


    def __init__(self) -> None:
        """Initialize ImplementationDataTypeElement."""
        super().__init__()
        self.array_impl_policy: Optional[ArrayImplPolicyEnum] = None
        self.array_size: Optional[PositiveInteger] = None
        self.array_size_handling: Optional[ArraySizeHandlingEnum] = None
        self.array_size_semantics: Optional[ArraySizeSemanticsEnum] = None
        self.is_optional: Optional[Boolean] = None
        self.sub_elements: list[ImplementationDataTypeElement] = []
        self.sw_data_def_props: Optional[SwDataDefProps] = None

    def serialize(self) -> ET.Element:
        """Serialize ImplementationDataTypeElement to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ImplementationDataTypeElement, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize array_impl_policy
        if self.array_impl_policy is not None:
            serialized = SerializationHelper.serialize_item(self.array_impl_policy, "ArrayImplPolicyEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ARRAY-IMPL-POLICY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize array_size
        if self.array_size is not None:
            serialized = SerializationHelper.serialize_item(self.array_size, "PositiveInteger")
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

        # Serialize array_size_handling
        if self.array_size_handling is not None:
            serialized = SerializationHelper.serialize_item(self.array_size_handling, "ArraySizeHandlingEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ARRAY-SIZE-HANDLING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize array_size_semantics
        if self.array_size_semantics is not None:
            serialized = SerializationHelper.serialize_item(self.array_size_semantics, "ArraySizeSemanticsEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ARRAY-SIZE-SEMANTICS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize is_optional
        if self.is_optional is not None:
            serialized = SerializationHelper.serialize_item(self.is_optional, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IS-OPTIONAL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sub_elements (list to container "SUB-ELEMENTS")
        if self.sub_elements:
            wrapper = ET.Element("SUB-ELEMENTS")
            for item in self.sub_elements:
                serialized = SerializationHelper.serialize_item(item, "ImplementationDataTypeElement")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize sw_data_def_props
        if self.sw_data_def_props is not None:
            serialized = SerializationHelper.serialize_item(self.sw_data_def_props, "SwDataDefProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-DATA-DEF-PROPS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ImplementationDataTypeElement":
        """Deserialize XML element to ImplementationDataTypeElement object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ImplementationDataTypeElement object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ImplementationDataTypeElement, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ARRAY-IMPL-POLICY":
                setattr(obj, "array_impl_policy", ArrayImplPolicyEnum.deserialize(child))
            elif tag == "ARRAY-SIZE":
                setattr(obj, "array_size", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "ARRAY-SIZE-HANDLING":
                setattr(obj, "array_size_handling", ArraySizeHandlingEnum.deserialize(child))
            elif tag == "ARRAY-SIZE-SEMANTICS":
                setattr(obj, "array_size_semantics", ArraySizeSemanticsEnum.deserialize(child))
            elif tag == "IS-OPTIONAL":
                setattr(obj, "is_optional", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "SUB-ELEMENTS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.sub_elements.append(SerializationHelper.deserialize_by_tag(item_elem, "ImplementationDataTypeElement"))
            elif tag == "SW-DATA-DEF-PROPS":
                setattr(obj, "sw_data_def_props", SerializationHelper.deserialize_by_tag(child, "SwDataDefProps"))

        return obj



class ImplementationDataTypeElementBuilder(AbstractImplementationDataTypeElementBuilder):
    """Builder for ImplementationDataTypeElement with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ImplementationDataTypeElement = ImplementationDataTypeElement()


    def with_array_impl_policy(self, value: Optional[ArrayImplPolicyEnum]) -> "ImplementationDataTypeElementBuilder":
        """Set array_impl_policy attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'array_impl_policy' is required and cannot be None")
        self._obj.array_impl_policy = value
        return self

    def with_array_size(self, value: Optional[PositiveInteger]) -> "ImplementationDataTypeElementBuilder":
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

    def with_array_size_handling(self, value: Optional[ArraySizeHandlingEnum]) -> "ImplementationDataTypeElementBuilder":
        """Set array_size_handling attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'array_size_handling' is required and cannot be None")
        self._obj.array_size_handling = value
        return self

    def with_array_size_semantics(self, value: Optional[ArraySizeSemanticsEnum]) -> "ImplementationDataTypeElementBuilder":
        """Set array_size_semantics attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'array_size_semantics' is required and cannot be None")
        self._obj.array_size_semantics = value
        return self

    def with_is_optional(self, value: Optional[Boolean]) -> "ImplementationDataTypeElementBuilder":
        """Set is_optional attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'is_optional' is required and cannot be None")
        self._obj.is_optional = value
        return self

    def with_sub_elements(self, items: list[ImplementationDataTypeElement]) -> "ImplementationDataTypeElementBuilder":
        """Set sub_elements list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.sub_elements = list(items) if items else []
        return self

    def with_sw_data_def_props(self, value: Optional[SwDataDefProps]) -> "ImplementationDataTypeElementBuilder":
        """Set sw_data_def_props attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'sw_data_def_props' is required and cannot be None")
        self._obj.sw_data_def_props = value
        return self


    def add_sub_element(self, item: ImplementationDataTypeElement) -> "ImplementationDataTypeElementBuilder":
        """Add a single item to sub_elements list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.sub_elements.append(item)
        return self

    def clear_sub_elements(self) -> "ImplementationDataTypeElementBuilder":
        """Clear all items from sub_elements list.

        Returns:
            self for method chaining
        """
        self._obj.sub_elements = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "arrayImplPolicy",
        "arraySize",
        "arraySizeHandling",
        "arraySizeSemantics",
        "isOptional",
        "subElement",
        "swDataDefProps",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> ImplementationDataTypeElement:
        """Build and return the ImplementationDataTypeElement instance with validation."""
        self._validate_instance()
        return self._obj