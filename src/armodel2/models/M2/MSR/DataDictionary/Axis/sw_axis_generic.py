"""SwAxisGeneric AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 355)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_Axis.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.MSR.DataDictionary.Axis.sw_axis_type import (
    SwAxisType,
)
from armodel2.models.M2.MSR.DataDictionary.Axis.sw_generic_axis_param import (
    SwGenericAxisParam,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SwAxisGeneric(ARObject):
    """AUTOSAR SwAxisGeneric."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SW-AXIS-GENERIC"


    sw_axis_type_ref: Optional[ARRef]
    sw_generic_axis_params: list[SwGenericAxisParam]
    _DESERIALIZE_DISPATCH = {
        "SW-AXIS-TYPE-REF": lambda obj, elem: setattr(obj, "sw_axis_type_ref", ARRef.deserialize(elem)),
        "SW-GENERIC-AXIS-PARAMS": lambda obj, elem: obj.sw_generic_axis_params.append(SerializationHelper.deserialize_by_tag(elem, "SwGenericAxisParam")),
    }


    def __init__(self) -> None:
        """Initialize SwAxisGeneric."""
        super().__init__()
        self.sw_axis_type_ref: Optional[ARRef] = None
        self.sw_generic_axis_params: list[SwGenericAxisParam] = []

    def serialize(self) -> ET.Element:
        """Serialize SwAxisGeneric to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwAxisGeneric, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize sw_axis_type_ref
        if self.sw_axis_type_ref is not None:
            serialized = SerializationHelper.serialize_item(self.sw_axis_type_ref, "SwAxisType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-AXIS-TYPE-REF")
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
    def deserialize(cls, element: ET.Element) -> "SwAxisGeneric":
        """Deserialize XML element to SwAxisGeneric object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwAxisGeneric object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwAxisGeneric, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "SW-AXIS-TYPE-REF":
                setattr(obj, "sw_axis_type_ref", ARRef.deserialize(child))
            elif tag == "SW-GENERIC-AXIS-PARAMS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.sw_generic_axis_params.append(SerializationHelper.deserialize_by_tag(item_elem, "SwGenericAxisParam"))

        return obj



class SwAxisGenericBuilder(BuilderBase):
    """Builder for SwAxisGeneric with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SwAxisGeneric = SwAxisGeneric()


    def with_sw_axis_type(self, value: Optional[SwAxisType]) -> "SwAxisGenericBuilder":
        """Set sw_axis_type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'sw_axis_type' is required and cannot be None")
        self._obj.sw_axis_type = value
        return self

    def with_sw_generic_axis_params(self, items: list[SwGenericAxisParam]) -> "SwAxisGenericBuilder":
        """Set sw_generic_axis_params list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.sw_generic_axis_params = list(items) if items else []
        return self


    def add_sw_generic_axis_param(self, item: SwGenericAxisParam) -> "SwAxisGenericBuilder":
        """Add a single item to sw_generic_axis_params list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.sw_generic_axis_params.append(item)
        return self

    def clear_sw_generic_axis_params(self) -> "SwAxisGenericBuilder":
        """Clear all items from sw_generic_axis_params list.

        Returns:
            self for method chaining
        """
        self._obj.sw_generic_axis_params = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "swAxisType",
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


    def build(self) -> SwAxisGeneric:
        """Build and return the SwAxisGeneric instance with validation."""
        self._validate_instance()
        return self._obj