"""SignalServiceTranslationProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 336)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 1005)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 730)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_SignalServiceTranslation.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.consumed_event_group import (
    ConsumedEventGroup,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.event_handler import (
    EventHandler,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.PncMapping.pnc_mapping_ident import (
    PncMappingIdent,
)


class SignalServiceTranslationProps(Identifiable):
    """AUTOSAR SignalServiceTranslationProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    control_refs: list[ARRef]
    control_pnc_refs: list[ARRef]
    control_provided_refs: list[ARRef]
    service_control: Optional[Any]
    signal_service_event_propses: list[Any]
    def __init__(self) -> None:
        """Initialize SignalServiceTranslationProps."""
        super().__init__()
        self.control_refs: list[ARRef] = []
        self.control_pnc_refs: list[ARRef] = []
        self.control_provided_refs: list[ARRef] = []
        self.service_control: Optional[Any] = None
        self.signal_service_event_propses: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize SignalServiceTranslationProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SignalServiceTranslationProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize control_refs (list to container "CONTROL-REFS")
        if self.control_refs:
            wrapper = ET.Element("CONTROL-REFS")
            for item in self.control_refs:
                serialized = SerializationHelper.serialize_item(item, "ConsumedEventGroup")
                if serialized is not None:
                    child_elem = ET.Element("CONTROL-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize control_pnc_refs (list to container "CONTROL-PNC-REFS")
        if self.control_pnc_refs:
            wrapper = ET.Element("CONTROL-PNC-REFS")
            for item in self.control_pnc_refs:
                serialized = SerializationHelper.serialize_item(item, "PncMappingIdent")
                if serialized is not None:
                    child_elem = ET.Element("CONTROL-PNC-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize control_provided_refs (list to container "CONTROL-PROVIDED-REFS")
        if self.control_provided_refs:
            wrapper = ET.Element("CONTROL-PROVIDED-REFS")
            for item in self.control_provided_refs:
                serialized = SerializationHelper.serialize_item(item, "EventHandler")
                if serialized is not None:
                    child_elem = ET.Element("CONTROL-PROVIDED-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize service_control
        if self.service_control is not None:
            serialized = SerializationHelper.serialize_item(self.service_control, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SERVICE-CONTROL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize signal_service_event_propses (list to container "SIGNAL-SERVICE-EVENT-PROPSES")
        if self.signal_service_event_propses:
            wrapper = ET.Element("SIGNAL-SERVICE-EVENT-PROPSES")
            for item in self.signal_service_event_propses:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SignalServiceTranslationProps":
        """Deserialize XML element to SignalServiceTranslationProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SignalServiceTranslationProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SignalServiceTranslationProps, cls).deserialize(element)

        # Parse control_refs (list from container "CONTROL-REFS")
        obj.control_refs = []
        container = SerializationHelper.find_child_element(element, "CONTROL-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.control_refs.append(child_value)

        # Parse control_pnc_refs (list from container "CONTROL-PNC-REFS")
        obj.control_pnc_refs = []
        container = SerializationHelper.find_child_element(element, "CONTROL-PNC-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.control_pnc_refs.append(child_value)

        # Parse control_provided_refs (list from container "CONTROL-PROVIDED-REFS")
        obj.control_provided_refs = []
        container = SerializationHelper.find_child_element(element, "CONTROL-PROVIDED-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.control_provided_refs.append(child_value)

        # Parse service_control
        child = SerializationHelper.find_child_element(element, "SERVICE-CONTROL")
        if child is not None:
            service_control_value = child.text
            obj.service_control = service_control_value

        # Parse signal_service_event_propses (list from container "SIGNAL-SERVICE-EVENT-PROPSES")
        obj.signal_service_event_propses = []
        container = SerializationHelper.find_child_element(element, "SIGNAL-SERVICE-EVENT-PROPSES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.signal_service_event_propses.append(child_value)

        return obj



class SignalServiceTranslationPropsBuilder:
    """Builder for SignalServiceTranslationProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: SignalServiceTranslationProps = SignalServiceTranslationProps()


    def with_short_name(self, value: Identifier) -> "SignalServiceTranslationPropsBuilder":
        """Set short_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.short_name = value
        return self

    def with_short_name_fragments(self, items: list[ShortNameFragment]) -> "SignalServiceTranslationPropsBuilder":
        """Set short_name_fragments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = list(items) if items else []
        return self

    def with_long_name(self, value: Optional[MultilanguageLongName]) -> "SignalServiceTranslationPropsBuilder":
        """Set long_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.long_name = value
        return self

    def with_admin_data(self, value: Optional[AdminData]) -> "SignalServiceTranslationPropsBuilder":
        """Set admin_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.admin_data = value
        return self

    def with_annotations(self, items: list[Annotation]) -> "SignalServiceTranslationPropsBuilder":
        """Set annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.annotations = list(items) if items else []
        return self

    def with_desc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "SignalServiceTranslationPropsBuilder":
        """Set desc attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.desc = value
        return self

    def with_category(self, value: Optional[CategoryString]) -> "SignalServiceTranslationPropsBuilder":
        """Set category attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.category = value
        return self

    def with_introduction(self, value: Optional[DocumentationBlock]) -> "SignalServiceTranslationPropsBuilder":
        """Set introduction attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.introduction = value
        return self

    def with_uuid(self, value: Optional[String]) -> "SignalServiceTranslationPropsBuilder":
        """Set uuid attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.uuid = value
        return self

    def with_controls(self, items: list[ConsumedEventGroup]) -> "SignalServiceTranslationPropsBuilder":
        """Set controls list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.controls = list(items) if items else []
        return self

    def with_control_pncs(self, items: list[PncMappingIdent]) -> "SignalServiceTranslationPropsBuilder":
        """Set control_pncs list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.control_pncs = list(items) if items else []
        return self

    def with_control_provideds(self, items: list[EventHandler]) -> "SignalServiceTranslationPropsBuilder":
        """Set control_provideds list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.control_provideds = list(items) if items else []
        return self

    def with_service_control(self, value: Optional[any (SignalService)]) -> "SignalServiceTranslationPropsBuilder":
        """Set service_control attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.service_control = value
        return self

    def with_signal_service_event_propses(self, items: list[any (SignalService)]) -> "SignalServiceTranslationPropsBuilder":
        """Set signal_service_event_propses list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.signal_service_event_propses = list(items) if items else []
        return self


    def add_short_name_fragment(self, item: ShortNameFragment) -> "SignalServiceTranslationPropsBuilder":
        """Add a single item to short_name_fragments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments.append(item)
        return self

    def clear_short_name_fragments(self) -> "SignalServiceTranslationPropsBuilder":
        """Clear all items from short_name_fragments list.

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = []
        return self

    def add_annotation(self, item: Annotation) -> "SignalServiceTranslationPropsBuilder":
        """Add a single item to annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.annotations.append(item)
        return self

    def clear_annotations(self) -> "SignalServiceTranslationPropsBuilder":
        """Clear all items from annotations list.

        Returns:
            self for method chaining
        """
        self._obj.annotations = []
        return self

    def add_control(self, item: ConsumedEventGroup) -> "SignalServiceTranslationPropsBuilder":
        """Add a single item to controls list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.controls.append(item)
        return self

    def clear_controls(self) -> "SignalServiceTranslationPropsBuilder":
        """Clear all items from controls list.

        Returns:
            self for method chaining
        """
        self._obj.controls = []
        return self

    def add_control_pnc(self, item: PncMappingIdent) -> "SignalServiceTranslationPropsBuilder":
        """Add a single item to control_pncs list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.control_pncs.append(item)
        return self

    def clear_control_pncs(self) -> "SignalServiceTranslationPropsBuilder":
        """Clear all items from control_pncs list.

        Returns:
            self for method chaining
        """
        self._obj.control_pncs = []
        return self

    def add_control_provided(self, item: EventHandler) -> "SignalServiceTranslationPropsBuilder":
        """Add a single item to control_provideds list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.control_provideds.append(item)
        return self

    def clear_control_provideds(self) -> "SignalServiceTranslationPropsBuilder":
        """Clear all items from control_provideds list.

        Returns:
            self for method chaining
        """
        self._obj.control_provideds = []
        return self

    def add_signal_service_event_propse(self, item: any (SignalService)) -> "SignalServiceTranslationPropsBuilder":
        """Add a single item to signal_service_event_propses list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.signal_service_event_propses.append(item)
        return self

    def clear_signal_service_event_propses(self) -> "SignalServiceTranslationPropsBuilder":
        """Clear all items from signal_service_event_propses list.

        Returns:
            self for method chaining
        """
        self._obj.signal_service_event_propses = []
        return self


    @staticmethod
    def _coerce_to_int(value: Any) -> int:
        """Coerce value to int.

        Args:
            value: Value to coerce

        Returns:
            Integer value

        Raises:
            ValueError: If value cannot be coerced to int
        """
        if isinstance(value, int):
            return value
        if isinstance(value, str) and value.isdigit():
            return int(value)
        if isinstance(value, float):
            return int(value)
        if isinstance(value, bool):
            return int(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to int: {value}")

    @staticmethod
    def _coerce_to_float(value: Any) -> float:
        """Coerce value to float.

        Args:
            value: Value to coerce

        Returns:
            Float value

        Raises:
            ValueError: If value cannot be coerced to float
        """
        if isinstance(value, float):
            return value
        if isinstance(value, int):
            return float(value)
        if isinstance(value, str):
            try:
                return float(value)
            except ValueError:
                pass
        raise ValueError(f"Cannot coerce {type(value).__name__} to float: {value}")

    @staticmethod
    def _coerce_to_bool(value: Any) -> bool:
        """Coerce value to bool.

        Args:
            value: Value to coerce

        Returns:
            Boolean value

        Raises:
            ValueError: If value cannot be coerced to bool
        """
        if isinstance(value, bool):
            return value
        if isinstance(value, int):
            return bool(value)
        if isinstance(value, str):
            if value.lower() in ("true", "1", "yes"):
                return True
            if value.lower() in ("false", "0", "no"):
                return False
        raise ValueError(f"Cannot coerce {type(value).__name__} to bool: {value}")

    @staticmethod
    def _coerce_to_str(value: Any) -> str:
        """Coerce value to str.

        Args:
            value: Value to coerce

        Returns:
            String value
        """
        return str(value)


    @staticmethod
    def _coerce_to_list(value: Any, item_type: str) -> list:
        """Coerce value to list.

        Args:
            value: Value to coerce
            item_type: Expected item type (for error messages)

        Returns:
            List value

        Raises:
            ValueError: If value cannot be coerced to list
        """
        if isinstance(value, list):
            return value
        if isinstance(value, tuple):
            return list(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to list[{item_type}]: {value}")


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


    def build(self) -> SignalServiceTranslationProps:
        """Build and return the SignalServiceTranslationProps instance with validation."""
        self._validate_instance()
        pass
        return self._obj