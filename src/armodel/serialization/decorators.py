"""Decorators for XML serialization edge cases."""

from typing import Any, Callable


def xml_attribute(func_or_name: Any = None) -> Any:
    """Mark a property/attribute to be serialized as XML attribute instead of element.

    Usage (without parameter):
        class AUTOSAR(ARObject):
            @xml_attribute
            @property
            def schema_version(self) -> str:
                return self._schema_version

    Usage (with custom XML attribute name):
        class ARObject(ARObject):
            @xml_attribute("T")
            @property
            def timestamp(self) -> str:
                return self._timestamp

    Args:
        func_or_name: Either a property/function to mark, or a custom XML attribute name (string)

    Returns:
        The decorated function/property with _is_xml_attribute marker set,
        or a decorator function if called with a parameter
    """
    # If called with a parameter (custom attribute name), return a decorator
    if isinstance(func_or_name, str):
        custom_attr_name = func_or_name
        def decorator(func: Any) -> Any:
            # If func is a property, mark its fget (the underlying function)
            if isinstance(func, property):
                func.fget._is_xml_attribute = True  # type: ignore[union-attr]
                func.fget._xml_attr_name = custom_attr_name  # type: ignore[union-attr]
            else:
                func._is_xml_attribute = True  # type: ignore[union-attr]
                func._xml_attr_name = custom_attr_name  # type: ignore[union-attr]
            return func
        return decorator
    else:
        # No parameter, mark the function directly
        func = func_or_name
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


def lang_prefix(xml_tag: str) -> Callable[[Any], Any]:
    """Decorator to mark an attribute as using the lang_prefix pattern.

    The lang_prefix pattern wraps child elements in language-specific XML tags.
    This is used for MultiLanguage* classes where language-specific content
    is wrapped in L-<number> elements.

    For example, attribute `l10` with type `LPlainText` is serialized as:
    <L-10 L="EN">English text</L-10>

    Usage:
        class MultiLanguagePlainText(ARObject):
            @lang_prefix("L-10")
            l10: LPlainText = None

    Args:
        xml_tag: The XML tag to use for wrapping (e.g., "L-10", "L-4", "L-2")

    Returns:
        Decorator that sets _lang_prefix and _lang_prefix_tag on the attribute
    """
    def decorator(attr_or_func: Any) -> Any:
        attr_or_func._lang_prefix = True  # type: ignore[union-attr]
        attr_or_func._lang_prefix_tag = xml_tag  # type: ignore[union-attr]
        return attr_or_func
    return decorator


def lang_abbr(xml_attr_name: str) -> Callable[[Any], Any]:
    """Decorator to mark an attribute as a language abbreviation XML attribute.

    This decorator is used for LanguageSpecific series classes where the
    language abbreviation attribute (typically 'l') should be serialized as
    an XML attribute with a custom name (typically 'L').

    Unlike @xml_attribute which uses NameConverter to auto-convert names,
    @lang_abbr allows specifying the exact XML attribute name.

    Usage:
        class LanguageSpecific(ARObject):
            @lang_abbr("L")
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


def ref_conditional(xml_tag: str) -> Callable[[Any], Any]:
    """Decorator to mark an attribute as using the -REF-CONDITIONAL pattern.

    The -REF-CONDITIONAL pattern is used in AUTOSAR atpVariation for reference lists
    where each reference is wrapped in a <TAG>-REF-CONDITIONAL element containing
    the actual <TAG>-REF element.

    For example, fibexElements with @ref_conditional("FIBEX-ELEMENTS") serializes as:
    <FIBEX-ELEMENTS>
      <FIBEX-ELEMENT-REF-CONDITIONAL>
        <FIBEX-ELEMENT-REF DEST="...">...</FIBEX-ELEMENT-REF>
      </FIBEX-ELEMENT-REF-CONDITIONAL>
    </FIBEX-ELEMENTS>

    This is different from the standard reference list pattern which uses:
    <TAG-REFS>
      <TAG-REF>...</TAG-REF>
    </TAG-REFS>

    Usage:
        class System(ARElement):
            @ref_conditional("FIBEX-ELEMENTS")
            fibex_element_refs: list[ARRef] = []

    Args:
        xml_tag: The container element name (e.g., "FIBEX-ELEMENTS")

    Returns:
        Decorator that sets _is_ref_conditional and _xml_tag markers on the attribute
    """
    def decorator(attr_or_func: Any) -> Any:
        attr_or_func._is_ref_conditional = True  # type: ignore[union-attr]
        attr_or_func._xml_tag = xml_tag  # type: ignore[union-attr]
        return attr_or_func
    return decorator


def instance_ref(flatten: bool = False) -> Callable[[Any], Any]:
    """Decorator to mark an attribute as an instance reference (iref).

    Instance references are wrapped in a <TAG>-IREF element.
    The flatten parameter controls whether children are flattened directly into
    the wrapper or wrapped in their own element.

    Usage (flattened - AssemblySwConnector):
        @instance_ref(flatten=True)
        @property
        def provider_iref(self) -> PPortInCompositionInstanceRef:
            return self._provider_iref

    Serializes as:
        <PROVIDER-IREF>
          <CONTEXT-COMPONENT-REF>...</CONTEXT-COMPONENT-REF>
          <TARGET-P-PORT-REF>...</TARGET-P-PORT-REF>
        </PROVIDER-IREF>

    Usage (non-flattened - DelegationSwConnector):
        @instance_ref(flatten=False)
        @property
        def inner_port_iref(self) -> PortInCompositionTypeInstanceRef:
            return self._inner_port_iref

    Serializes as:
        <INNER-PORT-IREF>
          <R-PORT-IN-COMPOSITION-INSTANCE-REF>
            <CONTEXT-COMPONENT-REF>...</CONTEXT-COMPONENT-REF>
            <TARGET-R-PORT-REF>...</TARGET-R-PORT-REF>
          </R-PORT-IN-COMPOSITION-INSTANCE-REF>
        </INNER-PORT-IREF>

    Args:
        flatten: If True, children are flattened directly into wrapper.
                If False, the element is wrapped. Default: False

    Returns:
        Decorator that sets _is_instance_ref and _flatten markers on the attribute
    """
    def decorator(attr_or_func: Any) -> Any:
        attr_or_func._is_instance_ref = True  # type: ignore[union-attr]
        attr_or_func._flatten = flatten  # type: ignore[union-attr]
        return attr_or_func
    return decorator
