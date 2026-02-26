"""DiagnosticValueNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 245)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 114)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 782)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import DiagnosticCapabilityElementBuilder
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    DiagnosticProcessingStyleEnum,
    DiagnosticValueAccessEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticValueNeeds(DiagnosticCapabilityElement):
    """AUTOSAR DiagnosticValueNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_length: Optional[PositiveInteger]
    diagnostic_value_access: Optional[DiagnosticValueAccessEnum]
    fixed_length: Optional[Boolean]
    processing_style: Optional[DiagnosticProcessingStyleEnum]
    def __init__(self) -> None:
        """Initialize DiagnosticValueNeeds."""
        super().__init__()
        self.data_length: Optional[PositiveInteger] = None
        self.diagnostic_value_access: Optional[DiagnosticValueAccessEnum] = None
        self.fixed_length: Optional[Boolean] = None
        self.processing_style: Optional[DiagnosticProcessingStyleEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticValueNeeds to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticValueNeeds, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_length
        if self.data_length is not None:
            serialized = SerializationHelper.serialize_item(self.data_length, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize diagnostic_value_access
        if self.diagnostic_value_access is not None:
            serialized = SerializationHelper.serialize_item(self.diagnostic_value_access, "DiagnosticValueAccessEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DIAGNOSTIC-VALUE-ACCESS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize fixed_length
        if self.fixed_length is not None:
            serialized = SerializationHelper.serialize_item(self.fixed_length, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FIXED-LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize processing_style
        if self.processing_style is not None:
            serialized = SerializationHelper.serialize_item(self.processing_style, "DiagnosticProcessingStyleEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PROCESSING-STYLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticValueNeeds":
        """Deserialize XML element to DiagnosticValueNeeds object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticValueNeeds object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticValueNeeds, cls).deserialize(element)

        # Parse data_length
        child = SerializationHelper.find_child_element(element, "DATA-LENGTH")
        if child is not None:
            data_length_value = child.text
            obj.data_length = data_length_value

        # Parse diagnostic_value_access
        child = SerializationHelper.find_child_element(element, "DIAGNOSTIC-VALUE-ACCESS")
        if child is not None:
            diagnostic_value_access_value = DiagnosticValueAccessEnum.deserialize(child)
            obj.diagnostic_value_access = diagnostic_value_access_value

        # Parse fixed_length
        child = SerializationHelper.find_child_element(element, "FIXED-LENGTH")
        if child is not None:
            fixed_length_value = child.text
            obj.fixed_length = fixed_length_value

        # Parse processing_style
        child = SerializationHelper.find_child_element(element, "PROCESSING-STYLE")
        if child is not None:
            processing_style_value = DiagnosticProcessingStyleEnum.deserialize(child)
            obj.processing_style = processing_style_value

        return obj



class DiagnosticValueNeedsBuilder(DiagnosticCapabilityElementBuilder):
    """Builder for DiagnosticValueNeeds with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticValueNeeds = DiagnosticValueNeeds()


    def with_data_length(self, value: Optional[PositiveInteger]) -> "DiagnosticValueNeedsBuilder":
        """Set data_length attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.data_length = value
        return self

    def with_diagnostic_value_access(self, value: Optional[DiagnosticValueAccessEnum]) -> "DiagnosticValueNeedsBuilder":
        """Set diagnostic_value_access attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.diagnostic_value_access = value
        return self

    def with_fixed_length(self, value: Optional[Boolean]) -> "DiagnosticValueNeedsBuilder":
        """Set fixed_length attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.fixed_length = value
        return self

    def with_processing_style(self, value: Optional[DiagnosticProcessingStyleEnum]) -> "DiagnosticValueNeedsBuilder":
        """Set processing_style attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.processing_style = value
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


    def build(self) -> DiagnosticValueNeeds:
        """Build and return the DiagnosticValueNeeds instance with validation."""
        self._validate_instance()
        pass
        return self._obj