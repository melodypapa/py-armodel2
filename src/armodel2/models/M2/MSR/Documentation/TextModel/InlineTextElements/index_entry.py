"""IndexEntry AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 317)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_InlineTextElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.MSR.Documentation.TextModel.InlineTextElements import (
    Superscript,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class IndexEntry(ARObject):
    """AUTOSAR IndexEntry."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "INDEX-ENTRY"


    sub: Superscript
    sup: Superscript
    _DESERIALIZE_DISPATCH = {
        "SUB": lambda obj, elem: setattr(obj, "sub", SerializationHelper.deserialize_by_tag(elem, "Superscript")),
        "SUP": lambda obj, elem: setattr(obj, "sup", SerializationHelper.deserialize_by_tag(elem, "Superscript")),
    }


    def __init__(self) -> None:
        """Initialize IndexEntry."""
        super().__init__()
        self.sub: Superscript = None
        self.sup: Superscript = None

    def serialize(self) -> ET.Element:
        """Serialize IndexEntry to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IndexEntry, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize sub
        if self.sub is not None:
            serialized = SerializationHelper.serialize_item(self.sub, "Superscript")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SUB")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sup
        if self.sup is not None:
            serialized = SerializationHelper.serialize_item(self.sup, "Superscript")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SUP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IndexEntry":
        """Deserialize XML element to IndexEntry object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IndexEntry object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IndexEntry, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "SUB":
                setattr(obj, "sub", SerializationHelper.deserialize_by_tag(child, "Superscript"))
            elif tag == "SUP":
                setattr(obj, "sup", SerializationHelper.deserialize_by_tag(child, "Superscript"))

        return obj



class IndexEntryBuilder(BuilderBase):
    """Builder for IndexEntry with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: IndexEntry = IndexEntry()


    def with_sub(self, value: Superscript) -> "IndexEntryBuilder":
        """Set sub attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sub = value
        return self

    def with_sup(self, value: Superscript) -> "IndexEntryBuilder":
        """Set sup attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sup = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "sub",
        "sup",
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
        if getattr(self._obj, "sub", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError(f"Required attribute 'sub' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn(f"Required attribute 'sub' is None", UserWarning)
        if getattr(self._obj, "sup", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError(f"Required attribute 'sup' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn(f"Required attribute 'sup' is None", UserWarning)


    def build(self) -> IndexEntry:
        """Build and return the IndexEntry instance with validation."""
        self._validate_instance()
        return self._obj