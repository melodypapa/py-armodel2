"""IEEE1722TpIidcConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 648)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols_IEEE1722Tp_IEEE1722TpAv.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.ieee1722_tp_av_connection import (
    IEEE1722TpAvConnection,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.ieee1722_tp_av_connection import IEEE1722TpAvConnectionBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class IEEE1722TpIidcConnection(IEEE1722TpAvConnection):
    """AUTOSAR IEEE1722TpIidcConnection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "I-E-E-E1722-TP-IIDC-CONNECTION"


    iidc_channel: Optional[PositiveInteger]
    iidc_data_block: Optional[PositiveInteger]
    iidc_fraction: Optional[PositiveInteger]
    iidc_source: Optional[Boolean]
    iidc_stream: Optional[PositiveInteger]
    iidc_sy: Optional[PositiveInteger]
    iidc_tag: Optional[PositiveInteger]
    iidc_t_code: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "IIDC-CHANNEL": lambda obj, elem: setattr(obj, "iidc_channel", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "IIDC-DATA-BLOCK": lambda obj, elem: setattr(obj, "iidc_data_block", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "IIDC-FRACTION": lambda obj, elem: setattr(obj, "iidc_fraction", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "IIDC-SOURCE": lambda obj, elem: setattr(obj, "iidc_source", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "IIDC-STREAM": lambda obj, elem: setattr(obj, "iidc_stream", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "IIDC-SY": lambda obj, elem: setattr(obj, "iidc_sy", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "IIDC-TAG": lambda obj, elem: setattr(obj, "iidc_tag", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "IIDC-T-CODE": lambda obj, elem: setattr(obj, "iidc_t_code", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize IEEE1722TpIidcConnection."""
        super().__init__()
        self.iidc_channel: Optional[PositiveInteger] = None
        self.iidc_data_block: Optional[PositiveInteger] = None
        self.iidc_fraction: Optional[PositiveInteger] = None
        self.iidc_source: Optional[Boolean] = None
        self.iidc_stream: Optional[PositiveInteger] = None
        self.iidc_sy: Optional[PositiveInteger] = None
        self.iidc_tag: Optional[PositiveInteger] = None
        self.iidc_t_code: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize IEEE1722TpIidcConnection to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IEEE1722TpIidcConnection, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize iidc_channel
        if self.iidc_channel is not None:
            serialized = SerializationHelper.serialize_item(self.iidc_channel, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IIDC-CHANNEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize iidc_data_block
        if self.iidc_data_block is not None:
            serialized = SerializationHelper.serialize_item(self.iidc_data_block, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IIDC-DATA-BLOCK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize iidc_fraction
        if self.iidc_fraction is not None:
            serialized = SerializationHelper.serialize_item(self.iidc_fraction, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IIDC-FRACTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize iidc_source
        if self.iidc_source is not None:
            serialized = SerializationHelper.serialize_item(self.iidc_source, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IIDC-SOURCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize iidc_stream
        if self.iidc_stream is not None:
            serialized = SerializationHelper.serialize_item(self.iidc_stream, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IIDC-STREAM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize iidc_sy
        if self.iidc_sy is not None:
            serialized = SerializationHelper.serialize_item(self.iidc_sy, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IIDC-SY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize iidc_tag
        if self.iidc_tag is not None:
            serialized = SerializationHelper.serialize_item(self.iidc_tag, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IIDC-TAG")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize iidc_t_code
        if self.iidc_t_code is not None:
            serialized = SerializationHelper.serialize_item(self.iidc_t_code, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IIDC-T-CODE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IEEE1722TpIidcConnection":
        """Deserialize XML element to IEEE1722TpIidcConnection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IEEE1722TpIidcConnection object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IEEE1722TpIidcConnection, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "IIDC-CHANNEL":
                setattr(obj, "iidc_channel", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "IIDC-DATA-BLOCK":
                setattr(obj, "iidc_data_block", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "IIDC-FRACTION":
                setattr(obj, "iidc_fraction", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "IIDC-SOURCE":
                setattr(obj, "iidc_source", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "IIDC-STREAM":
                setattr(obj, "iidc_stream", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "IIDC-SY":
                setattr(obj, "iidc_sy", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "IIDC-TAG":
                setattr(obj, "iidc_tag", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "IIDC-T-CODE":
                setattr(obj, "iidc_t_code", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class IEEE1722TpIidcConnectionBuilder(IEEE1722TpAvConnectionBuilder):
    """Builder for IEEE1722TpIidcConnection with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: IEEE1722TpIidcConnection = IEEE1722TpIidcConnection()


    def with_iidc_channel(self, value: Optional[PositiveInteger]) -> "IEEE1722TpIidcConnectionBuilder":
        """Set iidc_channel attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.iidc_channel = value
        return self

    def with_iidc_data_block(self, value: Optional[PositiveInteger]) -> "IEEE1722TpIidcConnectionBuilder":
        """Set iidc_data_block attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.iidc_data_block = value
        return self

    def with_iidc_fraction(self, value: Optional[PositiveInteger]) -> "IEEE1722TpIidcConnectionBuilder":
        """Set iidc_fraction attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.iidc_fraction = value
        return self

    def with_iidc_source(self, value: Optional[Boolean]) -> "IEEE1722TpIidcConnectionBuilder":
        """Set iidc_source attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.iidc_source = value
        return self

    def with_iidc_stream(self, value: Optional[PositiveInteger]) -> "IEEE1722TpIidcConnectionBuilder":
        """Set iidc_stream attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.iidc_stream = value
        return self

    def with_iidc_sy(self, value: Optional[PositiveInteger]) -> "IEEE1722TpIidcConnectionBuilder":
        """Set iidc_sy attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.iidc_sy = value
        return self

    def with_iidc_tag(self, value: Optional[PositiveInteger]) -> "IEEE1722TpIidcConnectionBuilder":
        """Set iidc_tag attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.iidc_tag = value
        return self

    def with_iidc_t_code(self, value: Optional[PositiveInteger]) -> "IEEE1722TpIidcConnectionBuilder":
        """Set iidc_t_code attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.iidc_t_code = value
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


    def build(self) -> IEEE1722TpIidcConnection:
        """Build and return the IEEE1722TpIidcConnection instance with validation."""
        self._validate_instance()
        pass
        return self._obj