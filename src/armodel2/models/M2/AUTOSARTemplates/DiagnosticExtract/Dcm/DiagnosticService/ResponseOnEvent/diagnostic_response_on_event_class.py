"""DiagnosticResponseOnEventClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 132)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_ResponseOnEvent.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import DiagnosticServiceClassBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticResponseOnEventClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticResponseOnEventClass."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    max_number_of: Optional[PositiveInteger]
    max_num: Optional[PositiveInteger]
    max_supported: Optional[PositiveInteger]
    response_on: Optional[TimeValue]
    store_event: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize DiagnosticResponseOnEventClass."""
        super().__init__()
        self.max_number_of: Optional[PositiveInteger] = None
        self.max_num: Optional[PositiveInteger] = None
        self.max_supported: Optional[PositiveInteger] = None
        self.response_on: Optional[TimeValue] = None
        self.store_event: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticResponseOnEventClass to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticResponseOnEventClass, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize max_number_of
        if self.max_number_of is not None:
            serialized = SerializationHelper.serialize_item(self.max_number_of, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-NUMBER-OF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_num
        if self.max_num is not None:
            serialized = SerializationHelper.serialize_item(self.max_num, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-NUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_supported
        if self.max_supported is not None:
            serialized = SerializationHelper.serialize_item(self.max_supported, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-SUPPORTED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize response_on
        if self.response_on is not None:
            serialized = SerializationHelper.serialize_item(self.response_on, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RESPONSE-ON")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize store_event
        if self.store_event is not None:
            serialized = SerializationHelper.serialize_item(self.store_event, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("STORE-EVENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticResponseOnEventClass":
        """Deserialize XML element to DiagnosticResponseOnEventClass object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticResponseOnEventClass object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticResponseOnEventClass, cls).deserialize(element)

        # Parse max_number_of
        child = SerializationHelper.find_child_element(element, "MAX-NUMBER-OF")
        if child is not None:
            max_number_of_value = child.text
            obj.max_number_of = max_number_of_value

        # Parse max_num
        child = SerializationHelper.find_child_element(element, "MAX-NUM")
        if child is not None:
            max_num_value = child.text
            obj.max_num = max_num_value

        # Parse max_supported
        child = SerializationHelper.find_child_element(element, "MAX-SUPPORTED")
        if child is not None:
            max_supported_value = child.text
            obj.max_supported = max_supported_value

        # Parse response_on
        child = SerializationHelper.find_child_element(element, "RESPONSE-ON")
        if child is not None:
            response_on_value = child.text
            obj.response_on = response_on_value

        # Parse store_event
        child = SerializationHelper.find_child_element(element, "STORE-EVENT")
        if child is not None:
            store_event_value = child.text
            obj.store_event = store_event_value

        return obj



class DiagnosticResponseOnEventClassBuilder(DiagnosticServiceClassBuilder):
    """Builder for DiagnosticResponseOnEventClass with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticResponseOnEventClass = DiagnosticResponseOnEventClass()


    def with_max_number_of(self, value: Optional[PositiveInteger]) -> "DiagnosticResponseOnEventClassBuilder":
        """Set max_number_of attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.max_number_of = value
        return self

    def with_max_num(self, value: Optional[PositiveInteger]) -> "DiagnosticResponseOnEventClassBuilder":
        """Set max_num attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.max_num = value
        return self

    def with_max_supported(self, value: Optional[PositiveInteger]) -> "DiagnosticResponseOnEventClassBuilder":
        """Set max_supported attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.max_supported = value
        return self

    def with_response_on(self, value: Optional[TimeValue]) -> "DiagnosticResponseOnEventClassBuilder":
        """Set response_on attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.response_on = value
        return self

    def with_store_event(self, value: Optional[Boolean]) -> "DiagnosticResponseOnEventClassBuilder":
        """Set store_event attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.store_event = value
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


    def build(self) -> DiagnosticResponseOnEventClass:
        """Build and return the DiagnosticResponseOnEventClass instance with validation."""
        self._validate_instance()
        pass
        return self._obj