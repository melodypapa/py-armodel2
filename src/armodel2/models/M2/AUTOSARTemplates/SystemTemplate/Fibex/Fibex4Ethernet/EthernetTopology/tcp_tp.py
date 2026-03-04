"""TcpTp AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 460)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.tcp_udp_config import (
    TcpUdpConfig,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.tcp_udp_config import TcpUdpConfigBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.tp_port import (
    TpPort,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class TcpTp(TcpUdpConfig):
    """AUTOSAR TcpTp."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "TCP-TP"


    keep_alive: Optional[PositiveInteger]
    keep_alives: Optional[Boolean]
    keep_alive_time: Optional[TimeValue]
    nagles_algorithm: Optional[Boolean]
    receive_window_min: Optional[PositiveInteger]
    tcp: Optional[TimeValue]
    tcp_tp_port: Optional[TpPort]
    _DESERIALIZE_DISPATCH = {
        "KEEP-ALIVE": lambda obj, elem: setattr(obj, "keep_alive", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "KEEP-ALIVES": lambda obj, elem: setattr(obj, "keep_alives", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "KEEP-ALIVE-TIME": lambda obj, elem: setattr(obj, "keep_alive_time", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "NAGLES-ALGORITHM": lambda obj, elem: setattr(obj, "nagles_algorithm", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "RECEIVE-WINDOW-MIN": lambda obj, elem: setattr(obj, "receive_window_min", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "TCP": lambda obj, elem: setattr(obj, "tcp", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "TCP-TP-PORT": lambda obj, elem: setattr(obj, "tcp_tp_port", SerializationHelper.deserialize_by_tag(elem, "TpPort")),
    }


    def __init__(self) -> None:
        """Initialize TcpTp."""
        super().__init__()
        self.keep_alive: Optional[PositiveInteger] = None
        self.keep_alives: Optional[Boolean] = None
        self.keep_alive_time: Optional[TimeValue] = None
        self.nagles_algorithm: Optional[Boolean] = None
        self.receive_window_min: Optional[PositiveInteger] = None
        self.tcp: Optional[TimeValue] = None
        self.tcp_tp_port: Optional[TpPort] = None

    def serialize(self) -> ET.Element:
        """Serialize TcpTp to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TcpTp, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize keep_alive
        if self.keep_alive is not None:
            serialized = SerializationHelper.serialize_item(self.keep_alive, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("KEEP-ALIVE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize keep_alives
        if self.keep_alives is not None:
            serialized = SerializationHelper.serialize_item(self.keep_alives, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("KEEP-ALIVES")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize keep_alive_time
        if self.keep_alive_time is not None:
            serialized = SerializationHelper.serialize_item(self.keep_alive_time, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("KEEP-ALIVE-TIME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nagles_algorithm
        if self.nagles_algorithm is not None:
            serialized = SerializationHelper.serialize_item(self.nagles_algorithm, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NAGLES-ALGORITHM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize receive_window_min
        if self.receive_window_min is not None:
            serialized = SerializationHelper.serialize_item(self.receive_window_min, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RECEIVE-WINDOW-MIN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp
        if self.tcp is not None:
            serialized = SerializationHelper.serialize_item(self.tcp, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_tp_port
        if self.tcp_tp_port is not None:
            serialized = SerializationHelper.serialize_item(self.tcp_tp_port, "TpPort")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-TP-PORT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TcpTp":
        """Deserialize XML element to TcpTp object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TcpTp object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TcpTp, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "KEEP-ALIVE":
                setattr(obj, "keep_alive", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "KEEP-ALIVES":
                setattr(obj, "keep_alives", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "KEEP-ALIVE-TIME":
                setattr(obj, "keep_alive_time", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "NAGLES-ALGORITHM":
                setattr(obj, "nagles_algorithm", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "RECEIVE-WINDOW-MIN":
                setattr(obj, "receive_window_min", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "TCP":
                setattr(obj, "tcp", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "TCP-TP-PORT":
                setattr(obj, "tcp_tp_port", SerializationHelper.deserialize_by_tag(child, "TpPort"))

        return obj



class TcpTpBuilder(TcpUdpConfigBuilder):
    """Builder for TcpTp with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TcpTp = TcpTp()


    def with_keep_alive(self, value: Optional[PositiveInteger]) -> "TcpTpBuilder":
        """Set keep_alive attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.keep_alive = value
        return self

    def with_keep_alives(self, value: Optional[Boolean]) -> "TcpTpBuilder":
        """Set keep_alives attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.keep_alives = value
        return self

    def with_keep_alive_time(self, value: Optional[TimeValue]) -> "TcpTpBuilder":
        """Set keep_alive_time attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.keep_alive_time = value
        return self

    def with_nagles_algorithm(self, value: Optional[Boolean]) -> "TcpTpBuilder":
        """Set nagles_algorithm attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nagles_algorithm = value
        return self

    def with_receive_window_min(self, value: Optional[PositiveInteger]) -> "TcpTpBuilder":
        """Set receive_window_min attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.receive_window_min = value
        return self

    def with_tcp(self, value: Optional[TimeValue]) -> "TcpTpBuilder":
        """Set tcp attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tcp = value
        return self

    def with_tcp_tp_port(self, value: Optional[TpPort]) -> "TcpTpBuilder":
        """Set tcp_tp_port attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tcp_tp_port = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "keepAlive",
        "keepAliveTime",
        "keepAlives",
        "naglesAlgorithm",
        "receiveWindowMin",
        "tcp",
        "tcpTpPort",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> TcpTp:
        """Build and return the TcpTp instance with validation."""
        self._validate_instance()
        return self._obj