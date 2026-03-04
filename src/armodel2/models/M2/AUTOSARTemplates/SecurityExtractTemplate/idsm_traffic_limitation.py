"""IdsmTrafficLimitation AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 28)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Float,
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class IdsmTrafficLimitation(Identifiable):
    """AUTOSAR IdsmTrafficLimitation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "IDSM-TRAFFIC-LIMITATION"


    max_bytes_in: Optional[PositiveInteger]
    time_interval: Optional[Float]
    _DESERIALIZE_DISPATCH = {
        "MAX-BYTES-IN": lambda obj, elem: setattr(obj, "max_bytes_in", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "TIME-INTERVAL": lambda obj, elem: setattr(obj, "time_interval", SerializationHelper.deserialize_by_tag(elem, "Float")),
    }


    def __init__(self) -> None:
        """Initialize IdsmTrafficLimitation."""
        super().__init__()
        self.max_bytes_in: Optional[PositiveInteger] = None
        self.time_interval: Optional[Float] = None

    def serialize(self) -> ET.Element:
        """Serialize IdsmTrafficLimitation to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IdsmTrafficLimitation, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize max_bytes_in
        if self.max_bytes_in is not None:
            serialized = SerializationHelper.serialize_item(self.max_bytes_in, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-BYTES-IN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize time_interval
        if self.time_interval is not None:
            serialized = SerializationHelper.serialize_item(self.time_interval, "Float")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME-INTERVAL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IdsmTrafficLimitation":
        """Deserialize XML element to IdsmTrafficLimitation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IdsmTrafficLimitation object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IdsmTrafficLimitation, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "MAX-BYTES-IN":
                setattr(obj, "max_bytes_in", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "TIME-INTERVAL":
                setattr(obj, "time_interval", SerializationHelper.deserialize_by_tag(child, "Float"))

        return obj



class IdsmTrafficLimitationBuilder(IdentifiableBuilder):
    """Builder for IdsmTrafficLimitation with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: IdsmTrafficLimitation = IdsmTrafficLimitation()


    def with_max_bytes_in(self, value: Optional[PositiveInteger]) -> "IdsmTrafficLimitationBuilder":
        """Set max_bytes_in attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.max_bytes_in = value
        return self

    def with_time_interval(self, value: Optional[Float]) -> "IdsmTrafficLimitationBuilder":
        """Set time_interval attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.time_interval = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "maxBytesIn",
        "timeInterval",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> IdsmTrafficLimitation:
        """Build and return the IdsmTrafficLimitation instance with validation."""
        self._validate_instance()
        return self._obj