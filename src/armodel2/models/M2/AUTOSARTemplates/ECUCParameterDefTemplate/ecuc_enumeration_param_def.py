"""EcucEnumerationParamDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 66)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 186)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_parameter_def import (
    EcucParameterDef,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_parameter_def import EcucParameterDefBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel2.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_enumeration_literal_def import (
    EcucEnumerationLiteralDef,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class EcucEnumerationParamDef(EcucParameterDef):
    """AUTOSAR EcucEnumerationParamDef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ECUC-ENUMERATION-PARAM-DEF"


    default_value: Optional[Identifier]
    literals: list[EcucEnumerationLiteralDef]
    _DESERIALIZE_DISPATCH = {
        "DEFAULT-VALUE": lambda obj, elem: setattr(obj, "default_value", elem.text),
        "LITERALS": lambda obj, elem: obj.literals.append(EcucEnumerationLiteralDef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize EcucEnumerationParamDef."""
        super().__init__()
        self.default_value: Optional[Identifier] = None
        self.literals: list[EcucEnumerationLiteralDef] = []

    def serialize(self) -> ET.Element:
        """Serialize EcucEnumerationParamDef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucEnumerationParamDef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize default_value
        if self.default_value is not None:
            serialized = SerializationHelper.serialize_item(self.default_value, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEFAULT-VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize literals (list to container "LITERALS")
        if self.literals:
            wrapper = ET.Element("LITERALS")
            for item in self.literals:
                serialized = SerializationHelper.serialize_item(item, "EcucEnumerationLiteralDef")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucEnumerationParamDef":
        """Deserialize XML element to EcucEnumerationParamDef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucEnumerationParamDef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucEnumerationParamDef, cls).deserialize(element)

        # Parse default_value
        child = SerializationHelper.find_child_element(element, "DEFAULT-VALUE")
        if child is not None:
            default_value_value = SerializationHelper.deserialize_by_tag(child, "Identifier")
            obj.default_value = default_value_value

        # Parse literals (list from container "LITERALS")
        obj.literals = []
        container = SerializationHelper.find_child_element(element, "LITERALS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.literals.append(child_value)

        return obj



class EcucEnumerationParamDefBuilder(EcucParameterDefBuilder):
    """Builder for EcucEnumerationParamDef with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EcucEnumerationParamDef = EcucEnumerationParamDef()


    def with_default_value(self, value: Optional[Identifier]) -> "EcucEnumerationParamDefBuilder":
        """Set default_value attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.default_value = value
        return self

    def with_literals(self, items: list[EcucEnumerationLiteralDef]) -> "EcucEnumerationParamDefBuilder":
        """Set literals list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.literals = list(items) if items else []
        return self


    def add_literal(self, item: EcucEnumerationLiteralDef) -> "EcucEnumerationParamDefBuilder":
        """Add a single item to literals list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.literals.append(item)
        return self

    def clear_literals(self) -> "EcucEnumerationParamDefBuilder":
        """Clear all items from literals list.

        Returns:
            self for method chaining
        """
        self._obj.literals = []
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


    def build(self) -> EcucEnumerationParamDef:
        """Build and return the EcucEnumerationParamDef instance with validation."""
        self._validate_instance()
        pass
        return self._obj