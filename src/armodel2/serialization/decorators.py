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


def atp_mixed() -> Callable[[Any], Any]:
    """Decorator to mark a class as using AUTOSAR atpMixed pattern.

    Classes with atpMixed are container classes that can hold multiple
    different child types. Children are serialized directly without wrapping.

    Usage:
        @atp_mixed()
        class SwRecordLayoutGroupContent(ARObject):
            sw_record_layout_ref: Optional[ARRef] = None
            sw_record_layout_group: Optional[SwRecordLayoutGroup] = None
            sw_record_layout_v: Optional[SwRecordLayoutV] = None

    The ARObject serialization framework automatically:
    1. Serializes all children directly (no wrapping)
    2. Deserializes children by matching XML tags

    Returns:
        Decorator that sets _atp_mixed flag on the class
    """
    def decorator(cls: Any) -> Any:
        cls._atp_mixed = True  # type: ignore[union-attr]
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


def instance_ref(flatten: bool = False, list_type: str = "single") -> Callable[[Any], Any]:
    """Decorator to mark an attribute as an instance reference (iref).

    Instance references are wrapped in a <TAG>-IREF element.
    The flatten parameter controls whether children are flattened directly into
    the wrapper or wrapped in their own element.
    The list_type parameter controls how list attributes are serialized.

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

    Usage (multi-wrapper list - SwcToEcuMapping):
        @instance_ref(flatten=True, list_type="multi")
        @property
        def component_irefs(self) -> list[ComponentInSystemInstanceRef]:
            return self._component_irefs

    Serializes as:
        <COMPONENT-IREFS>
          <COMPONENT-IREF>
            <CONTEXT-COMPOSITION-REF>...</CONTEXT-COMPOSITION-REF>
            <TARGET-COMPONENT-REF>...</TARGET-COMPONENT-REF>
          </COMPONENT-IREF>
          <COMPONENT-IREF>
            <CONTEXT-COMPOSITION-REF>...</CONTEXT-COMPOSITION-REF>
            <TARGET-COMPONENT-REF>...</TARGET-COMPONENT-REF>
          </COMPONENT-IREF>
        </COMPONENT-IREFS>

    Args:
        flatten: If True, children are flattened directly into wrapper.
                If False, the element is wrapped. Default: False
        list_type: For list attributes only. "single" for single-wrapper behavior
                  (all items in one wrapper), "multi" for multi-wrapper behavior
                  (each item in its own wrapper). Default: "single"

    Returns:
        Decorator that sets _is_instance_ref, _flatten, and _list_type markers on the attribute
    """
    def decorator(attr_or_func: Any) -> Any:
        attr_or_func._is_instance_ref = True  # type: ignore[union-attr]
        attr_or_func._flatten = flatten  # type: ignore[union-attr]
        attr_or_func._list_type = list_type  # type: ignore[union-attr]
        return attr_or_func
    return decorator


def polymorphic(mapping: dict[str, str]) -> Callable[[Any], Any]:
    """Decorator to mark an attribute as polymorphic with wrapper element mapping.

    The polymorphic pattern is used when an XML wrapper element contains a concrete
    implementation of an abstract base class. The decorator accepts a dictionary
    mapping wrapper XML tags to base class names.

    For example, value_spec with @polymorphic({"VALUE-SPEC": "ValueSpecification"}):
    <VALUE-SPEC>
      <NUMERICAL-VALUE-SPECIFICATION>
        <SHORT-LABEL>MyValue</SHORT-LABEL>
        <VALUE>42</VALUE>
      </NUMERICAL-VALUE-SPECIFICATION>
    </VALUE-SPEC>

    The deserialization automatically:
    1. Finds the child element (<NUMERICAL-VALUE-SPECIFICATION>)
    2. Resolves the concrete class (NumericalValueSpecification)
    3. Validates it's a subclass of ValueSpecification (from mapping)
    4. Deserializes using the concrete class

    Usage (single mapping):
        class ConstantSpecification(ARElement):
            @polymorphic({"VALUE-SPEC": "ValueSpecification"})
            value_spec: Optional[ValueSpecification] = None

    Usage (multiple mappings):
        class CompuMethod(ARObject):
            @polymorphic({
                "COMPU-INTERNAL-TO-PHYS": "CompuContent",
                "COMPU-PHYS-TO-INTERNAL": "CompuContent"
            })
            compu_internal_to_phys: Optional[CompuContent] = None

    Args:
        mapping: Dictionary mapping wrapper XML tags to base class names
                Example: {"VALUE-SPEC": "ValueSpecification"}

    Returns:
        Decorator that sets _is_polymorphic and _polymorphic_mapping markers on the attribute
    """
    def decorator(attr_or_func: Any) -> Any:
        attr_or_func._is_polymorphic = True  # type: ignore[union-attr]
        attr_or_func._polymorphic_mapping = mapping  # type: ignore[union-attr]
        return attr_or_func
    return decorator
