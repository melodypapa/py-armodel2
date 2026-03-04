"""SomeipTpConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 620)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.someip_tp_channel import (
    SomeipTpChannel,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SomeipTpConnection(ARObject):
    """AUTOSAR SomeipTpConnection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SOMEIP-TP-CONNECTION"


    tp_channel_ref: Optional[ARRef]
    tp_sdu_ref: Optional[ARRef]
    transport_pdu_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "TP-CHANNEL-REF": lambda obj, elem: setattr(obj, "tp_channel_ref", ARRef.deserialize(elem)),
        "TP-SDU-REF": lambda obj, elem: setattr(obj, "tp_sdu_ref", ARRef.deserialize(elem)),
        "TRANSPORT-PDU-REF": lambda obj, elem: setattr(obj, "transport_pdu_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize SomeipTpConnection."""
        super().__init__()
        self.tp_channel_ref: Optional[ARRef] = None
        self.tp_sdu_ref: Optional[ARRef] = None
        self.transport_pdu_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize SomeipTpConnection to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SomeipTpConnection, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize tp_channel_ref
        if self.tp_channel_ref is not None:
            serialized = SerializationHelper.serialize_item(self.tp_channel_ref, "SomeipTpChannel")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TP-CHANNEL-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tp_sdu_ref
        if self.tp_sdu_ref is not None:
            serialized = SerializationHelper.serialize_item(self.tp_sdu_ref, "PduTriggering")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TP-SDU-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize transport_pdu_ref
        if self.transport_pdu_ref is not None:
            serialized = SerializationHelper.serialize_item(self.transport_pdu_ref, "PduTriggering")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRANSPORT-PDU-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SomeipTpConnection":
        """Deserialize XML element to SomeipTpConnection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SomeipTpConnection object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SomeipTpConnection, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "TP-CHANNEL-REF":
                setattr(obj, "tp_channel_ref", ARRef.deserialize(child))
            elif tag == "TP-SDU-REF":
                setattr(obj, "tp_sdu_ref", ARRef.deserialize(child))
            elif tag == "TRANSPORT-PDU-REF":
                setattr(obj, "transport_pdu_ref", ARRef.deserialize(child))

        return obj



class SomeipTpConnectionBuilder(BuilderBase):
    """Builder for SomeipTpConnection with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SomeipTpConnection = SomeipTpConnection()


    def with_tp_channel(self, value: Optional[SomeipTpChannel]) -> "SomeipTpConnectionBuilder":
        """Set tp_channel attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tp_channel = value
        return self

    def with_tp_sdu(self, value: Optional[PduTriggering]) -> "SomeipTpConnectionBuilder":
        """Set tp_sdu attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tp_sdu = value
        return self

    def with_transport_pdu(self, value: Optional[PduTriggering]) -> "SomeipTpConnectionBuilder":
        """Set transport_pdu attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.transport_pdu = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "tpChannel",
        "tpSdu",
        "transportPdu",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> SomeipTpConnection:
        """Build and return the SomeipTpConnection instance with validation."""
        self._validate_instance()
        return self._obj