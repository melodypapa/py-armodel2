"""SenderReceiverToSignalMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 1005)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 229)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DataMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel2.serialization.decorators import instance_ref
from armodel2.serialization.decorators import ref_conditional

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.data_mapping import (
    DataMapping,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.data_mapping import DataMappingBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.system_signal import (
    SystemSignal,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.text_table_mapping import (
    TextTableMapping,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs.variable_data_prototype_in_system_instance_ref import (
    VariableDataPrototypeInSystemInstanceRef,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SenderReceiverToSignalMapping(DataMapping):
    """AUTOSAR SenderReceiverToSignalMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _data_element_iref: Optional[VariableDataPrototypeInSystemInstanceRef]
    sender_to_signal_text_table_mapping: Optional[TextTableMapping]
    signal_to_receiver_text_table_mapping: Optional[TextTableMapping]
    system_signal_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize SenderReceiverToSignalMapping."""
        super().__init__()
        self._data_element_iref: Optional[VariableDataPrototypeInSystemInstanceRef] = None
        self.sender_to_signal_text_table_mapping: Optional[TextTableMapping] = None
        self.signal_to_receiver_text_table_mapping: Optional[TextTableMapping] = None
        self.system_signal_ref: Optional[ARRef] = None
    @property
    @instance_ref(flatten=True)
    def data_element_iref(self) -> Optional[VariableDataPrototypeInSystemInstanceRef]:
        """Get data_element_iref instance reference."""
        return self._data_element_iref

    @data_element_iref.setter
    def data_element_iref(self, value: Optional[VariableDataPrototypeInSystemInstanceRef]) -> None:
        """Set data_element_iref instance reference."""
        self._data_element_iref = value


    def serialize(self) -> ET.Element:
        """Serialize SenderReceiverToSignalMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SenderReceiverToSignalMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_element_iref (instance reference with wrapper "DATA-ELEMENT-IREF")
        if self.data_element_iref is not None:
            serialized = SerializationHelper.serialize_item(self.data_element_iref, "VariableDataPrototypeInSystemInstanceRef")
            if serialized is not None:
                # Wrap in IREF wrapper element
                iref_wrapper = ET.Element("DATA-ELEMENT-IREF")
                # Flatten: append children of serialized element directly to iref wrapper
                for child in serialized:
                    iref_wrapper.append(child)
                elem.append(iref_wrapper)

        # Serialize sender_to_signal_text_table_mapping
        if self.sender_to_signal_text_table_mapping is not None:
            serialized = SerializationHelper.serialize_item(self.sender_to_signal_text_table_mapping, "TextTableMapping")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SENDER-TO-SIGNAL-TEXT-TABLE-MAPPING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize signal_to_receiver_text_table_mapping
        if self.signal_to_receiver_text_table_mapping is not None:
            serialized = SerializationHelper.serialize_item(self.signal_to_receiver_text_table_mapping, "TextTableMapping")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SIGNAL-TO-RECEIVER-TEXT-TABLE-MAPPING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize system_signal_ref
        if self.system_signal_ref is not None:
            serialized = SerializationHelper.serialize_item(self.system_signal_ref, "SystemSignal")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SYSTEM-SIGNAL-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SenderReceiverToSignalMapping":
        """Deserialize XML element to SenderReceiverToSignalMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SenderReceiverToSignalMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SenderReceiverToSignalMapping, cls).deserialize(element)

        # Parse data_element_iref (instance reference from wrapper "DATA-ELEMENT-IREF")
        wrapper = SerializationHelper.find_child_element(element, "DATA-ELEMENT-IREF")
        if wrapper is not None:
            # Deserialize wrapper element directly as the type (flattened structure)
            data_element_iref_value = SerializationHelper.deserialize_by_tag(wrapper, "VariableDataPrototypeInSystemInstanceRef")
            obj.data_element_iref = data_element_iref_value

        # Parse sender_to_signal_text_table_mapping
        child = SerializationHelper.find_child_element(element, "SENDER-TO-SIGNAL-TEXT-TABLE-MAPPING")
        if child is not None:
            sender_to_signal_text_table_mapping_value = SerializationHelper.deserialize_by_tag(child, "TextTableMapping")
            obj.sender_to_signal_text_table_mapping = sender_to_signal_text_table_mapping_value

        # Parse signal_to_receiver_text_table_mapping
        child = SerializationHelper.find_child_element(element, "SIGNAL-TO-RECEIVER-TEXT-TABLE-MAPPING")
        if child is not None:
            signal_to_receiver_text_table_mapping_value = SerializationHelper.deserialize_by_tag(child, "TextTableMapping")
            obj.signal_to_receiver_text_table_mapping = signal_to_receiver_text_table_mapping_value

        # Parse system_signal_ref
        child = SerializationHelper.find_child_element(element, "SYSTEM-SIGNAL-REF")
        if child is not None:
            system_signal_ref_value = ARRef.deserialize(child)
            obj.system_signal_ref = system_signal_ref_value

        return obj



class SenderReceiverToSignalMappingBuilder(DataMappingBuilder):
    """Builder for SenderReceiverToSignalMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SenderReceiverToSignalMapping = SenderReceiverToSignalMapping()


    def with_data_element(self, value: Optional[VariableDataPrototypeInSystemInstanceRef]) -> "SenderReceiverToSignalMappingBuilder":
        """Set data_element attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.data_element = value
        return self

    def with_sender_to_signal_text_table_mapping(self, value: Optional[TextTableMapping]) -> "SenderReceiverToSignalMappingBuilder":
        """Set sender_to_signal_text_table_mapping attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sender_to_signal_text_table_mapping = value
        return self

    def with_signal_to_receiver_text_table_mapping(self, value: Optional[TextTableMapping]) -> "SenderReceiverToSignalMappingBuilder":
        """Set signal_to_receiver_text_table_mapping attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.signal_to_receiver_text_table_mapping = value
        return self

    def with_system_signal(self, value: Optional[SystemSignal]) -> "SenderReceiverToSignalMappingBuilder":
        """Set system_signal attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.system_signal = value
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


    def build(self) -> SenderReceiverToSignalMapping:
        """Build and return the SenderReceiverToSignalMapping instance with validation."""
        self._validate_instance()
        pass
        return self._obj