"""BlueprintPolicy AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 163)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_AbstractBlueprintStructure.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class BlueprintPolicy(ARObject, ABC):
    """AUTOSAR BlueprintPolicy."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    attribute_name: String
    _DESERIALIZE_DISPATCH = {
        "ATTRIBUTE-NAME": lambda obj, elem: setattr(obj, "attribute_name", SerializationHelper.deserialize_by_tag(elem, "String")),
    }


    def __init__(self) -> None:
        """Initialize BlueprintPolicy."""
        super().__init__()
        self.attribute_name: String = None

    def serialize(self) -> ET.Element:
        """Serialize BlueprintPolicy to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BlueprintPolicy, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize attribute_name
        if self.attribute_name is not None:
            serialized = SerializationHelper.serialize_item(self.attribute_name, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ATTRIBUTE-NAME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BlueprintPolicy":
        """Deserialize XML element to BlueprintPolicy object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BlueprintPolicy object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BlueprintPolicy, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ATTRIBUTE-NAME":
                setattr(obj, "attribute_name", SerializationHelper.deserialize_by_tag(child, "String"))

        return obj



class BlueprintPolicyBuilder(BuilderBase, ABC):
    """Builder for BlueprintPolicy with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: BlueprintPolicy = BlueprintPolicy()


    def with_attribute_name(self, value: String) -> "BlueprintPolicyBuilder":
        """Set attribute_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.attribute_name = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "attributeName",
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
        if getattr(self._obj, "attributeName", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError(f"Required attribute 'attributeName' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn(f"Required attribute 'attributeName' is None", UserWarning)


    @abstractmethod
    def build(self) -> BlueprintPolicy:
        """Build and return the BlueprintPolicy instance (abstract)."""
        raise NotImplementedError