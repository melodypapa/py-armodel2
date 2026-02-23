"""Base class for all AUTOSAR model Builders.

This module provides shared functionality for Builder classes including
type coercion and validation methods that are common across all Builders.
"""

from __future__ import annotations

from typing import Any, Optional, get_args, get_origin, Union


class BuilderBase:
    """Base class for all AUTOSAR model Builders with shared functionality.

    Provides common type coercion and validation methods used by all
    Builder classes in the codebase.
    """

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

    @staticmethod
    def _validate_value(value: Any, expected_type: type) -> None:
        """Validate that value is of expected type.

        Args:
            value: Value to validate
            expected_type: Expected type (can be Optional, list, or direct type)

        Raises:
            TypeError: If value is not of expected type
        """
        if expected_type is None:
            return

        # Handle Optional types
        if BuilderBase._is_optional_type(expected_type):
            if value is None:
                return
            # Extract the inner type from Optional
            inner_type = BuilderBase._get_expected_type(expected_type)
            if not isinstance(value, inner_type):
                raise TypeError(
                    f"Expected {expected_type.__name__}, got {type(value).__name__}"
                )
            return

        # Handle list types
        if expected_type is list or get_origin(expected_type) is list:
            if not isinstance(value, list):
                raise TypeError(
                    f"Expected list, got {type(value).__name__}"
                )
            return

        # Handle direct types
        if not isinstance(value, expected_type):
            raise TypeError(
                f"Expected {expected_type.__name__}, got {type(value).__name__}"
            )

    @staticmethod
    def _is_optional_type(type_hint: Any) -> bool:
        """Check if type hint is Optional.

        Args:
            type_hint: Type hint to check

        Returns:
            True if type hint is Optional
        """
        if type_hint is None:
            return False
        origin = get_origin(type_hint)
        return origin is Union or origin is Optional

    @staticmethod
    def _get_expected_type(type_hint: Any) -> type:
        """Extract the expected type from a type hint.

        Args:
            type_hint: Type hint (can be Optional, list, or direct type)

        Returns:
            The expected type
        """
        if type_hint is None:
            return type(None)

        origin = get_origin(type_hint)

        # Handle Optional types
        if origin is Union or origin is Optional:
            args = get_args(type_hint)
            # Return the first non-None type
            for arg in args:
                if arg is not type(None):
                    return arg
            return type(None)

        # Handle list types
        if origin is list:
            args = get_args(type_hint)
            if args:
                return args[0]
            return Any

        # Handle direct types
        return type_hint if isinstance(type_hint, type) else type_hint