"""DocumentViewSelectable AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 340)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_PaginationAndView.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameTokens,
)
from armodel2.models.M2.MSR.Documentation.BlockElements.PaginationAndView import (
    ViewTokens,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DocumentViewSelectable(ARObject, ABC):
    """AUTOSAR DocumentViewSelectable."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    si: NameTokens
    view: Optional[ViewTokens]
    _DESERIALIZE_DISPATCH = {
        "SI": lambda obj, elem: setattr(obj, "si", SerializationHelper.deserialize_by_tag(elem, "NameTokens")),
        "VIEW": lambda obj, elem: setattr(obj, "view", SerializationHelper.deserialize_by_tag(elem, "ViewTokens")),
    }


    def __init__(self) -> None:
        """Initialize DocumentViewSelectable."""
        super().__init__()
        self.si: NameTokens = None
        self.view: Optional[ViewTokens] = None

    def serialize(self) -> ET.Element:
        """Serialize DocumentViewSelectable to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DocumentViewSelectable, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize si
        if self.si is not None:
            serialized = SerializationHelper.serialize_item(self.si, "NameTokens")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SI")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize view
        if self.view is not None:
            serialized = SerializationHelper.serialize_item(self.view, "ViewTokens")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VIEW")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DocumentViewSelectable":
        """Deserialize XML element to DocumentViewSelectable object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DocumentViewSelectable object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DocumentViewSelectable, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "SI":
                setattr(obj, "si", SerializationHelper.deserialize_by_tag(child, "NameTokens"))
            elif tag == "VIEW":
                setattr(obj, "view", SerializationHelper.deserialize_by_tag(child, "ViewTokens"))

        return obj



class DocumentViewSelectableBuilder(BuilderBase, ABC):
    """Builder for DocumentViewSelectable with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DocumentViewSelectable = DocumentViewSelectable()


    def with_si(self, value: NameTokens) -> "DocumentViewSelectableBuilder":
        """Set si attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute 'si' is required and cannot be None")
        self._obj.si = value
        return self

    def with_view(self, value: Optional[ViewTokens]) -> "DocumentViewSelectableBuilder":
        """Set view attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'view' is required and cannot be None")
        self._obj.view = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "si",
    }
    _OPTIONAL_ATTRIBUTES = {
        "view",
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
        if getattr(self._obj, "si", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'si' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'si' is None", UserWarning)


    @abstractmethod
    def build(self) -> DocumentViewSelectable:
        """Build and return the DocumentViewSelectable instance (abstract)."""
        raise NotImplementedError