"""SomeipSdClientEventGroupTimingConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 521)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.request_response_delay import (
    RequestResponseDelay,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SomeipSdClientEventGroupTimingConfig(ARElement):
    """AUTOSAR SomeipSdClientEventGroupTimingConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SOMEIP-SD-CLIENT-EVENT-GROUP-TIMING-CONFIG"


    request: Optional[RequestResponseDelay]
    subscribe: Optional[PositiveInteger]
    time_to_live: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "REQUEST": lambda obj, elem: setattr(obj, "request", SerializationHelper.deserialize_by_tag(elem, "RequestResponseDelay")),
        "SUBSCRIBE": lambda obj, elem: setattr(obj, "subscribe", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "TIME-TO-LIVE": lambda obj, elem: setattr(obj, "time_to_live", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize SomeipSdClientEventGroupTimingConfig."""
        super().__init__()
        self.request: Optional[RequestResponseDelay] = None
        self.subscribe: Optional[PositiveInteger] = None
        self.time_to_live: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize SomeipSdClientEventGroupTimingConfig to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SomeipSdClientEventGroupTimingConfig, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize request
        if self.request is not None:
            serialized = SerializationHelper.serialize_item(self.request, "RequestResponseDelay")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REQUEST")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize subscribe
        if self.subscribe is not None:
            serialized = SerializationHelper.serialize_item(self.subscribe, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SUBSCRIBE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize time_to_live
        if self.time_to_live is not None:
            serialized = SerializationHelper.serialize_item(self.time_to_live, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME-TO-LIVE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SomeipSdClientEventGroupTimingConfig":
        """Deserialize XML element to SomeipSdClientEventGroupTimingConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SomeipSdClientEventGroupTimingConfig object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SomeipSdClientEventGroupTimingConfig, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "REQUEST":
                setattr(obj, "request", SerializationHelper.deserialize_by_tag(child, "RequestResponseDelay"))
            elif tag == "SUBSCRIBE":
                setattr(obj, "subscribe", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "TIME-TO-LIVE":
                setattr(obj, "time_to_live", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class SomeipSdClientEventGroupTimingConfigBuilder(ARElementBuilder):
    """Builder for SomeipSdClientEventGroupTimingConfig with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SomeipSdClientEventGroupTimingConfig = SomeipSdClientEventGroupTimingConfig()


    def with_request(self, value: Optional[RequestResponseDelay]) -> "SomeipSdClientEventGroupTimingConfigBuilder":
        """Set request attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.request = value
        return self

    def with_subscribe(self, value: Optional[PositiveInteger]) -> "SomeipSdClientEventGroupTimingConfigBuilder":
        """Set subscribe attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.subscribe = value
        return self

    def with_time_to_live(self, value: Optional[PositiveInteger]) -> "SomeipSdClientEventGroupTimingConfigBuilder":
        """Set time_to_live attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.time_to_live = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "request",
        "subscribe",
        "timeToLive",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> SomeipSdClientEventGroupTimingConfig:
        """Build and return the SomeipSdClientEventGroupTimingConfig instance with validation."""
        self._validate_instance()
        return self._obj