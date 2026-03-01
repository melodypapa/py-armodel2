"""ArgumentDataPrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 303)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 300)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 102)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 1998)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 29)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 160)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.autosar_data_prototype import (
    AutosarDataPrototype,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.autosar_data_prototype import AutosarDataPrototypeBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ArgumentDirectionEnum,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import (
    ServerArgumentImplPolicyEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ArgumentDataPrototype(AutosarDataPrototype):
    """AUTOSAR ArgumentDataPrototype."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ARGUMENT-DATA-PROTOTYPE"


    direction: Optional[ArgumentDirectionEnum]
    server_argument_impl: Optional[ServerArgumentImplPolicyEnum]
    _DESERIALIZE_DISPATCH = {
        "DIRECTION": lambda obj, elem: setattr(obj, "direction", ArgumentDirectionEnum.deserialize(elem)),
        "SERVER-ARGUMENT-IMPL": lambda obj, elem: setattr(obj, "server_argument_impl", ServerArgumentImplPolicyEnum.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize ArgumentDataPrototype."""
        super().__init__()
        self.direction: Optional[ArgumentDirectionEnum] = None
        self.server_argument_impl: Optional[ServerArgumentImplPolicyEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize ArgumentDataPrototype to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ArgumentDataPrototype, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize direction
        if self.direction is not None:
            serialized = SerializationHelper.serialize_item(self.direction, "ArgumentDirectionEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DIRECTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize server_argument_impl
        if self.server_argument_impl is not None:
            serialized = SerializationHelper.serialize_item(self.server_argument_impl, "ServerArgumentImplPolicyEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SERVER-ARGUMENT-IMPL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ArgumentDataPrototype":
        """Deserialize XML element to ArgumentDataPrototype object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ArgumentDataPrototype object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ArgumentDataPrototype, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "DIRECTION":
                setattr(obj, "direction", ArgumentDirectionEnum.deserialize(child))
            elif tag == "SERVER-ARGUMENT-IMPL":
                setattr(obj, "server_argument_impl", ServerArgumentImplPolicyEnum.deserialize(child))

        return obj



class ArgumentDataPrototypeBuilder(AutosarDataPrototypeBuilder):
    """Builder for ArgumentDataPrototype with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ArgumentDataPrototype = ArgumentDataPrototype()


    def with_direction(self, value: Optional[ArgumentDirectionEnum]) -> "ArgumentDataPrototypeBuilder":
        """Set direction attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.direction = value
        return self

    def with_server_argument_impl(self, value: Optional[ServerArgumentImplPolicyEnum]) -> "ArgumentDataPrototypeBuilder":
        """Set server_argument_impl attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.server_argument_impl = value
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


    def build(self) -> ArgumentDataPrototype:
        """Build and return the ArgumentDataPrototype instance with validation."""
        self._validate_instance()
        pass
        return self._obj