"""SomeipSdServerServiceInstanceConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 513)

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
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.initial_sd_delay_config import (
    InitialSdDelayConfig,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.request_response_delay import (
    RequestResponseDelay,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SomeipSdServerServiceInstanceConfig(ARElement):
    """AUTOSAR SomeipSdServerServiceInstanceConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SOMEIP-SD-SERVER-SERVICE-INSTANCE-CONFIG"


    initial_offer_behavior: Optional[InitialSdDelayConfig]
    offer_cyclic_delay: Optional[TimeValue]
    priority: Optional[PositiveInteger]
    request: Optional[RequestResponseDelay]
    service_offer: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "INITIAL-OFFER-BEHAVIOR": lambda obj, elem: setattr(obj, "initial_offer_behavior", InitialSdDelayConfig.deserialize(elem)),
        "OFFER-CYCLIC-DELAY": lambda obj, elem: setattr(obj, "offer_cyclic_delay", elem.text),
        "PRIORITY": lambda obj, elem: setattr(obj, "priority", elem.text),
        "REQUEST": lambda obj, elem: setattr(obj, "request", RequestResponseDelay.deserialize(elem)),
        "SERVICE-OFFER": lambda obj, elem: setattr(obj, "service_offer", elem.text),
    }


    def __init__(self) -> None:
        """Initialize SomeipSdServerServiceInstanceConfig."""
        super().__init__()
        self.initial_offer_behavior: Optional[InitialSdDelayConfig] = None
        self.offer_cyclic_delay: Optional[TimeValue] = None
        self.priority: Optional[PositiveInteger] = None
        self.request: Optional[RequestResponseDelay] = None
        self.service_offer: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize SomeipSdServerServiceInstanceConfig to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SomeipSdServerServiceInstanceConfig, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize initial_offer_behavior
        if self.initial_offer_behavior is not None:
            serialized = SerializationHelper.serialize_item(self.initial_offer_behavior, "InitialSdDelayConfig")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INITIAL-OFFER-BEHAVIOR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize offer_cyclic_delay
        if self.offer_cyclic_delay is not None:
            serialized = SerializationHelper.serialize_item(self.offer_cyclic_delay, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OFFER-CYCLIC-DELAY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize priority
        if self.priority is not None:
            serialized = SerializationHelper.serialize_item(self.priority, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PRIORITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

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

        # Serialize service_offer
        if self.service_offer is not None:
            serialized = SerializationHelper.serialize_item(self.service_offer, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SERVICE-OFFER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SomeipSdServerServiceInstanceConfig":
        """Deserialize XML element to SomeipSdServerServiceInstanceConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SomeipSdServerServiceInstanceConfig object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SomeipSdServerServiceInstanceConfig, cls).deserialize(element)

        # Parse initial_offer_behavior
        child = SerializationHelper.find_child_element(element, "INITIAL-OFFER-BEHAVIOR")
        if child is not None:
            initial_offer_behavior_value = SerializationHelper.deserialize_by_tag(child, "InitialSdDelayConfig")
            obj.initial_offer_behavior = initial_offer_behavior_value

        # Parse offer_cyclic_delay
        child = SerializationHelper.find_child_element(element, "OFFER-CYCLIC-DELAY")
        if child is not None:
            offer_cyclic_delay_value = child.text
            obj.offer_cyclic_delay = offer_cyclic_delay_value

        # Parse priority
        child = SerializationHelper.find_child_element(element, "PRIORITY")
        if child is not None:
            priority_value = child.text
            obj.priority = priority_value

        # Parse request
        child = SerializationHelper.find_child_element(element, "REQUEST")
        if child is not None:
            request_value = SerializationHelper.deserialize_by_tag(child, "RequestResponseDelay")
            obj.request = request_value

        # Parse service_offer
        child = SerializationHelper.find_child_element(element, "SERVICE-OFFER")
        if child is not None:
            service_offer_value = child.text
            obj.service_offer = service_offer_value

        return obj



class SomeipSdServerServiceInstanceConfigBuilder(ARElementBuilder):
    """Builder for SomeipSdServerServiceInstanceConfig with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SomeipSdServerServiceInstanceConfig = SomeipSdServerServiceInstanceConfig()


    def with_initial_offer_behavior(self, value: Optional[InitialSdDelayConfig]) -> "SomeipSdServerServiceInstanceConfigBuilder":
        """Set initial_offer_behavior attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.initial_offer_behavior = value
        return self

    def with_offer_cyclic_delay(self, value: Optional[TimeValue]) -> "SomeipSdServerServiceInstanceConfigBuilder":
        """Set offer_cyclic_delay attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.offer_cyclic_delay = value
        return self

    def with_priority(self, value: Optional[PositiveInteger]) -> "SomeipSdServerServiceInstanceConfigBuilder":
        """Set priority attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.priority = value
        return self

    def with_request(self, value: Optional[RequestResponseDelay]) -> "SomeipSdServerServiceInstanceConfigBuilder":
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

    def with_service_offer(self, value: Optional[PositiveInteger]) -> "SomeipSdServerServiceInstanceConfigBuilder":
        """Set service_offer attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.service_offer = value
        return self




    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Get type hints for the class
        try:
            type_hints_dict = get_type_hints(type(self._obj))
        except Exception:
            # Cannot resolve type hints (e.g., forward references), skip validation
            return

        for attr_name, attr_type in type_hints_dict.items():
            if attr_name.startswith("_"):
                continue

            value = getattr(self._obj, attr_name)

            # Check required fields (not Optional)
            if value is None and not self._is_optional_type(attr_type):
                if mode == BuilderValidationMode.STRICT:
                    raise ValueError(
                        f"Required attribute '{attr_name}' is None"
                    )
                elif mode == BuilderValidationMode.LENIENT:
                    import warnings
                    warnings.warn(
                        f"Required attribute '{attr_name}' is None",
                        UserWarning
                    )

    @staticmethod
    def _is_optional_type(type_hint: Any) -> bool:
        """Check if a type hint is Optional.

        Args:
            type_hint: Type hint to check

        Returns:
            True if type is Optional, False otherwise
        """
        origin = getattr(type_hint, "__origin__", None)
        return origin is Union

    @staticmethod
    def _get_expected_type(type_hint: Any) -> type:
        """Extract expected type from type hint.

        Args:
            type_hint: Type hint to extract from

        Returns:
            Expected type
        """
        if isinstance(type_hint, str):
            return object
        origin = getattr(type_hint, "__origin__", None)
        if origin is Union:
            args = getattr(type_hint, "__args__", [])
            for arg in args:
                if arg is not type(None):
                    return arg
        elif origin is list:
            args = getattr(type_hint, "__args__", [object])
            return args[0] if args else object
        return type_hint if isinstance(type_hint, type) else object


    def build(self) -> SomeipSdServerServiceInstanceConfig:
        """Build and return the SomeipSdServerServiceInstanceConfig instance with validation."""
        self._validate_instance()
        pass
        return self._obj