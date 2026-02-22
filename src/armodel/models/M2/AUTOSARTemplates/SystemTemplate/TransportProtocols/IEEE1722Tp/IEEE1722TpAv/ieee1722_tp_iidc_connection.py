"""IEEE1722TpIidcConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 648)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols_IEEE1722Tp_IEEE1722TpAv.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.ieee1722_tp_av_connection import (
    IEEE1722TpAvConnection,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class IEEE1722TpIidcConnection(IEEE1722TpAvConnection):
    """AUTOSAR IEEE1722TpIidcConnection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    iidc_channel: Optional[PositiveInteger]
    iidc_data_block: Optional[PositiveInteger]
    iidc_fraction: Optional[PositiveInteger]
    iidc_source: Optional[Boolean]
    iidc_stream: Optional[PositiveInteger]
    iidc_sy: Optional[PositiveInteger]
    iidc_tag: Optional[PositiveInteger]
    iidc_t_code: Optional[PositiveInteger]
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
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

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

        # Parse iidc_channel
        child = SerializationHelper.find_child_element(element, "IIDC-CHANNEL")
        if child is not None:
            iidc_channel_value = child.text
            obj.iidc_channel = iidc_channel_value

        # Parse iidc_data_block
        child = SerializationHelper.find_child_element(element, "IIDC-DATA-BLOCK")
        if child is not None:
            iidc_data_block_value = child.text
            obj.iidc_data_block = iidc_data_block_value

        # Parse iidc_fraction
        child = SerializationHelper.find_child_element(element, "IIDC-FRACTION")
        if child is not None:
            iidc_fraction_value = child.text
            obj.iidc_fraction = iidc_fraction_value

        # Parse iidc_source
        child = SerializationHelper.find_child_element(element, "IIDC-SOURCE")
        if child is not None:
            iidc_source_value = child.text
            obj.iidc_source = iidc_source_value

        # Parse iidc_stream
        child = SerializationHelper.find_child_element(element, "IIDC-STREAM")
        if child is not None:
            iidc_stream_value = child.text
            obj.iidc_stream = iidc_stream_value

        # Parse iidc_sy
        child = SerializationHelper.find_child_element(element, "IIDC-SY")
        if child is not None:
            iidc_sy_value = child.text
            obj.iidc_sy = iidc_sy_value

        # Parse iidc_tag
        child = SerializationHelper.find_child_element(element, "IIDC-TAG")
        if child is not None:
            iidc_tag_value = child.text
            obj.iidc_tag = iidc_tag_value

        # Parse iidc_t_code
        child = SerializationHelper.find_child_element(element, "IIDC-T-CODE")
        if child is not None:
            iidc_t_code_value = child.text
            obj.iidc_t_code = iidc_t_code_value

        return obj



