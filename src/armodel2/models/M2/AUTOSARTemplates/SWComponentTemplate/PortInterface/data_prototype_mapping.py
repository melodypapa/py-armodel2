"""DataPrototypeMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 125)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2014)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.autosar_data_prototype import (
    AutosarDataPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.data_transformation import (
    DataTransformation,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.sub_element_mapping import (
    SubElementMapping,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.text_table_mapping import (
    TextTableMapping,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DataPrototypeMapping(ARObject):
    """AUTOSAR DataPrototypeMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DATA-PROTOTYPE-MAPPING"


    first_data_ref: Optional[ARRef]
    first_to_second_ref: Optional[ARRef]
    second_data_ref: Optional[ARRef]
    second_to_first_ref: Optional[ARRef]
    sub_element_refs: list[ARRef]
    text_table_ref: ARRef
    _DESERIALIZE_DISPATCH = {
        "FIRST-DATA-REF": ("_POLYMORPHIC", "first_data_ref", ["ArgumentDataPrototype", "ParameterDataPrototype", "VariableDataPrototype"]),
        "FIRST-TO-SECOND-REF": lambda obj, elem: setattr(obj, "first_to_second_ref", ARRef.deserialize(elem)),
        "SECOND-DATA-REF": ("_POLYMORPHIC", "second_data_ref", ["ArgumentDataPrototype", "ParameterDataPrototype", "VariableDataPrototype"]),
        "SECOND-TO-FIRST-REF": lambda obj, elem: setattr(obj, "second_to_first_ref", ARRef.deserialize(elem)),
        "SUB-ELEMENT-REFS": lambda obj, elem: [obj.sub_element_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "TEXT-TABLE-REF": lambda obj, elem: setattr(obj, "text_table_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize DataPrototypeMapping."""
        super().__init__()
        self.first_data_ref: Optional[ARRef] = None
        self.first_to_second_ref: Optional[ARRef] = None
        self.second_data_ref: Optional[ARRef] = None
        self.second_to_first_ref: Optional[ARRef] = None
        self.sub_element_refs: list[ARRef] = []
        self.text_table_ref: ARRef = None

    def serialize(self) -> ET.Element:
        """Serialize DataPrototypeMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DataPrototypeMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize first_data_ref
        if self.first_data_ref is not None:
            serialized = SerializationHelper.serialize_item(self.first_data_ref, "AutosarDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FIRST-DATA-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize first_to_second_ref
        if self.first_to_second_ref is not None:
            serialized = SerializationHelper.serialize_item(self.first_to_second_ref, "DataTransformation")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FIRST-TO-SECOND-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize second_data_ref
        if self.second_data_ref is not None:
            serialized = SerializationHelper.serialize_item(self.second_data_ref, "AutosarDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SECOND-DATA-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize second_to_first_ref
        if self.second_to_first_ref is not None:
            serialized = SerializationHelper.serialize_item(self.second_to_first_ref, "DataTransformation")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SECOND-TO-FIRST-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sub_element_refs (list to container "SUB-ELEMENT-REFS")
        if self.sub_element_refs:
            wrapper = ET.Element("SUB-ELEMENT-REFS")
            for item in self.sub_element_refs:
                serialized = SerializationHelper.serialize_item(item, "SubElementMapping")
                if serialized is not None:
                    child_elem = ET.Element("SUB-ELEMENT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

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
    def deserialize(cls, element: ET.Element) -> "DataPrototypeMapping":
        """Deserialize XML element to DataPrototypeMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataPrototypeMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DataPrototypeMapping, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "FIRST-DATA-REF":
                setattr(obj, "first_data_ref", ARRef.deserialize(child))
            elif tag == "FIRST-TO-SECOND-REF":
                setattr(obj, "first_to_second_ref", ARRef.deserialize(child))
            elif tag == "SECOND-DATA-REF":
                setattr(obj, "second_data_ref", ARRef.deserialize(child))
            elif tag == "SECOND-TO-FIRST-REF":
                setattr(obj, "second_to_first_ref", ARRef.deserialize(child))
            elif tag == "SUB-ELEMENT-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.sub_element_refs.append(ARRef.deserialize(item_elem))
            elif tag == "TEXT-TABLE-REF":
                setattr(obj, "text_table_ref", ARRef.deserialize(child))

        return obj



class DataPrototypeMappingBuilder(BuilderBase):
    """Builder for DataPrototypeMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DataPrototypeMapping = DataPrototypeMapping()


    def with_first_data(self, value: Optional[AutosarDataPrototype]) -> "DataPrototypeMappingBuilder":
        """Set first_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.first_data = value
        return self

    def with_first_to_second(self, value: Optional[DataTransformation]) -> "DataPrototypeMappingBuilder":
        """Set first_to_second attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.first_to_second = value
        return self

    def with_second_data(self, value: Optional[AutosarDataPrototype]) -> "DataPrototypeMappingBuilder":
        """Set second_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.second_data = value
        return self

    def with_second_to_first(self, value: Optional[DataTransformation]) -> "DataPrototypeMappingBuilder":
        """Set second_to_first attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.second_to_first = value
        return self

    def with_sub_elements(self, items: list[SubElementMapping]) -> "DataPrototypeMappingBuilder":
        """Set sub_elements list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.sub_elements = list(items) if items else []
        return self

    def with_text_table(self, value: TextTableMapping) -> "DataPrototypeMappingBuilder":
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


    def add_sub_element(self, item: SubElementMapping) -> "DataPrototypeMappingBuilder":
        """Add a single item to sub_elements list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.sub_elements.append(item)
        return self

    def clear_sub_elements(self) -> "DataPrototypeMappingBuilder":
        """Clear all items from sub_elements list.

        Returns:
            self for method chaining
        """
        self._obj.sub_elements = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "textTable",
    }
    _OPTIONAL_ATTRIBUTES = {
        "firstData",
        "firstToSecond",
        "secondData",
        "secondToFirst",
        "subElement",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Validate required attributes using pre-computed constants (O(1) lookup)
        # This is much faster than calling get_type_hints() at runtime
        if getattr(self._obj, "textTable", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'textTable' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'textTable' is None", UserWarning)


    def build(self) -> DataPrototypeMapping:
        """Build and return the DataPrototypeMapping instance with validation."""
        self._validate_instance()
        return self._obj