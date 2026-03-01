"""DiagnosticServiceTable AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 59)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticContribution.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import DiagnosticCommonElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection.diagnostic_connection import (
    DiagnosticConnection,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticServiceTable(DiagnosticCommonElement):
    """AUTOSAR DiagnosticServiceTable."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-SERVICE-TABLE"


    diagnostic_refs: list[ARRef]
    ecu_instance_ref: Optional[ARRef]
    protocol_kind: Optional[NameToken]
    service_instance_refs: list[Any]
    _DESERIALIZE_DISPATCH = {
        "DIAGNOSTICS": lambda obj, elem: obj.diagnostic_refs.append(ARRef.deserialize(elem)),
        "ECU-INSTANCE-REF": lambda obj, elem: setattr(obj, "ecu_instance_ref", ARRef.deserialize(elem)),
        "PROTOCOL-KIND": lambda obj, elem: setattr(obj, "protocol_kind", SerializationHelper.deserialize_by_tag(elem, "NameToken")),
        "SERVICE-INSTANCES": lambda obj, elem: obj.service_instance_refs.append(ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticServiceTable."""
        super().__init__()
        self.diagnostic_refs: list[ARRef] = []
        self.ecu_instance_ref: Optional[ARRef] = None
        self.protocol_kind: Optional[NameToken] = None
        self.service_instance_refs: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticServiceTable to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticServiceTable, self).serialize()

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

        # Serialize ecu_instance_ref
        if self.ecu_instance_ref is not None:
            serialized = SerializationHelper.serialize_item(self.ecu_instance_ref, "EcuInstance")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ECU-INSTANCE-REF")
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

        # Serialize service_instance_refs (list to container "SERVICE-INSTANCE-REFS")
        if self.service_instance_refs:
            wrapper = ET.Element("SERVICE-INSTANCE-REFS")
            for item in self.service_instance_refs:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("SERVICE-INSTANCE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticServiceTable":
        """Deserialize XML element to DiagnosticServiceTable object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticServiceTable object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticServiceTable, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "DIAGNOSTICS":
                obj.diagnostic_refs.append(ARRef.deserialize(child))
            elif tag == "ECU-INSTANCE-REF":
                setattr(obj, "ecu_instance_ref", ARRef.deserialize(child))
            elif tag == "PROTOCOL-KIND":
                setattr(obj, "protocol_kind", SerializationHelper.deserialize_by_tag(child, "NameToken"))
            elif tag == "SERVICE-INSTANCES":
                obj.service_instance_refs.append(ARRef.deserialize(child))

        return obj



class DiagnosticServiceTableBuilder(DiagnosticCommonElementBuilder):
    """Builder for DiagnosticServiceTable with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticServiceTable = DiagnosticServiceTable()


    def with_diagnostics(self, items: list[DiagnosticConnection]) -> "DiagnosticServiceTableBuilder":
        """Set diagnostics list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.diagnostics = list(items) if items else []
        return self

    def with_ecu_instance(self, value: Optional[EcuInstance]) -> "DiagnosticServiceTableBuilder":
        """Set ecu_instance attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ecu_instance = value
        return self

    def with_protocol_kind(self, value: Optional[NameToken]) -> "DiagnosticServiceTableBuilder":
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

    def with_service_instances(self, items: list[any (DiagnosticService)]) -> "DiagnosticServiceTableBuilder":
        """Set service_instances list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.service_instances = list(items) if items else []
        return self


    def add_diagnostic(self, item: DiagnosticConnection) -> "DiagnosticServiceTableBuilder":
        """Add a single item to diagnostics list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.diagnostics.append(item)
        return self

    def clear_diagnostics(self) -> "DiagnosticServiceTableBuilder":
        """Clear all items from diagnostics list.

        Returns:
            self for method chaining
        """
        self._obj.diagnostics = []
        return self

    def add_service_instance(self, item: any (DiagnosticService)) -> "DiagnosticServiceTableBuilder":
        """Add a single item to service_instances list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.service_instances.append(item)
        return self

    def clear_service_instances(self) -> "DiagnosticServiceTableBuilder":
        """Clear all items from service_instances list.

        Returns:
            self for method chaining
        """
        self._obj.service_instances = []
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


    def build(self) -> DiagnosticServiceTable:
        """Build and return the DiagnosticServiceTable instance with validation."""
        self._validate_instance()
        pass
        return self._obj