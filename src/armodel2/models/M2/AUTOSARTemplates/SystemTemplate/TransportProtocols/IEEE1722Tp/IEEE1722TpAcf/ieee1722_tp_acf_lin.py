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
        "BASE-FREQUENCY": lambda obj, elem: setattr(obj, "base_frequency", elem.text),
        "FRAME-SYNC-ENABLED": lambda obj, elem: setattr(obj, "frame_sync_enabled", elem.text),
        "TIMESTAMP": lambda obj, elem: setattr(obj, "timestamp", elem.text),
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

        # Parse base_frequency
        child = SerializationHelper.find_child_element(element, "BASE-FREQUENCY")
        if child is not None:
            base_frequency_value = child.text
            obj.base_frequency = base_frequency_value

        # Parse frame_sync_enabled
        child = SerializationHelper.find_child_element(element, "FRAME-SYNC-ENABLED")
        if child is not None:
            frame_sync_enabled_value = child.text
            obj.frame_sync_enabled = frame_sync_enabled_value

        # Parse timestamp
        child = SerializationHelper.find_child_element(element, "TIMESTAMP")
        if child is not None:
            timestamp_value = child.text
            obj.timestamp = timestamp_value

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
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
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
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
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
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.timestamp = value
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


    def build(self) -> IEEE1722TpAcfLin:
        """Build and return the IEEE1722TpAcfLin instance with validation."""
        self._validate_instance()
        pass
        return self._obj