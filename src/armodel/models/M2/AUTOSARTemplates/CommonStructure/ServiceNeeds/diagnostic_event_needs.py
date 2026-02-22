"""DiagnosticEventNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 258)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 311)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 756)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.function_inhibition_needs import (
    FunctionInhibitionNeeds,
)


class DiagnosticEventNeeds(DiagnosticCapabilityElement):
    """AUTOSAR DiagnosticEventNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    deferring_fid_refs: list[ARRef]
    diag_event_debounce: Optional[Any]
    inhibiting_fid_ref: Optional[ARRef]
    inhibiting_refs: list[ARRef]
    prestored: Optional[Boolean]
    uses_monitor: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize DiagnosticEventNeeds."""
        super().__init__()
        self.deferring_fid_refs: list[ARRef] = []
        self.diag_event_debounce: Optional[Any] = None
        self.inhibiting_fid_ref: Optional[ARRef] = None
        self.inhibiting_refs: list[ARRef] = []
        self.prestored: Optional[Boolean] = None
        self.uses_monitor: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticEventNeeds to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticEventNeeds, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize deferring_fid_refs (list to container "DEFERRING-FID-REFS")
        if self.deferring_fid_refs:
            wrapper = ET.Element("DEFERRING-FID-REFS")
            for item in self.deferring_fid_refs:
                serialized = SerializationHelper.serialize_item(item, "FunctionInhibitionNeeds")
                if serialized is not None:
                    child_elem = ET.Element("DEFERRING-FID-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize diag_event_debounce
        if self.diag_event_debounce is not None:
            serialized = SerializationHelper.serialize_item(self.diag_event_debounce, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DIAG-EVENT-DEBOUNCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize inhibiting_fid_ref
        if self.inhibiting_fid_ref is not None:
            serialized = SerializationHelper.serialize_item(self.inhibiting_fid_ref, "FunctionInhibitionNeeds")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INHIBITING-FID-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize inhibiting_refs (list to container "INHIBITING-REFS")
        if self.inhibiting_refs:
            wrapper = ET.Element("INHIBITING-REFS")
            for item in self.inhibiting_refs:
                serialized = SerializationHelper.serialize_item(item, "FunctionInhibitionNeeds")
                if serialized is not None:
                    child_elem = ET.Element("INHIBITING-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize prestored
        if self.prestored is not None:
            serialized = SerializationHelper.serialize_item(self.prestored, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PRESTORED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize uses_monitor
        if self.uses_monitor is not None:
            serialized = SerializationHelper.serialize_item(self.uses_monitor, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("USES-MONITOR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEventNeeds":
        """Deserialize XML element to DiagnosticEventNeeds object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticEventNeeds object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticEventNeeds, cls).deserialize(element)

        # Parse deferring_fid_refs (list from container "DEFERRING-FID-REFS")
        obj.deferring_fid_refs = []
        container = SerializationHelper.find_child_element(element, "DEFERRING-FID-REFS")
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
                    obj.deferring_fid_refs.append(child_value)

        # Parse diag_event_debounce
        child = SerializationHelper.find_child_element(element, "DIAG-EVENT-DEBOUNCE")
        if child is not None:
            diag_event_debounce_value = child.text
            obj.diag_event_debounce = diag_event_debounce_value

        # Parse inhibiting_fid_ref
        child = SerializationHelper.find_child_element(element, "INHIBITING-FID-REF")
        if child is not None:
            inhibiting_fid_ref_value = ARRef.deserialize(child)
            obj.inhibiting_fid_ref = inhibiting_fid_ref_value

        # Parse inhibiting_refs (list from container "INHIBITING-REFS")
        obj.inhibiting_refs = []
        container = SerializationHelper.find_child_element(element, "INHIBITING-REFS")
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
                    obj.inhibiting_refs.append(child_value)

        # Parse prestored
        child = SerializationHelper.find_child_element(element, "PRESTORED")
        if child is not None:
            prestored_value = child.text
            obj.prestored = prestored_value

        # Parse uses_monitor
        child = SerializationHelper.find_child_element(element, "USES-MONITOR")
        if child is not None:
            uses_monitor_value = child.text
            obj.uses_monitor = uses_monitor_value

        return obj



