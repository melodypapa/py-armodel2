"""SenderReceiverCompositeElementToSignalMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 247)

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
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.sender_rec_composite_type_mapping import (
    SenderRecCompositeTypeMapping,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.system_signal import (
    SystemSignal,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SenderReceiverCompositeElementToSignalMapping(DataMapping):
    """AUTOSAR SenderReceiverCompositeElementToSignalMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SENDER-RECEIVER-COMPOSITE-ELEMENT-TO-SIGNAL-MAPPING"


    data_element_ref: Optional[ARRef]
    system_signal_ref: Optional[ARRef]
    type_mapping: Optional[SenderRecCompositeTypeMapping]
    _DESERIALIZE_DISPATCH = {
        "DATA-ELEMENT-REF": lambda obj, elem: setattr(obj, "data_element_ref", ARRef.deserialize(elem)),
        "SYSTEM-SIGNAL-REF": lambda obj, elem: setattr(obj, "system_signal_ref", ARRef.deserialize(elem)),
        "TYPE-MAPPING": ("_POLYMORPHIC", "type_mapping", ["SenderRecArrayTypeMapping", "SenderRecRecordTypeMapping"]),
    }


    def __init__(self) -> None:
        """Initialize SenderReceiverCompositeElementToSignalMapping."""
        super().__init__()
        self.data_element_ref: Optional[ARRef] = None
        self.system_signal_ref: Optional[ARRef] = None
        self.type_mapping: Optional[SenderRecCompositeTypeMapping] = None

    def serialize(self) -> ET.Element:
        """Serialize SenderReceiverCompositeElementToSignalMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SenderReceiverCompositeElementToSignalMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_element_ref
        if self.data_element_ref is not None:
            serialized = SerializationHelper.serialize_item(self.data_element_ref, "VariableDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-ELEMENT-REF")
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

        # Serialize type_mapping
        if self.type_mapping is not None:
            serialized = SerializationHelper.serialize_item(self.type_mapping, "SenderRecCompositeTypeMapping")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TYPE-MAPPING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SenderReceiverCompositeElementToSignalMapping":
        """Deserialize XML element to SenderReceiverCompositeElementToSignalMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SenderReceiverCompositeElementToSignalMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SenderReceiverCompositeElementToSignalMapping, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DATA-ELEMENT-REF":
                setattr(obj, "data_element_ref", ARRef.deserialize(child))
            elif tag == "SYSTEM-SIGNAL-REF":
                setattr(obj, "system_signal_ref", ARRef.deserialize(child))
            elif tag == "TYPE-MAPPING":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "SENDER-REC-ARRAY-TYPE-MAPPING":
                        setattr(obj, "type_mapping", SerializationHelper.deserialize_by_tag(child[0], "SenderRecArrayTypeMapping"))
                    elif concrete_tag == "SENDER-REC-RECORD-TYPE-MAPPING":
                        setattr(obj, "type_mapping", SerializationHelper.deserialize_by_tag(child[0], "SenderRecRecordTypeMapping"))

        return obj



class SenderReceiverCompositeElementToSignalMappingBuilder(DataMappingBuilder):
    """Builder for SenderReceiverCompositeElementToSignalMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SenderReceiverCompositeElementToSignalMapping = SenderReceiverCompositeElementToSignalMapping()


    def with_data_element(self, value: Optional[VariableDataPrototype]) -> "SenderReceiverCompositeElementToSignalMappingBuilder":
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

    def with_system_signal(self, value: Optional[SystemSignal]) -> "SenderReceiverCompositeElementToSignalMappingBuilder":
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

    def with_type_mapping(self, value: Optional[SenderRecCompositeTypeMapping]) -> "SenderReceiverCompositeElementToSignalMappingBuilder":
        """Set type_mapping attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.type_mapping = value
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


    def build(self) -> SenderReceiverCompositeElementToSignalMapping:
        """Build and return the SenderReceiverCompositeElementToSignalMapping instance with validation."""
        self._validate_instance()
        pass
        return self._obj