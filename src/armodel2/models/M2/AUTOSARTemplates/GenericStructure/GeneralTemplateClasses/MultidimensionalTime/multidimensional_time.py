"""MultidimensionalTime AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 164)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 109)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 165)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_MultidimensionalTime.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CseCodeType,
    Integer,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class MultidimensionalTime(ARObject):
    """AUTOSAR MultidimensionalTime."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    cse_code: Optional[CseCodeType]
    cse_code_factor: Optional[Integer]
    def __init__(self) -> None:
        """Initialize MultidimensionalTime."""
        super().__init__()
        self.cse_code: Optional[CseCodeType] = None
        self.cse_code_factor: Optional[Integer] = None

    def serialize(self) -> ET.Element:
        """Serialize MultidimensionalTime to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(MultidimensionalTime, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize cse_code
        if self.cse_code is not None:
            serialized = SerializationHelper.serialize_item(self.cse_code, "CseCodeType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CSE-CODE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize cse_code_factor
        if self.cse_code_factor is not None:
            serialized = SerializationHelper.serialize_item(self.cse_code_factor, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CSE-CODE-FACTOR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MultidimensionalTime":
        """Deserialize XML element to MultidimensionalTime object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MultidimensionalTime object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(MultidimensionalTime, cls).deserialize(element)

        # Parse cse_code
        child = SerializationHelper.find_child_element(element, "CSE-CODE")
        if child is not None:
            cse_code_value = child.text
            obj.cse_code = cse_code_value

        # Parse cse_code_factor
        child = SerializationHelper.find_child_element(element, "CSE-CODE-FACTOR")
        if child is not None:
            cse_code_factor_value = child.text
            obj.cse_code_factor = cse_code_factor_value

        return obj



class MultidimensionalTimeBuilder(BuilderBase):
    """Builder for MultidimensionalTime with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: MultidimensionalTime = MultidimensionalTime()


    def with_cse_code(self, value: Optional[CseCodeType]) -> "MultidimensionalTimeBuilder":
        """Set cse_code attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.cse_code = value
        return self

    def with_cse_code_factor(self, value: Optional[Integer]) -> "MultidimensionalTimeBuilder":
        """Set cse_code_factor attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.cse_code_factor = value
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


    def build(self) -> MultidimensionalTime:
        """Build and return the MultidimensionalTime instance with validation."""
        self._validate_instance()
        pass
        return self._obj