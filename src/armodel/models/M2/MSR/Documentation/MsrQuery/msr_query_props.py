"""MsrQueryProps AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 344)

JSON Source: docs/json/packages/M2_MSR_Documentation_MsrQuery.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.MSR.Documentation.MsrQuery.msr_query_arg import (
    MsrQueryArg,
)


class MsrQueryProps(ARObject):
    """AUTOSAR MsrQueryProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    comment: Optional[String]
    msr_query_args: list[MsrQueryArg]
    msr_query_name: String
    def __init__(self) -> None:
        """Initialize MsrQueryProps."""
        super().__init__()
        self.comment: Optional[String] = None
        self.msr_query_args: list[MsrQueryArg] = []
        self.msr_query_name: String = None

    def serialize(self) -> ET.Element:
        """Serialize MsrQueryProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(MsrQueryProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize comment
        if self.comment is not None:
            serialized = SerializationHelper.serialize_item(self.comment, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMMENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize msr_query_args (list to container "MSR-QUERY-ARGS")
        if self.msr_query_args:
            wrapper = ET.Element("MSR-QUERY-ARGS")
            for item in self.msr_query_args:
                serialized = SerializationHelper.serialize_item(item, "MsrQueryArg")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize msr_query_name
        if self.msr_query_name is not None:
            serialized = SerializationHelper.serialize_item(self.msr_query_name, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MSR-QUERY-NAME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MsrQueryProps":
        """Deserialize XML element to MsrQueryProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MsrQueryProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(MsrQueryProps, cls).deserialize(element)

        # Parse comment
        child = SerializationHelper.find_child_element(element, "COMMENT")
        if child is not None:
            comment_value = child.text
            obj.comment = comment_value

        # Parse msr_query_args (list from container "MSR-QUERY-ARGS")
        obj.msr_query_args = []
        container = SerializationHelper.find_child_element(element, "MSR-QUERY-ARGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.msr_query_args.append(child_value)

        # Parse msr_query_name
        child = SerializationHelper.find_child_element(element, "MSR-QUERY-NAME")
        if child is not None:
            msr_query_name_value = child.text
            obj.msr_query_name = msr_query_name_value

        return obj



class MsrQueryPropsBuilder:
    """Builder for MsrQueryProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: MsrQueryProps = MsrQueryProps()


    def with_comment(self, value: Optional[String]) -> "MsrQueryPropsBuilder":
        """Set comment attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.comment = value
        return self

    def with_msr_query_args(self, items: list[MsrQueryArg]) -> "MsrQueryPropsBuilder":
        """Set msr_query_args list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.msr_query_args = list(items) if items else []
        return self

    def with_msr_query_name(self, value: String) -> "MsrQueryPropsBuilder":
        """Set msr_query_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.msr_query_name = value
        return self


    def add_msr_query_arg(self, item: MsrQueryArg) -> "MsrQueryPropsBuilder":
        """Add a single item to msr_query_args list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.msr_query_args.append(item)
        return self

    def clear_msr_query_args(self) -> "MsrQueryPropsBuilder":
        """Clear all items from msr_query_args list.

        Returns:
            self for method chaining
        """
        self._obj.msr_query_args = []
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


    def build(self) -> MsrQueryProps:
        """Build and return the MsrQueryProps instance with validation."""
        self._validate_instance()
        pass
        return self._obj