"""IPduPort AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 304)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.comm_connector_port import (
    CommConnectorPort,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.comm_connector_port import CommConnectorPortBuilder
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    IPduSignalProcessingEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class IPduPort(CommConnectorPort):
    """AUTOSAR IPduPort."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    i_pdu_signal: Optional[IPduSignalProcessingEnum]
    rx_security: Optional[Boolean]
    timestamp_rx: Optional[TimeValue]
    use_auth_data: Optional[Boolean]
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
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

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

        # Parse i_pdu_signal
        child = SerializationHelper.find_child_element(element, "I-PDU-SIGNAL")
        if child is not None:
            i_pdu_signal_value = IPduSignalProcessingEnum.deserialize(child)
            obj.i_pdu_signal = i_pdu_signal_value

        # Parse rx_security
        child = SerializationHelper.find_child_element(element, "RX-SECURITY")
        if child is not None:
            rx_security_value = child.text
            obj.rx_security = rx_security_value

        # Parse timestamp_rx
        child = SerializationHelper.find_child_element(element, "TIMESTAMP-RX")
        if child is not None:
            timestamp_rx_value = child.text
            obj.timestamp_rx = timestamp_rx_value

        # Parse use_auth_data
        child = SerializationHelper.find_child_element(element, "USE-AUTH-DATA")
        if child is not None:
            use_auth_data_value = child.text
            obj.use_auth_data = use_auth_data_value

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




    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel.core import GlobalSettingsManager, BuilderValidationMode

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


    def build(self) -> IPduPort:
        """Build and return the IPduPort instance with validation."""
        self._validate_instance()
        pass
        return self._obj