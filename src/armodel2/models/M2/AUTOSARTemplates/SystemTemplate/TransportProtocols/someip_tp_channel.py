"""SomeipTpChannel AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 620)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SomeipTpChannel(Identifiable):
    """AUTOSAR SomeipTpChannel."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SOMEIP-TP-CHANNEL"


    burst_size: Optional[PositiveInteger]
    rx_timeout_time: Optional[TimeValue]
    separation_time: Optional[TimeValue]
    _DESERIALIZE_DISPATCH = {
        "BURST-SIZE": lambda obj, elem: setattr(obj, "burst_size", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "RX-TIMEOUT-TIME": lambda obj, elem: setattr(obj, "rx_timeout_time", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "SEPARATION-TIME": lambda obj, elem: setattr(obj, "separation_time", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
    }


    def __init__(self) -> None:
        """Initialize SomeipTpChannel."""
        super().__init__()
        self.burst_size: Optional[PositiveInteger] = None
        self.rx_timeout_time: Optional[TimeValue] = None
        self.separation_time: Optional[TimeValue] = None

    def serialize(self) -> ET.Element:
        """Serialize SomeipTpChannel to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SomeipTpChannel, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize burst_size
        if self.burst_size is not None:
            serialized = SerializationHelper.serialize_item(self.burst_size, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BURST-SIZE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rx_timeout_time
        if self.rx_timeout_time is not None:
            serialized = SerializationHelper.serialize_item(self.rx_timeout_time, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RX-TIMEOUT-TIME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize separation_time
        if self.separation_time is not None:
            serialized = SerializationHelper.serialize_item(self.separation_time, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SEPARATION-TIME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SomeipTpChannel":
        """Deserialize XML element to SomeipTpChannel object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SomeipTpChannel object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SomeipTpChannel, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "BURST-SIZE":
                setattr(obj, "burst_size", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "RX-TIMEOUT-TIME":
                setattr(obj, "rx_timeout_time", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "SEPARATION-TIME":
                setattr(obj, "separation_time", SerializationHelper.deserialize_by_tag(child, "TimeValue"))

        return obj



class SomeipTpChannelBuilder(IdentifiableBuilder):
    """Builder for SomeipTpChannel with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SomeipTpChannel = SomeipTpChannel()


    def with_burst_size(self, value: Optional[PositiveInteger]) -> "SomeipTpChannelBuilder":
        """Set burst_size attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'burst_size' is required and cannot be None")
        self._obj.burst_size = value
        return self

    def with_rx_timeout_time(self, value: Optional[TimeValue]) -> "SomeipTpChannelBuilder":
        """Set rx_timeout_time attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'rx_timeout_time' is required and cannot be None")
        self._obj.rx_timeout_time = value
        return self

    def with_separation_time(self, value: Optional[TimeValue]) -> "SomeipTpChannelBuilder":
        """Set separation_time attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'separation_time' is required and cannot be None")
        self._obj.separation_time = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "burstSize",
        "rxTimeoutTime",
        "separationTime",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> SomeipTpChannel:
        """Build and return the SomeipTpChannel instance with validation."""
        self._validate_instance()
        return self._obj