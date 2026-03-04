"""EnumerationMappingEntry AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 443)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling_AttributeValueVariationPoints.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class EnumerationMappingEntry(ARObject):
    """AUTOSAR EnumerationMappingEntry."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ENUMERATION-MAPPING-ENTRY"


    enumerator: NameToken
    numerical_value: PositiveInteger
    _DESERIALIZE_DISPATCH = {
        "ENUMERATOR": lambda obj, elem: setattr(obj, "enumerator", SerializationHelper.deserialize_by_tag(elem, "NameToken")),
        "NUMERICAL-VALUE": lambda obj, elem: setattr(obj, "numerical_value", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize EnumerationMappingEntry."""
        super().__init__()
        self.enumerator: NameToken = None
        self.numerical_value: PositiveInteger = None

    def serialize(self) -> ET.Element:
        """Serialize EnumerationMappingEntry to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EnumerationMappingEntry, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize enumerator
        if self.enumerator is not None:
            serialized = SerializationHelper.serialize_item(self.enumerator, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ENUMERATOR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize numerical_value
        if self.numerical_value is not None:
            serialized = SerializationHelper.serialize_item(self.numerical_value, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NUMERICAL-VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EnumerationMappingEntry":
        """Deserialize XML element to EnumerationMappingEntry object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EnumerationMappingEntry object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EnumerationMappingEntry, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ENUMERATOR":
                setattr(obj, "enumerator", SerializationHelper.deserialize_by_tag(child, "NameToken"))
            elif tag == "NUMERICAL-VALUE":
                setattr(obj, "numerical_value", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class EnumerationMappingEntryBuilder(BuilderBase):
    """Builder for EnumerationMappingEntry with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EnumerationMappingEntry = EnumerationMappingEntry()


    def with_enumerator(self, value: NameToken) -> "EnumerationMappingEntryBuilder":
        """Set enumerator attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.enumerator = value
        return self

    def with_numerical_value(self, value: PositiveInteger) -> "EnumerationMappingEntryBuilder":
        """Set numerical_value attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.numerical_value = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "enumerator",
        "numericalValue",
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
        if getattr(self._obj, "enumerator", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError(f"Required attribute 'enumerator' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn(f"Required attribute 'enumerator' is None", UserWarning)
        if getattr(self._obj, "numericalValue", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError(f"Required attribute 'numericalValue' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn(f"Required attribute 'numericalValue' is None", UserWarning)


    def build(self) -> EnumerationMappingEntry:
        """Build and return the EnumerationMappingEntry instance with validation."""
        self._validate_instance()
        return self._obj