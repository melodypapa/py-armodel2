"""Global settings management for ARXML processing."""

from enum import Enum
from typing import Optional, Any, Dict


class BuilderValidationMode(Enum):
    """Builder validation modes.

    STRICT: Validate all fields, raise on errors
    LENIENT: Validate required fields, warn on optional
    DISABLED: Skip validation
    """
    STRICT = "strict"
    LENIENT = "lenient"
    DISABLED = "disabled"


class GlobalSettingsManager:
    """Manages global settings for ARXML processing.

    This class provides a singleton instance for managing application-wide
    settings such as validation behavior during deserialization.

    Example:
        >>> settings = GlobalSettingsManager()
        >>> settings.strict_validation = True  # Enable strict mode
        >>> settings.reset()  # Restore defaults
    """

    _instance: Optional["GlobalSettingsManager"] = None
    _initialized: bool = False

    DEFAULTS: Dict[str, Any] = {
        "strict_validation": False,      # Raise exception on unrecognized XML elements
        "warn_on_unrecognized": True,    # Log warning for unrecognized XML elements
        "builder_validation": BuilderValidationMode.STRICT,  # Builder validation mode
        "builder_type_coercion": True,   # Enable type coercion in builders
    }

    def __new__(cls) -> "GlobalSettingsManager":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self) -> None:
        """Initialize settings manager (singleton pattern)."""
        if self._initialized:
            return

        self._settings: Dict[str, Any] = dict(self.DEFAULTS)
        self._initialized = True

    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value by key.

        Args:
            key: Setting key name
            default: Default value if key not found

        Returns:
            Setting value or default
        """
        return self._settings.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """Set setting value.

        Args:
            key: Setting key name
            value: Setting value
        """
        self._settings[key] = value

    def reset(self) -> None:
        """Reset all settings to default values."""
        self._settings = dict(self.DEFAULTS)

    # Convenience properties

    @property
    def strict_validation(self) -> bool:
        """Whether to raise exception on unrecognized XML elements."""
        value = self._settings.get("strict_validation", False)
        # Type narrowing: ensure we return bool
        return bool(value) if isinstance(value, (bool, int, str)) else False

    @strict_validation.setter
    def strict_validation(self, value: bool) -> None:
        self._settings["strict_validation"] = value

    @property
    def warn_on_unrecognized(self) -> bool:
        """Whether to log warning for unrecognized XML elements."""
        value = self._settings.get("warn_on_unrecognized", True)
        # Type narrowing: ensure we return bool
        return bool(value) if isinstance(value, (bool, int, str)) else True

    @warn_on_unrecognized.setter
    def warn_on_unrecognized(self, value: bool) -> None:
        self._settings["warn_on_unrecognized"] = value

    @property
    def builder_validation(self) -> BuilderValidationMode:
        """Get builder validation mode."""
        value = self._settings.get("builder_validation", BuilderValidationMode.STRICT)
        # Handle both string and enum values
        if isinstance(value, str):
            try:
                return BuilderValidationMode(value)
            except ValueError:
                return BuilderValidationMode.STRICT
        if isinstance(value, BuilderValidationMode):
            return value
        return BuilderValidationMode.STRICT

    @builder_validation.setter
    def builder_validation(self, value: BuilderValidationMode) -> None:
        self._settings["builder_validation"] = value

    @property
    def builder_type_coercion(self) -> bool:
        """Get builder type coercion enabled flag."""
        value = self._settings.get("builder_type_coercion", True)
        return bool(value) if isinstance(value, (bool, int, str)) else True

    @builder_type_coercion.setter
    def builder_type_coercion(self, value: bool) -> None:
        self._settings["builder_type_coercion"] = value
