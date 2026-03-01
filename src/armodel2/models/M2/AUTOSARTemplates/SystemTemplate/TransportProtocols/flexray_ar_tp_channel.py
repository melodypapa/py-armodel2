"""FlexrayArTpChannel AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 600)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import (
    FrArTpAckType,
    MaximumMessageLengthType,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    PositiveInteger,
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.flexray_ar_tp_connection import (
    FlexrayArTpConnection,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.n_pdu import (
    NPdu,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class FlexrayArTpChannel(ARObject):
    """AUTOSAR FlexrayArTpChannel."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "FLEXRAY-AR-TP-CHANNEL"


    ack_type: Optional[FrArTpAckType]
    cancellation: Optional[Boolean]
    extended: Optional[Boolean]
    max_ar: Optional[Integer]
    max_as: Optional[Integer]
    max_bs: Optional[Integer]
    max_fc_wait: Optional[PositiveInteger]
    maximum_message: Optional[MaximumMessageLengthType]
    max_retries: Optional[Integer]
    minimum: Optional[TimeValue]
    multicast: Optional[Boolean]
    n_pdu_refs: list[ARRef]
    time_br: Optional[TimeValue]
    time_cs: Optional[TimeValue]
    timeout_ar: Optional[TimeValue]
    timeout_as: Optional[TimeValue]
    timeout_bs: Optional[TimeValue]
    timeout_cr: Optional[TimeValue]
    tp_connections: list[FlexrayArTpConnection]
    _DESERIALIZE_DISPATCH = {
        "ACK-TYPE": lambda obj, elem: setattr(obj, "ack_type", FrArTpAckType.deserialize(elem)),
        "CANCELLATION": lambda obj, elem: setattr(obj, "cancellation", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "EXTENDED": lambda obj, elem: setattr(obj, "extended", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "MAX-AR": lambda obj, elem: setattr(obj, "max_ar", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "MAX-AS": lambda obj, elem: setattr(obj, "max_as", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "MAX-BS": lambda obj, elem: setattr(obj, "max_bs", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "MAX-FC-WAIT": lambda obj, elem: setattr(obj, "max_fc_wait", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "MAXIMUM-MESSAGE": lambda obj, elem: setattr(obj, "maximum_message", MaximumMessageLengthType.deserialize(elem)),
        "MAX-RETRIES": lambda obj, elem: setattr(obj, "max_retries", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "MINIMUM": lambda obj, elem: setattr(obj, "minimum", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "MULTICAST": lambda obj, elem: setattr(obj, "multicast", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "N-PDU-REFS": lambda obj, elem: [obj.n_pdu_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "TIME-BR": lambda obj, elem: setattr(obj, "time_br", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "TIME-CS": lambda obj, elem: setattr(obj, "time_cs", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "TIMEOUT-AR": lambda obj, elem: setattr(obj, "timeout_ar", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "TIMEOUT-AS": lambda obj, elem: setattr(obj, "timeout_as", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "TIMEOUT-BS": lambda obj, elem: setattr(obj, "timeout_bs", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "TIMEOUT-CR": lambda obj, elem: setattr(obj, "timeout_cr", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "TP-CONNECTIONS": lambda obj, elem: obj.tp_connections.append(SerializationHelper.deserialize_by_tag(elem, "FlexrayArTpConnection")),
    }


    def __init__(self) -> None:
        """Initialize FlexrayArTpChannel."""
        super().__init__()
        self.ack_type: Optional[FrArTpAckType] = None
        self.cancellation: Optional[Boolean] = None
        self.extended: Optional[Boolean] = None
        self.max_ar: Optional[Integer] = None
        self.max_as: Optional[Integer] = None
        self.max_bs: Optional[Integer] = None
        self.max_fc_wait: Optional[PositiveInteger] = None
        self.maximum_message: Optional[MaximumMessageLengthType] = None
        self.max_retries: Optional[Integer] = None
        self.minimum: Optional[TimeValue] = None
        self.multicast: Optional[Boolean] = None
        self.n_pdu_refs: list[ARRef] = []
        self.time_br: Optional[TimeValue] = None
        self.time_cs: Optional[TimeValue] = None
        self.timeout_ar: Optional[TimeValue] = None
        self.timeout_as: Optional[TimeValue] = None
        self.timeout_bs: Optional[TimeValue] = None
        self.timeout_cr: Optional[TimeValue] = None
        self.tp_connections: list[FlexrayArTpConnection] = []

    def serialize(self) -> ET.Element:
        """Serialize FlexrayArTpChannel to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FlexrayArTpChannel, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ack_type
        if self.ack_type is not None:
            serialized = SerializationHelper.serialize_item(self.ack_type, "FrArTpAckType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ACK-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize cancellation
        if self.cancellation is not None:
            serialized = SerializationHelper.serialize_item(self.cancellation, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CANCELLATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize extended
        if self.extended is not None:
            serialized = SerializationHelper.serialize_item(self.extended, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EXTENDED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_ar
        if self.max_ar is not None:
            serialized = SerializationHelper.serialize_item(self.max_ar, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-AR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_as
        if self.max_as is not None:
            serialized = SerializationHelper.serialize_item(self.max_as, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-AS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_bs
        if self.max_bs is not None:
            serialized = SerializationHelper.serialize_item(self.max_bs, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-BS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_fc_wait
        if self.max_fc_wait is not None:
            serialized = SerializationHelper.serialize_item(self.max_fc_wait, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-FC-WAIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize maximum_message
        if self.maximum_message is not None:
            serialized = SerializationHelper.serialize_item(self.maximum_message, "MaximumMessageLengthType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAXIMUM-MESSAGE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_retries
        if self.max_retries is not None:
            serialized = SerializationHelper.serialize_item(self.max_retries, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-RETRIES")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize minimum
        if self.minimum is not None:
            serialized = SerializationHelper.serialize_item(self.minimum, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MINIMUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize multicast
        if self.multicast is not None:
            serialized = SerializationHelper.serialize_item(self.multicast, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MULTICAST")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize n_pdu_refs (list to container "N-PDU-REFS")
        if self.n_pdu_refs:
            wrapper = ET.Element("N-PDU-REFS")
            for item in self.n_pdu_refs:
                serialized = SerializationHelper.serialize_item(item, "NPdu")
                if serialized is not None:
                    child_elem = ET.Element("N-PDU-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize time_br
        if self.time_br is not None:
            serialized = SerializationHelper.serialize_item(self.time_br, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME-BR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize time_cs
        if self.time_cs is not None:
            serialized = SerializationHelper.serialize_item(self.time_cs, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME-CS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize timeout_ar
        if self.timeout_ar is not None:
            serialized = SerializationHelper.serialize_item(self.timeout_ar, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMEOUT-AR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize timeout_as
        if self.timeout_as is not None:
            serialized = SerializationHelper.serialize_item(self.timeout_as, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMEOUT-AS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize timeout_bs
        if self.timeout_bs is not None:
            serialized = SerializationHelper.serialize_item(self.timeout_bs, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMEOUT-BS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize timeout_cr
        if self.timeout_cr is not None:
            serialized = SerializationHelper.serialize_item(self.timeout_cr, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMEOUT-CR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tp_connections (list to container "TP-CONNECTIONS")
        if self.tp_connections:
            wrapper = ET.Element("TP-CONNECTIONS")
            for item in self.tp_connections:
                serialized = SerializationHelper.serialize_item(item, "FlexrayArTpConnection")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayArTpChannel":
        """Deserialize XML element to FlexrayArTpChannel object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FlexrayArTpChannel object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FlexrayArTpChannel, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ACK-TYPE":
                setattr(obj, "ack_type", FrArTpAckType.deserialize(child))
            elif tag == "CANCELLATION":
                setattr(obj, "cancellation", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "EXTENDED":
                setattr(obj, "extended", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "MAX-AR":
                setattr(obj, "max_ar", SerializationHelper.deserialize_by_tag(child, "Integer"))
            elif tag == "MAX-AS":
                setattr(obj, "max_as", SerializationHelper.deserialize_by_tag(child, "Integer"))
            elif tag == "MAX-BS":
                setattr(obj, "max_bs", SerializationHelper.deserialize_by_tag(child, "Integer"))
            elif tag == "MAX-FC-WAIT":
                setattr(obj, "max_fc_wait", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "MAXIMUM-MESSAGE":
                setattr(obj, "maximum_message", MaximumMessageLengthType.deserialize(child))
            elif tag == "MAX-RETRIES":
                setattr(obj, "max_retries", SerializationHelper.deserialize_by_tag(child, "Integer"))
            elif tag == "MINIMUM":
                setattr(obj, "minimum", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "MULTICAST":
                setattr(obj, "multicast", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "N-PDU-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.n_pdu_refs.append(ARRef.deserialize(item_elem))
            elif tag == "TIME-BR":
                setattr(obj, "time_br", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "TIME-CS":
                setattr(obj, "time_cs", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "TIMEOUT-AR":
                setattr(obj, "timeout_ar", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "TIMEOUT-AS":
                setattr(obj, "timeout_as", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "TIMEOUT-BS":
                setattr(obj, "timeout_bs", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "TIMEOUT-CR":
                setattr(obj, "timeout_cr", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "TP-CONNECTIONS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.tp_connections.append(SerializationHelper.deserialize_by_tag(item_elem, "FlexrayArTpConnection"))

        return obj



class FlexrayArTpChannelBuilder(BuilderBase):
    """Builder for FlexrayArTpChannel with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: FlexrayArTpChannel = FlexrayArTpChannel()


    def with_ack_type(self, value: Optional[FrArTpAckType]) -> "FlexrayArTpChannelBuilder":
        """Set ack_type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ack_type = value
        return self

    def with_cancellation(self, value: Optional[Boolean]) -> "FlexrayArTpChannelBuilder":
        """Set cancellation attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.cancellation = value
        return self

    def with_extended(self, value: Optional[Boolean]) -> "FlexrayArTpChannelBuilder":
        """Set extended attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.extended = value
        return self

    def with_max_ar(self, value: Optional[Integer]) -> "FlexrayArTpChannelBuilder":
        """Set max_ar attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.max_ar = value
        return self

    def with_max_as(self, value: Optional[Integer]) -> "FlexrayArTpChannelBuilder":
        """Set max_as attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.max_as = value
        return self

    def with_max_bs(self, value: Optional[Integer]) -> "FlexrayArTpChannelBuilder":
        """Set max_bs attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.max_bs = value
        return self

    def with_max_fc_wait(self, value: Optional[PositiveInteger]) -> "FlexrayArTpChannelBuilder":
        """Set max_fc_wait attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.max_fc_wait = value
        return self

    def with_maximum_message(self, value: Optional[MaximumMessageLengthType]) -> "FlexrayArTpChannelBuilder":
        """Set maximum_message attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.maximum_message = value
        return self

    def with_max_retries(self, value: Optional[Integer]) -> "FlexrayArTpChannelBuilder":
        """Set max_retries attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.max_retries = value
        return self

    def with_minimum(self, value: Optional[TimeValue]) -> "FlexrayArTpChannelBuilder":
        """Set minimum attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.minimum = value
        return self

    def with_multicast(self, value: Optional[Boolean]) -> "FlexrayArTpChannelBuilder":
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

    def with_n_pdus(self, items: list[NPdu]) -> "FlexrayArTpChannelBuilder":
        """Set n_pdus list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.n_pdus = list(items) if items else []
        return self

    def with_time_br(self, value: Optional[TimeValue]) -> "FlexrayArTpChannelBuilder":
        """Set time_br attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.time_br = value
        return self

    def with_time_cs(self, value: Optional[TimeValue]) -> "FlexrayArTpChannelBuilder":
        """Set time_cs attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.time_cs = value
        return self

    def with_timeout_ar(self, value: Optional[TimeValue]) -> "FlexrayArTpChannelBuilder":
        """Set timeout_ar attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.timeout_ar = value
        return self

    def with_timeout_as(self, value: Optional[TimeValue]) -> "FlexrayArTpChannelBuilder":
        """Set timeout_as attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.timeout_as = value
        return self

    def with_timeout_bs(self, value: Optional[TimeValue]) -> "FlexrayArTpChannelBuilder":
        """Set timeout_bs attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.timeout_bs = value
        return self

    def with_timeout_cr(self, value: Optional[TimeValue]) -> "FlexrayArTpChannelBuilder":
        """Set timeout_cr attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.timeout_cr = value
        return self

    def with_tp_connections(self, items: list[FlexrayArTpConnection]) -> "FlexrayArTpChannelBuilder":
        """Set tp_connections list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.tp_connections = list(items) if items else []
        return self


    def add_n_pdu(self, item: NPdu) -> "FlexrayArTpChannelBuilder":
        """Add a single item to n_pdus list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.n_pdus.append(item)
        return self

    def clear_n_pdus(self) -> "FlexrayArTpChannelBuilder":
        """Clear all items from n_pdus list.

        Returns:
            self for method chaining
        """
        self._obj.n_pdus = []
        return self

    def add_tp_connection(self, item: FlexrayArTpConnection) -> "FlexrayArTpChannelBuilder":
        """Add a single item to tp_connections list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.tp_connections.append(item)
        return self

    def clear_tp_connections(self) -> "FlexrayArTpChannelBuilder":
        """Clear all items from tp_connections list.

        Returns:
            self for method chaining
        """
        self._obj.tp_connections = []
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


    def build(self) -> FlexrayArTpChannel:
        """Build and return the FlexrayArTpChannel instance with validation."""
        self._validate_instance()
        pass
        return self._obj