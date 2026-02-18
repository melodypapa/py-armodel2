"""Decorators for XML serialization edge cases."""

from typing import Any, Callable, Optional


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


def xml_element_tag(xml_element_name: str, python_class_name: Optional[str] = None) -> Callable[[Any], Any]:
    """Decorator to specify custom XML element name and optional Python class name for a class attribute/element.

    Supports multi-level XML element names using '/' separator for nested elements.

    Usage:
        # Single-level element
        class CompuMethod(ARElement):
            @xml_element_tag("COMPU-INTERNAL-TO-PHYS")
            compu_internal_to_phys: Optional[Compu] = None

        # Multi-level element with explicit Python class
        class SwDataDefProps(ARElement):
            @xml_element_tag("SW-DATA-DEF-PROPS-VARIANTS/SW-DATA-DEF-PROPS-CONDITIONAL", "SwDataDefPropsConditional")
            variants: Optional[SwDataDefPropsConditional] = None

    Args:
        xml_element_name: XML element name to use for this element. Can be single-level
                          (e.g., "COMPU-INTERNAL-TO-PHYS") or multi-level
                          (e.g., "SW-DATA-DEF-PROPS-VARIANTS/SW-DATA-DEF-PROPS-CONDITIONAL")
        python_class_name: Optional Python class name to use for deserialization.
                         If provided, ARObject will use this class instead of inferring
                         from type hints. Useful for polymorphic types.

    Returns:
        Decorator function that sets _xml_element_tag and _xml_element_class on the class attribute
    """
    def decorator(cls_or_func: Any) -> Any:
        # Split multi-level element name
        element_path = xml_element_name.split('/')
        cls_or_func._xml_element_tag = element_path  # type: ignore[union-attr]

        # Store Python class name if provided
        # Convert class object to class name string if needed
        if python_class_name is not None:
            if isinstance(python_class_name, type):
                # It's a class object, get its name
                cls_or_func._xml_element_class = python_class_name.__name__  # type: ignore[union-attr]
            else:
                # It's already a string
                cls_or_func._xml_element_class = python_class_name  # type: ignore[union-attr]

        return cls_or_func
    return decorator