class DiagnosticEventNeedsBuilder:
    """Builder for DiagnosticEventNeeds with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: DiagnosticEventNeeds = DiagnosticEventNeeds()


    def with_short_name(self, value: Identifier) -> "DiagnosticEventNeedsBuilder":
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

    def with_short_name_fragments(self, items: list[ShortNameFragment]) -> "DiagnosticEventNeedsBuilder":
        """Set short_name_fragments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = list(items) if items else []
        return self

    def with_long_name(self, value: Optional[MultilanguageLongName]) -> "DiagnosticEventNeedsBuilder":
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

    def with_admin_data(self, value: Optional[AdminData]) -> "DiagnosticEventNeedsBuilder":
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

    def with_annotations(self, items: list[Annotation]) -> "DiagnosticEventNeedsBuilder":
        """Set annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.annotations = list(items) if items else []
        return self

    def with_desc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "DiagnosticEventNeedsBuilder":
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

    def with_category(self, value: Optional[CategoryString]) -> "DiagnosticEventNeedsBuilder":
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

    def with_introduction(self, value: Optional[DocumentationBlock]) -> "DiagnosticEventNeedsBuilder":
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

    def with_uuid(self, value: Optional[String]) -> "DiagnosticEventNeedsBuilder":
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

    def with_audiences(self, items: list[DiagnosticAudienceEnum]) -> "DiagnosticEventNeedsBuilder":
        """Set audiences list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.audiences = list(items) if items else []
        return self

    def with_diag(self, value: Optional[DiagRequirementIdString]) -> "DiagnosticEventNeedsBuilder":
        """Set diag attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.diag = value
        return self

    def with_security_access(self, value: Optional[PositiveInteger]) -> "DiagnosticEventNeedsBuilder":
        """Set security_access attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.security_access = value
        return self

    def with_deferring_fids(self, items: list[FunctionInhibitionNeeds]) -> "DiagnosticEventNeedsBuilder":
        """Set deferring_fids list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.deferring_fids = list(items) if items else []
        return self

    def with_diag_event_debounce(self, value: Optional[any (DiagEventDebounce)]) -> "DiagnosticEventNeedsBuilder":
        """Set diag_event_debounce attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.diag_event_debounce = value
        return self

    def with_inhibiting_fid(self, value: Optional[FunctionInhibitionNeeds]) -> "DiagnosticEventNeedsBuilder":
        """Set inhibiting_fid attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.inhibiting_fid = value
        return self

    def with_inhibitings(self, items: list[FunctionInhibitionNeeds]) -> "DiagnosticEventNeedsBuilder":
        """Set inhibitings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.inhibitings = list(items) if items else []
        return self

    def with_prestored(self, value: Optional[Boolean]) -> "DiagnosticEventNeedsBuilder":
        """Set prestored attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.prestored = value
        return self

    def with_uses_monitor(self, value: Optional[Boolean]) -> "DiagnosticEventNeedsBuilder":
        """Set uses_monitor attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.uses_monitor = value
        return self


    def add_short_name_fragment(self, item: ShortNameFragment) -> "DiagnosticEventNeedsBuilder":
        """Add a single item to short_name_fragments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments.append(item)
        return self

    def clear_short_name_fragments(self) -> "DiagnosticEventNeedsBuilder":
        """Clear all items from short_name_fragments list.

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = []
        return self

    def add_annotation(self, item: Annotation) -> "DiagnosticEventNeedsBuilder":
        """Add a single item to annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.annotations.append(item)
        return self

    def clear_annotations(self) -> "DiagnosticEventNeedsBuilder":
        """Clear all items from annotations list.

        Returns:
            self for method chaining
        """
        self._obj.annotations = []
        return self

    def add_audience(self, item: DiagnosticAudienceEnum) -> "DiagnosticEventNeedsBuilder":
        """Add a single item to audiences list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.audiences.append(item)
        return self

    def clear_audiences(self) -> "DiagnosticEventNeedsBuilder":
        """Clear all items from audiences list.

        Returns:
            self for method chaining
        """
        self._obj.audiences = []
        return self

    def add_deferring_fid(self, item: FunctionInhibitionNeeds) -> "DiagnosticEventNeedsBuilder":
        """Add a single item to deferring_fids list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.deferring_fids.append(item)
        return self

    def clear_deferring_fids(self) -> "DiagnosticEventNeedsBuilder":
        """Clear all items from deferring_fids list.

        Returns:
            self for method chaining
        """
        self._obj.deferring_fids = []
        return self

    def add_inhibiting(self, item: FunctionInhibitionNeeds) -> "DiagnosticEventNeedsBuilder":
        """Add a single item to inhibitings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.inhibitings.append(item)
        return self

    def clear_inhibitings(self) -> "DiagnosticEventNeedsBuilder":
        """Clear all items from inhibitings list.

        Returns:
            self for method chaining
        """
        self._obj.inhibitings = []
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


    def build(self) -> DiagnosticEventNeeds:
        """Build and return the DiagnosticEventNeeds instance with validation."""
        self._validate_instance()
        pass
        return self._obj