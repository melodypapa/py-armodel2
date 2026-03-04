"""ClientServerToSignalMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 242)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DataMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.data_mapping import (
    DataMapping,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.data_mapping import DataMappingBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.system_signal import (
    SystemSignal,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ClientServerToSignalMapping(DataMapping):
    """AUTOSAR ClientServerToSignalMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CLIENT-SERVER-TO-SIGNAL-MAPPING"


    call_signal_ref: Optional[ARRef]
    client_server: Optional[ClientServerOperation]
    return_signal_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "CALL-SIGNAL-REF": lambda obj, elem: setattr(obj, "call_signal_ref", ARRef.deserialize(elem)),
        "CLIENT-SERVER": lambda obj, elem: setattr(obj, "client_server", SerializationHelper.deserialize_by_tag(elem, "ClientServerOperation")),
        "RETURN-SIGNAL-REF": lambda obj, elem: setattr(obj, "return_signal_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize ClientServerToSignalMapping."""
        super().__init__()
        self.call_signal_ref: Optional[ARRef] = None
        self.client_server: Optional[ClientServerOperation] = None
        self.return_signal_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize ClientServerToSignalMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ClientServerToSignalMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize call_signal_ref
        if self.call_signal_ref is not None:
            serialized = SerializationHelper.serialize_item(self.call_signal_ref, "SystemSignal")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CALL-SIGNAL-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize client_server
        if self.client_server is not None:
            serialized = SerializationHelper.serialize_item(self.client_server, "ClientServerOperation")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CLIENT-SERVER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize return_signal_ref
        if self.return_signal_ref is not None:
            serialized = SerializationHelper.serialize_item(self.return_signal_ref, "SystemSignal")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RETURN-SIGNAL-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ClientServerToSignalMapping":
        """Deserialize XML element to ClientServerToSignalMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ClientServerToSignalMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ClientServerToSignalMapping, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CALL-SIGNAL-REF":
                setattr(obj, "call_signal_ref", ARRef.deserialize(child))
            elif tag == "CLIENT-SERVER":
                setattr(obj, "client_server", SerializationHelper.deserialize_by_tag(child, "ClientServerOperation"))
            elif tag == "RETURN-SIGNAL-REF":
                setattr(obj, "return_signal_ref", ARRef.deserialize(child))

        return obj



class ClientServerToSignalMappingBuilder(DataMappingBuilder):
    """Builder for ClientServerToSignalMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ClientServerToSignalMapping = ClientServerToSignalMapping()


    def with_call_signal(self, value: Optional[SystemSignal]) -> "ClientServerToSignalMappingBuilder":
        """Set call_signal attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.call_signal = value
        return self

    def with_client_server(self, value: Optional[ClientServerOperation]) -> "ClientServerToSignalMappingBuilder":
        """Set client_server attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.client_server = value
        return self

    def with_return_signal(self, value: Optional[SystemSignal]) -> "ClientServerToSignalMappingBuilder":
        """Set return_signal attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.return_signal = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "callSignal",
        "clientServer",
        "returnSignal",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> ClientServerToSignalMapping:
        """Build and return the ClientServerToSignalMapping instance with validation."""
        self._validate_instance()
        return self._obj