"""MixedContentForLongName AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 62)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_InlineTextModel.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.MSR.Documentation.TextModel.InlineTextElements import (
    Superscript,
)
from armodel2.models.M2.MSR.Documentation.TextModel.InlineTextElements.emphasis_text import (
    EmphasisText,
)
from armodel2.models.M2.MSR.Documentation.TextModel.InlineTextElements.index_entry import (
    IndexEntry,
)
from armodel2.models.M2.MSR.Documentation.TextModel.InlineTextElements.tt import (
    Tt,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class MixedContentForLongName(ARObject, ABC):
    """AUTOSAR MixedContentForLongName."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    e: EmphasisText
    ie: IndexEntry
    sub: Superscript
    sup: Superscript
    tt: Tt
    _DESERIALIZE_DISPATCH = {
        "E": lambda obj, elem: setattr(obj, "e", SerializationHelper.deserialize_by_tag(elem, "EmphasisText")),
        "IE": lambda obj, elem: setattr(obj, "ie", SerializationHelper.deserialize_by_tag(elem, "IndexEntry")),
        "SUB": lambda obj, elem: setattr(obj, "sub", SerializationHelper.deserialize_by_tag(elem, "Superscript")),
        "SUP": lambda obj, elem: setattr(obj, "sup", SerializationHelper.deserialize_by_tag(elem, "Superscript")),
        "TT": lambda obj, elem: setattr(obj, "tt", SerializationHelper.deserialize_by_tag(elem, "Tt")),
    }


    def __init__(self) -> None:
        """Initialize MixedContentForLongName."""
        super().__init__()
        self.e: EmphasisText = None
        self.ie: IndexEntry = None
        self.sub: Superscript = None
        self.sup: Superscript = None
        self.tt: Tt = None

    def serialize(self) -> ET.Element:
        """Serialize MixedContentForLongName to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(MixedContentForLongName, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize e
        if self.e is not None:
            serialized = SerializationHelper.serialize_item(self.e, "EmphasisText")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("E")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ie
        if self.ie is not None:
            serialized = SerializationHelper.serialize_item(self.ie, "IndexEntry")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

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

        # Serialize tt
        if self.tt is not None:
            serialized = SerializationHelper.serialize_item(self.tt, "Tt")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MixedContentForLongName":
        """Deserialize XML element to MixedContentForLongName object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MixedContentForLongName object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(MixedContentForLongName, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "E":
                setattr(obj, "e", SerializationHelper.deserialize_by_tag(child, "EmphasisText"))
            elif tag == "IE":
                setattr(obj, "ie", SerializationHelper.deserialize_by_tag(child, "IndexEntry"))
            elif tag == "SUB":
                setattr(obj, "sub", SerializationHelper.deserialize_by_tag(child, "Superscript"))
            elif tag == "SUP":
                setattr(obj, "sup", SerializationHelper.deserialize_by_tag(child, "Superscript"))
            elif tag == "TT":
                setattr(obj, "tt", SerializationHelper.deserialize_by_tag(child, "Tt"))

        return obj



class MixedContentForLongNameBuilder(BuilderBase, ABC):
    """Builder for MixedContentForLongName with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: MixedContentForLongName = MixedContentForLongName()


    def with_e(self, value: EmphasisText) -> "MixedContentForLongNameBuilder":
        """Set e attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.e = value
        return self

    def with_ie(self, value: IndexEntry) -> "MixedContentForLongNameBuilder":
        """Set ie attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ie = value
        return self

    def with_sub(self, value: Superscript) -> "MixedContentForLongNameBuilder":
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

    def with_sup(self, value: Superscript) -> "MixedContentForLongNameBuilder":
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

    def with_tt(self, value: Tt) -> "MixedContentForLongNameBuilder":
        """Set tt attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tt = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "e",
        "ie",
        "sub",
        "sup",
        "tt",
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
        if getattr(self._obj, "e", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'e' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'e' is None", UserWarning)
        if getattr(self._obj, "ie", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'ie' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'ie' is None", UserWarning)
        if getattr(self._obj, "sub", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'sub' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'sub' is None", UserWarning)
        if getattr(self._obj, "sup", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'sup' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'sup' is None", UserWarning)
        if getattr(self._obj, "tt", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'tt' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'tt' is None", UserWarning)


    @abstractmethod
    def build(self) -> MixedContentForLongName:
        """Build and return the MixedContentForLongName instance (abstract)."""
        raise NotImplementedError