"""SecurityEventDefinition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 259)
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 17)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SecurityExtractTemplate.ids_common_element import (
    IdsCommonElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SecurityExtractTemplate.ids_common_element import IdsCommonElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SecurityEventDefinition(IdsCommonElement):
    """AUTOSAR SecurityEventDefinition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SECURITY-EVENT-DEFINITION"


    event_symbol_name: Optional[Any]
    id: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "EVENT-SYMBOL-NAME": lambda obj, elem: setattr(obj, "event_symbol_name", SerializationHelper.deserialize_by_tag(elem, "any (SymbolPropsName)")),
        "ID": lambda obj, elem: setattr(obj, "id", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize SecurityEventDefinition."""
        super().__init__()
        self.event_symbol_name: Optional[Any] = None
        self.id: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize SecurityEventDefinition to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SecurityEventDefinition, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize event_symbol_name
        if self.event_symbol_name is not None:
            serialized = SerializationHelper.serialize_item(self.event_symbol_name, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EVENT-SYMBOL-NAME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize id
        if self.id is not None:
            serialized = SerializationHelper.serialize_item(self.id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SecurityEventDefinition":
        """Deserialize XML element to SecurityEventDefinition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SecurityEventDefinition object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SecurityEventDefinition, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "EVENT-SYMBOL-NAME":
                setattr(obj, "event_symbol_name", SerializationHelper.deserialize_by_tag(child, "any (SymbolPropsName)"))
            elif tag == "ID":
                setattr(obj, "id", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class SecurityEventDefinitionBuilder(IdsCommonElementBuilder):
    """Builder for SecurityEventDefinition with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SecurityEventDefinition = SecurityEventDefinition()


    def with_event_symbol_name(self, value: Optional[any (SymbolPropsName)]) -> "SecurityEventDefinitionBuilder":
        """Set event_symbol_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.event_symbol_name = value
        return self

    def with_id(self, value: Optional[PositiveInteger]) -> "SecurityEventDefinitionBuilder":
        """Set id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.id = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "eventSymbolName",
        "id",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> SecurityEventDefinition:
        """Build and return the SecurityEventDefinition instance with validation."""
        self._validate_instance()
        return self._obj