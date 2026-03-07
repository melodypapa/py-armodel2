"""IEEE1722TpAcfLin AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 666)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols_IEEE1722Tp_IEEE1722TpAcf.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf.ieee1722_tp_acf_bus import (
    IEEE1722TpAcfBus,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf.ieee1722_tp_acf_bus import IEEE1722TpAcfBusBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class IEEE1722TpAcfLin(IEEE1722TpAcfBus):
    """AUTOSAR IEEE1722TpAcfLin."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "I-E-E-E1722-TP-ACF-LIN"


    base_frequency: Optional[PositiveInteger]
    frame_sync_enabled: Optional[Boolean]
    timestamp: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "BASE-FREQUENCY": lambda obj, elem: setattr(obj, "base_frequency", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "FRAME-SYNC-ENABLED": lambda obj, elem: setattr(obj, "frame_sync_enabled", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "TIMESTAMP": lambda obj, elem: setattr(obj, "timestamp", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize IEEE1722TpAcfLin."""
        super().__init__()
        self.base_frequency: Optional[PositiveInteger] = None
        self.frame_sync_enabled: Optional[Boolean] = None
        self.timestamp: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize IEEE1722TpAcfLin to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IEEE1722TpAcfLin, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize base_frequency
        if self.base_frequency is not None:
            serialized = SerializationHelper.serialize_item(self.base_frequency, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BASE-FREQUENCY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize frame_sync_enabled
        if self.frame_sync_enabled is not None:
            serialized = SerializationHelper.serialize_item(self.frame_sync_enabled, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FRAME-SYNC-ENABLED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize timestamp
        if self.timestamp is not None:
            serialized = SerializationHelper.serialize_item(self.timestamp, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMESTAMP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IEEE1722TpAcfLin":
        """Deserialize XML element to IEEE1722TpAcfLin object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IEEE1722TpAcfLin object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IEEE1722TpAcfLin, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "BASE-FREQUENCY":
                setattr(obj, "base_frequency", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "FRAME-SYNC-ENABLED":
                setattr(obj, "frame_sync_enabled", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "TIMESTAMP":
                setattr(obj, "timestamp", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class IEEE1722TpAcfLinBuilder(IEEE1722TpAcfBusBuilder):
    """Builder for IEEE1722TpAcfLin with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: IEEE1722TpAcfLin = IEEE1722TpAcfLin()


    def with_base_frequency(self, value: Optional[PositiveInteger]) -> "IEEE1722TpAcfLinBuilder":
        """Set base_frequency attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'base_frequency' is required and cannot be None")
        self._obj.base_frequency = value
        return self

    def with_frame_sync_enabled(self, value: Optional[Boolean]) -> "IEEE1722TpAcfLinBuilder":
        """Set frame_sync_enabled attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'frame_sync_enabled' is required and cannot be None")
        self._obj.frame_sync_enabled = value
        return self

    def with_timestamp(self, value: Optional[PositiveInteger]) -> "IEEE1722TpAcfLinBuilder":
        """Set timestamp attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'timestamp' is required and cannot be None")
        self._obj.timestamp = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "baseFrequency",
        "frameSyncEnabled",
        "timestamp",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> IEEE1722TpAcfLin:
        """Build and return the IEEE1722TpAcfLin instance with validation."""
        self._validate_instance()
        return self._obj