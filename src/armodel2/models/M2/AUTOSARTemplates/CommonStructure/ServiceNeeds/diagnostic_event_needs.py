"""DiagnosticEventNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 258)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 311)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 756)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import DiagnosticCapabilityElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.function_inhibition_needs import (
    FunctionInhibitionNeeds,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticEventNeeds(DiagnosticCapabilityElement):
    """AUTOSAR DiagnosticEventNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-EVENT-NEEDS"


    deferring_fid_refs: list[ARRef]
    diag_event_debounce: Optional[Any]
    inhibiting_fid_ref: Optional[ARRef]
    inhibiting_refs: list[ARRef]
    prestored: Optional[Boolean]
    uses_monitor: Optional[Boolean]
    _DESERIALIZE_DISPATCH = {
        "DEFERRING-FIDS": lambda obj, elem: obj.deferring_fid_refs.append(ARRef.deserialize(elem)),
        "DIAG-EVENT-DEBOUNCE": lambda obj, elem: setattr(obj, "diag_event_debounce", SerializationHelper.deserialize_by_tag(elem, "any (DiagEventDebounce)")),
        "INHIBITING-FID-REF": lambda obj, elem: setattr(obj, "inhibiting_fid_ref", ARRef.deserialize(elem)),
        "INHIBITINGS": lambda obj, elem: obj.inhibiting_refs.append(ARRef.deserialize(elem)),
        "PRESTORED": lambda obj, elem: setattr(obj, "prestored", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "USES-MONITOR": lambda obj, elem: setattr(obj, "uses_monitor", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
    }


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
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "DEFERRING-FIDS":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.deferring_fid_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "FunctionInhibitionNeeds"))
            elif tag == "DIAG-EVENT-DEBOUNCE":
                setattr(obj, "diag_event_debounce", SerializationHelper.deserialize_by_tag(child, "any (DiagEventDebounce)"))
            elif tag == "INHIBITING-FID-REF":
                setattr(obj, "inhibiting_fid_ref", ARRef.deserialize(child))
            elif tag == "INHIBITINGS":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.inhibiting_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "FunctionInhibitionNeeds"))
            elif tag == "PRESTORED":
                setattr(obj, "prestored", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "USES-MONITOR":
                setattr(obj, "uses_monitor", SerializationHelper.deserialize_by_tag(child, "Boolean"))

        return obj



class DiagnosticEventNeedsBuilder(DiagnosticCapabilityElementBuilder):
    """Builder for DiagnosticEventNeeds with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticEventNeeds = DiagnosticEventNeeds()


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



    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

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