"""SwAxisType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 355)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_Axis.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from armodel2.models.M2.MSR.DataDictionary.Axis.sw_generic_axis_param import (
    SwGenericAxisParam,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SwAxisType(ARElement):
    """AUTOSAR SwAxisType."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SW-AXIS-TYPE"


    sw_generic_axis: Optional[DocumentationBlock]
    sw_generic_axis_params: list[SwGenericAxisParam]
    _DESERIALIZE_DISPATCH = {
        "SW-GENERIC-AXIS": lambda obj, elem: setattr(obj, "sw_generic_axis", SerializationHelper.deserialize_by_tag(elem, "DocumentationBlock")),
        "SW-GENERIC-AXIS-PARAMS": lambda obj, elem: obj.sw_generic_axis_params.append(SerializationHelper.deserialize_by_tag(elem, "SwGenericAxisParam")),
    }


    def __init__(self) -> None:
        """Initialize SwAxisType."""
        super().__init__()
        self.sw_generic_axis: Optional[DocumentationBlock] = None
        self.sw_generic_axis_params: list[SwGenericAxisParam] = []

    def serialize(self) -> ET.Element:
        """Serialize SwAxisType to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwAxisType, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize sw_generic_axis
        if self.sw_generic_axis is not None:
            serialized = SerializationHelper.serialize_item(self.sw_generic_axis, "DocumentationBlock")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-GENERIC-AXIS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_generic_axis_params (list to container "SW-GENERIC-AXIS-PARAMS")
        if self.sw_generic_axis_params:
            wrapper = ET.Element("SW-GENERIC-AXIS-PARAMS")
            for item in self.sw_generic_axis_params:
                serialized = SerializationHelper.serialize_item(item, "SwGenericAxisParam")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwAxisType":
        """Deserialize XML element to SwAxisType object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwAxisType object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwAxisType, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "SW-GENERIC-AXIS":
                setattr(obj, "sw_generic_axis", SerializationHelper.deserialize_by_tag(child, "DocumentationBlock"))
            elif tag == "SW-GENERIC-AXIS-PARAMS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.sw_generic_axis_params.append(SerializationHelper.deserialize_by_tag(item_elem, "SwGenericAxisParam"))

        return obj



class SwAxisTypeBuilder(ARElementBuilder):
    """Builder for SwAxisType with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SwAxisType = SwAxisType()


    def with_sw_generic_axis(self, value: Optional[DocumentationBlock]) -> "SwAxisTypeBuilder":
        """Set sw_generic_axis attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_generic_axis = value
        return self

    def with_sw_generic_axis_params(self, items: list[SwGenericAxisParam]) -> "SwAxisTypeBuilder":
        """Set sw_generic_axis_params list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.sw_generic_axis_params = list(items) if items else []
        return self


    def add_sw_generic_axis_param(self, item: SwGenericAxisParam) -> "SwAxisTypeBuilder":
        """Add a single item to sw_generic_axis_params list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.sw_generic_axis_params.append(item)
        return self

    def clear_sw_generic_axis_params(self) -> "SwAxisTypeBuilder":
        """Clear all items from sw_generic_axis_params list.

        Returns:
            self for method chaining
        """
        self._obj.sw_generic_axis_params = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "swGenericAxis",
        "swGenericAxisParam",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> SwAxisType:
        """Build and return the SwAxisType instance with validation."""
        self._validate_instance()
        return self._obj