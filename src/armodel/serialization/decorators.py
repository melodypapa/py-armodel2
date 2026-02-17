"""Decorators for XML serialization edge cases."""

from typing import Any, Callable


def xml_attribute(func: Any) -> Any:
    """Mark a property/attribute to be serialized as XML attribute instead of element.

    Usage:
        class AUTOSAR(ARObject):
            @xml_attribute
            @property
            def schema_version(self) -> str:
                return self._schema_version

    Args:
        func: Property or function to mark as XML attribute

    Returns:
        The decorated function/property with _is_xml_attribute marker set
    """
    # If func is a property, mark its fget (the underlying function)
    if isinstance(func, property):
        func.fget._is_xml_attribute = True  # type: ignore[union-attr]
    else:
        func._is_xml_attribute = True  # type: ignore[union-attr]
    return func


def xml_tag(tag_name: str) -> Callable[[Any], Any]:
    """Decorator to specify custom XML tag name for a class or attribute.

    Usage:
        @xml_tag("AUTOSAR")
        class AUTOSAR(ARObject):
            pass

    Args:
        tag_name: Custom XML tag name to use

    Returns:
        Decorator function that sets _xml_tag on the class/function
    """
    def decorator(cls_or_func: Any) -> Any:
        cls_or_func._xml_tag = tag_name  # type: ignore[union-attr]
        return cls_or_func
    return decorator
