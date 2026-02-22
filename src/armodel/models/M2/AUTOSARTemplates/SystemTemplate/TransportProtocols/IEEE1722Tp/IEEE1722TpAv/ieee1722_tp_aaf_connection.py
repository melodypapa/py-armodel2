"""IEEE1722TpAafConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 642)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols_IEEE1722Tp_IEEE1722TpAv.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.ieee1722_tp_av_connection import (
    IEEE1722TpAvConnection,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAv import (
    IEEE1722TpAafAes3DataTypeEnum,
    IEEE1722TpAafFormatEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class IEEE1722TpAafConnection(IEEE1722TpAvConnection):
    """AUTOSAR IEEE1722TpAafConnection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    aaf_aes3_data: Optional[IEEE1722TpAafAes3DataTypeEnum]
    aaf_format_enum: Optional[IEEE1722TpAafFormatEnum]
    aaf_nominal_rate: Optional[Any]
    aes3_data_type_h: Optional[PositiveInteger]
    aes3_data_type_l: Optional[PositiveInteger]
    channels_per: Optional[PositiveInteger]
    event_default: Optional[PositiveInteger]
    pcm_bit_depth: Optional[PositiveInteger]
    sparse: Optional[Boolean]
    streams_per: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize IEEE1722TpAafConnection."""
        super().__init__()
        self.aaf_aes3_data: Optional[IEEE1722TpAafAes3DataTypeEnum] = None
        self.aaf_format_enum: Optional[IEEE1722TpAafFormatEnum] = None
        self.aaf_nominal_rate: Optional[Any] = None
        self.aes3_data_type_h: Optional[PositiveInteger] = None
        self.aes3_data_type_l: Optional[PositiveInteger] = None
        self.channels_per: Optional[PositiveInteger] = None
        self.event_default: Optional[PositiveInteger] = None
        self.pcm_bit_depth: Optional[PositiveInteger] = None
        self.sparse: Optional[Boolean] = None
        self.streams_per: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize IEEE1722TpAafConnection to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IEEE1722TpAafConnection, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize aaf_aes3_data
        if self.aaf_aes3_data is not None:
            serialized = SerializationHelper.serialize_item(self.aaf_aes3_data, "IEEE1722TpAafAes3DataTypeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("AAF-AES3-DATA")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize aaf_format_enum
        if self.aaf_format_enum is not None:
            serialized = SerializationHelper.serialize_item(self.aaf_format_enum, "IEEE1722TpAafFormatEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("AAF-FORMAT-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize aaf_nominal_rate
        if self.aaf_nominal_rate is not None:
            serialized = SerializationHelper.serialize_item(self.aaf_nominal_rate, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("AAF-NOMINAL-RATE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize aes3_data_type_h
        if self.aes3_data_type_h is not None:
            serialized = SerializationHelper.serialize_item(self.aes3_data_type_h, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("AES3-DATA-TYPE-H")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize aes3_data_type_l
        if self.aes3_data_type_l is not None:
            serialized = SerializationHelper.serialize_item(self.aes3_data_type_l, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("AES3-DATA-TYPE-L")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize channels_per
        if self.channels_per is not None:
            serialized = SerializationHelper.serialize_item(self.channels_per, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CHANNELS-PER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize event_default
        if self.event_default is not None:
            serialized = SerializationHelper.serialize_item(self.event_default, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EVENT-DEFAULT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pcm_bit_depth
        if self.pcm_bit_depth is not None:
            serialized = SerializationHelper.serialize_item(self.pcm_bit_depth, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PCM-BIT-DEPTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sparse
        if self.sparse is not None:
            serialized = SerializationHelper.serialize_item(self.sparse, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SPARSE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize streams_per
        if self.streams_per is not None:
            serialized = SerializationHelper.serialize_item(self.streams_per, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("STREAMS-PER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IEEE1722TpAafConnection":
        """Deserialize XML element to IEEE1722TpAafConnection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IEEE1722TpAafConnection object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IEEE1722TpAafConnection, cls).deserialize(element)

        # Parse aaf_aes3_data
        child = SerializationHelper.find_child_element(element, "AAF-AES3-DATA")
        if child is not None:
            aaf_aes3_data_value = IEEE1722TpAafAes3DataTypeEnum.deserialize(child)
            obj.aaf_aes3_data = aaf_aes3_data_value

        # Parse aaf_format_enum
        child = SerializationHelper.find_child_element(element, "AAF-FORMAT-ENUM")
        if child is not None:
            aaf_format_enum_value = IEEE1722TpAafFormatEnum.deserialize(child)
            obj.aaf_format_enum = aaf_format_enum_value

        # Parse aaf_nominal_rate
        child = SerializationHelper.find_child_element(element, "AAF-NOMINAL-RATE")
        if child is not None:
            aaf_nominal_rate_value = child.text
            obj.aaf_nominal_rate = aaf_nominal_rate_value

        # Parse aes3_data_type_h
        child = SerializationHelper.find_child_element(element, "AES3-DATA-TYPE-H")
        if child is not None:
            aes3_data_type_h_value = child.text
            obj.aes3_data_type_h = aes3_data_type_h_value

        # Parse aes3_data_type_l
        child = SerializationHelper.find_child_element(element, "AES3-DATA-TYPE-L")
        if child is not None:
            aes3_data_type_l_value = child.text
            obj.aes3_data_type_l = aes3_data_type_l_value

        # Parse channels_per
        child = SerializationHelper.find_child_element(element, "CHANNELS-PER")
        if child is not None:
            channels_per_value = child.text
            obj.channels_per = channels_per_value

        # Parse event_default
        child = SerializationHelper.find_child_element(element, "EVENT-DEFAULT")
        if child is not None:
            event_default_value = child.text
            obj.event_default = event_default_value

        # Parse pcm_bit_depth
        child = SerializationHelper.find_child_element(element, "PCM-BIT-DEPTH")
        if child is not None:
            pcm_bit_depth_value = child.text
            obj.pcm_bit_depth = pcm_bit_depth_value

        # Parse sparse
        child = SerializationHelper.find_child_element(element, "SPARSE")
        if child is not None:
            sparse_value = child.text
            obj.sparse = sparse_value

        # Parse streams_per
        child = SerializationHelper.find_child_element(element, "STREAMS-PER")
        if child is not None:
            streams_per_value = child.text
            obj.streams_per = streams_per_value

        return obj



