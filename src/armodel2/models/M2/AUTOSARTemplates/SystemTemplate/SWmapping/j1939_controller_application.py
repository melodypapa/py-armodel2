"""J1939ControllerApplication AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 207)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SWmapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.sw_component_prototype import (
    SwComponentPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class J1939ControllerApplication(ARElement):
    """AUTOSAR J1939ControllerApplication."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "J1939-CONTROLLER-APPLICATION"


    function_id: Optional[PositiveInteger]
    sw_component_prototype_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "FUNCTION-ID": lambda obj, elem: setattr(obj, "function_id", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "SW-COMPONENT-PROTOTYPE-REF": lambda obj, elem: setattr(obj, "sw_component_prototype_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize J1939ControllerApplication."""
        super().__init__()
        self.function_id: Optional[PositiveInteger] = None
        self.sw_component_prototype_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize J1939ControllerApplication to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(J1939ControllerApplication, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize function_id
        if self.function_id is not None:
            serialized = SerializationHelper.serialize_item(self.function_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FUNCTION-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_component_prototype_ref
        if self.sw_component_prototype_ref is not None:
            serialized = SerializationHelper.serialize_item(self.sw_component_prototype_ref, "SwComponentPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-COMPONENT-PROTOTYPE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "J1939ControllerApplication":
        """Deserialize XML element to J1939ControllerApplication object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized J1939ControllerApplication object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(J1939ControllerApplication, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "FUNCTION-ID":
                setattr(obj, "function_id", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "SW-COMPONENT-PROTOTYPE-REF":
                setattr(obj, "sw_component_prototype_ref", ARRef.deserialize(child))

        return obj



class J1939ControllerApplicationBuilder(ARElementBuilder):
    """Builder for J1939ControllerApplication with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: J1939ControllerApplication = J1939ControllerApplication()


    def with_function_id(self, value: Optional[PositiveInteger]) -> "J1939ControllerApplicationBuilder":
        """Set function_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.function_id = value
        return self

    def with_sw_component_prototype(self, value: Optional[SwComponentPrototype]) -> "J1939ControllerApplicationBuilder":
        """Set sw_component_prototype attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_component_prototype = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "functionId",
        "swComponentPrototype",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> J1939ControllerApplication:
        """Build and return the J1939ControllerApplication instance with validation."""
        self._validate_instance()
        return self._obj