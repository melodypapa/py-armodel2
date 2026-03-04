"""SoftwareContext AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 163)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ResourceConsumption.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SoftwareContext(ARObject):
    """AUTOSAR SoftwareContext."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SOFTWARE-CONTEXT"


    input: Optional[String]
    state: Optional[String]
    _DESERIALIZE_DISPATCH = {
        "INPUT": lambda obj, elem: setattr(obj, "input", SerializationHelper.deserialize_by_tag(elem, "String")),
        "STATE": lambda obj, elem: setattr(obj, "state", SerializationHelper.deserialize_by_tag(elem, "String")),
    }


    def __init__(self) -> None:
        """Initialize SoftwareContext."""
        super().__init__()
        self.input: Optional[String] = None
        self.state: Optional[String] = None

    def serialize(self) -> ET.Element:
        """Serialize SoftwareContext to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SoftwareContext, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize input
        if self.input is not None:
            serialized = SerializationHelper.serialize_item(self.input, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INPUT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize state
        if self.state is not None:
            serialized = SerializationHelper.serialize_item(self.state, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("STATE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SoftwareContext":
        """Deserialize XML element to SoftwareContext object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SoftwareContext object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SoftwareContext, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "INPUT":
                setattr(obj, "input", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "STATE":
                setattr(obj, "state", SerializationHelper.deserialize_by_tag(child, "String"))

        return obj



class SoftwareContextBuilder(BuilderBase):
    """Builder for SoftwareContext with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SoftwareContext = SoftwareContext()


    def with_input(self, value: Optional[String]) -> "SoftwareContextBuilder":
        """Set input attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.input = value
        return self

    def with_state(self, value: Optional[String]) -> "SoftwareContextBuilder":
        """Set state attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.state = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "input",
        "state",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> SoftwareContext:
        """Build and return the SoftwareContext instance with validation."""
        self._validate_instance()
        return self._obj