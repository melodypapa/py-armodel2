"""DltContext AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2017)
  - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (page 9)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_LogAndTraceExtract.classes.json"""

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
    String,
)
from armodel2.models.M2.AUTOSARTemplates.LogAndTraceExtract.dlt_message import (
    DltMessage,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DltContext(ARElement):
    """AUTOSAR DltContext."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DLT-CONTEXT"


    context: Optional[String]
    context_id: Optional[String]
    dlt_message_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "CONTEXT": lambda obj, elem: setattr(obj, "context", SerializationHelper.deserialize_by_tag(elem, "String")),
        "CONTEXT-ID": lambda obj, elem: setattr(obj, "context_id", SerializationHelper.deserialize_by_tag(elem, "String")),
        "DLT-MESSAGE-REFS": lambda obj, elem: [obj.dlt_message_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
    }


    def __init__(self) -> None:
        """Initialize DltContext."""
        super().__init__()
        self.context: Optional[String] = None
        self.context_id: Optional[String] = None
        self.dlt_message_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize DltContext to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DltContext, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize context
        if self.context is not None:
            serialized = SerializationHelper.serialize_item(self.context, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTEXT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize context_id
        if self.context_id is not None:
            serialized = SerializationHelper.serialize_item(self.context_id, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTEXT-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize dlt_message_refs (list to container "DLT-MESSAGE-REFS")
        if self.dlt_message_refs:
            wrapper = ET.Element("DLT-MESSAGE-REFS")
            for item in self.dlt_message_refs:
                serialized = SerializationHelper.serialize_item(item, "DltMessage")
                if serialized is not None:
                    child_elem = ET.Element("DLT-MESSAGE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DltContext":
        """Deserialize XML element to DltContext object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DltContext object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DltContext, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CONTEXT":
                setattr(obj, "context", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "CONTEXT-ID":
                setattr(obj, "context_id", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "DLT-MESSAGE-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.dlt_message_refs.append(ARRef.deserialize(item_elem))

        return obj



class DltContextBuilder(ARElementBuilder):
    """Builder for DltContext with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DltContext = DltContext()


    def with_context(self, value: Optional[String]) -> "DltContextBuilder":
        """Set context attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.context = value
        return self

    def with_context_id(self, value: Optional[String]) -> "DltContextBuilder":
        """Set context_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.context_id = value
        return self

    def with_dlt_messages(self, items: list[DltMessage]) -> "DltContextBuilder":
        """Set dlt_messages list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.dlt_messages = list(items) if items else []
        return self


    def add_dlt_message(self, item: DltMessage) -> "DltContextBuilder":
        """Add a single item to dlt_messages list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.dlt_messages.append(item)
        return self

    def clear_dlt_messages(self) -> "DltContextBuilder":
        """Clear all items from dlt_messages list.

        Returns:
            self for method chaining
        """
        self._obj.dlt_messages = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "context",
        "contextId",
        "dltMessage",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DltContext:
        """Build and return the DltContext instance with validation."""
        self._validate_instance()
        return self._obj