class IEEE1722TpAafConnectionBuilder:
    """Builder for IEEE1722TpAafConnection with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: IEEE1722TpAafConnection = IEEE1722TpAafConnection()


    def with_short_name(self, value: Identifier) -> "IEEE1722TpAafConnectionBuilder":
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

    def with_short_name_fragments(self, items: list[ShortNameFragment]) -> "IEEE1722TpAafConnectionBuilder":
        """Set short_name_fragments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = list(items) if items else []
        return self

    def with_long_name(self, value: Optional[MultilanguageLongName]) -> "IEEE1722TpAafConnectionBuilder":
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

    def with_admin_data(self, value: Optional[AdminData]) -> "IEEE1722TpAafConnectionBuilder":
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

    def with_annotations(self, items: list[Annotation]) -> "IEEE1722TpAafConnectionBuilder":
        """Set annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.annotations = list(items) if items else []
        return self

    def with_desc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "IEEE1722TpAafConnectionBuilder":
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

    def with_category(self, value: Optional[CategoryString]) -> "IEEE1722TpAafConnectionBuilder":
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

    def with_introduction(self, value: Optional[DocumentationBlock]) -> "IEEE1722TpAafConnectionBuilder":
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

    def with_uuid(self, value: Optional[String]) -> "IEEE1722TpAafConnectionBuilder":
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

    def with_destination_mac(self, value: Optional[MacAddressString]) -> "IEEE1722TpAafConnectionBuilder":
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

    def with_mac_address_string(self, value: Optional[MacAddressString]) -> "IEEE1722TpAafConnectionBuilder":
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

    def with_pdu(self, value: Optional[PduTriggering]) -> "IEEE1722TpAafConnectionBuilder":
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

    def with_unique_stream_id(self, value: Optional[PositiveInteger]) -> "IEEE1722TpAafConnectionBuilder":
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

    def with_version(self, value: Optional[PositiveInteger]) -> "IEEE1722TpAafConnectionBuilder":
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

    def with_vlan_priority(self, value: Optional[PositiveInteger]) -> "IEEE1722TpAafConnectionBuilder":
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

    def with_max_transit_time(self, value: Optional[TimeValue]) -> "IEEE1722TpAafConnectionBuilder":
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

    def with_sdus(self, items: list[PduTriggering]) -> "IEEE1722TpAafConnectionBuilder":
        """Set sdus list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.sdus = list(items) if items else []
        return self

    def with_aaf_aes3_data(self, value: Optional[IEEE1722TpAafAes3DataTypeEnum]) -> "IEEE1722TpAafConnectionBuilder":
        """Set aaf_aes3_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.aaf_aes3_data = value
        return self

    def with_aaf_format_enum(self, value: Optional[IEEE1722TpAafFormatEnum]) -> "IEEE1722TpAafConnectionBuilder":
        """Set aaf_format_enum attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.aaf_format_enum = value
        return self

    def with_aaf_nominal_rate(self, value: Optional[any (IEEE1722TpAaf)]) -> "IEEE1722TpAafConnectionBuilder":
        """Set aaf_nominal_rate attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.aaf_nominal_rate = value
        return self

    def with_aes3_data_type_h(self, value: Optional[PositiveInteger]) -> "IEEE1722TpAafConnectionBuilder":
        """Set aes3_data_type_h attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.aes3_data_type_h = value
        return self

    def with_aes3_data_type_l(self, value: Optional[PositiveInteger]) -> "IEEE1722TpAafConnectionBuilder":
        """Set aes3_data_type_l attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.aes3_data_type_l = value
        return self

    def with_channels_per(self, value: Optional[PositiveInteger]) -> "IEEE1722TpAafConnectionBuilder":
        """Set channels_per attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.channels_per = value
        return self

    def with_event_default(self, value: Optional[PositiveInteger]) -> "IEEE1722TpAafConnectionBuilder":
        """Set event_default attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.event_default = value
        return self

    def with_pcm_bit_depth(self, value: Optional[PositiveInteger]) -> "IEEE1722TpAafConnectionBuilder":
        """Set pcm_bit_depth attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.pcm_bit_depth = value
        return self

    def with_sparse(self, value: Optional[Boolean]) -> "IEEE1722TpAafConnectionBuilder":
        """Set sparse attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sparse = value
        return self

    def with_streams_per(self, value: Optional[PositiveInteger]) -> "IEEE1722TpAafConnectionBuilder":
        """Set streams_per attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.streams_per = value
        return self


    def add_short_name_fragment(self, item: ShortNameFragment) -> "IEEE1722TpAafConnectionBuilder":
        """Add a single item to short_name_fragments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments.append(item)
        return self

    def clear_short_name_fragments(self) -> "IEEE1722TpAafConnectionBuilder":
        """Clear all items from short_name_fragments list.

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = []
        return self

    def add_annotation(self, item: Annotation) -> "IEEE1722TpAafConnectionBuilder":
        """Add a single item to annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.annotations.append(item)
        return self

    def clear_annotations(self) -> "IEEE1722TpAafConnectionBuilder":
        """Clear all items from annotations list.

        Returns:
            self for method chaining
        """
        self._obj.annotations = []
        return self

    def add_sdu(self, item: PduTriggering) -> "IEEE1722TpAafConnectionBuilder":
        """Add a single item to sdus list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.sdus.append(item)
        return self

    def clear_sdus(self) -> "IEEE1722TpAafConnectionBuilder":
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


    def build(self) -> IEEE1722TpAafConnection:
        """Build and return the IEEE1722TpAafConnection instance with validation."""
        self._validate_instance()
        pass
        return self._obj