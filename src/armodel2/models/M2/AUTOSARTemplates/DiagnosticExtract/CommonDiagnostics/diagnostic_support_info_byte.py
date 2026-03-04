"""DiagnosticSupportInfoByte AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 150)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_CommonDiagnostics.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticSupportInfoByte(ARObject):
    """AUTOSAR DiagnosticSupportInfoByte."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-SUPPORT-INFO-BYTE"


    position: Optional[PositiveInteger]
    size: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "POSITION": lambda obj, elem: setattr(obj, "position", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "SIZE": lambda obj, elem: setattr(obj, "size", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticSupportInfoByte."""
        super().__init__()
        self.position: Optional[PositiveInteger] = None
        self.size: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticSupportInfoByte to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticSupportInfoByte, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize position
        if self.position is not None:
            serialized = SerializationHelper.serialize_item(self.position, "PositiveInteger")
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

        # Serialize size
        if self.size is not None:
            serialized = SerializationHelper.serialize_item(self.size, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SIZE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticSupportInfoByte":
        """Deserialize XML element to DiagnosticSupportInfoByte object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticSupportInfoByte object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticSupportInfoByte, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "POSITION":
                setattr(obj, "position", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "SIZE":
                setattr(obj, "size", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class DiagnosticSupportInfoByteBuilder(BuilderBase):
    """Builder for DiagnosticSupportInfoByte with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticSupportInfoByte = DiagnosticSupportInfoByte()


    def with_position(self, value: Optional[PositiveInteger]) -> "DiagnosticSupportInfoByteBuilder":
        """Set position attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.position = value
        return self

    def with_size(self, value: Optional[PositiveInteger]) -> "DiagnosticSupportInfoByteBuilder":
        """Set size attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.size = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "position",
        "size",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DiagnosticSupportInfoByte:
        """Build and return the DiagnosticSupportInfoByte instance with validation."""
        self._validate_instance()
        return self._obj