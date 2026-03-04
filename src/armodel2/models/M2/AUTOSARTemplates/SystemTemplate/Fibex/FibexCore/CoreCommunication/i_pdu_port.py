"""IPduPort AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 304)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.comm_connector_port import (
    CommConnectorPort,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.comm_connector_port import CommConnectorPortBuilder
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    IPduSignalProcessingEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class IPduPort(CommConnectorPort):
    """AUTOSAR IPduPort."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "I-PDU-PORT"


    i_pdu_signal: Optional[IPduSignalProcessingEnum]
    rx_security: Optional[Boolean]
    timestamp_rx: Optional[TimeValue]
    use_auth_data: Optional[Boolean]
    _DESERIALIZE_DISPATCH = {
        "I-PDU-SIGNAL": lambda obj, elem: setattr(obj, "i_pdu_signal", IPduSignalProcessingEnum.deserialize(elem)),
        "RX-SECURITY": lambda obj, elem: setattr(obj, "rx_security", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "TIMESTAMP-RX": lambda obj, elem: setattr(obj, "timestamp_rx", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "USE-AUTH-DATA": lambda obj, elem: setattr(obj, "use_auth_data", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
    }


    def __init__(self) -> None:
        """Initialize IPduPort."""
        super().__init__()
        self.i_pdu_signal: Optional[IPduSignalProcessingEnum] = None
        self.rx_security: Optional[Boolean] = None
        self.timestamp_rx: Optional[TimeValue] = None
        self.use_auth_data: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize IPduPort to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IPduPort, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize i_pdu_signal
        if self.i_pdu_signal is not None:
            serialized = SerializationHelper.serialize_item(self.i_pdu_signal, "IPduSignalProcessingEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("I-PDU-SIGNAL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rx_security
        if self.rx_security is not None:
            serialized = SerializationHelper.serialize_item(self.rx_security, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RX-SECURITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize timestamp_rx
        if self.timestamp_rx is not None:
            serialized = SerializationHelper.serialize_item(self.timestamp_rx, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMESTAMP-RX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize use_auth_data
        if self.use_auth_data is not None:
            serialized = SerializationHelper.serialize_item(self.use_auth_data, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("USE-AUTH-DATA")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IPduPort":
        """Deserialize XML element to IPduPort object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IPduPort object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IPduPort, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "I-PDU-SIGNAL":
                setattr(obj, "i_pdu_signal", IPduSignalProcessingEnum.deserialize(child))
            elif tag == "RX-SECURITY":
                setattr(obj, "rx_security", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "TIMESTAMP-RX":
                setattr(obj, "timestamp_rx", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "USE-AUTH-DATA":
                setattr(obj, "use_auth_data", SerializationHelper.deserialize_by_tag(child, "Boolean"))

        return obj



class IPduPortBuilder(CommConnectorPortBuilder):
    """Builder for IPduPort with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: IPduPort = IPduPort()


    def with_i_pdu_signal(self, value: Optional[IPduSignalProcessingEnum]) -> "IPduPortBuilder":
        """Set i_pdu_signal attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.i_pdu_signal = value
        return self

    def with_rx_security(self, value: Optional[Boolean]) -> "IPduPortBuilder":
        """Set rx_security attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.rx_security = value
        return self

    def with_timestamp_rx(self, value: Optional[TimeValue]) -> "IPduPortBuilder":
        """Set timestamp_rx attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.timestamp_rx = value
        return self

    def with_use_auth_data(self, value: Optional[Boolean]) -> "IPduPortBuilder":
        """Set use_auth_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.use_auth_data = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "iPduSignal",
        "rxSecurity",
        "timestampRx",
        "useAuthData",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> IPduPort:
        """Build and return the IPduPort instance with validation."""
        self._validate_instance()
        return self._obj