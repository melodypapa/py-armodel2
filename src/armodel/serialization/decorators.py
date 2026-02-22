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


def atp_variant(variant_type: str = "default") -> Callable[[Any], Any]:
    """Decorator to mark a class/attribute as using AUTOSAR atpVariation pattern.

    Classes with atpVariation wrap their content in nested XML elements.
    The variant_type parameter determines the wrapper pattern:
    - "default" (class-level): Two-level wrapper <CLASS-TAG>-VARIANTS/<CLASS-TAG>-CONDITIONAL
    - "ref_conditional" (attribute-level): Single-level <REF-TAG>-CONDITIONAL for references

    Usage (class-level - default pattern):
        @atp_variant()
        class SwDataDefProps(ARObject):
            base_type_ref: Optional[ARRef] = None
            sw_calibration_access: Optional[SwCalibrationAccessEnum] = None

        Generates: <SW-DATA-DEF-PROPS-VARIANTS><SW-DATA-DEF-PROPS-CONDITIONAL>...attributes...</SW-DATA-DEF-PROPS-CONDITIONAL></SW-DATA-DEF-PROPS-VARIANTS>

    Usage (attribute-level - ref_conditional pattern):
        @atp_variant("ref_conditional")
        encapsulated_entry: Optional[ARRef] = None

        Generates: <BSW-MODULE-ENTRY-REF-CONDITIONAL><BSW-MODULE-ENTRY-REF>...</BSW-MODULE-ENTRY-REF></BSW-MODULE-ENTRY-REF-CONDITIONAL>

    Args:
        variant_type: Pattern type - "default" (VARIANTS/CONDITIONAL) or "ref_conditional" (REF-CONDITIONAL)

    Returns:
        Decorator that sets _atp_variant flag and _atp_variant_type on the class/attribute
    """
    def decorator(obj: Any) -> Any:
        obj._atp_variant = True  # type: ignore[union-attr]
        obj._atp_variant_type = variant_type  # type: ignore[union-attr]
        return obj
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


def xml_element_name(xml_tag: str) -> Callable[[Any], Any]:
    """Decorator to specify custom XML element name for attributes.

    This decorator is used when the XML element name differs from the
    auto-generated name. For example, 'providedClientServerEntries' should
    serialize to 'PROVIDED-ENTRYS' instead of 'PROVIDED-CLIENT-SERVER-ENTRIES'.

    Usage:
        class BswModuleDescription(ARElement):
            @xml_element_name("PROVIDED-ENTRYS")
            provided_client_server_entries: list[BswModuleClientServerEntry] = []

    Args:
        xml_tag: The exact XML element name to use (e.g., "PROVIDED-ENTRYS")

    Returns:
        Decorator that sets _xml_element_name marker on the attribute
    """
    def decorator(attr_or_func: Any) -> Any:
        attr_or_func._xml_element_name = True  # type: ignore[union-attr]
        attr_or_func._xml_tag = xml_tag  # type: ignore[union-attr]
        return attr_or_func
    return decorator
