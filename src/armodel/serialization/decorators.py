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


def atp_variant() -> Callable[[Any], Any]:
    """Decorator to mark a class as using AUTOSAR atpVariation pattern.

    Classes with atpVariation wrap all their attributes in nested XML elements.
    The wrapper path is automatically derived from the class name using AUTOSAR convention:
    - First level: <CLASS-TAG>-VARIANTS
    - Second level: <CLASS-TAG>-CONDITIONAL

    Usage:
        @atp_variant()
        class SwDataDefProps(ARObject):
            base_type_ref: Optional[ARRef] = None
            sw_calibration_access: Optional[SwCalibrationAccessEnum] = None

    Generates wrapper path: "SW-DATA-DEF-PROPS-VARIANTS/SW-DATA-DEF-PROPS-CONDITIONAL"

    The ARObject serialization framework automatically:
    1. Creates the nested wrapper elements during serialization
    2. Navigates through wrapper elements during deserialization

    Returns:
        Decorator that sets _atp_variant flag on the class
    """
    def decorator(cls: Any) -> Any:
        cls._atp_variant = True  # type: ignore[union-attr]
        return cls
    return decorator


def l_prefix(xml_tag: str) -> Callable[[Any], Any]:
    """Decorator to mark an attribute as using the l_prefix pattern.

    The l_prefix pattern wraps child elements in language-specific XML tags.
    This is used for MultiLanguage* classes where language-specific content
    is wrapped in L-<number> elements.

    For example, attribute `l10` with type `LPlainText` is serialized as:
    <L-10 L="EN">English text</L-10>

    Usage:
        class MultiLanguagePlainText(ARObject):
            @l_prefix("L-10")
            l10: LPlainText = None

    Args:
        xml_tag: The XML tag to use for wrapping (e.g., "L-10", "L-4", "L-2")

    Returns:
        Decorator that sets _l_prefix and _l_prefix_tag on the attribute
    """
    def decorator(attr_or_func: Any) -> Any:
        attr_or_func._l_prefix = True  # type: ignore[union-attr]
        attr_or_func._l_prefix_tag = xml_tag  # type: ignore[union-attr]
        return attr_or_func
    return decorator


def language_abbr(xml_attr_name: str) -> Callable[[Any], Any]:
    """Decorator to mark an attribute as a language abbreviation XML attribute.

    This decorator is used for LanguageSpecific series classes where the
    language abbreviation attribute (typically 'l') should be serialized as
    an XML attribute with a custom name (typically 'L').

    Unlike @xml_attribute which uses NameConverter to auto-convert names,
    @language_abbr allows specifying the exact XML attribute name.

    Usage:
        class LanguageSpecific(ARObject):
            @language_abbr("L")
            @property
            def l(self) -> LEnum:
                return self._l

    Generated XML:
        <L-LONG-NAME L="EN">Long Name</L-LONG-NAME>

    Args:
        xml_attr_name: The exact XML attribute name to use (e.g., "L")

    Returns:
        Decorator that sets _language_abbr and _xml_attr_name markers on the attribute
    """
    def decorator(attr_or_func: Any) -> Any:
        attr_or_func._language_abbr = True  # type: ignore[union-attr]
        attr_or_func._xml_attr_name = xml_attr_name  # type: ignore[union-attr]
        return attr_or_func
    return decorator
