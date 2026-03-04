"""DltConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 722)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Dlt.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel2.models.M2.AUTOSARTemplates.LogAndTraceExtract.dlt_ecu import (
    DltEcu,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Dlt.dlt_log_channel import (
    DltLogChannel,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DltConfig(ARObject):
    """AUTOSAR DltConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DLT-CONFIG"


    dlt_ecu_ref: Optional[ARRef]
    dlt_log_channels: list[DltLogChannel]
    session_id: Optional[Boolean]
    timestamp: Optional[Boolean]
    _DESERIALIZE_DISPATCH = {
        "DLT-ECU-REF": lambda obj, elem: setattr(obj, "dlt_ecu_ref", ARRef.deserialize(elem)),
        "DLT-LOG-CHANNELS": lambda obj, elem: obj.dlt_log_channels.append(SerializationHelper.deserialize_by_tag(elem, "DltLogChannel")),
        "SESSION-ID": lambda obj, elem: setattr(obj, "session_id", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "TIMESTAMP": lambda obj, elem: setattr(obj, "timestamp", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
    }


    def __init__(self) -> None:
        """Initialize DltConfig."""
        super().__init__()
        self.dlt_ecu_ref: Optional[ARRef] = None
        self.dlt_log_channels: list[DltLogChannel] = []
        self.session_id: Optional[Boolean] = None
        self.timestamp: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize DltConfig to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DltConfig, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize dlt_ecu_ref
        if self.dlt_ecu_ref is not None:
            serialized = SerializationHelper.serialize_item(self.dlt_ecu_ref, "DltEcu")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DLT-ECU-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize dlt_log_channels (list to container "DLT-LOG-CHANNELS")
        if self.dlt_log_channels:
            wrapper = ET.Element("DLT-LOG-CHANNELS")
            for item in self.dlt_log_channels:
                serialized = SerializationHelper.serialize_item(item, "DltLogChannel")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize session_id
        if self.session_id is not None:
            serialized = SerializationHelper.serialize_item(self.session_id, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SESSION-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize timestamp
        if self.timestamp is not None:
            serialized = SerializationHelper.serialize_item(self.timestamp, "Boolean")
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
    def deserialize(cls, element: ET.Element) -> "DltConfig":
        """Deserialize XML element to DltConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DltConfig object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DltConfig, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DLT-ECU-REF":
                setattr(obj, "dlt_ecu_ref", ARRef.deserialize(child))
            elif tag == "DLT-LOG-CHANNELS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.dlt_log_channels.append(SerializationHelper.deserialize_by_tag(item_elem, "DltLogChannel"))
            elif tag == "SESSION-ID":
                setattr(obj, "session_id", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "TIMESTAMP":
                setattr(obj, "timestamp", SerializationHelper.deserialize_by_tag(child, "Boolean"))

        return obj



class DltConfigBuilder(BuilderBase):
    """Builder for DltConfig with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DltConfig = DltConfig()


    def with_dlt_ecu(self, value: Optional[DltEcu]) -> "DltConfigBuilder":
        """Set dlt_ecu attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.dlt_ecu = value
        return self

    def with_dlt_log_channels(self, items: list[DltLogChannel]) -> "DltConfigBuilder":
        """Set dlt_log_channels list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.dlt_log_channels = list(items) if items else []
        return self

    def with_session_id(self, value: Optional[Boolean]) -> "DltConfigBuilder":
        """Set session_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.session_id = value
        return self

    def with_timestamp(self, value: Optional[Boolean]) -> "DltConfigBuilder":
        """Set timestamp attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.timestamp = value
        return self


    def add_dlt_log_channel(self, item: DltLogChannel) -> "DltConfigBuilder":
        """Add a single item to dlt_log_channels list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.dlt_log_channels.append(item)
        return self

    def clear_dlt_log_channels(self) -> "DltConfigBuilder":
        """Clear all items from dlt_log_channels list.

        Returns:
            self for method chaining
        """
        self._obj.dlt_log_channels = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "dltEcu",
        "dltLogChannel",
        "sessionId",
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


    def build(self) -> DltConfig:
        """Build and return the DltConfig instance with validation."""
        self._validate_instance()
        return self._obj