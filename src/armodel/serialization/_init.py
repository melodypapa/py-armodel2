"""Initialize the serialization registry with default strategies.

This module is imported when armodel.serialization is imported to ensure
the registry is initialized with the default strategies.
"""

from armodel.serialization.registry import get_global_registry
from armodel.serialization.strategies import AUTOSARSerializer, ReflectionSerializer


def _initialize_registry() -> None:
    """Initialize the global registry with default strategies."""
    registry = get_global_registry()

    # Register strategies in order (most specific last)
    # AUTOSARSerializer is more specific, so register it first
    registry.register_strategy(AUTOSARSerializer())
    # ReflectionSerializer is the general fallback
    registry.register_strategy(ReflectionSerializer())


# Initialize on module import
_initialize_registry()
