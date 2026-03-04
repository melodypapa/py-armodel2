"""McSwEmulationMethodSupport AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 180)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_MeasurementCalibrationSupport.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.mc_parameter_element_group import (
    McParameterElementGroup,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class McSwEmulationMethodSupport(ARObject):
    """AUTOSAR McSwEmulationMethodSupport."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "MC-SW-EMULATION-METHOD-SUPPORT"


    base_reference_ref: Optional[ARRef]
    category: Optional[Identifier]
    element_groups: list[McParameterElementGroup]
    reference_table_ref: Optional[ARRef]
    short_label: Optional[Identifier]
    _DESERIALIZE_DISPATCH = {
        "BASE-REFERENCE-REF": lambda obj, elem: setattr(obj, "base_reference_ref", ARRef.deserialize(elem)),
        "CATEGORY": lambda obj, elem: setattr(obj, "category", SerializationHelper.deserialize_by_tag(elem, "Identifier")),
        "ELEMENT-GROUPS": lambda obj, elem: obj.element_groups.append(SerializationHelper.deserialize_by_tag(elem, "McParameterElementGroup")),
        "REFERENCE-TABLE-REF": lambda obj, elem: setattr(obj, "reference_table_ref", ARRef.deserialize(elem)),
        "SHORT-LABEL": lambda obj, elem: setattr(obj, "short_label", SerializationHelper.deserialize_by_tag(elem, "Identifier")),
    }


    def __init__(self) -> None:
        """Initialize McSwEmulationMethodSupport."""
        super().__init__()
        self.base_reference_ref: Optional[ARRef] = None
        self.category: Optional[Identifier] = None
        self.element_groups: list[McParameterElementGroup] = []
        self.reference_table_ref: Optional[ARRef] = None
        self.short_label: Optional[Identifier] = None

    def serialize(self) -> ET.Element:
        """Serialize McSwEmulationMethodSupport to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(McSwEmulationMethodSupport, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize base_reference_ref
        if self.base_reference_ref is not None:
            serialized = SerializationHelper.serialize_item(self.base_reference_ref, "VariableDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BASE-REFERENCE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

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

        # Serialize element_groups (list to container "ELEMENT-GROUPS")
        if self.element_groups:
            wrapper = ET.Element("ELEMENT-GROUPS")
            for item in self.element_groups:
                serialized = SerializationHelper.serialize_item(item, "McParameterElementGroup")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize reference_table_ref
        if self.reference_table_ref is not None:
            serialized = SerializationHelper.serialize_item(self.reference_table_ref, "VariableDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REFERENCE-TABLE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize short_label
        if self.short_label is not None:
            serialized = SerializationHelper.serialize_item(self.short_label, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHORT-LABEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "McSwEmulationMethodSupport":
        """Deserialize XML element to McSwEmulationMethodSupport object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized McSwEmulationMethodSupport object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(McSwEmulationMethodSupport, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "BASE-REFERENCE-REF":
                setattr(obj, "base_reference_ref", ARRef.deserialize(child))
            elif tag == "CATEGORY":
                setattr(obj, "category", SerializationHelper.deserialize_by_tag(child, "Identifier"))
            elif tag == "ELEMENT-GROUPS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.element_groups.append(SerializationHelper.deserialize_by_tag(item_elem, "McParameterElementGroup"))
            elif tag == "REFERENCE-TABLE-REF":
                setattr(obj, "reference_table_ref", ARRef.deserialize(child))
            elif tag == "SHORT-LABEL":
                setattr(obj, "short_label", SerializationHelper.deserialize_by_tag(child, "Identifier"))

        return obj



class McSwEmulationMethodSupportBuilder(BuilderBase):
    """Builder for McSwEmulationMethodSupport with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: McSwEmulationMethodSupport = McSwEmulationMethodSupport()


    def with_base_reference(self, value: Optional[VariableDataPrototype]) -> "McSwEmulationMethodSupportBuilder":
        """Set base_reference attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.base_reference = value
        return self

    def with_category(self, value: Optional[Identifier]) -> "McSwEmulationMethodSupportBuilder":
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

    def with_element_groups(self, items: list[McParameterElementGroup]) -> "McSwEmulationMethodSupportBuilder":
        """Set element_groups list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.element_groups = list(items) if items else []
        return self

    def with_reference_table(self, value: Optional[VariableDataPrototype]) -> "McSwEmulationMethodSupportBuilder":
        """Set reference_table attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.reference_table = value
        return self

    def with_short_label(self, value: Optional[Identifier]) -> "McSwEmulationMethodSupportBuilder":
        """Set short_label attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.short_label = value
        return self


    def add_element_group(self, item: McParameterElementGroup) -> "McSwEmulationMethodSupportBuilder":
        """Add a single item to element_groups list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.element_groups.append(item)
        return self

    def clear_element_groups(self) -> "McSwEmulationMethodSupportBuilder":
        """Clear all items from element_groups list.

        Returns:
            self for method chaining
        """
        self._obj.element_groups = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "baseReference",
        "category",
        "elementGroup",
        "referenceTable",
        "shortLabel",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> McSwEmulationMethodSupport:
        """Build and return the McSwEmulationMethodSupport instance with validation."""
        self._validate_instance()
        return self._obj