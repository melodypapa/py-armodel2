"""DiagnosticFimAliasEventMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 262)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticEvent.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import DiagnosticMappingBuilder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_event import (
    DiagnosticEvent,
)


class DiagnosticFimAliasEventMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticFimAliasEventMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    actual_event_ref: Optional[ARRef]
    alias_event_event_ref: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticFimAliasEventMapping."""
        super().__init__()
        self.actual_event_ref: Optional[ARRef] = None
        self.alias_event_event_ref: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticFimAliasEventMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticFimAliasEventMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize actual_event_ref
        if self.actual_event_ref is not None:
            serialized = SerializationHelper.serialize_item(self.actual_event_ref, "DiagnosticEvent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ACTUAL-EVENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize alias_event_event_ref
        if self.alias_event_event_ref is not None:
            serialized = SerializationHelper.serialize_item(self.alias_event_event_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ALIAS-EVENT-EVENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticFimAliasEventMapping":
        """Deserialize XML element to DiagnosticFimAliasEventMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticFimAliasEventMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticFimAliasEventMapping, cls).deserialize(element)

        # Parse actual_event_ref
        child = SerializationHelper.find_child_element(element, "ACTUAL-EVENT-REF")
        if child is not None:
            actual_event_ref_value = ARRef.deserialize(child)
            obj.actual_event_ref = actual_event_ref_value

        # Parse alias_event_event_ref
        child = SerializationHelper.find_child_element(element, "ALIAS-EVENT-EVENT-REF")
        if child is not None:
            alias_event_event_ref_value = ARRef.deserialize(child)
            obj.alias_event_event_ref = alias_event_event_ref_value

        return obj



class DiagnosticFimAliasEventMappingBuilder(DiagnosticMappingBuilder):
    """Builder for DiagnosticFimAliasEventMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticFimAliasEventMapping = DiagnosticFimAliasEventMapping()


    def with_actual_event(self, value: Optional[DiagnosticEvent]) -> "DiagnosticFimAliasEventMappingBuilder":
        """Set actual_event attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.actual_event = value
        return self

    def with_alias_event_event(self, value: Optional[any (DiagnosticFimAlias)]) -> "DiagnosticFimAliasEventMappingBuilder":
        """Set alias_event_event attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.alias_event_event = value
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


    def build(self) -> DiagnosticFimAliasEventMapping:
        """Build and return the DiagnosticFimAliasEventMapping instance with validation."""
        self._validate_instance()
        pass
        return self._obj