"""ElementCollection module."""

# Use lazy import to avoid circular dependency with ARPackage
def __getattr__(name: str):
    """Lazy import to avoid circular dependency."""
    if name == "Collection":
        from .collection import Collection
        return Collection
    elif name == "CollectableElement":
        from .collectable_element import CollectableElement
        raise AttributeError(f"module {__name__} has no attribute {name}")
    raise AttributeError(f"module {__name__} has no attribute {name}")

