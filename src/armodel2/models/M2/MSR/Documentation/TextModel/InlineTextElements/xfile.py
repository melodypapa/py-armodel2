"""Xfile AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 319)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_InlineTextElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.single_language_referrable import (
    SingleLanguageReferrable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.single_language_referrable import SingleLanguageReferrableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class Xfile(SingleLanguageReferrable):
    """AUTOSAR Xfile."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "XFILE"


    tool: Optional[String]
    tool_version: Optional[String]
    url: Optional[Any]
    _DESERIALIZE_DISPATCH = {
        "TOOL": lambda obj, elem: setattr(obj, "tool", SerializationHelper.deserialize_by_tag(elem, "String")),
        "TOOL-VERSION": lambda obj, elem: setattr(obj, "tool_version", SerializationHelper.deserialize_by_tag(elem, "String")),
        "URL": lambda obj, elem: setattr(obj, "url", SerializationHelper.deserialize_by_tag(elem, "any (Url)")),
    }


    def __init__(self) -> None:
        """Initialize Xfile."""
        super().__init__()
        self.tool: Optional[String] = None
        self.tool_version: Optional[String] = None
        self.url: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize Xfile to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Xfile, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize tool
        if self.tool is not None:
            serialized = SerializationHelper.serialize_item(self.tool, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TOOL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tool_version
        if self.tool_version is not None:
            serialized = SerializationHelper.serialize_item(self.tool_version, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TOOL-VERSION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize url
        if self.url is not None:
            serialized = SerializationHelper.serialize_item(self.url, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("URL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Xfile":
        """Deserialize XML element to Xfile object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Xfile object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Xfile, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "TOOL":
                setattr(obj, "tool", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "TOOL-VERSION":
                setattr(obj, "tool_version", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "URL":
                setattr(obj, "url", SerializationHelper.deserialize_by_tag(child, "any (Url)"))

        return obj



class XfileBuilder(SingleLanguageReferrableBuilder):
    """Builder for Xfile with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: Xfile = Xfile()


    def with_tool(self, value: Optional[String]) -> "XfileBuilder":
        """Set tool attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'tool' is required and cannot be None")
        self._obj.tool = value
        return self

    def with_tool_version(self, value: Optional[String]) -> "XfileBuilder":
        """Set tool_version attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'tool_version' is required and cannot be None")
        self._obj.tool_version = value
        return self

    def with_url(self, value: Optional[Any]) -> "XfileBuilder":
        """Set url attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'url' is required and cannot be None")
        self._obj.url = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "tool",
        "toolVersion",
        "url",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> Xfile:
        """Build and return the Xfile instance with validation."""
        self._validate_instance()
        return self._obj