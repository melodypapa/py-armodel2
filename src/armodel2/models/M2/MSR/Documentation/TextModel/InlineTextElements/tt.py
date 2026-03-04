"""Tt AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 318)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_InlineTextElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    String,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class Tt(ARObject):
    """AUTOSAR Tt."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "TT"


    term: String
    tex_render: Optional[String]
    type: NameToken
    _DESERIALIZE_DISPATCH = {
        "TERM": lambda obj, elem: setattr(obj, "term", SerializationHelper.deserialize_by_tag(elem, "String")),
        "TEX-RENDER": lambda obj, elem: setattr(obj, "tex_render", SerializationHelper.deserialize_by_tag(elem, "String")),
        "TYPE": lambda obj, elem: setattr(obj, "type", SerializationHelper.deserialize_by_tag(elem, "NameToken")),
    }


    def __init__(self) -> None:
        """Initialize Tt."""
        super().__init__()
        self.term: String = None
        self.tex_render: Optional[String] = None
        self.type: NameToken = None

    def serialize(self) -> ET.Element:
        """Serialize Tt to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Tt, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize term
        if self.term is not None:
            serialized = SerializationHelper.serialize_item(self.term, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TERM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tex_render
        if self.tex_render is not None:
            serialized = SerializationHelper.serialize_item(self.tex_render, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TEX-RENDER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize type
        if self.type is not None:
            serialized = SerializationHelper.serialize_item(self.type, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Tt":
        """Deserialize XML element to Tt object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Tt object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Tt, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "TERM":
                setattr(obj, "term", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "TEX-RENDER":
                setattr(obj, "tex_render", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "TYPE":
                setattr(obj, "type", SerializationHelper.deserialize_by_tag(child, "NameToken"))

        return obj



class TtBuilder(BuilderBase):
    """Builder for Tt with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: Tt = Tt()


    def with_term(self, value: String) -> "TtBuilder":
        """Set term attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.term = value
        return self

    def with_tex_render(self, value: Optional[String]) -> "TtBuilder":
        """Set tex_render attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tex_render = value
        return self

    def with_type(self, value: NameToken) -> "TtBuilder":
        """Set type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.type = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "term",
        "type",
    }
    _OPTIONAL_ATTRIBUTES = {
        "texRender",
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
        if getattr(self._obj, "term", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'term' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'term' is None", UserWarning)
        if getattr(self._obj, "type", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'type' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'type' is None", UserWarning)


    def build(self) -> Tt:
        """Build and return the Tt instance with validation."""
        self._validate_instance()
        return self._obj