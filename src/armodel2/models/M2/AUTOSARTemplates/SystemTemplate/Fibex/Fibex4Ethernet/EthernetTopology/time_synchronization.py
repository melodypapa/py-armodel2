"""TimeSynchronization AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 469)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.time_sync_client_configuration import (
    TimeSyncClientConfiguration,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.time_sync_server_configuration import (
    TimeSyncServerConfiguration,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class TimeSynchronization(ARObject):
    """AUTOSAR TimeSynchronization."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "TIME-SYNCHRONIZATION"


    time_sync_client_configuration: Optional[TimeSyncClientConfiguration]
    time_sync_server_configuration: Optional[TimeSyncServerConfiguration]
    _DESERIALIZE_DISPATCH = {
        "TIME-SYNC-CLIENT-CONFIGURATION": lambda obj, elem: setattr(obj, "time_sync_client_configuration", SerializationHelper.deserialize_by_tag(elem, "TimeSyncClientConfiguration")),
        "TIME-SYNC-SERVER-CONFIGURATION": lambda obj, elem: setattr(obj, "time_sync_server_configuration", SerializationHelper.deserialize_by_tag(elem, "TimeSyncServerConfiguration")),
    }


    def __init__(self) -> None:
        """Initialize TimeSynchronization."""
        super().__init__()
        self.time_sync_client_configuration: Optional[TimeSyncClientConfiguration] = None
        self.time_sync_server_configuration: Optional[TimeSyncServerConfiguration] = None

    def serialize(self) -> ET.Element:
        """Serialize TimeSynchronization to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TimeSynchronization, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize time_sync_client_configuration
        if self.time_sync_client_configuration is not None:
            serialized = SerializationHelper.serialize_item(self.time_sync_client_configuration, "TimeSyncClientConfiguration")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME-SYNC-CLIENT-CONFIGURATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize time_sync_server_configuration
        if self.time_sync_server_configuration is not None:
            serialized = SerializationHelper.serialize_item(self.time_sync_server_configuration, "TimeSyncServerConfiguration")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME-SYNC-SERVER-CONFIGURATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TimeSynchronization":
        """Deserialize XML element to TimeSynchronization object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TimeSynchronization object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TimeSynchronization, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "TIME-SYNC-CLIENT-CONFIGURATION":
                setattr(obj, "time_sync_client_configuration", SerializationHelper.deserialize_by_tag(child, "TimeSyncClientConfiguration"))
            elif tag == "TIME-SYNC-SERVER-CONFIGURATION":
                setattr(obj, "time_sync_server_configuration", SerializationHelper.deserialize_by_tag(child, "TimeSyncServerConfiguration"))

        return obj



class TimeSynchronizationBuilder(BuilderBase):
    """Builder for TimeSynchronization with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TimeSynchronization = TimeSynchronization()


    def with_time_sync_client_configuration(self, value: Optional[TimeSyncClientConfiguration]) -> "TimeSynchronizationBuilder":
        """Set time_sync_client_configuration attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'time_sync_client_configuration' is required and cannot be None")
        self._obj.time_sync_client_configuration = value
        return self

    def with_time_sync_server_configuration(self, value: Optional[TimeSyncServerConfiguration]) -> "TimeSynchronizationBuilder":
        """Set time_sync_server_configuration attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'time_sync_server_configuration' is required and cannot be None")
        self._obj.time_sync_server_configuration = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "timeSyncClientConfiguration",
        "timeSyncServerConfiguration",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> TimeSynchronization:
        """Build and return the TimeSynchronization instance with validation."""
        self._validate_instance()
        return self._obj