"""BswInterruptEntity AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 75)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 212)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_module_entity import (
    BswModuleEntity,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_module_entity import BswModuleEntityBuilder
from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import (
    BswInterruptCategory,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class BswInterruptEntity(BswModuleEntity):
    """AUTOSAR BswInterruptEntity."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "BSW-INTERRUPT-ENTITY"


    interrupt_category: Optional[BswInterruptCategory]
    interrupt_source: Optional[String]
    _DESERIALIZE_DISPATCH = {
        "INTERRUPT-CATEGORY": lambda obj, elem: setattr(obj, "interrupt_category", BswInterruptCategory.deserialize(elem)),
        "INTERRUPT-SOURCE": lambda obj, elem: setattr(obj, "interrupt_source", elem.text),
    }


    def __init__(self) -> None:
        """Initialize BswInterruptEntity."""
        super().__init__()
        self.interrupt_category: Optional[BswInterruptCategory] = None
        self.interrupt_source: Optional[String] = None

    def serialize(self) -> ET.Element:
        """Serialize BswInterruptEntity to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BswInterruptEntity, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize interrupt_category
        if self.interrupt_category is not None:
            serialized = SerializationHelper.serialize_item(self.interrupt_category, "BswInterruptCategory")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INTERRUPT-CATEGORY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize interrupt_source
        if self.interrupt_source is not None:
            serialized = SerializationHelper.serialize_item(self.interrupt_source, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INTERRUPT-SOURCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswInterruptEntity":
        """Deserialize XML element to BswInterruptEntity object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswInterruptEntity object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswInterruptEntity, cls).deserialize(element)

        # Parse interrupt_category
        child = SerializationHelper.find_child_element(element, "INTERRUPT-CATEGORY")
        if child is not None:
            interrupt_category_value = BswInterruptCategory.deserialize(child)
            obj.interrupt_category = interrupt_category_value

        # Parse interrupt_source
        child = SerializationHelper.find_child_element(element, "INTERRUPT-SOURCE")
        if child is not None:
            interrupt_source_value = child.text
            obj.interrupt_source = interrupt_source_value

        return obj



class BswInterruptEntityBuilder(BswModuleEntityBuilder):
    """Builder for BswInterruptEntity with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: BswInterruptEntity = BswInterruptEntity()


    def with_interrupt_category(self, value: Optional[BswInterruptCategory]) -> "BswInterruptEntityBuilder":
        """Set interrupt_category attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.interrupt_category = value
        return self

    def with_interrupt_source(self, value: Optional[String]) -> "BswInterruptEntityBuilder":
        """Set interrupt_source attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.interrupt_source = value
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


    def build(self) -> BswInterruptEntity:
        """Build and return the BswInterruptEntity instance with validation."""
        self._validate_instance()
        pass
        return self._obj