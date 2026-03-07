"""TDHeaderIdRange AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 70)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class TDHeaderIdRange(ARObject):
    """AUTOSAR TDHeaderIdRange."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "T-D-HEADER-ID-RANGE"


    max_header_id: Optional[Integer]
    min_header_id: Optional[Integer]
    _DESERIALIZE_DISPATCH = {
        "MAX-HEADER-ID": lambda obj, elem: setattr(obj, "max_header_id", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "MIN-HEADER-ID": lambda obj, elem: setattr(obj, "min_header_id", SerializationHelper.deserialize_by_tag(elem, "Integer")),
    }


    def __init__(self) -> None:
        """Initialize TDHeaderIdRange."""
        super().__init__()
        self.max_header_id: Optional[Integer] = None
        self.min_header_id: Optional[Integer] = None

    def serialize(self) -> ET.Element:
        """Serialize TDHeaderIdRange to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TDHeaderIdRange, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize max_header_id
        if self.max_header_id is not None:
            serialized = SerializationHelper.serialize_item(self.max_header_id, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-HEADER-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize min_header_id
        if self.min_header_id is not None:
            serialized = SerializationHelper.serialize_item(self.min_header_id, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MIN-HEADER-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDHeaderIdRange":
        """Deserialize XML element to TDHeaderIdRange object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDHeaderIdRange object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TDHeaderIdRange, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "MAX-HEADER-ID":
                setattr(obj, "max_header_id", SerializationHelper.deserialize_by_tag(child, "Integer"))
            elif tag == "MIN-HEADER-ID":
                setattr(obj, "min_header_id", SerializationHelper.deserialize_by_tag(child, "Integer"))

        return obj



class TDHeaderIdRangeBuilder(BuilderBase):
    """Builder for TDHeaderIdRange with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TDHeaderIdRange = TDHeaderIdRange()


    def with_max_header_id(self, value: Optional[Integer]) -> "TDHeaderIdRangeBuilder":
        """Set max_header_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'max_header_id' is required and cannot be None")
        self._obj.max_header_id = value
        return self

    def with_min_header_id(self, value: Optional[Integer]) -> "TDHeaderIdRangeBuilder":
        """Set min_header_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'min_header_id' is required and cannot be None")
        self._obj.min_header_id = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "maxHeaderId",
        "minHeaderId",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> TDHeaderIdRange:
        """Build and return the TDHeaderIdRange instance with validation."""
        self._validate_instance()
        return self._obj