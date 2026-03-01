"""DiagnosticTestRoutineIdentifier AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 158)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_ObdService_Mode_0x08_RequestControlOfOnBoard.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import DiagnosticCommonElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticTestRoutineIdentifier(DiagnosticCommonElement):
    """AUTOSAR DiagnosticTestRoutineIdentifier."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-TEST-ROUTINE-IDENTIFIER"


    id: Optional[PositiveInteger]
    request_data: Optional[PositiveInteger]
    response_data: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "ID": lambda obj, elem: setattr(obj, "id", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "REQUEST-DATA": lambda obj, elem: setattr(obj, "request_data", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "RESPONSE-DATA": lambda obj, elem: setattr(obj, "response_data", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticTestRoutineIdentifier."""
        super().__init__()
        self.id: Optional[PositiveInteger] = None
        self.request_data: Optional[PositiveInteger] = None
        self.response_data: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticTestRoutineIdentifier to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticTestRoutineIdentifier, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize id
        if self.id is not None:
            serialized = SerializationHelper.serialize_item(self.id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize request_data
        if self.request_data is not None:
            serialized = SerializationHelper.serialize_item(self.request_data, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REQUEST-DATA")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize response_data
        if self.response_data is not None:
            serialized = SerializationHelper.serialize_item(self.response_data, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RESPONSE-DATA")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticTestRoutineIdentifier":
        """Deserialize XML element to DiagnosticTestRoutineIdentifier object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticTestRoutineIdentifier object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticTestRoutineIdentifier, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "ID":
                setattr(obj, "id", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "REQUEST-DATA":
                setattr(obj, "request_data", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "RESPONSE-DATA":
                setattr(obj, "response_data", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class DiagnosticTestRoutineIdentifierBuilder(DiagnosticCommonElementBuilder):
    """Builder for DiagnosticTestRoutineIdentifier with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticTestRoutineIdentifier = DiagnosticTestRoutineIdentifier()


    def with_id(self, value: Optional[PositiveInteger]) -> "DiagnosticTestRoutineIdentifierBuilder":
        """Set id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.id = value
        return self

    def with_request_data(self, value: Optional[PositiveInteger]) -> "DiagnosticTestRoutineIdentifierBuilder":
        """Set request_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.request_data = value
        return self

    def with_response_data(self, value: Optional[PositiveInteger]) -> "DiagnosticTestRoutineIdentifierBuilder":
        """Set response_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.response_data = value
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


    def build(self) -> DiagnosticTestRoutineIdentifier:
        """Build and return the DiagnosticTestRoutineIdentifier instance with validation."""
        self._validate_instance()
        pass
        return self._obj