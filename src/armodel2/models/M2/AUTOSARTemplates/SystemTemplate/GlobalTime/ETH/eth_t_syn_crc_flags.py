"""EthTSynCrcFlags AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 868)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime_ETH.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class EthTSynCrcFlags(ARObject):
    """AUTOSAR EthTSynCrcFlags."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ETH-T-SYN-CRC-FLAGS"


    crc_correction: Optional[Boolean]
    crc_domain: Optional[Boolean]
    crc_message: Optional[Boolean]
    crc_precise: Optional[Boolean]
    crc_sequence_id: Optional[Boolean]
    crc_source_port: Optional[Boolean]
    _DESERIALIZE_DISPATCH = {
        "CRC-CORRECTION": lambda obj, elem: setattr(obj, "crc_correction", elem.text),
        "CRC-DOMAIN": lambda obj, elem: setattr(obj, "crc_domain", elem.text),
        "CRC-MESSAGE": lambda obj, elem: setattr(obj, "crc_message", elem.text),
        "CRC-PRECISE": lambda obj, elem: setattr(obj, "crc_precise", elem.text),
        "CRC-SEQUENCE-ID": lambda obj, elem: setattr(obj, "crc_sequence_id", elem.text),
        "CRC-SOURCE-PORT": lambda obj, elem: setattr(obj, "crc_source_port", elem.text),
    }


    def __init__(self) -> None:
        """Initialize EthTSynCrcFlags."""
        super().__init__()
        self.crc_correction: Optional[Boolean] = None
        self.crc_domain: Optional[Boolean] = None
        self.crc_message: Optional[Boolean] = None
        self.crc_precise: Optional[Boolean] = None
        self.crc_sequence_id: Optional[Boolean] = None
        self.crc_source_port: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize EthTSynCrcFlags to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EthTSynCrcFlags, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize crc_correction
        if self.crc_correction is not None:
            serialized = SerializationHelper.serialize_item(self.crc_correction, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CRC-CORRECTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize crc_domain
        if self.crc_domain is not None:
            serialized = SerializationHelper.serialize_item(self.crc_domain, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CRC-DOMAIN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize crc_message
        if self.crc_message is not None:
            serialized = SerializationHelper.serialize_item(self.crc_message, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CRC-MESSAGE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize crc_precise
        if self.crc_precise is not None:
            serialized = SerializationHelper.serialize_item(self.crc_precise, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CRC-PRECISE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize crc_sequence_id
        if self.crc_sequence_id is not None:
            serialized = SerializationHelper.serialize_item(self.crc_sequence_id, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CRC-SEQUENCE-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize crc_source_port
        if self.crc_source_port is not None:
            serialized = SerializationHelper.serialize_item(self.crc_source_port, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CRC-SOURCE-PORT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EthTSynCrcFlags":
        """Deserialize XML element to EthTSynCrcFlags object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EthTSynCrcFlags object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EthTSynCrcFlags, cls).deserialize(element)

        # Parse crc_correction
        child = SerializationHelper.find_child_element(element, "CRC-CORRECTION")
        if child is not None:
            crc_correction_value = child.text
            obj.crc_correction = crc_correction_value

        # Parse crc_domain
        child = SerializationHelper.find_child_element(element, "CRC-DOMAIN")
        if child is not None:
            crc_domain_value = child.text
            obj.crc_domain = crc_domain_value

        # Parse crc_message
        child = SerializationHelper.find_child_element(element, "CRC-MESSAGE")
        if child is not None:
            crc_message_value = child.text
            obj.crc_message = crc_message_value

        # Parse crc_precise
        child = SerializationHelper.find_child_element(element, "CRC-PRECISE")
        if child is not None:
            crc_precise_value = child.text
            obj.crc_precise = crc_precise_value

        # Parse crc_sequence_id
        child = SerializationHelper.find_child_element(element, "CRC-SEQUENCE-ID")
        if child is not None:
            crc_sequence_id_value = child.text
            obj.crc_sequence_id = crc_sequence_id_value

        # Parse crc_source_port
        child = SerializationHelper.find_child_element(element, "CRC-SOURCE-PORT")
        if child is not None:
            crc_source_port_value = child.text
            obj.crc_source_port = crc_source_port_value

        return obj



class EthTSynCrcFlagsBuilder(BuilderBase):
    """Builder for EthTSynCrcFlags with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EthTSynCrcFlags = EthTSynCrcFlags()


    def with_crc_correction(self, value: Optional[Boolean]) -> "EthTSynCrcFlagsBuilder":
        """Set crc_correction attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.crc_correction = value
        return self

    def with_crc_domain(self, value: Optional[Boolean]) -> "EthTSynCrcFlagsBuilder":
        """Set crc_domain attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.crc_domain = value
        return self

    def with_crc_message(self, value: Optional[Boolean]) -> "EthTSynCrcFlagsBuilder":
        """Set crc_message attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.crc_message = value
        return self

    def with_crc_precise(self, value: Optional[Boolean]) -> "EthTSynCrcFlagsBuilder":
        """Set crc_precise attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.crc_precise = value
        return self

    def with_crc_sequence_id(self, value: Optional[Boolean]) -> "EthTSynCrcFlagsBuilder":
        """Set crc_sequence_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.crc_sequence_id = value
        return self

    def with_crc_source_port(self, value: Optional[Boolean]) -> "EthTSynCrcFlagsBuilder":
        """Set crc_source_port attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.crc_source_port = value
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


    def build(self) -> EthTSynCrcFlags:
        """Build and return the EthTSynCrcFlags instance with validation."""
        self._validate_instance()
        pass
        return self._obj