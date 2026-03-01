"""FlexrayTpConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 594)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection.tp_connection import (
    TpConnection,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection.tp_connection import TpConnectionBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.flexray_tp_node import (
    FlexrayTpNode,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.flexray_tp_pdu_pool import (
    FlexrayTpPduPool,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_address import (
    TpAddress,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class FlexrayTpConnection(TpConnection):
    """AUTOSAR FlexrayTpConnection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "FLEXRAY-TP-CONNECTION"


    bandwidth: Optional[Boolean]
    direct_tp_sdu_ref: Optional[ARRef]
    multicast_ref: Optional[ARRef]
    receiver_refs: list[ARRef]
    reversed_tp_sdu_ref: Optional[ARRef]
    rx_pdu_pool_ref: Optional[ARRef]
    tp_connection_ref: Optional[ARRef]
    transmitter_ref: Optional[ARRef]
    tx_pdu_pool_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "BANDWIDTH": lambda obj, elem: setattr(obj, "bandwidth", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "DIRECT-TP-SDU-REF": ("_POLYMORPHIC", "direct_tp_sdu_ref", ["ContainerIPdu", "DcmIPdu", "GeneralPurposeIPdu", "ISignalIPdu", "J1939DcmIPdu", "MultiplexedIPdu", "NPdu", "SecuredIPdu", "UserDefinedIPdu"]),
        "MULTICAST-REF": lambda obj, elem: setattr(obj, "multicast_ref", ARRef.deserialize(elem)),
        "RECEIVERS": lambda obj, elem: obj.receiver_refs.append(ARRef.deserialize(elem)),
        "REVERSED-TP-SDU-REF": ("_POLYMORPHIC", "reversed_tp_sdu_ref", ["ContainerIPdu", "DcmIPdu", "GeneralPurposeIPdu", "ISignalIPdu", "J1939DcmIPdu", "MultiplexedIPdu", "NPdu", "SecuredIPdu", "UserDefinedIPdu"]),
        "RX-PDU-POOL-REF": lambda obj, elem: setattr(obj, "rx_pdu_pool_ref", ARRef.deserialize(elem)),
        "TP-CONNECTION-REF": lambda obj, elem: setattr(obj, "tp_connection_ref", ARRef.deserialize(elem)),
        "TRANSMITTER-REF": lambda obj, elem: setattr(obj, "transmitter_ref", ARRef.deserialize(elem)),
        "TX-PDU-POOL-REF": lambda obj, elem: setattr(obj, "tx_pdu_pool_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize FlexrayTpConnection."""
        super().__init__()
        self.bandwidth: Optional[Boolean] = None
        self.direct_tp_sdu_ref: Optional[ARRef] = None
        self.multicast_ref: Optional[ARRef] = None
        self.receiver_refs: list[ARRef] = []
        self.reversed_tp_sdu_ref: Optional[ARRef] = None
        self.rx_pdu_pool_ref: Optional[ARRef] = None
        self.tp_connection_ref: Optional[ARRef] = None
        self.transmitter_ref: Optional[ARRef] = None
        self.tx_pdu_pool_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize FlexrayTpConnection to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FlexrayTpConnection, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize bandwidth
        if self.bandwidth is not None:
            serialized = SerializationHelper.serialize_item(self.bandwidth, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BANDWIDTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize direct_tp_sdu_ref
        if self.direct_tp_sdu_ref is not None:
            serialized = SerializationHelper.serialize_item(self.direct_tp_sdu_ref, "IPdu")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DIRECT-TP-SDU-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize multicast_ref
        if self.multicast_ref is not None:
            serialized = SerializationHelper.serialize_item(self.multicast_ref, "TpAddress")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MULTICAST-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize receiver_refs (list to container "RECEIVER-REFS")
        if self.receiver_refs:
            wrapper = ET.Element("RECEIVER-REFS")
            for item in self.receiver_refs:
                serialized = SerializationHelper.serialize_item(item, "FlexrayTpNode")
                if serialized is not None:
                    child_elem = ET.Element("RECEIVER-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize reversed_tp_sdu_ref
        if self.reversed_tp_sdu_ref is not None:
            serialized = SerializationHelper.serialize_item(self.reversed_tp_sdu_ref, "IPdu")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REVERSED-TP-SDU-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rx_pdu_pool_ref
        if self.rx_pdu_pool_ref is not None:
            serialized = SerializationHelper.serialize_item(self.rx_pdu_pool_ref, "FlexrayTpPduPool")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RX-PDU-POOL-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tp_connection_ref
        if self.tp_connection_ref is not None:
            serialized = SerializationHelper.serialize_item(self.tp_connection_ref, "FlexrayTpConnection")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TP-CONNECTION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize transmitter_ref
        if self.transmitter_ref is not None:
            serialized = SerializationHelper.serialize_item(self.transmitter_ref, "FlexrayTpNode")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRANSMITTER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tx_pdu_pool_ref
        if self.tx_pdu_pool_ref is not None:
            serialized = SerializationHelper.serialize_item(self.tx_pdu_pool_ref, "FlexrayTpPduPool")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TX-PDU-POOL-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayTpConnection":
        """Deserialize XML element to FlexrayTpConnection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FlexrayTpConnection object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FlexrayTpConnection, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "BANDWIDTH":
                setattr(obj, "bandwidth", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "DIRECT-TP-SDU-REF":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "CONTAINER-I-PDU":
                        setattr(obj, "direct_tp_sdu_ref", SerializationHelper.deserialize_by_tag(child[0], "ContainerIPdu"))
                    elif concrete_tag == "DCM-I-PDU":
                        setattr(obj, "direct_tp_sdu_ref", SerializationHelper.deserialize_by_tag(child[0], "DcmIPdu"))
                    elif concrete_tag == "GENERAL-PURPOSE-I-PDU":
                        setattr(obj, "direct_tp_sdu_ref", SerializationHelper.deserialize_by_tag(child[0], "GeneralPurposeIPdu"))
                    elif concrete_tag == "I-SIGNAL-I-PDU":
                        setattr(obj, "direct_tp_sdu_ref", SerializationHelper.deserialize_by_tag(child[0], "ISignalIPdu"))
                    elif concrete_tag == "J1939-DCM-I-PDU":
                        setattr(obj, "direct_tp_sdu_ref", SerializationHelper.deserialize_by_tag(child[0], "J1939DcmIPdu"))
                    elif concrete_tag == "MULTIPLEXED-I-PDU":
                        setattr(obj, "direct_tp_sdu_ref", SerializationHelper.deserialize_by_tag(child[0], "MultiplexedIPdu"))
                    elif concrete_tag == "N-PDU":
                        setattr(obj, "direct_tp_sdu_ref", SerializationHelper.deserialize_by_tag(child[0], "NPdu"))
                    elif concrete_tag == "SECURED-I-PDU":
                        setattr(obj, "direct_tp_sdu_ref", SerializationHelper.deserialize_by_tag(child[0], "SecuredIPdu"))
                    elif concrete_tag == "USER-DEFINED-I-PDU":
                        setattr(obj, "direct_tp_sdu_ref", SerializationHelper.deserialize_by_tag(child[0], "UserDefinedIPdu"))
            elif tag == "MULTICAST-REF":
                setattr(obj, "multicast_ref", ARRef.deserialize(child))
            elif tag == "RECEIVERS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.receiver_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "FlexrayTpNode"))
            elif tag == "REVERSED-TP-SDU-REF":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "CONTAINER-I-PDU":
                        setattr(obj, "reversed_tp_sdu_ref", SerializationHelper.deserialize_by_tag(child[0], "ContainerIPdu"))
                    elif concrete_tag == "DCM-I-PDU":
                        setattr(obj, "reversed_tp_sdu_ref", SerializationHelper.deserialize_by_tag(child[0], "DcmIPdu"))
                    elif concrete_tag == "GENERAL-PURPOSE-I-PDU":
                        setattr(obj, "reversed_tp_sdu_ref", SerializationHelper.deserialize_by_tag(child[0], "GeneralPurposeIPdu"))
                    elif concrete_tag == "I-SIGNAL-I-PDU":
                        setattr(obj, "reversed_tp_sdu_ref", SerializationHelper.deserialize_by_tag(child[0], "ISignalIPdu"))
                    elif concrete_tag == "J1939-DCM-I-PDU":
                        setattr(obj, "reversed_tp_sdu_ref", SerializationHelper.deserialize_by_tag(child[0], "J1939DcmIPdu"))
                    elif concrete_tag == "MULTIPLEXED-I-PDU":
                        setattr(obj, "reversed_tp_sdu_ref", SerializationHelper.deserialize_by_tag(child[0], "MultiplexedIPdu"))
                    elif concrete_tag == "N-PDU":
                        setattr(obj, "reversed_tp_sdu_ref", SerializationHelper.deserialize_by_tag(child[0], "NPdu"))
                    elif concrete_tag == "SECURED-I-PDU":
                        setattr(obj, "reversed_tp_sdu_ref", SerializationHelper.deserialize_by_tag(child[0], "SecuredIPdu"))
                    elif concrete_tag == "USER-DEFINED-I-PDU":
                        setattr(obj, "reversed_tp_sdu_ref", SerializationHelper.deserialize_by_tag(child[0], "UserDefinedIPdu"))
            elif tag == "RX-PDU-POOL-REF":
                setattr(obj, "rx_pdu_pool_ref", ARRef.deserialize(child))
            elif tag == "TP-CONNECTION-REF":
                setattr(obj, "tp_connection_ref", ARRef.deserialize(child))
            elif tag == "TRANSMITTER-REF":
                setattr(obj, "transmitter_ref", ARRef.deserialize(child))
            elif tag == "TX-PDU-POOL-REF":
                setattr(obj, "tx_pdu_pool_ref", ARRef.deserialize(child))

        return obj



class FlexrayTpConnectionBuilder(TpConnectionBuilder):
    """Builder for FlexrayTpConnection with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: FlexrayTpConnection = FlexrayTpConnection()


    def with_bandwidth(self, value: Optional[Boolean]) -> "FlexrayTpConnectionBuilder":
        """Set bandwidth attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.bandwidth = value
        return self

    def with_direct_tp_sdu(self, value: Optional[IPdu]) -> "FlexrayTpConnectionBuilder":
        """Set direct_tp_sdu attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.direct_tp_sdu = value
        return self

    def with_multicast(self, value: Optional[TpAddress]) -> "FlexrayTpConnectionBuilder":
        """Set multicast attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.multicast = value
        return self

    def with_receivers(self, items: list[FlexrayTpNode]) -> "FlexrayTpConnectionBuilder":
        """Set receivers list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.receivers = list(items) if items else []
        return self

    def with_reversed_tp_sdu(self, value: Optional[IPdu]) -> "FlexrayTpConnectionBuilder":
        """Set reversed_tp_sdu attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.reversed_tp_sdu = value
        return self

    def with_rx_pdu_pool(self, value: Optional[FlexrayTpPduPool]) -> "FlexrayTpConnectionBuilder":
        """Set rx_pdu_pool attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.rx_pdu_pool = value
        return self

    def with_tp_connection(self, value: Optional[FlexrayTpConnection]) -> "FlexrayTpConnectionBuilder":
        """Set tp_connection attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tp_connection = value
        return self

    def with_transmitter(self, value: Optional[FlexrayTpNode]) -> "FlexrayTpConnectionBuilder":
        """Set transmitter attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.transmitter = value
        return self

    def with_tx_pdu_pool(self, value: Optional[FlexrayTpPduPool]) -> "FlexrayTpConnectionBuilder":
        """Set tx_pdu_pool attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tx_pdu_pool = value
        return self


    def add_receiver(self, item: FlexrayTpNode) -> "FlexrayTpConnectionBuilder":
        """Add a single item to receivers list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.receivers.append(item)
        return self

    def clear_receivers(self) -> "FlexrayTpConnectionBuilder":
        """Clear all items from receivers list.

        Returns:
            self for method chaining
        """
        self._obj.receivers = []
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


    def build(self) -> FlexrayTpConnection:
        """Build and return the FlexrayTpConnection instance with validation."""
        self._validate_instance()
        pass
        return self._obj