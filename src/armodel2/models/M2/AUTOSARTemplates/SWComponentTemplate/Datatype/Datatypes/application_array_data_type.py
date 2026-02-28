"""ApplicationArrayDataType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 252)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 1995)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 35)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Datatype_Datatypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.application_composite_data_type import (
    ApplicationCompositeDataType,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.application_composite_data_type import ApplicationCompositeDataTypeBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.application_array_element import (
    ApplicationArrayElement,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ApplicationArrayDataType(ApplicationCompositeDataType):
    """AUTOSAR ApplicationArrayDataType."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "APPLICATION-ARRAY-DATA-TYPE"


    dynamic_array_size_profile: Optional[String]
    element: Optional[ApplicationArrayElement]
    _DESERIALIZE_DISPATCH = {
        "DYNAMIC-ARRAY-SIZE-PROFILE": lambda obj, elem: setattr(obj, "dynamic_array_size_profile", elem.text),
        "ELEMENT": lambda obj, elem: setattr(obj, "element", ApplicationArrayElement.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize ApplicationArrayDataType."""
        super().__init__()
        self.dynamic_array_size_profile: Optional[String] = None
        self.element: Optional[ApplicationArrayElement] = None

    def serialize(self) -> ET.Element:
        """Serialize ApplicationArrayDataType to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ApplicationArrayDataType, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize dynamic_array_size_profile
        if self.dynamic_array_size_profile is not None:
            serialized = SerializationHelper.serialize_item(self.dynamic_array_size_profile, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DYNAMIC-ARRAY-SIZE-PROFILE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize element
        if self.element is not None:
            serialized = SerializationHelper.serialize_item(self.element, "ApplicationArrayElement")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ELEMENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ApplicationArrayDataType":
        """Deserialize XML element to ApplicationArrayDataType object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ApplicationArrayDataType object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ApplicationArrayDataType, cls).deserialize(element)

        # Parse dynamic_array_size_profile
        child = SerializationHelper.find_child_element(element, "DYNAMIC-ARRAY-SIZE-PROFILE")
        if child is not None:
            dynamic_array_size_profile_value = child.text
            obj.dynamic_array_size_profile = dynamic_array_size_profile_value

        # Parse element
        child = SerializationHelper.find_child_element(element, "ELEMENT")
        if child is not None:
            element_value = SerializationHelper.deserialize_by_tag(child, "ApplicationArrayElement")
            obj.element = element_value

        return obj



class ApplicationArrayDataTypeBuilder(ApplicationCompositeDataTypeBuilder):
    """Builder for ApplicationArrayDataType with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ApplicationArrayDataType = ApplicationArrayDataType()


    def with_dynamic_array_size_profile(self, value: Optional[String]) -> "ApplicationArrayDataTypeBuilder":
        """Set dynamic_array_size_profile attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.dynamic_array_size_profile = value
        return self

    def with_element(self, value: Optional[ApplicationArrayElement]) -> "ApplicationArrayDataTypeBuilder":
        """Set element attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.element = value
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


    def build(self) -> ApplicationArrayDataType:
        """Build and return the ApplicationArrayDataType instance with validation."""
        self._validate_instance()
        pass
        return self._obj