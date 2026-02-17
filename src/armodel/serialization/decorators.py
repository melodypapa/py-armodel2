"""Decorators for XML serialization edge cases."""


def xml_attribute(func):
    """Mark a property/attribute to be serialized as XML attribute instead of element.

    Usage:
        class AUTOSAR(ARObject):
            @xml_attribute
            @property
            def schema_version(self) -> str:
                return self._schema_version
    """
    # If func is a property, mark its fget (the underlying function)
    if isinstance(func, property):
        func.fget._is_xml_attribute = True
    else:
        func._is_xml_attribute = True
    return func


def xml_tag(tag_name: str):
    """Decorator to specify custom XML tag name for a class or attribute.

    Usage:
        @xml_tag("AUTOSAR")
        class AUTOSAR(ARObject):
            pass
    """
    def decorator(cls_or_func):
        cls_or_func._xml_tag = tag_name
        return cls_or_func
    return decorator
