"""DiagnosticDynamicallyDefineDataIdentifierClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 128)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_DynamicallyDefineDataIdentifier.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import DiagnosticServiceClassBuilder
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.DynamicallyDefineData import (
    DiagnosticHandleDDDIConfigurationEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class DiagnosticDynamicallyDefineDataIdentifierClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticDynamicallyDefineDataIdentifierClass."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    check_per: Optional[Boolean]
    configuration: Optional[DiagnosticHandleDDDIConfigurationEnum]
    subfunctions: list[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticDynamicallyDefineDataIdentifierClass."""
        super().__init__()
        self.check_per: Optional[Boolean] = None
        self.configuration: Optional[DiagnosticHandleDDDIConfigurationEnum] = None
        self.subfunctions: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticDynamicallyDefineDataIdentifierClass to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticDynamicallyDefineDataIdentifierClass, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize check_per
        if self.check_per is not None:
            serialized = SerializationHelper.serialize_item(self.check_per, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CHECK-PER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize configuration
        if self.configuration is not None:
            serialized = SerializationHelper.serialize_item(self.configuration, "DiagnosticHandleDDDIConfigurationEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONFIGURATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize subfunctions (list to container "SUBFUNCTIONS")
        if self.subfunctions:
            wrapper = ET.Element("SUBFUNCTIONS")
            for item in self.subfunctions:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticDynamicallyDefineDataIdentifierClass":
        """Deserialize XML element to DiagnosticDynamicallyDefineDataIdentifierClass object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticDynamicallyDefineDataIdentifierClass object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticDynamicallyDefineDataIdentifierClass, cls).deserialize(element)

        # Parse check_per
        child = SerializationHelper.find_child_element(element, "CHECK-PER")
        if child is not None:
            check_per_value = child.text
            obj.check_per = check_per_value

        # Parse configuration
        child = SerializationHelper.find_child_element(element, "CONFIGURATION")
        if child is not None:
            configuration_value = DiagnosticHandleDDDIConfigurationEnum.deserialize(child)
            obj.configuration = configuration_value

        # Parse subfunctions (list from container "SUBFUNCTIONS")
        obj.subfunctions = []
        container = SerializationHelper.find_child_element(element, "SUBFUNCTIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.subfunctions.append(child_value)

        return obj



class DiagnosticDynamicallyDefineDataIdentifierClassBuilder(DiagnosticServiceClassBuilder):
    """Builder for DiagnosticDynamicallyDefineDataIdentifierClass with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticDynamicallyDefineDataIdentifierClass = DiagnosticDynamicallyDefineDataIdentifierClass()


    def with_check_per(self, value: Optional[Boolean]) -> "DiagnosticDynamicallyDefineDataIdentifierClassBuilder":
        """Set check_per attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.check_per = value
        return self

    def with_configuration(self, value: Optional[DiagnosticHandleDDDIConfigurationEnum]) -> "DiagnosticDynamicallyDefineDataIdentifierClassBuilder":
        """Set configuration attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.configuration = value
        return self

    def with_subfunctions(self, items: list[any (DiagnosticDynamically)]) -> "DiagnosticDynamicallyDefineDataIdentifierClassBuilder":
        """Set subfunctions list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.subfunctions = list(items) if items else []
        return self


    def add_subfunction(self, item: any (DiagnosticDynamically)) -> "DiagnosticDynamicallyDefineDataIdentifierClassBuilder":
        """Add a single item to subfunctions list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.subfunctions.append(item)
        return self

    def clear_subfunctions(self) -> "DiagnosticDynamicallyDefineDataIdentifierClassBuilder":
        """Clear all items from subfunctions list.

        Returns:
            self for method chaining
        """
        self._obj.subfunctions = []
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


    def build(self) -> DiagnosticDynamicallyDefineDataIdentifierClass:
        """Build and return the DiagnosticDynamicallyDefineDataIdentifierClass instance with validation."""
        self._validate_instance()
        pass
        return self._obj