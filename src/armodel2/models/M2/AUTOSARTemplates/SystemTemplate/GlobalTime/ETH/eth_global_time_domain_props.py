"""EthGlobalTimeDomainProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 867)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime_ETH.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.abstract_global_time_domain_props import (
    AbstractGlobalTimeDomainProps,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.abstract_global_time_domain_props import AbstractGlobalTimeDomainPropsBuilder
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.ETH import (
    EthGlobalTimeMessageFormatEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    MacAddressString,
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.ETH.eth_t_syn_crc_flags import (
    EthTSynCrcFlags,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class EthGlobalTimeDomainProps(AbstractGlobalTimeDomainProps):
    """AUTOSAR EthGlobalTimeDomainProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ETH-GLOBAL-TIME-DOMAIN-PROPS"


    crc_flags: Optional[EthTSynCrcFlags]
    destination: Optional[MacAddressString]
    fup_data_id_list: PositiveInteger
    manageds: list[Any]
    message: Optional[EthGlobalTimeMessageFormatEnum]
    vlan_priority: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "CRC-FLAGS": lambda obj, elem: setattr(obj, "crc_flags", SerializationHelper.deserialize_by_tag(elem, "EthTSynCrcFlags")),
        "DESTINATION": lambda obj, elem: setattr(obj, "destination", SerializationHelper.deserialize_by_tag(elem, "MacAddressString")),
        "FUP-DATA-ID-LIST": lambda obj, elem: setattr(obj, "fup_data_id_list", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "MANAGEDS": lambda obj, elem: obj.manageds.append(SerializationHelper.deserialize_by_tag(elem, "any (EthGlobalTime)")),
        "MESSAGE": lambda obj, elem: setattr(obj, "message", EthGlobalTimeMessageFormatEnum.deserialize(elem)),
        "VLAN-PRIORITY": lambda obj, elem: setattr(obj, "vlan_priority", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize EthGlobalTimeDomainProps."""
        super().__init__()
        self.crc_flags: Optional[EthTSynCrcFlags] = None
        self.destination: Optional[MacAddressString] = None
        self.fup_data_id_list: PositiveInteger = None
        self.manageds: list[Any] = []
        self.message: Optional[EthGlobalTimeMessageFormatEnum] = None
        self.vlan_priority: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize EthGlobalTimeDomainProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EthGlobalTimeDomainProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize crc_flags
        if self.crc_flags is not None:
            serialized = SerializationHelper.serialize_item(self.crc_flags, "EthTSynCrcFlags")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CRC-FLAGS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize destination
        if self.destination is not None:
            serialized = SerializationHelper.serialize_item(self.destination, "MacAddressString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DESTINATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize fup_data_id_list
        if self.fup_data_id_list is not None:
            serialized = SerializationHelper.serialize_item(self.fup_data_id_list, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FUP-DATA-ID-LIST")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize manageds (list to container "MANAGEDS")
        if self.manageds:
            wrapper = ET.Element("MANAGEDS")
            for item in self.manageds:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize message
        if self.message is not None:
            serialized = SerializationHelper.serialize_item(self.message, "EthGlobalTimeMessageFormatEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MESSAGE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize vlan_priority
        if self.vlan_priority is not None:
            serialized = SerializationHelper.serialize_item(self.vlan_priority, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VLAN-PRIORITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EthGlobalTimeDomainProps":
        """Deserialize XML element to EthGlobalTimeDomainProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EthGlobalTimeDomainProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EthGlobalTimeDomainProps, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "CRC-FLAGS":
                setattr(obj, "crc_flags", SerializationHelper.deserialize_by_tag(child, "EthTSynCrcFlags"))
            elif tag == "DESTINATION":
                setattr(obj, "destination", SerializationHelper.deserialize_by_tag(child, "MacAddressString"))
            elif tag == "FUP-DATA-ID-LIST":
                setattr(obj, "fup_data_id_list", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "MANAGEDS":
                obj.manageds.append(SerializationHelper.deserialize_by_tag(child, "any (EthGlobalTime)"))
            elif tag == "MESSAGE":
                setattr(obj, "message", EthGlobalTimeMessageFormatEnum.deserialize(child))
            elif tag == "VLAN-PRIORITY":
                setattr(obj, "vlan_priority", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class EthGlobalTimeDomainPropsBuilder(AbstractGlobalTimeDomainPropsBuilder):
    """Builder for EthGlobalTimeDomainProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EthGlobalTimeDomainProps = EthGlobalTimeDomainProps()


    def with_crc_flags(self, value: Optional[EthTSynCrcFlags]) -> "EthGlobalTimeDomainPropsBuilder":
        """Set crc_flags attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.crc_flags = value
        return self

    def with_destination(self, value: Optional[MacAddressString]) -> "EthGlobalTimeDomainPropsBuilder":
        """Set destination attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.destination = value
        return self

    def with_fup_data_id_list(self, value: PositiveInteger) -> "EthGlobalTimeDomainPropsBuilder":
        """Set fup_data_id_list attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.fup_data_id_list = value
        return self

    def with_manageds(self, items: list[any (EthGlobalTime)]) -> "EthGlobalTimeDomainPropsBuilder":
        """Set manageds list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.manageds = list(items) if items else []
        return self

    def with_message(self, value: Optional[EthGlobalTimeMessageFormatEnum]) -> "EthGlobalTimeDomainPropsBuilder":
        """Set message attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.message = value
        return self

    def with_vlan_priority(self, value: Optional[PositiveInteger]) -> "EthGlobalTimeDomainPropsBuilder":
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


    def add_managed(self, item: any (EthGlobalTime)) -> "EthGlobalTimeDomainPropsBuilder":
        """Add a single item to manageds list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.manageds.append(item)
        return self

    def clear_manageds(self) -> "EthGlobalTimeDomainPropsBuilder":
        """Clear all items from manageds list.

        Returns:
            self for method chaining
        """
        self._obj.manageds = []
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


    def build(self) -> EthGlobalTimeDomainProps:
        """Build and return the EthGlobalTimeDomainProps instance with validation."""
        self._validate_instance()
        pass
        return self._obj