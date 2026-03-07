"""Ieee1722Tp AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 460)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.transport_protocol_configuration import (
    TransportProtocolConfiguration,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.transport_protocol_configuration import TransportProtocolConfigurationBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class Ieee1722Tp(TransportProtocolConfiguration):
    """AUTOSAR Ieee1722Tp."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "IEEE1722-TP"


    relative: Optional[TimeValue]
    stream_identifier: Optional[PositiveInteger]
    sub_type: Optional[PositiveInteger]
    version: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "RELATIVE": lambda obj, elem: setattr(obj, "relative", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "STREAM-IDENTIFIER": lambda obj, elem: setattr(obj, "stream_identifier", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "SUB-TYPE": lambda obj, elem: setattr(obj, "sub_type", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "VERSION": lambda obj, elem: setattr(obj, "version", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize Ieee1722Tp."""
        super().__init__()
        self.relative: Optional[TimeValue] = None
        self.stream_identifier: Optional[PositiveInteger] = None
        self.sub_type: Optional[PositiveInteger] = None
        self.version: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize Ieee1722Tp to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Ieee1722Tp, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize relative
        if self.relative is not None:
            serialized = SerializationHelper.serialize_item(self.relative, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RELATIVE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize stream_identifier
        if self.stream_identifier is not None:
            serialized = SerializationHelper.serialize_item(self.stream_identifier, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("STREAM-IDENTIFIER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sub_type
        if self.sub_type is not None:
            serialized = SerializationHelper.serialize_item(self.sub_type, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SUB-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize version
        if self.version is not None:
            serialized = SerializationHelper.serialize_item(self.version, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VERSION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Ieee1722Tp":
        """Deserialize XML element to Ieee1722Tp object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Ieee1722Tp object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Ieee1722Tp, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "RELATIVE":
                setattr(obj, "relative", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "STREAM-IDENTIFIER":
                setattr(obj, "stream_identifier", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "SUB-TYPE":
                setattr(obj, "sub_type", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "VERSION":
                setattr(obj, "version", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class Ieee1722TpBuilder(TransportProtocolConfigurationBuilder):
    """Builder for Ieee1722Tp with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: Ieee1722Tp = Ieee1722Tp()


    def with_relative(self, value: Optional[TimeValue]) -> "Ieee1722TpBuilder":
        """Set relative attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'relative' is required and cannot be None")
        self._obj.relative = value
        return self

    def with_stream_identifier(self, value: Optional[PositiveInteger]) -> "Ieee1722TpBuilder":
        """Set stream_identifier attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'stream_identifier' is required and cannot be None")
        self._obj.stream_identifier = value
        return self

    def with_sub_type(self, value: Optional[PositiveInteger]) -> "Ieee1722TpBuilder":
        """Set sub_type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'sub_type' is required and cannot be None")
        self._obj.sub_type = value
        return self

    def with_version(self, value: Optional[PositiveInteger]) -> "Ieee1722TpBuilder":
        """Set version attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'version' is required and cannot be None")
        self._obj.version = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "relative",
        "streamIdentifier",
        "subType",
        "version",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> Ieee1722Tp:
        """Build and return the Ieee1722Tp instance with validation."""
        self._validate_instance()
        return self._obj