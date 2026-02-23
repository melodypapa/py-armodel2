"""SenderRecRecordElementMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 236)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DataMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.sender_rec_composite_type_mapping import (
    SenderRecCompositeTypeMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.system_signal import (
    SystemSignal,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.text_table_mapping import (
    TextTableMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class SenderRecRecordElementMapping(ARObject):
    """AUTOSAR SenderRecRecordElementMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    application_record_ref: Optional[Any]
    complex_type: Optional[SenderRecCompositeTypeMapping]
    implementation_ref: Optional[Any]
    sender_to_signal_ref: Optional[ARRef]
    signal_to_ref: Optional[ARRef]
    system_signal_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize SenderRecRecordElementMapping."""
        super().__init__()
        self.application_record_ref: Optional[Any] = None
        self.complex_type: Optional[SenderRecCompositeTypeMapping] = None
        self.implementation_ref: Optional[Any] = None
        self.sender_to_signal_ref: Optional[ARRef] = None
        self.signal_to_ref: Optional[ARRef] = None
        self.system_signal_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize SenderRecRecordElementMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SenderRecRecordElementMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize application_record_ref
        if self.application_record_ref is not None:
            serialized = SerializationHelper.serialize_item(self.application_record_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("APPLICATION-RECORD-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize complex_type
        if self.complex_type is not None:
            serialized = SerializationHelper.serialize_item(self.complex_type, "SenderRecCompositeTypeMapping")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMPLEX-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize implementation_ref
        if self.implementation_ref is not None:
            serialized = SerializationHelper.serialize_item(self.implementation_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IMPLEMENTATION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sender_to_signal_ref
        if self.sender_to_signal_ref is not None:
            serialized = SerializationHelper.serialize_item(self.sender_to_signal_ref, "TextTableMapping")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SENDER-TO-SIGNAL-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize signal_to_ref
        if self.signal_to_ref is not None:
            serialized = SerializationHelper.serialize_item(self.signal_to_ref, "TextTableMapping")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SIGNAL-TO-REF")
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
    def deserialize(cls, element: ET.Element) -> "SenderRecRecordElementMapping":
        """Deserialize XML element to SenderRecRecordElementMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SenderRecRecordElementMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SenderRecRecordElementMapping, cls).deserialize(element)

        # Parse application_record_ref
        child = SerializationHelper.find_child_element(element, "APPLICATION-RECORD-REF")
        if child is not None:
            application_record_ref_value = ARRef.deserialize(child)
            obj.application_record_ref = application_record_ref_value

        # Parse complex_type
        child = SerializationHelper.find_child_element(element, "COMPLEX-TYPE")
        if child is not None:
            complex_type_value = SerializationHelper.deserialize_by_tag(child, "SenderRecCompositeTypeMapping")
            obj.complex_type = complex_type_value

        # Parse implementation_ref
        child = SerializationHelper.find_child_element(element, "IMPLEMENTATION-REF")
        if child is not None:
            implementation_ref_value = ARRef.deserialize(child)
            obj.implementation_ref = implementation_ref_value

        # Parse sender_to_signal_ref
        child = SerializationHelper.find_child_element(element, "SENDER-TO-SIGNAL-REF")
        if child is not None:
            sender_to_signal_ref_value = ARRef.deserialize(child)
            obj.sender_to_signal_ref = sender_to_signal_ref_value

        # Parse signal_to_ref
        child = SerializationHelper.find_child_element(element, "SIGNAL-TO-REF")
        if child is not None:
            signal_to_ref_value = ARRef.deserialize(child)
            obj.signal_to_ref = signal_to_ref_value

        # Parse system_signal_ref
        child = SerializationHelper.find_child_element(element, "SYSTEM-SIGNAL-REF")
        if child is not None:
            system_signal_ref_value = ARRef.deserialize(child)
            obj.system_signal_ref = system_signal_ref_value

        return obj



class SenderRecRecordElementMappingBuilder(BuilderBase):
    """Builder for SenderRecRecordElementMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SenderRecRecordElementMapping = SenderRecRecordElementMapping()


    def with_application_record(self, value: Optional[any (ApplicationRecord)]) -> "SenderRecRecordElementMappingBuilder":
        """Set application_record attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.application_record = value
        return self

    def with_complex_type(self, value: Optional[SenderRecCompositeTypeMapping]) -> "SenderRecRecordElementMappingBuilder":
        """Set complex_type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.complex_type = value
        return self

    def with_implementation(self, value: Optional[any (ImplementationData)]) -> "SenderRecRecordElementMappingBuilder":
        """Set implementation attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.implementation = value
        return self

    def with_sender_to_signal(self, value: Optional[TextTableMapping]) -> "SenderRecRecordElementMappingBuilder":
        """Set sender_to_signal attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sender_to_signal = value
        return self

    def with_signal_to(self, value: Optional[TextTableMapping]) -> "SenderRecRecordElementMappingBuilder":
        """Set signal_to attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.signal_to = value
        return self

    def with_system_signal(self, value: Optional[SystemSignal]) -> "SenderRecRecordElementMappingBuilder":
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


    def build(self) -> SenderRecRecordElementMapping:
        """Build and return the SenderRecRecordElementMapping instance with validation."""
        self._validate_instance()
        pass
        return self._obj