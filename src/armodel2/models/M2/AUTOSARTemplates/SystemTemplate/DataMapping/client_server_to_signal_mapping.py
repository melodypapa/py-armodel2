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
        "CLIENT-SERVER": lambda obj, elem: setattr(obj, "client_server", ClientServerOperation.deserialize(elem)),
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

        # Parse call_signal_ref
        child = SerializationHelper.find_child_element(element, "CALL-SIGNAL-REF")
        if child is not None:
            call_signal_ref_value = ARRef.deserialize(child)
            obj.call_signal_ref = call_signal_ref_value

        # Parse client_server
        child = SerializationHelper.find_child_element(element, "CLIENT-SERVER")
        if child is not None:
            client_server_value = SerializationHelper.deserialize_by_tag(child, "ClientServerOperation")
            obj.client_server = client_server_value

        # Parse return_signal_ref
        child = SerializationHelper.find_child_element(element, "RETURN-SIGNAL-REF")
        if child is not None:
            return_signal_ref_value = ARRef.deserialize(child)
            obj.return_signal_ref = return_signal_ref_value

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


    def build(self) -> ClientServerToSignalMapping:
        """Build and return the ClientServerToSignalMapping instance with validation."""
        self._validate_instance()
        pass
        return self._obj