class IEEE1722TpIidcConnectionBuilder:
    """Builder for IEEE1722TpIidcConnection with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: IEEE1722TpIidcConnection = IEEE1722TpIidcConnection()


    def with_short_name(self, value: Identifier) -> "IEEE1722TpIidcConnectionBuilder":
        """Set short_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.short_name = value
        return self

    def with_short_name_fragments(self, items: list[ShortNameFragment]) -> "IEEE1722TpIidcConnectionBuilder":
        """Set short_name_fragments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = list(items) if items else []
        return self

    def with_long_name(self, value: Optional[MultilanguageLongName]) -> "IEEE1722TpIidcConnectionBuilder":
        """Set long_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.long_name = value
        return self

    def with_admin_data(self, value: Optional[AdminData]) -> "IEEE1722TpIidcConnectionBuilder":
        """Set admin_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.admin_data = value
        return self

    def with_annotations(self, items: list[Annotation]) -> "IEEE1722TpIidcConnectionBuilder":
        """Set annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.annotations = list(items) if items else []
        return self

    def with_desc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "IEEE1722TpIidcConnectionBuilder":
        """Set desc attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.desc = value
        return self

    def with_category(self, value: Optional[CategoryString]) -> "IEEE1722TpIidcConnectionBuilder":
        """Set category attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.category = value
        return self

    def with_introduction(self, value: Optional[DocumentationBlock]) -> "IEEE1722TpIidcConnectionBuilder":
        """Set introduction attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.introduction = value
        return self

    def with_uuid(self, value: Optional[String]) -> "IEEE1722TpIidcConnectionBuilder":
        """Set uuid attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.uuid = value
        return self

    def with_destination_mac(self, value: Optional[MacAddressString]) -> "IEEE1722TpIidcConnectionBuilder":
        """Set destination_mac attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.destination_mac = value
        return self

    def with_mac_address_string(self, value: Optional[MacAddressString]) -> "IEEE1722TpIidcConnectionBuilder":
        """Set mac_address_string attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.mac_address_string = value
        return self

    def with_pdu(self, value: Optional[PduTriggering]) -> "IEEE1722TpIidcConnectionBuilder":
        """Set pdu attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.pdu = value
        return self

    def with_unique_stream_id(self, value: Optional[PositiveInteger]) -> "IEEE1722TpIidcConnectionBuilder":
        """Set unique_stream_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.unique_stream_id = value
        return self

    def with_version(self, value: Optional[PositiveInteger]) -> "IEEE1722TpIidcConnectionBuilder":
        """Set version attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.version = value
        return self

    def with_vlan_priority(self, value: Optional[PositiveInteger]) -> "IEEE1722TpIidcConnectionBuilder":
        """Set vlan_priority attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.vlan_priority = value
        return self

    def with_max_transit_time(self, value: Optional[TimeValue]) -> "IEEE1722TpIidcConnectionBuilder":
        """Set max_transit_time attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.max_transit_time = value
        return self

    def with_sdus(self, items: list[PduTriggering]) -> "IEEE1722TpIidcConnectionBuilder":
        """Set sdus list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.sdus = list(items) if items else []
        return self

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


    def add_short_name_fragment(self, item: ShortNameFragment) -> "IEEE1722TpIidcConnectionBuilder":
        """Add a single item to short_name_fragments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments.append(item)
        return self

    def clear_short_name_fragments(self) -> "IEEE1722TpIidcConnectionBuilder":
        """Clear all items from short_name_fragments list.

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = []
        return self

    def add_annotation(self, item: Annotation) -> "IEEE1722TpIidcConnectionBuilder":
        """Add a single item to annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.annotations.append(item)
        return self

    def clear_annotations(self) -> "IEEE1722TpIidcConnectionBuilder":
        """Clear all items from annotations list.

        Returns:
            self for method chaining
        """
        self._obj.annotations = []
        return self

    def add_sdu(self, item: PduTriggering) -> "IEEE1722TpIidcConnectionBuilder":
        """Add a single item to sdus list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.sdus.append(item)
        return self

    def clear_sdus(self) -> "IEEE1722TpIidcConnectionBuilder":
        """Clear all items from sdus list.

        Returns:
            self for method chaining
        """
        self._obj.sdus = []
        return self


    @staticmethod
    def _coerce_to_int(value: Any) -> int:
        """Coerce value to int.

        Args:
            value: Value to coerce

        Returns:
            Integer value

        Raises:
            ValueError: If value cannot be coerced to int
        """
        if isinstance(value, int):
            return value
        if isinstance(value, str) and value.isdigit():
            return int(value)
        if isinstance(value, float):
            return int(value)
        if isinstance(value, bool):
            return int(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to int: {value}")

    @staticmethod
    def _coerce_to_float(value: Any) -> float:
        """Coerce value to float.

        Args:
            value: Value to coerce

        Returns:
            Float value

        Raises:
            ValueError: If value cannot be coerced to float
        """
        if isinstance(value, float):
            return value
        if isinstance(value, int):
            return float(value)
        if isinstance(value, str):
            try:
                return float(value)
            except ValueError:
                pass
        raise ValueError(f"Cannot coerce {type(value).__name__} to float: {value}")

    @staticmethod
    def _coerce_to_bool(value: Any) -> bool:
        """Coerce value to bool.

        Args:
            value: Value to coerce

        Returns:
            Boolean value

        Raises:
            ValueError: If value cannot be coerced to bool
        """
        if isinstance(value, bool):
            return value
        if isinstance(value, int):
            return bool(value)
        if isinstance(value, str):
            if value.lower() in ("true", "1", "yes"):
                return True
            if value.lower() in ("false", "0", "no"):
                return False
        raise ValueError(f"Cannot coerce {type(value).__name__} to bool: {value}")

    @staticmethod
    def _coerce_to_str(value: Any) -> str:
        """Coerce value to str.

        Args:
            value: Value to coerce

        Returns:
            String value
        """
        return str(value)


    @staticmethod
    def _coerce_to_list(value: Any, item_type: str) -> list:
        """Coerce value to list.

        Args:
            value: Value to coerce
            item_type: Expected item type (for error messages)

        Returns:
            List value

        Raises:
            ValueError: If value cannot be coerced to list
        """
        if isinstance(value, list):
            return value
        if isinstance(value, tuple):
            return list(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to list[{item_type}]: {value}")


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel.core import GlobalSettingsManager, BuilderValidationMode

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