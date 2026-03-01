"""DiagnosticProtocol AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 58)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticContribution.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import DiagnosticCommonElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    NameToken,
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection.diagnostic_connection import (
    DiagnosticConnection,
)
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticContribution.diagnostic_service_table import (
    DiagnosticServiceTable,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticProtocol(DiagnosticCommonElement):
    """AUTOSAR DiagnosticProtocol."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-PROTOCOL"


    diagnostic_refs: list[ARRef]
    priority: Optional[PositiveInteger]
    protocol_kind: Optional[NameToken]
    send_resp_pend: Optional[Boolean]
    service_table_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "DIAGNOSTIC-REFS": lambda obj, elem: obj.diagnostic_refs.append(ARRef.deserialize(elem)),
        "PRIORITY": lambda obj, elem: setattr(obj, "priority", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "PROTOCOL-KIND": lambda obj, elem: setattr(obj, "protocol_kind", SerializationHelper.deserialize_by_tag(elem, "NameToken")),
        "SEND-RESP-PEND": lambda obj, elem: setattr(obj, "send_resp_pend", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "SERVICE-TABLE-REF": lambda obj, elem: setattr(obj, "service_table_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticProtocol."""
        super().__init__()
        self.diagnostic_refs: list[ARRef] = []
        self.priority: Optional[PositiveInteger] = None
        self.protocol_kind: Optional[NameToken] = None
        self.send_resp_pend: Optional[Boolean] = None
        self.service_table_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticProtocol to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticProtocol, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize diagnostic_refs (list to container "DIAGNOSTIC-REFS")
        if self.diagnostic_refs:
            wrapper = ET.Element("DIAGNOSTIC-REFS")
            for item in self.diagnostic_refs:
                serialized = SerializationHelper.serialize_item(item, "DiagnosticConnection")
                if serialized is not None:
                    child_elem = ET.Element("DIAGNOSTIC-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize priority
        if self.priority is not None:
            serialized = SerializationHelper.serialize_item(self.priority, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PRIORITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize protocol_kind
        if self.protocol_kind is not None:
            serialized = SerializationHelper.serialize_item(self.protocol_kind, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PROTOCOL-KIND")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize send_resp_pend
        if self.send_resp_pend is not None:
            serialized = SerializationHelper.serialize_item(self.send_resp_pend, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SEND-RESP-PEND")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize service_table_ref
        if self.service_table_ref is not None:
            serialized = SerializationHelper.serialize_item(self.service_table_ref, "DiagnosticServiceTable")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SERVICE-TABLE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticProtocol":
        """Deserialize XML element to DiagnosticProtocol object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticProtocol object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticProtocol, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DIAGNOSTIC-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.diagnostic_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "DiagnosticConnection"))
            elif tag == "PRIORITY":
                setattr(obj, "priority", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "PROTOCOL-KIND":
                setattr(obj, "protocol_kind", SerializationHelper.deserialize_by_tag(child, "NameToken"))
            elif tag == "SEND-RESP-PEND":
                setattr(obj, "send_resp_pend", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "SERVICE-TABLE-REF":
                setattr(obj, "service_table_ref", ARRef.deserialize(child))

        return obj



class DiagnosticProtocolBuilder(DiagnosticCommonElementBuilder):
    """Builder for DiagnosticProtocol with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticProtocol = DiagnosticProtocol()


    def with_diagnostics(self, items: list[DiagnosticConnection]) -> "DiagnosticProtocolBuilder":
        """Set diagnostics list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.diagnostics = list(items) if items else []
        return self

    def with_priority(self, value: Optional[PositiveInteger]) -> "DiagnosticProtocolBuilder":
        """Set priority attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.priority = value
        return self

    def with_protocol_kind(self, value: Optional[NameToken]) -> "DiagnosticProtocolBuilder":
        """Set protocol_kind attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.protocol_kind = value
        return self

    def with_send_resp_pend(self, value: Optional[Boolean]) -> "DiagnosticProtocolBuilder":
        """Set send_resp_pend attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.send_resp_pend = value
        return self

    def with_service_table(self, value: Optional[DiagnosticServiceTable]) -> "DiagnosticProtocolBuilder":
        """Set service_table attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.service_table = value
        return self


    def add_diagnostic(self, item: DiagnosticConnection) -> "DiagnosticProtocolBuilder":
        """Add a single item to diagnostics list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.diagnostics.append(item)
        return self

    def clear_diagnostics(self) -> "DiagnosticProtocolBuilder":
        """Clear all items from diagnostics list.

        Returns:
            self for method chaining
        """
        self._obj.diagnostics = []
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


    def build(self) -> DiagnosticProtocol:
        """Build and return the DiagnosticProtocol instance with validation."""
        self._validate_instance()
        pass
        return self._obj