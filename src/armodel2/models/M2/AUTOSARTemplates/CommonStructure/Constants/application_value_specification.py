"""ApplicationValueSpecification AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 299)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 455)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
    ValueSpecification,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import ValueSpecificationBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel2.models.M2.MSR.CalibrationData.CalibrationValue.sw_axis_cont import (
    SwAxisCont,
)
from armodel2.models.M2.MSR.CalibrationData.CalibrationValue.sw_value_cont import (
    SwValueCont,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ApplicationValueSpecification(ValueSpecification):
    """AUTOSAR ApplicationValueSpecification."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "APPLICATION-VALUE-SPECIFICATION"


    category: Optional[Identifier]
    sw_axis_conts: list[SwAxisCont]
    sw_value_cont: Optional[SwValueCont]
    _DESERIALIZE_DISPATCH = {
        "CATEGORY": lambda obj, elem: setattr(obj, "category", SerializationHelper.deserialize_by_tag(elem, "Identifier")),
        "SW-AXIS-CONTS": lambda obj, elem: obj.sw_axis_conts.append(SerializationHelper.deserialize_by_tag(elem, "SwAxisCont")),
        "SW-VALUE-CONT": lambda obj, elem: setattr(obj, "sw_value_cont", SerializationHelper.deserialize_by_tag(elem, "SwValueCont")),
    }


    def __init__(self) -> None:
        """Initialize ApplicationValueSpecification."""
        super().__init__()
        self.category: Optional[Identifier] = None
        self.sw_axis_conts: list[SwAxisCont] = []
        self.sw_value_cont: Optional[SwValueCont] = None

    def serialize(self) -> ET.Element:
        """Serialize ApplicationValueSpecification to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ApplicationValueSpecification, self).serialize()

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
            serialized = SerializationHelper.serialize_item(self.category, "Identifier")
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

        # Serialize sw_axis_conts (list to container "SW-AXIS-CONTS")
        if self.sw_axis_conts:
            wrapper = ET.Element("SW-AXIS-CONTS")
            for item in self.sw_axis_conts:
                serialized = SerializationHelper.serialize_item(item, "SwAxisCont")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize sw_value_cont
        if self.sw_value_cont is not None:
            serialized = SerializationHelper.serialize_item(self.sw_value_cont, "SwValueCont")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-VALUE-CONT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ApplicationValueSpecification":
        """Deserialize XML element to ApplicationValueSpecification object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ApplicationValueSpecification object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ApplicationValueSpecification, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CATEGORY":
                setattr(obj, "category", SerializationHelper.deserialize_by_tag(child, "Identifier"))
            elif tag == "SW-AXIS-CONTS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.sw_axis_conts.append(SerializationHelper.deserialize_by_tag(item_elem, "SwAxisCont"))
            elif tag == "SW-VALUE-CONT":
                setattr(obj, "sw_value_cont", SerializationHelper.deserialize_by_tag(child, "SwValueCont"))

        return obj



class ApplicationValueSpecificationBuilder(ValueSpecificationBuilder):
    """Builder for ApplicationValueSpecification with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ApplicationValueSpecification = ApplicationValueSpecification()


    def with_category(self, value: Optional[Identifier]) -> "ApplicationValueSpecificationBuilder":
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

    def with_sw_axis_conts(self, items: list[SwAxisCont]) -> "ApplicationValueSpecificationBuilder":
        """Set sw_axis_conts list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.sw_axis_conts = list(items) if items else []
        return self

    def with_sw_value_cont(self, value: Optional[SwValueCont]) -> "ApplicationValueSpecificationBuilder":
        """Set sw_value_cont attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_value_cont = value
        return self


    def add_sw_axis_cont(self, item: SwAxisCont) -> "ApplicationValueSpecificationBuilder":
        """Add a single item to sw_axis_conts list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.sw_axis_conts.append(item)
        return self

    def clear_sw_axis_conts(self) -> "ApplicationValueSpecificationBuilder":
        """Clear all items from sw_axis_conts list.

        Returns:
            self for method chaining
        """
        self._obj.sw_axis_conts = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "category",
        "swAxisCont",
        "swValueCont",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> ApplicationValueSpecification:
        """Build and return the ApplicationValueSpecification instance with validation."""
        self._validate_instance()
        return self._obj