"""ClientServerApplicationErrorMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 129)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.application_error import (
    ApplicationError,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ClientServerApplicationErrorMapping(ARObject):
    """AUTOSAR ClientServerApplicationErrorMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CLIENT-SERVER-APPLICATION-ERROR-MAPPING"


    first_application_ref: Optional[ARRef]
    second_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "FIRST-APPLICATION-REF": lambda obj, elem: setattr(obj, "first_application_ref", ARRef.deserialize(elem)),
        "SECOND-REF": lambda obj, elem: setattr(obj, "second_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize ClientServerApplicationErrorMapping."""
        super().__init__()
        self.first_application_ref: Optional[ARRef] = None
        self.second_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize ClientServerApplicationErrorMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ClientServerApplicationErrorMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize first_application_ref
        if self.first_application_ref is not None:
            serialized = SerializationHelper.serialize_item(self.first_application_ref, "ApplicationError")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FIRST-APPLICATION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize second_ref
        if self.second_ref is not None:
            serialized = SerializationHelper.serialize_item(self.second_ref, "ApplicationError")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SECOND-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ClientServerApplicationErrorMapping":
        """Deserialize XML element to ClientServerApplicationErrorMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ClientServerApplicationErrorMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ClientServerApplicationErrorMapping, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "FIRST-APPLICATION-REF":
                setattr(obj, "first_application_ref", ARRef.deserialize(child))
            elif tag == "SECOND-REF":
                setattr(obj, "second_ref", ARRef.deserialize(child))

        return obj



class ClientServerApplicationErrorMappingBuilder(BuilderBase):
    """Builder for ClientServerApplicationErrorMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ClientServerApplicationErrorMapping = ClientServerApplicationErrorMapping()


    def with_first_application(self, value: Optional[ApplicationError]) -> "ClientServerApplicationErrorMappingBuilder":
        """Set first_application attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.first_application = value
        return self

    def with_second(self, value: Optional[ApplicationError]) -> "ClientServerApplicationErrorMappingBuilder":
        """Set second attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.second = value
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


    def build(self) -> ClientServerApplicationErrorMapping:
        """Build and return the ClientServerApplicationErrorMapping instance with validation."""
        self._validate_instance()
        pass
        return self._obj