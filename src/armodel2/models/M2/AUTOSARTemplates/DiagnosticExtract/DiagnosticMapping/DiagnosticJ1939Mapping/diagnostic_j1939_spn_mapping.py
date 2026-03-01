"""DiagnosticJ1939SpnMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 267)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping_DiagnosticJ1939Mapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import DiagnosticMappingBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.J1939.diagnostic_j1939_node import (
    DiagnosticJ1939Node,
)
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.J1939.diagnostic_j1939_spn import (
    DiagnosticJ1939Spn,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.system_signal import (
    SystemSignal,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticJ1939SpnMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticJ1939SpnMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-J1939-SPN-MAPPING"


    sending_node_refs: list[ARRef]
    spn_ref: Optional[ARRef]
    system_signal_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "SENDING-NODES": lambda obj, elem: obj.sending_node_refs.append(ARRef.deserialize(elem)),
        "SPN-REF": lambda obj, elem: setattr(obj, "spn_ref", ARRef.deserialize(elem)),
        "SYSTEM-SIGNAL-REF": lambda obj, elem: setattr(obj, "system_signal_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticJ1939SpnMapping."""
        super().__init__()
        self.sending_node_refs: list[ARRef] = []
        self.spn_ref: Optional[ARRef] = None
        self.system_signal_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticJ1939SpnMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticJ1939SpnMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize sending_node_refs (list to container "SENDING-NODE-REFS")
        if self.sending_node_refs:
            wrapper = ET.Element("SENDING-NODE-REFS")
            for item in self.sending_node_refs:
                serialized = SerializationHelper.serialize_item(item, "DiagnosticJ1939Node")
                if serialized is not None:
                    child_elem = ET.Element("SENDING-NODE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize spn_ref
        if self.spn_ref is not None:
            serialized = SerializationHelper.serialize_item(self.spn_ref, "DiagnosticJ1939Spn")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SPN-REF")
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
    def deserialize(cls, element: ET.Element) -> "DiagnosticJ1939SpnMapping":
        """Deserialize XML element to DiagnosticJ1939SpnMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticJ1939SpnMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticJ1939SpnMapping, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "SENDING-NODES":
                obj.sending_node_refs.append(ARRef.deserialize(child))
            elif tag == "SPN-REF":
                setattr(obj, "spn_ref", ARRef.deserialize(child))
            elif tag == "SYSTEM-SIGNAL-REF":
                setattr(obj, "system_signal_ref", ARRef.deserialize(child))

        return obj



class DiagnosticJ1939SpnMappingBuilder(DiagnosticMappingBuilder):
    """Builder for DiagnosticJ1939SpnMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticJ1939SpnMapping = DiagnosticJ1939SpnMapping()


    def with_sending_nodes(self, items: list[DiagnosticJ1939Node]) -> "DiagnosticJ1939SpnMappingBuilder":
        """Set sending_nodes list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.sending_nodes = list(items) if items else []
        return self

    def with_spn(self, value: Optional[DiagnosticJ1939Spn]) -> "DiagnosticJ1939SpnMappingBuilder":
        """Set spn attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.spn = value
        return self

    def with_system_signal(self, value: Optional[SystemSignal]) -> "DiagnosticJ1939SpnMappingBuilder":
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


    def add_sending_node(self, item: DiagnosticJ1939Node) -> "DiagnosticJ1939SpnMappingBuilder":
        """Add a single item to sending_nodes list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.sending_nodes.append(item)
        return self

    def clear_sending_nodes(self) -> "DiagnosticJ1939SpnMappingBuilder":
        """Clear all items from sending_nodes list.

        Returns:
            self for method chaining
        """
        self._obj.sending_nodes = []
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


    def build(self) -> DiagnosticJ1939SpnMapping:
        """Build and return the DiagnosticJ1939SpnMapping instance with validation."""
        self._validate_instance()
        pass
        return self._obj