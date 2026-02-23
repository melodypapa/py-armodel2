"""DiagnosticSecurityLevel AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 75)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import DiagnosticCommonElementBuilder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class DiagnosticSecurityLevel(DiagnosticCommonElement):
    """AUTOSAR DiagnosticSecurityLevel."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    access_data: Optional[PositiveInteger]
    key_size: Optional[PositiveInteger]
    num_failed: Optional[PositiveInteger]
    security_delay: Optional[TimeValue]
    seed_size: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DiagnosticSecurityLevel."""
        super().__init__()
        self.access_data: Optional[PositiveInteger] = None
        self.key_size: Optional[PositiveInteger] = None
        self.num_failed: Optional[PositiveInteger] = None
        self.security_delay: Optional[TimeValue] = None
        self.seed_size: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticSecurityLevel to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticSecurityLevel, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize access_data
        if self.access_data is not None:
            serialized = SerializationHelper.serialize_item(self.access_data, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ACCESS-DATA")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize key_size
        if self.key_size is not None:
            serialized = SerializationHelper.serialize_item(self.key_size, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("KEY-SIZE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize num_failed
        if self.num_failed is not None:
            serialized = SerializationHelper.serialize_item(self.num_failed, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NUM-FAILED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize security_delay
        if self.security_delay is not None:
            serialized = SerializationHelper.serialize_item(self.security_delay, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SECURITY-DELAY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize seed_size
        if self.seed_size is not None:
            serialized = SerializationHelper.serialize_item(self.seed_size, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SEED-SIZE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticSecurityLevel":
        """Deserialize XML element to DiagnosticSecurityLevel object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticSecurityLevel object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticSecurityLevel, cls).deserialize(element)

        # Parse access_data
        child = SerializationHelper.find_child_element(element, "ACCESS-DATA")
        if child is not None:
            access_data_value = child.text
            obj.access_data = access_data_value

        # Parse key_size
        child = SerializationHelper.find_child_element(element, "KEY-SIZE")
        if child is not None:
            key_size_value = child.text
            obj.key_size = key_size_value

        # Parse num_failed
        child = SerializationHelper.find_child_element(element, "NUM-FAILED")
        if child is not None:
            num_failed_value = child.text
            obj.num_failed = num_failed_value

        # Parse security_delay
        child = SerializationHelper.find_child_element(element, "SECURITY-DELAY")
        if child is not None:
            security_delay_value = child.text
            obj.security_delay = security_delay_value

        # Parse seed_size
        child = SerializationHelper.find_child_element(element, "SEED-SIZE")
        if child is not None:
            seed_size_value = child.text
            obj.seed_size = seed_size_value

        return obj



class DiagnosticSecurityLevelBuilder(DiagnosticCommonElementBuilder):
    """Builder for DiagnosticSecurityLevel with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticSecurityLevel = DiagnosticSecurityLevel()


    def with_access_data(self, value: Optional[PositiveInteger]) -> "DiagnosticSecurityLevelBuilder":
        """Set access_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.access_data = value
        return self

    def with_key_size(self, value: Optional[PositiveInteger]) -> "DiagnosticSecurityLevelBuilder":
        """Set key_size attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.key_size = value
        return self

    def with_num_failed(self, value: Optional[PositiveInteger]) -> "DiagnosticSecurityLevelBuilder":
        """Set num_failed attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.num_failed = value
        return self

    def with_security_delay(self, value: Optional[TimeValue]) -> "DiagnosticSecurityLevelBuilder":
        """Set security_delay attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.security_delay = value
        return self

    def with_seed_size(self, value: Optional[PositiveInteger]) -> "DiagnosticSecurityLevelBuilder":
        """Set seed_size attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.seed_size = value
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


    def build(self) -> DiagnosticSecurityLevel:
        """Build and return the DiagnosticSecurityLevel instance with validation."""
        self._validate_instance()
        pass
        return self._obj