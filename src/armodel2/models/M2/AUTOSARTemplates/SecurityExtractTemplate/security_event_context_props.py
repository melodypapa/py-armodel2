"""SecurityEventContextProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 258)
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 33)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.SecurityExtractTemplate.security_event_definition import (
    SecurityEventDefinition,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SecurityEventContextProps(Identifiable):
    """AUTOSAR SecurityEventContextProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SECURITY-EVENT-CONTEXT-PROPS"


    context_data: Optional[Any]
    default: Optional[Any]
    persistent: Optional[Boolean]
    security_event_ref: Optional[ARRef]
    sensor_instance: Optional[PositiveInteger]
    severity: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "CONTEXT-DATA": lambda obj, elem: setattr(obj, "context_data", SerializationHelper.deserialize_by_tag(elem, "any (SecurityEventContext)")),
        "DEFAULT": lambda obj, elem: setattr(obj, "default", SerializationHelper.deserialize_by_tag(elem, "any (SecurityEventReporting)")),
        "PERSISTENT": lambda obj, elem: setattr(obj, "persistent", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "SECURITY-EVENT-REF": lambda obj, elem: setattr(obj, "security_event_ref", ARRef.deserialize(elem)),
        "SENSOR-INSTANCE": lambda obj, elem: setattr(obj, "sensor_instance", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "SEVERITY": lambda obj, elem: setattr(obj, "severity", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize SecurityEventContextProps."""
        super().__init__()
        self.context_data: Optional[Any] = None
        self.default: Optional[Any] = None
        self.persistent: Optional[Boolean] = None
        self.security_event_ref: Optional[ARRef] = None
        self.sensor_instance: Optional[PositiveInteger] = None
        self.severity: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize SecurityEventContextProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SecurityEventContextProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize context_data
        if self.context_data is not None:
            serialized = SerializationHelper.serialize_item(self.context_data, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTEXT-DATA")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize default
        if self.default is not None:
            serialized = SerializationHelper.serialize_item(self.default, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEFAULT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize persistent
        if self.persistent is not None:
            serialized = SerializationHelper.serialize_item(self.persistent, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PERSISTENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize security_event_ref
        if self.security_event_ref is not None:
            serialized = SerializationHelper.serialize_item(self.security_event_ref, "SecurityEventDefinition")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SECURITY-EVENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sensor_instance
        if self.sensor_instance is not None:
            serialized = SerializationHelper.serialize_item(self.sensor_instance, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SENSOR-INSTANCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize severity
        if self.severity is not None:
            serialized = SerializationHelper.serialize_item(self.severity, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SEVERITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SecurityEventContextProps":
        """Deserialize XML element to SecurityEventContextProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SecurityEventContextProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SecurityEventContextProps, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CONTEXT-DATA":
                setattr(obj, "context_data", SerializationHelper.deserialize_by_tag(child, "any (SecurityEventContext)"))
            elif tag == "DEFAULT":
                setattr(obj, "default", SerializationHelper.deserialize_by_tag(child, "any (SecurityEventReporting)"))
            elif tag == "PERSISTENT":
                setattr(obj, "persistent", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "SECURITY-EVENT-REF":
                setattr(obj, "security_event_ref", ARRef.deserialize(child))
            elif tag == "SENSOR-INSTANCE":
                setattr(obj, "sensor_instance", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "SEVERITY":
                setattr(obj, "severity", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class SecurityEventContextPropsBuilder(IdentifiableBuilder):
    """Builder for SecurityEventContextProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SecurityEventContextProps = SecurityEventContextProps()


    def with_context_data(self, value: Optional[any (SecurityEventContext)]) -> "SecurityEventContextPropsBuilder":
        """Set context_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.context_data = value
        return self

    def with_default(self, value: Optional[any (SecurityEventReporting)]) -> "SecurityEventContextPropsBuilder":
        """Set default attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.default = value
        return self

    def with_persistent(self, value: Optional[Boolean]) -> "SecurityEventContextPropsBuilder":
        """Set persistent attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.persistent = value
        return self

    def with_security_event(self, value: Optional[SecurityEventDefinition]) -> "SecurityEventContextPropsBuilder":
        """Set security_event attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.security_event = value
        return self

    def with_sensor_instance(self, value: Optional[PositiveInteger]) -> "SecurityEventContextPropsBuilder":
        """Set sensor_instance attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sensor_instance = value
        return self

    def with_severity(self, value: Optional[PositiveInteger]) -> "SecurityEventContextPropsBuilder":
        """Set severity attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.severity = value
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


    def build(self) -> SecurityEventContextProps:
        """Build and return the SecurityEventContextProps instance with validation."""
        self._validate_instance()
        pass
        return self._obj