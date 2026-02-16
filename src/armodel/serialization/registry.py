"""
Global registry for serialization metadata and strategies.

This module provides the central registry that manages serialization metadata
for all AUTOSAR model classes and coordinates strategy selection.
"""

from __future__ import annotations

from threading import RLock
from typing import TYPE_CHECKING

from armodel.serialization.base import StrategyRegistry

if TYPE_CHECKING:
    from armodel.serialization.base import SerializationStrategy
    from armodel.serialization.metadata import XMLMember


class SerializationRegistry:
    """
    Global registry for serialization metadata and strategies.

    This singleton class manages:
    1. XML metadata for all registered classes
    2. Serialization strategies
    3. Type-to-metadata lookups
    4. Metadata inheritance (MRO traversal)
    """

    _instance: SerializationRegistry | None = None
    _lock = RLock()
    _initialized: bool = False

    def __new__(cls) -> SerializationRegistry:
        """Ensure singleton instance."""
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance

    def __init__(self) -> None:
        """Initialize the registry (only once)."""
        if self._initialized:
            return

        with self._lock:
            if self._initialized:
                return

            self._metadata_cache: dict[type, dict[str, XMLMember]] = {}
            self._strategy_registry = StrategyRegistry()
            self._initialized = True

    def register_strategy(self, strategy: SerializationStrategy) -> None:
        """
        Register a serialization strategy.

        Args:
            strategy: The strategy to register
        """
        self._strategy_registry.register(strategy)

    def get_strategy(self, obj: type | object) -> SerializationStrategy | None:
        """
        Get the appropriate serialization strategy for an object or class.

        Args:
            obj: The object or class to find a strategy for

        Returns:
            The strategy that can handle the object, or None
        """
        return self._strategy_registry.get_strategy(obj)

    def get_metadata(self, cls: type, *, use_cache: bool = True) -> dict[str, XMLMember]:
        """
        Get XML metadata for a class.

        This method traverses the MRO to collect metadata from all parent classes.
        Results are cached for performance.

        Args:
            cls: The class to get metadata for
            use_cache: Whether to use cached metadata (default: True)

        Returns:
            Dictionary mapping member names to XMLMember instances
        """
        if use_cache and cls in self._metadata_cache:
            return self._metadata_cache[cls]

        # Import here to avoid circular import
        from armodel.serialization.metadata import get_xml_metadata

        metadata = get_xml_metadata(cls)

        if use_cache:
            self._metadata_cache[cls] = metadata

        return metadata

    def invalidate_cache(self, cls: type | None = None) -> None:
        """
        Invalidate metadata cache.

        Args:
            cls: Specific class to invalidate (None to clear all)
        """
        if cls is None:
            self._metadata_cache.clear()
        elif cls in self._metadata_cache:
            del self._metadata_cache[cls]

    def clear_strategy_cache(self) -> None:
        """Clear the strategy lookup cache."""
        self._strategy_registry.clear_cache()

    def clear_all_caches(self) -> None:
        """Clear all caches (metadata and strategy)."""
        self._metadata_cache.clear()
        self._strategy_registry.clear_cache()


_global_registry: SerializationRegistry | None = None


def get_global_registry() -> SerializationRegistry:
    """
    Get the global serialization registry singleton.

    Returns:
        The global SerializationRegistry instance
    """
    global _global_registry
    if _global_registry is None:
        _global_registry = SerializationRegistry()
    return _global_registry


def reset_global_registry() -> None:
    """
    Reset the global registry.

    This is primarily intended for testing purposes.
    """
    global _global_registry
    _global_registry = None
