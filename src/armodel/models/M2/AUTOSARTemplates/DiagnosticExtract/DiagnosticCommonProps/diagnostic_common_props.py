"""DiagnosticCommonProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 64)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticCommonProps.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET
from armodel.serialization.decorators import atp_variant

from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticCommonProps import (
    DiagnosticOccurrenceCounterProcessingEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ByteOrderEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_event import (
    DiagnosticEvent,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


@atp_variant()

class DiagnosticCommonProps(ARObject):
    """AUTOSAR DiagnosticCommonProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    authentication: Optional[TimeValue]
    debounces: list[Any]
    default: Optional[ByteOrderEnum]
    event: Optional[DiagnosticEvent]
    max_number_of: Optional[PositiveInteger]
    occurrence: Optional[DiagnosticOccurrenceCounterProcessingEnum]
    reset_confirmed: Optional[Boolean]
    reset_pending_bit: Optional[Boolean]
    response_on_all: Optional[Boolean]
    response_on: Optional[Boolean]
    type_of_event: Optional[DiagnosticEvent]
    def __init__(self) -> None:
        """Initialize DiagnosticCommonProps."""
        super().__init__()
        self.authentication: Optional[TimeValue] = None
        self.debounces: list[Any] = []
        self.default: Optional[ByteOrderEnum] = None
        self.event: Optional[DiagnosticEvent] = None
        self.max_number_of: Optional[PositiveInteger] = None
        self.occurrence: Optional[DiagnosticOccurrenceCounterProcessingEnum] = None
        self.reset_confirmed: Optional[Boolean] = None
        self.reset_pending_bit: Optional[Boolean] = None
        self.response_on_all: Optional[Boolean] = None
        self.response_on: Optional[Boolean] = None
        self.type_of_event: Optional[DiagnosticEvent] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticCommonProps to XML element with atp_variant wrapper.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticCommonProps, self).serialize()

        # Copy all attributes from parent element to outer element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element to outer element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Create inner element to hold attributes before wrapping
        inner_elem = ET.Element("INNER")

        # Copy parent's children: metadata to outer element, others to inner element
        metadata_tags = {'SHORT-NAME', 'LONG-NAME', 'DESC', 'ADMIN-DATA'}
        for child in parent_elem:
            tag = SerializationHelper.strip_namespace(child.tag)
            if tag in metadata_tags:
                # Metadata elements stay outside the atp_variant wrapper
                elem.append(child)
            else:
                # Other elements go inside the atp_variant wrapper
                inner_elem.append(child)

        # Serialize authentication
        if self.authentication is not None:
            serialized = SerializationHelper.serialize_item(self.authentication, "TimeValue")
            if serialized is not None:
                wrapped = ET.Element("AUTHENTICATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize debounces (list from container "DEBOUNCES")
        if self.debounces:
            container = ET.Element("DEBOUNCES")
            for item in self.debounces:
                if is_ref:
                    # For reference lists, serialize as reference
                    if hasattr(item, "serialize"):
                        container.append(item.serialize())
                elif is_primitive_type("any (DiagnosticDebounce)", package_data):
                    # Simple primitive type
                    child = ET.Element("DEBOUNCE")
                    child.text = str(item)
                    container.append(child)
                elif is_enum_type("any (DiagnosticDebounce)", package_data):
                    # Enum type - use serialize method
                    if hasattr(item, "serialize"):
                        container.append(item.serialize())
                else:
                    # Complex object type
                    if hasattr(item, "serialize"):
                        container.append(item.serialize())
            inner_elem.append(container)

        # Serialize default
        if self.default is not None:
            serialized = SerializationHelper.serialize_item(self.default, "ByteOrderEnum")
            if serialized is not None:
                wrapped = ET.Element("DEFAULT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize event
        if self.event is not None:
            serialized = SerializationHelper.serialize_item(self.event, "DiagnosticEvent")
            if serialized is not None:
                wrapped = ET.Element("EVENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize max_number_of
        if self.max_number_of is not None:
            serialized = SerializationHelper.serialize_item(self.max_number_of, "PositiveInteger")
            if serialized is not None:
                wrapped = ET.Element("MAX-NUMBER-OF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize occurrence
        if self.occurrence is not None:
            serialized = SerializationHelper.serialize_item(self.occurrence, "DiagnosticOccurrenceCounterProcessingEnum")
            if serialized is not None:
                wrapped = ET.Element("OCCURRENCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize reset_confirmed
        if self.reset_confirmed is not None:
            serialized = SerializationHelper.serialize_item(self.reset_confirmed, "Boolean")
            if serialized is not None:
                wrapped = ET.Element("RESET-CONFIRMED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize reset_pending_bit
        if self.reset_pending_bit is not None:
            serialized = SerializationHelper.serialize_item(self.reset_pending_bit, "Boolean")
            if serialized is not None:
                wrapped = ET.Element("RESET-PENDING-BIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize response_on_all
        if self.response_on_all is not None:
            serialized = SerializationHelper.serialize_item(self.response_on_all, "Boolean")
            if serialized is not None:
                wrapped = ET.Element("RESPONSE-ON-ALL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize response_on
        if self.response_on is not None:
            serialized = SerializationHelper.serialize_item(self.response_on, "Boolean")
            if serialized is not None:
                wrapped = ET.Element("RESPONSE-ON")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize type_of_event
        if self.type_of_event is not None:
            serialized = SerializationHelper.serialize_item(self.type_of_event, "DiagnosticEvent")
            if serialized is not None:
                wrapped = ET.Element("TYPE-OF-EVENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Wrap inner element in atp_variant VARIANTS/CONDITIONAL structure
        wrapped = SerializationHelper.serialize_with_atp_variant(inner_elem, "DiagnosticCommonProps")
        elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticCommonProps":
        """Deserialize XML element to DiagnosticCommonProps object with atp_variant unwrapping.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticCommonProps object
        """
        # Unwrap atp_variant VARIANTS/CONDITIONAL structure
        inner_elem = SerializationHelper.deserialize_from_atp_variant(element, "DiagnosticCommonProps")
        if inner_elem is None:
            # No wrapper structure found, create instance with default values
            obj = cls.__new__(cls)
            obj.__init__()
            return obj

        # Temporarily copy children from inner element to outer element
        # so parent's deserialize can find inherited attributes
        for child in list(inner_elem):
            element.append(child)

        # Call parent's deserialize with outer element (now contains parent's children)
        obj = super(DiagnosticCommonProps, cls).deserialize(element)

        # Clean up: remove the temporarily copied children from outer element
        # (they are now in obj, so we don't need them in element anymore)
        for child in list(inner_elem):
            element.remove(child)

        # Parse authentication
        child = SerializationHelper.find_child_element(inner_elem, "AUTHENTICATION")
        if child is not None:
            authentication_value = child.text
            obj.authentication = authentication_value

        # Parse debounces (list from container "DEBOUNCES")
        obj.debounces = []
        container = SerializationHelper.find_child_element(inner_elem, "DEBOUNCES")
        if container is not None:
            for child in container:
                if is_ref:
                    # Use the child_tag from decorator if specified to match specific child tag
                    if child_tag:
                        child_element_tag = SerializationHelper.strip_namespace(child.tag)
                        if child_element_tag == "None":
                            child_value = ARRef.deserialize(child)
                        else:
                            child_value = SerializationHelper.deserialize_by_tag(child, None)
                    else:
                        child_element_tag = SerializationHelper.strip_namespace(child.tag)
                        if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                            child_value = ARRef.deserialize(child)
                        else:
                            child_value = SerializationHelper.deserialize_by_tag(child, None)
                elif is_primitive_type("any (DiagnosticDebounce)", package_data):
                    child_value = child.text
                elif is_enum_type("any (DiagnosticDebounce)", package_data):
                    child_value = any (DiagnosticDebounce).deserialize(child)
                else:
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.debounces.append(child_value)

        # Parse default
        child = SerializationHelper.find_child_element(inner_elem, "DEFAULT")
        if child is not None:
            default_value = ByteOrderEnum.deserialize(child)
            obj.default = default_value

        # Parse event
        child = SerializationHelper.find_child_element(inner_elem, "EVENT")
        if child is not None:
            event_value = SerializationHelper.deserialize_by_tag(child, "DiagnosticEvent")
            obj.event = event_value

        # Parse max_number_of
        child = SerializationHelper.find_child_element(inner_elem, "MAX-NUMBER-OF")
        if child is not None:
            max_number_of_value = child.text
            obj.max_number_of = max_number_of_value

        # Parse occurrence
        child = SerializationHelper.find_child_element(inner_elem, "OCCURRENCE")
        if child is not None:
            occurrence_value = DiagnosticOccurrenceCounterProcessingEnum.deserialize(child)
            obj.occurrence = occurrence_value

        # Parse reset_confirmed
        child = SerializationHelper.find_child_element(inner_elem, "RESET-CONFIRMED")
        if child is not None:
            reset_confirmed_value = child.text
            obj.reset_confirmed = reset_confirmed_value

        # Parse reset_pending_bit
        child = SerializationHelper.find_child_element(inner_elem, "RESET-PENDING-BIT")
        if child is not None:
            reset_pending_bit_value = child.text
            obj.reset_pending_bit = reset_pending_bit_value

        # Parse response_on_all
        child = SerializationHelper.find_child_element(inner_elem, "RESPONSE-ON-ALL")
        if child is not None:
            response_on_all_value = child.text
            obj.response_on_all = response_on_all_value

        # Parse response_on
        child = SerializationHelper.find_child_element(inner_elem, "RESPONSE-ON")
        if child is not None:
            response_on_value = child.text
            obj.response_on = response_on_value

        # Parse type_of_event
        child = SerializationHelper.find_child_element(inner_elem, "TYPE-OF-EVENT")
        if child is not None:
            type_of_event_value = SerializationHelper.deserialize_by_tag(child, "DiagnosticEvent")
            obj.type_of_event = type_of_event_value

        return obj



class DiagnosticCommonPropsBuilder(BuilderBase):
    """Builder for DiagnosticCommonProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticCommonProps = DiagnosticCommonProps()


    def with_authentication(self, value: Optional[TimeValue]) -> "DiagnosticCommonPropsBuilder":
        """Set authentication attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.authentication = value
        return self

    def with_debounces(self, items: list[any (DiagnosticDebounce)]) -> "DiagnosticCommonPropsBuilder":
        """Set debounces list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.debounces = list(items) if items else []
        return self

    def with_default(self, value: Optional[ByteOrderEnum]) -> "DiagnosticCommonPropsBuilder":
        """Set default attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.default = value
        return self

    def with_event(self, value: Optional[DiagnosticEvent]) -> "DiagnosticCommonPropsBuilder":
        """Set event attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.event = value
        return self

    def with_max_number_of(self, value: Optional[PositiveInteger]) -> "DiagnosticCommonPropsBuilder":
        """Set max_number_of attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.max_number_of = value
        return self

    def with_occurrence(self, value: Optional[DiagnosticOccurrenceCounterProcessingEnum]) -> "DiagnosticCommonPropsBuilder":
        """Set occurrence attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.occurrence = value
        return self

    def with_reset_confirmed(self, value: Optional[Boolean]) -> "DiagnosticCommonPropsBuilder":
        """Set reset_confirmed attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.reset_confirmed = value
        return self

    def with_reset_pending_bit(self, value: Optional[Boolean]) -> "DiagnosticCommonPropsBuilder":
        """Set reset_pending_bit attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.reset_pending_bit = value
        return self

    def with_response_on_all(self, value: Optional[Boolean]) -> "DiagnosticCommonPropsBuilder":
        """Set response_on_all attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.response_on_all = value
        return self

    def with_response_on(self, value: Optional[Boolean]) -> "DiagnosticCommonPropsBuilder":
        """Set response_on attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.response_on = value
        return self

    def with_type_of_event(self, value: Optional[DiagnosticEvent]) -> "DiagnosticCommonPropsBuilder":
        """Set type_of_event attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.type_of_event = value
        return self


    def add_debounce(self, item: any (DiagnosticDebounce)) -> "DiagnosticCommonPropsBuilder":
        """Add a single item to debounces list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.debounces.append(item)
        return self

    def clear_debounces(self) -> "DiagnosticCommonPropsBuilder":
        """Clear all items from debounces list.

        Returns:
            self for method chaining
        """
        self._obj.debounces = []
        return self



    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Get type hints for the class
        try:
            type_hints_dict = get_type_hints(type(self._obj))
        except Exception:
            # Cannot resolve type hints (e.g., forward references), skip validation
            return

        for attr_name, attr_type in type_hints_dict.items():
            if attr_name.startswith("_"):
                continue

            value = getattr(self._obj, attr_name)

            # Check required fields (not Optional)
            if value is None and not self._is_optional_type(attr_type):
                if mode == BuilderValidationMode.STRICT:
                    raise ValueError(
                        f"Required attribute '{attr_name}' is None"
                    )
                elif mode == BuilderValidationMode.LENIENT:
                    import warnings
                    warnings.warn(
                        f"Required attribute '{attr_name}' is None",
                        UserWarning
                    )

    @staticmethod
    def _is_optional_type(type_hint: Any) -> bool:
        """Check if a type hint is Optional.

        Args:
            type_hint: Type hint to check

        Returns:
            True if type is Optional, False otherwise
        """
        origin = getattr(type_hint, "__origin__", None)
        return origin is Union

    @staticmethod
    def _get_expected_type(type_hint: Any) -> type:
        """Extract expected type from type hint.

        Args:
            type_hint: Type hint to extract from

        Returns:
            Expected type
        """
        if isinstance(type_hint, str):
            return object
        origin = getattr(type_hint, "__origin__", None)
        if origin is Union:
            args = getattr(type_hint, "__args__", [])
            for arg in args:
                if arg is not type(None):
                    return arg
        elif origin is list:
            args = getattr(type_hint, "__args__", [object])
            return args[0] if args else object
        return type_hint if isinstance(type_hint, type) else object


    def build(self) -> DiagnosticCommonProps:
        """Build and return the DiagnosticCommonProps instance with validation."""
        self._validate_instance()
        pass
        return self._obj