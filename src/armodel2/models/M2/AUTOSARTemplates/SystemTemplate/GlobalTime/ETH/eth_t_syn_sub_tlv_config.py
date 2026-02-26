"""EthTSynSubTlvConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 867)

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


class EthTSynSubTlvConfig(ARObject):
    """AUTOSAR EthTSynSubTlvConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ofs_sub_tlv: Optional[Boolean]
    status_sub_tlv: Optional[Boolean]
    time_sub_tlv: Optional[Boolean]
    user_data_sub_tlv: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize EthTSynSubTlvConfig."""
        super().__init__()
        self.ofs_sub_tlv: Optional[Boolean] = None
        self.status_sub_tlv: Optional[Boolean] = None
        self.time_sub_tlv: Optional[Boolean] = None
        self.user_data_sub_tlv: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize EthTSynSubTlvConfig to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EthTSynSubTlvConfig, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ofs_sub_tlv
        if self.ofs_sub_tlv is not None:
            serialized = SerializationHelper.serialize_item(self.ofs_sub_tlv, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OFS-SUB-TLV")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize status_sub_tlv
        if self.status_sub_tlv is not None:
            serialized = SerializationHelper.serialize_item(self.status_sub_tlv, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("STATUS-SUB-TLV")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize time_sub_tlv
        if self.time_sub_tlv is not None:
            serialized = SerializationHelper.serialize_item(self.time_sub_tlv, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME-SUB-TLV")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize user_data_sub_tlv
        if self.user_data_sub_tlv is not None:
            serialized = SerializationHelper.serialize_item(self.user_data_sub_tlv, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("USER-DATA-SUB-TLV")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EthTSynSubTlvConfig":
        """Deserialize XML element to EthTSynSubTlvConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EthTSynSubTlvConfig object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EthTSynSubTlvConfig, cls).deserialize(element)

        # Parse ofs_sub_tlv
        child = SerializationHelper.find_child_element(element, "OFS-SUB-TLV")
        if child is not None:
            ofs_sub_tlv_value = child.text
            obj.ofs_sub_tlv = ofs_sub_tlv_value

        # Parse status_sub_tlv
        child = SerializationHelper.find_child_element(element, "STATUS-SUB-TLV")
        if child is not None:
            status_sub_tlv_value = child.text
            obj.status_sub_tlv = status_sub_tlv_value

        # Parse time_sub_tlv
        child = SerializationHelper.find_child_element(element, "TIME-SUB-TLV")
        if child is not None:
            time_sub_tlv_value = child.text
            obj.time_sub_tlv = time_sub_tlv_value

        # Parse user_data_sub_tlv
        child = SerializationHelper.find_child_element(element, "USER-DATA-SUB-TLV")
        if child is not None:
            user_data_sub_tlv_value = child.text
            obj.user_data_sub_tlv = user_data_sub_tlv_value

        return obj



class EthTSynSubTlvConfigBuilder(BuilderBase):
    """Builder for EthTSynSubTlvConfig with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EthTSynSubTlvConfig = EthTSynSubTlvConfig()


    def with_ofs_sub_tlv(self, value: Optional[Boolean]) -> "EthTSynSubTlvConfigBuilder":
        """Set ofs_sub_tlv attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ofs_sub_tlv = value
        return self

    def with_status_sub_tlv(self, value: Optional[Boolean]) -> "EthTSynSubTlvConfigBuilder":
        """Set status_sub_tlv attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.status_sub_tlv = value
        return self

    def with_time_sub_tlv(self, value: Optional[Boolean]) -> "EthTSynSubTlvConfigBuilder":
        """Set time_sub_tlv attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.time_sub_tlv = value
        return self

    def with_user_data_sub_tlv(self, value: Optional[Boolean]) -> "EthTSynSubTlvConfigBuilder":
        """Set user_data_sub_tlv attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.user_data_sub_tlv = value
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


    def build(self) -> EthTSynSubTlvConfig:
        """Build and return the EthTSynSubTlvConfig instance with validation."""
        self._validate_instance()
        pass
        return self._obj