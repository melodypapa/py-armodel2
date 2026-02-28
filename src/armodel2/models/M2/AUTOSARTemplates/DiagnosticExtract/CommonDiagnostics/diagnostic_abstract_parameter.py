"""DiagnosticAbstractParameter AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 37)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_CommonDiagnostics.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_data_element import (
    DiagnosticDataElement,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticAbstractParameter(ARObject, ABC):
    """AUTOSAR DiagnosticAbstractParameter."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    bit_offset: Optional[PositiveInteger]
    data_element: Optional[DiagnosticDataElement]
    parameter_size: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "BIT-OFFSET": lambda obj, elem: setattr(obj, "bit_offset", elem.text),
        "DATA-ELEMENT": lambda obj, elem: setattr(obj, "data_element", DiagnosticDataElement.deserialize(elem)),
        "PARAMETER-SIZE": lambda obj, elem: setattr(obj, "parameter_size", elem.text),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticAbstractParameter."""
        super().__init__()
        self.bit_offset: Optional[PositiveInteger] = None
        self.data_element: Optional[DiagnosticDataElement] = None
        self.parameter_size: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticAbstractParameter to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticAbstractParameter, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize bit_offset
        if self.bit_offset is not None:
            serialized = SerializationHelper.serialize_item(self.bit_offset, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BIT-OFFSET")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize data_element
        if self.data_element is not None:
            serialized = SerializationHelper.serialize_item(self.data_element, "DiagnosticDataElement")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-ELEMENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize parameter_size
        if self.parameter_size is not None:
            serialized = SerializationHelper.serialize_item(self.parameter_size, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PARAMETER-SIZE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticAbstractParameter":
        """Deserialize XML element to DiagnosticAbstractParameter object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticAbstractParameter object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticAbstractParameter, cls).deserialize(element)

        # Parse bit_offset
        child = SerializationHelper.find_child_element(element, "BIT-OFFSET")
        if child is not None:
            bit_offset_value = child.text
            obj.bit_offset = bit_offset_value

        # Parse data_element
        child = SerializationHelper.find_child_element(element, "DATA-ELEMENT")
        if child is not None:
            data_element_value = SerializationHelper.deserialize_by_tag(child, "DiagnosticDataElement")
            obj.data_element = data_element_value

        # Parse parameter_size
        child = SerializationHelper.find_child_element(element, "PARAMETER-SIZE")
        if child is not None:
            parameter_size_value = child.text
            obj.parameter_size = parameter_size_value

        return obj



class DiagnosticAbstractParameterBuilder(BuilderBase, ABC):
    """Builder for DiagnosticAbstractParameter with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticAbstractParameter = DiagnosticAbstractParameter()


    def with_bit_offset(self, value: Optional[PositiveInteger]) -> "DiagnosticAbstractParameterBuilder":
        """Set bit_offset attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.bit_offset = value
        return self

    def with_data_element(self, value: Optional[DiagnosticDataElement]) -> "DiagnosticAbstractParameterBuilder":
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

    def with_parameter_size(self, value: Optional[PositiveInteger]) -> "DiagnosticAbstractParameterBuilder":
        """Set parameter_size attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.parameter_size = value
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


    @abstractmethod
    def build(self) -> DiagnosticAbstractParameter:
        """Build and return the DiagnosticAbstractParameter instance (abstract)."""
        raise NotImplementedError