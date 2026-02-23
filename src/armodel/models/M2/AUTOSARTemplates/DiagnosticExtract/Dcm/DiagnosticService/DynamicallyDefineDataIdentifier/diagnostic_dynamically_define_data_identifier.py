"""DiagnosticDynamicallyDefineDataIdentifier AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 127)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_DynamicallyDefineDataIdentifier.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import DiagnosticServiceInstanceBuilder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_dynamic_data_identifier import (
    DiagnosticDynamicDataIdentifier,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class DiagnosticDynamicallyDefineDataIdentifier(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticDynamicallyDefineDataIdentifier."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_identifier_ref: Optional[ARRef]
    dynamically_ref: Optional[Any]
    max_source: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DiagnosticDynamicallyDefineDataIdentifier."""
        super().__init__()
        self.data_identifier_ref: Optional[ARRef] = None
        self.dynamically_ref: Optional[Any] = None
        self.max_source: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticDynamicallyDefineDataIdentifier to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticDynamicallyDefineDataIdentifier, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_identifier_ref
        if self.data_identifier_ref is not None:
            serialized = SerializationHelper.serialize_item(self.data_identifier_ref, "DiagnosticDynamicDataIdentifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-IDENTIFIER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize dynamically_ref
        if self.dynamically_ref is not None:
            serialized = SerializationHelper.serialize_item(self.dynamically_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DYNAMICALLY-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_source
        if self.max_source is not None:
            serialized = SerializationHelper.serialize_item(self.max_source, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-SOURCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticDynamicallyDefineDataIdentifier":
        """Deserialize XML element to DiagnosticDynamicallyDefineDataIdentifier object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticDynamicallyDefineDataIdentifier object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticDynamicallyDefineDataIdentifier, cls).deserialize(element)

        # Parse data_identifier_ref
        child = SerializationHelper.find_child_element(element, "DATA-IDENTIFIER-REF")
        if child is not None:
            data_identifier_ref_value = ARRef.deserialize(child)
            obj.data_identifier_ref = data_identifier_ref_value

        # Parse dynamically_ref
        child = SerializationHelper.find_child_element(element, "DYNAMICALLY-REF")
        if child is not None:
            dynamically_ref_value = ARRef.deserialize(child)
            obj.dynamically_ref = dynamically_ref_value

        # Parse max_source
        child = SerializationHelper.find_child_element(element, "MAX-SOURCE")
        if child is not None:
            max_source_value = child.text
            obj.max_source = max_source_value

        return obj



class DiagnosticDynamicallyDefineDataIdentifierBuilder(DiagnosticServiceInstanceBuilder):
    """Builder for DiagnosticDynamicallyDefineDataIdentifier with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticDynamicallyDefineDataIdentifier = DiagnosticDynamicallyDefineDataIdentifier()


    def with_data_identifier(self, value: Optional[DiagnosticDynamicDataIdentifier]) -> "DiagnosticDynamicallyDefineDataIdentifierBuilder":
        """Set data_identifier attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.data_identifier = value
        return self

    def with_dynamically(self, value: Optional[any (DiagnosticDynamically)]) -> "DiagnosticDynamicallyDefineDataIdentifierBuilder":
        """Set dynamically attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.dynamically = value
        return self

    def with_max_source(self, value: Optional[PositiveInteger]) -> "DiagnosticDynamicallyDefineDataIdentifierBuilder":
        """Set max_source attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.max_source = value
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


    def build(self) -> DiagnosticDynamicallyDefineDataIdentifier:
        """Build and return the DiagnosticDynamicallyDefineDataIdentifier instance with validation."""
        self._validate_instance()
        pass
        return self._obj