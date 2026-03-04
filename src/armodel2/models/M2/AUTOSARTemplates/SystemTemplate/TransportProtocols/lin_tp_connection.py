"""LinTpConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 615)

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
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.lin_tp_node import (
    LinTpNode,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.n_pdu import (
    NPdu,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_address import (
    TpAddress,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class LinTpConnection(TpConnection):
    """AUTOSAR LinTpConnection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "LIN-TP-CONNECTION"


    data_pdu_ref: Optional[ARRef]
    flow_control_ref: Optional[ARRef]
    lin_tp_n_sdu_ref: Optional[ARRef]
    multicast_ref: Optional[ARRef]
    receiver_refs: list[ARRef]
    timeout_as: Optional[TimeValue]
    timeout_cr: Optional[TimeValue]
    timeout_cs: Optional[TimeValue]
    transmitter_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "DATA-PDU-REF": lambda obj, elem: setattr(obj, "data_pdu_ref", ARRef.deserialize(elem)),
        "FLOW-CONTROL-REF": lambda obj, elem: setattr(obj, "flow_control_ref", ARRef.deserialize(elem)),
        "LIN-TP-N-SDU-REF": ("_POLYMORPHIC", "lin_tp_n_sdu_ref", ["ContainerIPdu", "DcmIPdu", "GeneralPurposeIPdu", "ISignalIPdu", "J1939DcmIPdu", "MultiplexedIPdu", "NPdu", "SecuredIPdu", "UserDefinedIPdu"]),
        "MULTICAST-REF": lambda obj, elem: setattr(obj, "multicast_ref", ARRef.deserialize(elem)),
        "RECEIVER-REFS": lambda obj, elem: [obj.receiver_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "TIMEOUT-AS": lambda obj, elem: setattr(obj, "timeout_as", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "TIMEOUT-CR": lambda obj, elem: setattr(obj, "timeout_cr", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "TIMEOUT-CS": lambda obj, elem: setattr(obj, "timeout_cs", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "TRANSMITTER-REF": lambda obj, elem: setattr(obj, "transmitter_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize LinTpConnection."""
        super().__init__()
        self.data_pdu_ref: Optional[ARRef] = None
        self.flow_control_ref: Optional[ARRef] = None
        self.lin_tp_n_sdu_ref: Optional[ARRef] = None
        self.multicast_ref: Optional[ARRef] = None
        self.receiver_refs: list[ARRef] = []
        self.timeout_as: Optional[TimeValue] = None
        self.timeout_cr: Optional[TimeValue] = None
        self.timeout_cs: Optional[TimeValue] = None
        self.transmitter_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize LinTpConnection to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(LinTpConnection, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_pdu_ref
        if self.data_pdu_ref is not None:
            serialized = SerializationHelper.serialize_item(self.data_pdu_ref, "NPdu")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-PDU-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize flow_control_ref
        if self.flow_control_ref is not None:
            serialized = SerializationHelper.serialize_item(self.flow_control_ref, "NPdu")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FLOW-CONTROL-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize lin_tp_n_sdu_ref
        if self.lin_tp_n_sdu_ref is not None:
            serialized = SerializationHelper.serialize_item(self.lin_tp_n_sdu_ref, "IPdu")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LIN-TP-N-SDU-REF")
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
                serialized = SerializationHelper.serialize_item(item, "LinTpNode")
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

        # Serialize timeout_cs
        if self.timeout_cs is not None:
            serialized = SerializationHelper.serialize_item(self.timeout_cs, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMEOUT-CS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize transmitter_ref
        if self.transmitter_ref is not None:
            serialized = SerializationHelper.serialize_item(self.transmitter_ref, "LinTpNode")
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

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LinTpConnection":
        """Deserialize XML element to LinTpConnection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LinTpConnection object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(LinTpConnection, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DATA-PDU-REF":
                setattr(obj, "data_pdu_ref", ARRef.deserialize(child))
            elif tag == "FLOW-CONTROL-REF":
                setattr(obj, "flow_control_ref", ARRef.deserialize(child))
            elif tag == "LIN-TP-N-SDU-REF":
                setattr(obj, "lin_tp_n_sdu_ref", ARRef.deserialize(child))
            elif tag == "MULTICAST-REF":
                setattr(obj, "multicast_ref", ARRef.deserialize(child))
            elif tag == "RECEIVER-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.receiver_refs.append(ARRef.deserialize(item_elem))
            elif tag == "TIMEOUT-AS":
                setattr(obj, "timeout_as", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "TIMEOUT-CR":
                setattr(obj, "timeout_cr", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "TIMEOUT-CS":
                setattr(obj, "timeout_cs", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "TRANSMITTER-REF":
                setattr(obj, "transmitter_ref", ARRef.deserialize(child))

        return obj



class LinTpConnectionBuilder(TpConnectionBuilder):
    """Builder for LinTpConnection with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: LinTpConnection = LinTpConnection()


    def with_data_pdu(self, value: Optional[NPdu]) -> "LinTpConnectionBuilder":
        """Set data_pdu attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.data_pdu = value
        return self

    def with_flow_control(self, value: Optional[NPdu]) -> "LinTpConnectionBuilder":
        """Set flow_control attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.flow_control = value
        return self

    def with_lin_tp_n_sdu(self, value: Optional[IPdu]) -> "LinTpConnectionBuilder":
        """Set lin_tp_n_sdu attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.lin_tp_n_sdu = value
        return self

    def with_multicast(self, value: Optional[TpAddress]) -> "LinTpConnectionBuilder":
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

    def with_receivers(self, items: list[LinTpNode]) -> "LinTpConnectionBuilder":
        """Set receivers list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.receivers = list(items) if items else []
        return self

    def with_timeout_as(self, value: Optional[TimeValue]) -> "LinTpConnectionBuilder":
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

    def with_timeout_cr(self, value: Optional[TimeValue]) -> "LinTpConnectionBuilder":
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

    def with_timeout_cs(self, value: Optional[TimeValue]) -> "LinTpConnectionBuilder":
        """Set timeout_cs attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.timeout_cs = value
        return self

    def with_transmitter(self, value: Optional[LinTpNode]) -> "LinTpConnectionBuilder":
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


    def add_receiver(self, item: LinTpNode) -> "LinTpConnectionBuilder":
        """Add a single item to receivers list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.receivers.append(item)
        return self

    def clear_receivers(self) -> "LinTpConnectionBuilder":
        """Clear all items from receivers list.

        Returns:
            self for method chaining
        """
        self._obj.receivers = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "dataPdu",
        "flowControl",
        "linTpNSdu",
        "multicast",
        "receiver",
        "timeoutAs",
        "timeoutCr",
        "timeoutCs",
        "transmitter",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> LinTpConnection:
        """Build and return the LinTpConnection instance with validation."""
        self._validate_instance()
        return self._obj