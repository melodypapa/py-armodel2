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

    _XML_TAG = "ETH-T-SYN-SUB-TLV-CONFIG"


    ofs_sub_tlv: Optional[Boolean]
    status_sub_tlv: Optional[Boolean]
    time_sub_tlv: Optional[Boolean]
    user_data_sub_tlv: Optional[Boolean]
    _DESERIALIZE_DISPATCH = {
        "OFS-SUB-TLV": lambda obj, elem: setattr(obj, "ofs_sub_tlv", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "STATUS-SUB-TLV": lambda obj, elem: setattr(obj, "status_sub_tlv", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "TIME-SUB-TLV": lambda obj, elem: setattr(obj, "time_sub_tlv", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "USER-DATA-SUB-TLV": lambda obj, elem: setattr(obj, "user_data_sub_tlv", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
    }


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
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "OFS-SUB-TLV":
                setattr(obj, "ofs_sub_tlv", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "STATUS-SUB-TLV":
                setattr(obj, "status_sub_tlv", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "TIME-SUB-TLV":
                setattr(obj, "time_sub_tlv", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "USER-DATA-SUB-TLV":
                setattr(obj, "user_data_sub_tlv", SerializationHelper.deserialize_by_tag(child, "Boolean"))

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



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "ofsSubTlv",
        "statusSubTlv",
        "timeSubTlv",
        "userDataSubTlv",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> EthTSynSubTlvConfig:
        """Build and return the EthTSynSubTlvConfig instance with validation."""
        self._validate_instance()
        return self._obj