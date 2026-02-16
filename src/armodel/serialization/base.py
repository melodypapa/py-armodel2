"""
Base classes and interfaces for the serialization framework.

This module provides the abstract base classes and context objects
that form the foundation of the serialization system.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    import xml.etree.ElementTree as ET

    from armodel.core.version import SchemaVersionManager


class SerializationContext:
    """
    Context object for serialization operations.

    Contains namespace information, schema version manager, and other
    serialization-time configuration.
    """

    __slots__ = ("namespace", "version_manager", "_cache")

    def __init__(
        self,
        namespace: str,
        version_manager: SchemaVersionManager | None = None,
    ) -> None:
        """
        Initialize serialization context.

        Args:
            namespace: XML namespace for the current serialization
            version_manager: Optional schema version manager for version-aware serialization
        """
        self.namespace: str = namespace
        self.version_manager: SchemaVersionManager | None = version_manager
        self._cache: dict[str, Any] = {}

    def get_cached(self, key: str) -> Any:
        """Get a value from the context cache."""
        return self._cache.get(key)

    def set_cached(self, key: str, value: Any) -> None:
        """Set a value in the context cache."""
        self._cache[key] = value


class DeserializationContext:
    """
    Context object for deserialization operations.

    Contains namespace information, schema version manager, and other
    deserialization-time configuration.
    """

    __slots__ = ("namespace", "version_manager", "_cache", "_element_cache")

    def __init__(
        self,
        namespace: str,
        version_manager: SchemaVersionManager | None = None,
    ) -> None:
        """
        Initialize deserialization context.

        Args:
            namespace: XML namespace for the current deserialization
            version_manager: Optional schema version manager for version-aware deserialization
        """
        self.namespace: str = namespace
        self.version_manager: SchemaVersionManager | None = version_manager
        self._cache: dict[str, Any] = {}
        self._element_cache: dict[str, Any] = {}

    def get_cached(self, key: str) -> Any:
        """Get a value from the context cache."""
        return self._cache.get(key)

    def set_cached(self, key: str, value: Any) -> None:
        """Set a value in the context cache."""
        self._cache[key] = value

    def get_element_cache(self, class_name: str) -> Any:
        """Get cached element for a class."""
        return self._element_cache.get(class_name)

    def set_element_cache(self, class_name: str, element: Any) -> None:
        """Cache element for a class."""
        self._element_cache[class_name] = element


class SerializationStrategy(ABC):
    """
    Abstract base class for serialization strategies.

    Each strategy is responsible for serializing and deserializing
    a specific type or pattern of AUTOSAR objects.
    """

    @abstractmethod
    def can_handle(self, obj: type | object) -> bool:
        """
        Check if this strategy can handle the given object or class.

        Args:
            obj: The object or class to check

        Returns:
            True if this strategy can handle the object
        """
        ...

    @abstractmethod
    def serialize(
        self,
        obj: object,
        context: SerializationContext,
        element: ET.Element | None = None,
    ) -> ET.Element:
        """
        Serialize an object to XML.

        Args:
            obj: The object to serialize
            context: Serialization context
            element: Optional existing element to serialize into

        Returns:
            The XML element representing the object
        """
        ...

    @abstractmethod
    def deserialize(
        self,
        cls: type,
        element: ET.Element,
        context: DeserializationContext,
    ) -> object:
        """
        Deserialize an object from XML.

        Args:
            cls: The class to instantiate
            element: The XML element to deserialize from
            context: Deserialization context

        Returns:
            The deserialized object
        """
        ...


class StrategyRegistry:
    """
    Registry for serialization strategies.

    Manages the registration and lookup of serialization strategies
    based on object types.
    """

    def __init__(self) -> None:
        """Initialize the strategy registry."""
        self._strategies: list[SerializationStrategy] = []
        self._type_cache: dict[type, SerializationStrategy] = {}

    def register(self, strategy: SerializationStrategy) -> None:
        """
        Register a serialization strategy.

        Strategies are checked in registration order, so more specific
        strategies should be registered after more general ones.

        Args:
            strategy: The strategy to register
        """
        self._strategies.append(strategy)
        self._type_cache.clear()  # Clear cache when strategies change

    def get_strategy(self, obj: type | object) -> SerializationStrategy | None:
        """
        Get the appropriate strategy for an object or class.

        Args:
            obj: The object or class to find a strategy for

        Returns:
            The first strategy that can handle the object, or None
        """
        # Check cache for type objects
        if isinstance(obj, type):
            if obj in self._type_cache:
                return self._type_cache[obj]

            for strategy in self._strategies:
                if strategy.can_handle(obj):
                    self._type_cache[obj] = strategy
                    return strategy

        # For instances and cache misses, check all strategies
        for strategy in self._strategies:
            if strategy.can_handle(obj):
                # Cache for type objects
                if isinstance(obj, type):
                    self._type_cache[obj] = strategy
                return strategy

        return None

    def clear_cache(self) -> None:
        """Clear the type lookup cache."""
        self._type_cache.clear()
