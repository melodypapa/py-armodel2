"""DiagnosticIOControl AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 118)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_IOControl.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import DiagnosticServiceInstanceBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_data_identifier import (
    DiagnosticDataIdentifier,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticIOControl(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticIOControl."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-I-O-CONTROL"


    control_enables: list[Any]
    data_identifier_identifier_ref: Optional[ARRef]
    freeze_current: Optional[Boolean]
    io_control_class_ref: Optional[ARRef]
    reset_to_default: Optional[Boolean]
    short_term: Optional[Boolean]
    _DESERIALIZE_DISPATCH = {
        "CONTROL-ENABLES": lambda obj, elem: obj.control_enables.append(SerializationHelper.deserialize_by_tag(elem, "any (DiagnosticControl)")),
        "DATA-IDENTIFIER-IDENTIFIER-REF": lambda obj, elem: setattr(obj, "data_identifier_identifier_ref", ARRef.deserialize(elem)),
        "FREEZE-CURRENT": lambda obj, elem: setattr(obj, "freeze_current", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "IO-CONTROL-CLASS-REF": lambda obj, elem: setattr(obj, "io_control_class_ref", ARRef.deserialize(elem)),
        "RESET-TO-DEFAULT": lambda obj, elem: setattr(obj, "reset_to_default", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "SHORT-TERM": lambda obj, elem: setattr(obj, "short_term", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticIOControl."""
        super().__init__()
        self.control_enables: list[Any] = []
        self.data_identifier_identifier_ref: Optional[ARRef] = None
        self.freeze_current: Optional[Boolean] = None
        self.io_control_class_ref: Optional[ARRef] = None
        self.reset_to_default: Optional[Boolean] = None
        self.short_term: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticIOControl to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticIOControl, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize control_enables (list to container "CONTROL-ENABLES")
        if self.control_enables:
            wrapper = ET.Element("CONTROL-ENABLES")
            for item in self.control_enables:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize data_identifier_identifier_ref
        if self.data_identifier_identifier_ref is not None:
            serialized = SerializationHelper.serialize_item(self.data_identifier_identifier_ref, "DiagnosticDataIdentifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-IDENTIFIER-IDENTIFIER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize freeze_current
        if self.freeze_current is not None:
            serialized = SerializationHelper.serialize_item(self.freeze_current, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FREEZE-CURRENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize io_control_class_ref
        if self.io_control_class_ref is not None:
            serialized = SerializationHelper.serialize_item(self.io_control_class_ref, "DiagnosticIOControl")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IO-CONTROL-CLASS-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize reset_to_default
        if self.reset_to_default is not None:
            serialized = SerializationHelper.serialize_item(self.reset_to_default, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RESET-TO-DEFAULT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize short_term
        if self.short_term is not None:
            serialized = SerializationHelper.serialize_item(self.short_term, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHORT-TERM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticIOControl":
        """Deserialize XML element to DiagnosticIOControl object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticIOControl object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticIOControl, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CONTROL-ENABLES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.control_enables.append(SerializationHelper.deserialize_by_tag(item_elem, "any (DiagnosticControl)"))
            elif tag == "DATA-IDENTIFIER-IDENTIFIER-REF":
                setattr(obj, "data_identifier_identifier_ref", ARRef.deserialize(child))
            elif tag == "FREEZE-CURRENT":
                setattr(obj, "freeze_current", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "IO-CONTROL-CLASS-REF":
                setattr(obj, "io_control_class_ref", ARRef.deserialize(child))
            elif tag == "RESET-TO-DEFAULT":
                setattr(obj, "reset_to_default", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "SHORT-TERM":
                setattr(obj, "short_term", SerializationHelper.deserialize_by_tag(child, "Boolean"))

        return obj



class DiagnosticIOControlBuilder(DiagnosticServiceInstanceBuilder):
    """Builder for DiagnosticIOControl with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticIOControl = DiagnosticIOControl()


    def with_control_enables(self, items: list[any (DiagnosticControl)]) -> "DiagnosticIOControlBuilder":
        """Set control_enables list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.control_enables = list(items) if items else []
        return self

    def with_data_identifier_identifier(self, value: Optional[DiagnosticDataIdentifier]) -> "DiagnosticIOControlBuilder":
        """Set data_identifier_identifier attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.data_identifier_identifier = value
        return self

    def with_freeze_current(self, value: Optional[Boolean]) -> "DiagnosticIOControlBuilder":
        """Set freeze_current attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.freeze_current = value
        return self

    def with_io_control_class(self, value: Optional[DiagnosticIOControl]) -> "DiagnosticIOControlBuilder":
        """Set io_control_class attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.io_control_class = value
        return self

    def with_reset_to_default(self, value: Optional[Boolean]) -> "DiagnosticIOControlBuilder":
        """Set reset_to_default attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.reset_to_default = value
        return self

    def with_short_term(self, value: Optional[Boolean]) -> "DiagnosticIOControlBuilder":
        """Set short_term attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.short_term = value
        return self


    def add_control_enable(self, item: any (DiagnosticControl)) -> "DiagnosticIOControlBuilder":
        """Add a single item to control_enables list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.control_enables.append(item)
        return self

    def clear_control_enables(self) -> "DiagnosticIOControlBuilder":
        """Clear all items from control_enables list.

        Returns:
            self for method chaining
        """
        self._obj.control_enables = []
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


    def build(self) -> DiagnosticIOControl:
        """Build and return the DiagnosticIOControl instance with validation."""
        self._validate_instance()
        pass
        return self._obj