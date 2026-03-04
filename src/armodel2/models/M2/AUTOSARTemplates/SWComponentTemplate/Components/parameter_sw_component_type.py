"""ParameterSwComponentType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 41)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2043)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.sw_component_type import (
    SwComponentType,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.sw_component_type import SwComponentTypeBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Constants.constant_specification import (
    ConstantSpecification,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.data_type_mapping_set import (
    DataTypeMappingSet,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.InstantiationDataDefProps.instantiation_data_def_props import (
    InstantiationDataDefProps,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ParameterSwComponentType(SwComponentType):
    """AUTOSAR ParameterSwComponentType."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "PARAMETER-SW-COMPONENT-TYPE"


    constant_refs: list[ARRef]
    data_type_refs: list[ARRef]
    instantiation_data_defs: list[InstantiationDataDefProps]
    _DESERIALIZE_DISPATCH = {
        "CONSTANT-REFS": lambda obj, elem: [obj.constant_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "DATA-TYPE-REFS": lambda obj, elem: [obj.data_type_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "INSTANTIATION-DATA-DEFS": lambda obj, elem: obj.instantiation_data_defs.append(SerializationHelper.deserialize_by_tag(elem, "InstantiationDataDefProps")),
    }


    def __init__(self) -> None:
        """Initialize ParameterSwComponentType."""
        super().__init__()
        self.constant_refs: list[ARRef] = []
        self.data_type_refs: list[ARRef] = []
        self.instantiation_data_defs: list[InstantiationDataDefProps] = []

    def serialize(self) -> ET.Element:
        """Serialize ParameterSwComponentType to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ParameterSwComponentType, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize constant_refs (list to container "CONSTANT-REFS")
        if self.constant_refs:
            wrapper = ET.Element("CONSTANT-REFS")
            for item in self.constant_refs:
                serialized = SerializationHelper.serialize_item(item, "ConstantSpecification")
                if serialized is not None:
                    child_elem = ET.Element("CONSTANT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize data_type_refs (list to container "DATA-TYPE-REFS")
        if self.data_type_refs:
            wrapper = ET.Element("DATA-TYPE-REFS")
            for item in self.data_type_refs:
                serialized = SerializationHelper.serialize_item(item, "DataTypeMappingSet")
                if serialized is not None:
                    child_elem = ET.Element("DATA-TYPE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize instantiation_data_defs (list to container "INSTANTIATION-DATA-DEFS")
        if self.instantiation_data_defs:
            wrapper = ET.Element("INSTANTIATION-DATA-DEFS")
            for item in self.instantiation_data_defs:
                serialized = SerializationHelper.serialize_item(item, "InstantiationDataDefProps")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ParameterSwComponentType":
        """Deserialize XML element to ParameterSwComponentType object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ParameterSwComponentType object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ParameterSwComponentType, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CONSTANT-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.constant_refs.append(ARRef.deserialize(item_elem))
            elif tag == "DATA-TYPE-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.data_type_refs.append(ARRef.deserialize(item_elem))
            elif tag == "INSTANTIATION-DATA-DEFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.instantiation_data_defs.append(SerializationHelper.deserialize_by_tag(item_elem, "InstantiationDataDefProps"))

        return obj



class ParameterSwComponentTypeBuilder(SwComponentTypeBuilder):
    """Builder for ParameterSwComponentType with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ParameterSwComponentType = ParameterSwComponentType()


    def with_constants(self, items: list[ConstantSpecification]) -> "ParameterSwComponentTypeBuilder":
        """Set constants list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.constants = list(items) if items else []
        return self

    def with_data_types(self, items: list[DataTypeMappingSet]) -> "ParameterSwComponentTypeBuilder":
        """Set data_types list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.data_types = list(items) if items else []
        return self

    def with_instantiation_data_defs(self, items: list[InstantiationDataDefProps]) -> "ParameterSwComponentTypeBuilder":
        """Set instantiation_data_defs list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.instantiation_data_defs = list(items) if items else []
        return self


    def add_constant(self, item: ConstantSpecification) -> "ParameterSwComponentTypeBuilder":
        """Add a single item to constants list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.constants.append(item)
        return self

    def clear_constants(self) -> "ParameterSwComponentTypeBuilder":
        """Clear all items from constants list.

        Returns:
            self for method chaining
        """
        self._obj.constants = []
        return self

    def add_data_type(self, item: DataTypeMappingSet) -> "ParameterSwComponentTypeBuilder":
        """Add a single item to data_types list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.data_types.append(item)
        return self

    def clear_data_types(self) -> "ParameterSwComponentTypeBuilder":
        """Clear all items from data_types list.

        Returns:
            self for method chaining
        """
        self._obj.data_types = []
        return self

    def add_instantiation_data_def(self, item: InstantiationDataDefProps) -> "ParameterSwComponentTypeBuilder":
        """Add a single item to instantiation_data_defs list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.instantiation_data_defs.append(item)
        return self

    def clear_instantiation_data_defs(self) -> "ParameterSwComponentTypeBuilder":
        """Clear all items from instantiation_data_defs list.

        Returns:
            self for method chaining
        """
        self._obj.instantiation_data_defs = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "constant",
        "dataType",
        "instantiationDataDef",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> ParameterSwComponentType:
        """Build and return the ParameterSwComponentType instance with validation."""
        self._validate_instance()
        return self._obj