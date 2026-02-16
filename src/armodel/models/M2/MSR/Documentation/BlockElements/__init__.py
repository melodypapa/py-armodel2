"""BlockElements module."""

# Use lazy imports to avoid circular dependencies
def __getattr__(name):
    if name == 'DocumentationBlock':
        from .documentation_block import DocumentationBlock
        return DocumentationBlock
    elif name == 'Caption':
        from .caption import Caption
        return Caption
    else:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

__all__ = ['DocumentationBlock', 'Caption']

