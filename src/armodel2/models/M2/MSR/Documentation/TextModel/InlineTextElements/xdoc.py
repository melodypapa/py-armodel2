"""Xdoc AUTOSAR element.

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
    DateTime,
    String,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class Xdoc(SingleLanguageReferrable):
    """AUTOSAR Xdoc."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "XDOC"


    date: Optional[DateTime]
    number: Optional[String]
    position: Optional[String]
    publisher: Optional[String]
    state: Optional[String]
    url: Optional[Any]
    _DESERIALIZE_DISPATCH = {
        "DATE": lambda obj, elem: setattr(obj, "date", SerializationHelper.deserialize_by_tag(elem, "DateTime")),
        "NUMBER": lambda obj, elem: setattr(obj, "number", SerializationHelper.deserialize_by_tag(elem, "String")),
        "POSITION": lambda obj, elem: setattr(obj, "position", SerializationHelper.deserialize_by_tag(elem, "String")),
        "PUBLISHER": lambda obj, elem: setattr(obj, "publisher", SerializationHelper.deserialize_by_tag(elem, "String")),
        "STATE": lambda obj, elem: setattr(obj, "state", SerializationHelper.deserialize_by_tag(elem, "String")),
        "URL": lambda obj, elem: setattr(obj, "url", SerializationHelper.deserialize_by_tag(elem, "any (Url)")),
    }


    def __init__(self) -> None:
        """Initialize Xdoc."""
        super().__init__()
        self.date: Optional[DateTime] = None
        self.number: Optional[String] = None
        self.position: Optional[String] = None
        self.publisher: Optional[String] = None
        self.state: Optional[String] = None
        self.url: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize Xdoc to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Xdoc, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize date
        if self.date is not None:
            serialized = SerializationHelper.serialize_item(self.date, "DateTime")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize number
        if self.number is not None:
            serialized = SerializationHelper.serialize_item(self.number, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NUMBER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize position
        if self.position is not None:
            serialized = SerializationHelper.serialize_item(self.position, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("POSITION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize publisher
        if self.publisher is not None:
            serialized = SerializationHelper.serialize_item(self.publisher, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PUBLISHER")
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
    def deserialize(cls, element: ET.Element) -> "Xdoc":
        """Deserialize XML element to Xdoc object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Xdoc object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Xdoc, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DATE":
                setattr(obj, "date", SerializationHelper.deserialize_by_tag(child, "DateTime"))
            elif tag == "NUMBER":
                setattr(obj, "number", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "POSITION":
                setattr(obj, "position", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "PUBLISHER":
                setattr(obj, "publisher", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "STATE":
                setattr(obj, "state", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "URL":
                setattr(obj, "url", SerializationHelper.deserialize_by_tag(child, "any (Url)"))

        return obj



class XdocBuilder(SingleLanguageReferrableBuilder):
    """Builder for Xdoc with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: Xdoc = Xdoc()


    def with_date(self, value: Optional[DateTime]) -> "XdocBuilder":
        """Set date attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'date' is required and cannot be None")
        self._obj.date = value
        return self

    def with_number(self, value: Optional[String]) -> "XdocBuilder":
        """Set number attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'number' is required and cannot be None")
        self._obj.number = value
        return self

    def with_position(self, value: Optional[String]) -> "XdocBuilder":
        """Set position attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'position' is required and cannot be None")
        self._obj.position = value
        return self

    def with_publisher(self, value: Optional[String]) -> "XdocBuilder":
        """Set publisher attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'publisher' is required and cannot be None")
        self._obj.publisher = value
        return self

    def with_state(self, value: Optional[String]) -> "XdocBuilder":
        """Set state attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'state' is required and cannot be None")
        self._obj.state = value
        return self

    def with_url(self, value: Optional[Any]) -> "XdocBuilder":
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
        "date",
        "number",
        "position",
        "publisher",
        "state",
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


    def build(self) -> Xdoc:
        """Build and return the Xdoc instance with validation."""
        self._validate_instance()
        return self._obj