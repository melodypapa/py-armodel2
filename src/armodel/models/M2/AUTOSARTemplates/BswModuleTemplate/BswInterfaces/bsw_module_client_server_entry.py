"""BswModuleClientServerEntry AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 53)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswInterfaces.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_entry import (
    BswModuleEntry,
)


class BswModuleClientServerEntry(Referrable):
    """AUTOSAR BswModuleClientServerEntry."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    encapsulated_entry_ref: Optional[ARRef]
    is_reentrant: Optional[Boolean]
    is_synchronous: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize BswModuleClientServerEntry."""
        super().__init__()
        self.encapsulated_entry_ref: Optional[ARRef] = None
        self.is_reentrant: Optional[Boolean] = None
        self.is_synchronous: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize BswModuleClientServerEntry to XML element.

        BswModuleClientServerEntry is serialized as BSW-MODULE-ENTRY-REF-CONDITIONAL
        element containing BSW-MODULE-ENTRY-REF inner element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Serialize as BSW-MODULE-ENTRY-REF-CONDITIONAL element
        elem = ET.Element("BSW-MODULE-ENTRY-REF-CONDITIONAL")

        # Serialize encapsulated_entry_ref as BSW-MODULE-ENTRY-REF
        if self.encapsulated_entry_ref is not None:
            inner_ref = ET.Element("BSW-MODULE-ENTRY-REF")
            # Set DEST attribute
            if hasattr(self.encapsulated_entry_ref, '_dest') and self.encapsulated_entry_ref._dest is not None:
                inner_ref.set("DEST", self.encapsulated_entry_ref._dest)
            else:
                inner_ref.set("DEST", "BSW-MODULE-ENTRY")
            # Set text content (reference path)
            if hasattr(self.encapsulated_entry_ref, '_value') and self.encapsulated_entry_ref._value is not None:
                inner_ref.text = self.encapsulated_entry_ref._value
            # Append inner ref to element
            elem.append(inner_ref)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswModuleClientServerEntry":
        """Deserialize XML element to BswModuleClientServerEntry object.

        BswModuleClientServerEntry is deserialized from BSW-MODULE-ENTRY-REF-CONDITIONAL
        element containing BSW-MODULE-ENTRY-REF inner element.

        Args:
            element: XML element to deserialize from (BSW-MODULE-ENTRY-REF-CONDITIONAL)

        Returns:
            Deserialized BswModuleClientServerEntry object
        """
        obj = cls.__new__(cls)
        obj.__init__()

        # Extract BSW-MODULE-ENTRY-REF from the wrapper
        inner_ref = SerializationHelper.find_child_element(element, "BSW-MODULE-ENTRY-REF")
        if inner_ref is not None:
            encapsulated_entry_ref_value = ARRef.deserialize(inner_ref)
            obj.encapsulated_entry_ref = encapsulated_entry_ref_value

        return obj



class BswModuleClientServerEntryBuilder:
    """Builder for BswModuleClientServerEntry with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: BswModuleClientServerEntry = BswModuleClientServerEntry()


    def with_short_name(self, value: Identifier) -> "BswModuleClientServerEntryBuilder":
        """Set short_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.short_name = value
        return self

    def with_short_name_fragments(self, items: list[ShortNameFragment]) -> "BswModuleClientServerEntryBuilder":
        """Set short_name_fragments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = list(items) if items else []
        return self

    def with_encapsulated_entry(self, value: Optional[BswModuleEntry]) -> "BswModuleClientServerEntryBuilder":
        """Set encapsulated_entry attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.encapsulated_entry = value
        return self

    def with_is_reentrant(self, value: Optional[Boolean]) -> "BswModuleClientServerEntryBuilder":
        """Set is_reentrant attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.is_reentrant = value
        return self

    def with_is_synchronous(self, value: Optional[Boolean]) -> "BswModuleClientServerEntryBuilder":
        """Set is_synchronous attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.is_synchronous = value
        return self


    def add_short_name_fragment(self, item: ShortNameFragment) -> "BswModuleClientServerEntryBuilder":
        """Add a single item to short_name_fragments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments.append(item)
        return self

    def clear_short_name_fragments(self) -> "BswModuleClientServerEntryBuilder":
        """Clear all items from short_name_fragments list.

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = []
        return self


    @staticmethod
    def _coerce_to_int(value: Any) -> int:
        """Coerce value to int.

        Args:
            value: Value to coerce

        Returns:
            Integer value

        Raises:
            ValueError: If value cannot be coerced to int
        """
        if isinstance(value, int):
            return value
        if isinstance(value, str) and value.isdigit():
            return int(value)
        if isinstance(value, float):
            return int(value)
        if isinstance(value, bool):
            return int(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to int: {value}")

    @staticmethod
    def _coerce_to_float(value: Any) -> float:
        """Coerce value to float.

        Args:
            value: Value to coerce

        Returns:
            Float value

        Raises:
            ValueError: If value cannot be coerced to float
        """
        if isinstance(value, float):
            return value
        if isinstance(value, int):
            return float(value)
        if isinstance(value, str):
            try:
                return float(value)
            except ValueError:
                pass
        raise ValueError(f"Cannot coerce {type(value).__name__} to float: {value}")

    @staticmethod
    def _coerce_to_bool(value: Any) -> bool:
        """Coerce value to bool.

        Args:
            value: Value to coerce

        Returns:
            Boolean value

        Raises:
            ValueError: If value cannot be coerced to bool
        """
        if isinstance(value, bool):
            return value
        if isinstance(value, int):
            return bool(value)
        if isinstance(value, str):
            if value.lower() in ("true", "1", "yes"):
                return True
            if value.lower() in ("false", "0", "no"):
                return False
        raise ValueError(f"Cannot coerce {type(value).__name__} to bool: {value}")

    @staticmethod
    def _coerce_to_str(value: Any) -> str:
        """Coerce value to str.

        Args:
            value: Value to coerce

        Returns:
            String value
        """
        return str(value)


    @staticmethod
    def _coerce_to_list(value: Any, item_type: str) -> list:
        """Coerce value to list.

        Args:
            value: Value to coerce
            item_type: Expected item type (for error messages)

        Returns:
            List value

        Raises:
            ValueError: If value cannot be coerced to list
        """
        if isinstance(value, list):
            return value
        if isinstance(value, tuple):
            return list(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to list[{item_type}]: {value}")


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


    def build(self) -> BswModuleClientServerEntry:
        """Build and return the BswModuleClientServerEntry instance with validation."""
        self._validate_instance()
        pass
        return self._obj