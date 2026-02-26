"""SwcExclusiveAreaPolicy AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 556)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior import (
    ApiPrincipleEnum,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.exclusive_area import (
    ExclusiveArea,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SwcExclusiveAreaPolicy(ARObject):
    """AUTOSAR SwcExclusiveAreaPolicy."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    api_principle_enum: Optional[ApiPrincipleEnum]
    exclusive_area_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize SwcExclusiveAreaPolicy."""
        super().__init__()
        self.api_principle_enum: Optional[ApiPrincipleEnum] = None
        self.exclusive_area_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize SwcExclusiveAreaPolicy to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwcExclusiveAreaPolicy, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize api_principle_enum
        if self.api_principle_enum is not None:
            serialized = SerializationHelper.serialize_item(self.api_principle_enum, "ApiPrincipleEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("API-PRINCIPLE-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize exclusive_area_ref
        if self.exclusive_area_ref is not None:
            serialized = SerializationHelper.serialize_item(self.exclusive_area_ref, "ExclusiveArea")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EXCLUSIVE-AREA-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwcExclusiveAreaPolicy":
        """Deserialize XML element to SwcExclusiveAreaPolicy object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwcExclusiveAreaPolicy object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwcExclusiveAreaPolicy, cls).deserialize(element)

        # Parse api_principle_enum
        child = SerializationHelper.find_child_element(element, "API-PRINCIPLE-ENUM")
        if child is not None:
            api_principle_enum_value = ApiPrincipleEnum.deserialize(child)
            obj.api_principle_enum = api_principle_enum_value

        # Parse exclusive_area_ref
        child = SerializationHelper.find_child_element(element, "EXCLUSIVE-AREA-REF")
        if child is not None:
            exclusive_area_ref_value = ARRef.deserialize(child)
            obj.exclusive_area_ref = exclusive_area_ref_value

        return obj



class SwcExclusiveAreaPolicyBuilder(BuilderBase):
    """Builder for SwcExclusiveAreaPolicy with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SwcExclusiveAreaPolicy = SwcExclusiveAreaPolicy()


    def with_api_principle_enum(self, value: Optional[ApiPrincipleEnum]) -> "SwcExclusiveAreaPolicyBuilder":
        """Set api_principle_enum attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.api_principle_enum = value
        return self

    def with_exclusive_area(self, value: Optional[ExclusiveArea]) -> "SwcExclusiveAreaPolicyBuilder":
        """Set exclusive_area attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.exclusive_area = value
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


    def build(self) -> SwcExclusiveAreaPolicy:
        """Build and return the SwcExclusiveAreaPolicy instance with validation."""
        self._validate_instance()
        pass
        return self._obj