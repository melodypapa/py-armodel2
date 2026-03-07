"""DltApplication AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2017)
  - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (page 8)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_LogAndTraceExtract.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel2.models.M2.AUTOSARTemplates.LogAndTraceExtract.dlt_context import (
    DltContext,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DltApplication(Identifiable):
    """AUTOSAR DltApplication."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DLT-APPLICATION"


    application: Optional[String]
    application_id: Optional[String]
    context_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "APPLICATION": lambda obj, elem: setattr(obj, "application", SerializationHelper.deserialize_by_tag(elem, "String")),
        "APPLICATION-ID": lambda obj, elem: setattr(obj, "application_id", SerializationHelper.deserialize_by_tag(elem, "String")),
        "CONTEXT-REFS": lambda obj, elem: [obj.context_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
    }


    def __init__(self) -> None:
        """Initialize DltApplication."""
        super().__init__()
        self.application: Optional[String] = None
        self.application_id: Optional[String] = None
        self.context_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize DltApplication to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DltApplication, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize application
        if self.application is not None:
            serialized = SerializationHelper.serialize_item(self.application, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("APPLICATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize application_id
        if self.application_id is not None:
            serialized = SerializationHelper.serialize_item(self.application_id, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("APPLICATION-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize context_refs (list to container "CONTEXT-REFS")
        if self.context_refs:
            wrapper = ET.Element("CONTEXT-REFS")
            for item in self.context_refs:
                serialized = SerializationHelper.serialize_item(item, "DltContext")
                if serialized is not None:
                    child_elem = ET.Element("CONTEXT-REF")
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
    def deserialize(cls, element: ET.Element) -> "DltApplication":
        """Deserialize XML element to DltApplication object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DltApplication object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DltApplication, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "APPLICATION":
                setattr(obj, "application", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "APPLICATION-ID":
                setattr(obj, "application_id", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "CONTEXT-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.context_refs.append(ARRef.deserialize(item_elem))

        return obj



class DltApplicationBuilder(IdentifiableBuilder):
    """Builder for DltApplication with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DltApplication = DltApplication()


    def with_application(self, value: Optional[String]) -> "DltApplicationBuilder":
        """Set application attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'application' is required and cannot be None")
        self._obj.application = value
        return self

    def with_application_id(self, value: Optional[String]) -> "DltApplicationBuilder":
        """Set application_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'application_id' is required and cannot be None")
        self._obj.application_id = value
        return self

    def with_contexts(self, items: list[DltContext]) -> "DltApplicationBuilder":
        """Set contexts list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.contexts = list(items) if items else []
        return self


    def add_context(self, item: DltContext) -> "DltApplicationBuilder":
        """Add a single item to contexts list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.contexts.append(item)
        return self

    def clear_contexts(self) -> "DltApplicationBuilder":
        """Clear all items from contexts list.

        Returns:
            self for method chaining
        """
        self._obj.contexts = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "application",
        "applicationId",
        "context",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DltApplication:
        """Build and return the DltApplication instance with validation."""
        self._validate_instance()
        return self._obj