"""DiagnosticMemoryDestination AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 181)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticMemoryDestination.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import DiagnosticCommonElementBuilder
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticMemoryDestination import (
    DiagnosticMemoryEntryStorageTriggerEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_event import (
    DiagnosticEvent,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticMemoryDestination(DiagnosticCommonElement, ABC):
    """AUTOSAR DiagnosticMemoryDestination."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    aging_requires: Optional[Boolean]
    clear_dtc: Optional[Any]
    dtc_status: Optional[PositiveInteger]
    event: Optional[DiagnosticEvent]
    max_number_of: Optional[PositiveInteger]
    memory_entry: Optional[DiagnosticMemoryEntryStorageTriggerEnum]
    status_bit: Optional[Boolean]
    type_of_freeze: Optional[Any]
    _DESERIALIZE_DISPATCH = {
        "AGING-REQUIRES": lambda obj, elem: setattr(obj, "aging_requires", elem.text),
        "CLEAR-DTC": lambda obj, elem: setattr(obj, "clear_dtc", any (DiagnosticClearDtc).deserialize(elem)),
        "DTC-STATUS": lambda obj, elem: setattr(obj, "dtc_status", elem.text),
        "EVENT": lambda obj, elem: setattr(obj, "event", DiagnosticEvent.deserialize(elem)),
        "MAX-NUMBER-OF": lambda obj, elem: setattr(obj, "max_number_of", elem.text),
        "MEMORY-ENTRY": lambda obj, elem: setattr(obj, "memory_entry", DiagnosticMemoryEntryStorageTriggerEnum.deserialize(elem)),
        "STATUS-BIT": lambda obj, elem: setattr(obj, "status_bit", elem.text),
        "TYPE-OF-FREEZE": lambda obj, elem: setattr(obj, "type_of_freeze", any (DiagnosticTypeOf).deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticMemoryDestination."""
        super().__init__()
        self.aging_requires: Optional[Boolean] = None
        self.clear_dtc: Optional[Any] = None
        self.dtc_status: Optional[PositiveInteger] = None
        self.event: Optional[DiagnosticEvent] = None
        self.max_number_of: Optional[PositiveInteger] = None
        self.memory_entry: Optional[DiagnosticMemoryEntryStorageTriggerEnum] = None
        self.status_bit: Optional[Boolean] = None
        self.type_of_freeze: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticMemoryDestination to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticMemoryDestination, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize aging_requires
        if self.aging_requires is not None:
            serialized = SerializationHelper.serialize_item(self.aging_requires, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("AGING-REQUIRES")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize clear_dtc
        if self.clear_dtc is not None:
            serialized = SerializationHelper.serialize_item(self.clear_dtc, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CLEAR-DTC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize dtc_status
        if self.dtc_status is not None:
            serialized = SerializationHelper.serialize_item(self.dtc_status, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DTC-STATUS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize event
        if self.event is not None:
            serialized = SerializationHelper.serialize_item(self.event, "DiagnosticEvent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EVENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_number_of
        if self.max_number_of is not None:
            serialized = SerializationHelper.serialize_item(self.max_number_of, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-NUMBER-OF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize memory_entry
        if self.memory_entry is not None:
            serialized = SerializationHelper.serialize_item(self.memory_entry, "DiagnosticMemoryEntryStorageTriggerEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MEMORY-ENTRY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize status_bit
        if self.status_bit is not None:
            serialized = SerializationHelper.serialize_item(self.status_bit, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("STATUS-BIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize type_of_freeze
        if self.type_of_freeze is not None:
            serialized = SerializationHelper.serialize_item(self.type_of_freeze, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TYPE-OF-FREEZE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticMemoryDestination":
        """Deserialize XML element to DiagnosticMemoryDestination object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticMemoryDestination object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticMemoryDestination, cls).deserialize(element)

        # Parse aging_requires
        child = SerializationHelper.find_child_element(element, "AGING-REQUIRES")
        if child is not None:
            aging_requires_value = child.text
            obj.aging_requires = aging_requires_value

        # Parse clear_dtc
        child = SerializationHelper.find_child_element(element, "CLEAR-DTC")
        if child is not None:
            clear_dtc_value = child.text
            obj.clear_dtc = clear_dtc_value

        # Parse dtc_status
        child = SerializationHelper.find_child_element(element, "DTC-STATUS")
        if child is not None:
            dtc_status_value = child.text
            obj.dtc_status = dtc_status_value

        # Parse event
        child = SerializationHelper.find_child_element(element, "EVENT")
        if child is not None:
            event_value = SerializationHelper.deserialize_by_tag(child, "DiagnosticEvent")
            obj.event = event_value

        # Parse max_number_of
        child = SerializationHelper.find_child_element(element, "MAX-NUMBER-OF")
        if child is not None:
            max_number_of_value = child.text
            obj.max_number_of = max_number_of_value

        # Parse memory_entry
        child = SerializationHelper.find_child_element(element, "MEMORY-ENTRY")
        if child is not None:
            memory_entry_value = DiagnosticMemoryEntryStorageTriggerEnum.deserialize(child)
            obj.memory_entry = memory_entry_value

        # Parse status_bit
        child = SerializationHelper.find_child_element(element, "STATUS-BIT")
        if child is not None:
            status_bit_value = child.text
            obj.status_bit = status_bit_value

        # Parse type_of_freeze
        child = SerializationHelper.find_child_element(element, "TYPE-OF-FREEZE")
        if child is not None:
            type_of_freeze_value = child.text
            obj.type_of_freeze = type_of_freeze_value

        return obj



class DiagnosticMemoryDestinationBuilder(DiagnosticCommonElementBuilder):
    """Builder for DiagnosticMemoryDestination with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticMemoryDestination = DiagnosticMemoryDestination()


    def with_aging_requires(self, value: Optional[Boolean]) -> "DiagnosticMemoryDestinationBuilder":
        """Set aging_requires attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.aging_requires = value
        return self

    def with_clear_dtc(self, value: Optional[any (DiagnosticClearDtc)]) -> "DiagnosticMemoryDestinationBuilder":
        """Set clear_dtc attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.clear_dtc = value
        return self

    def with_dtc_status(self, value: Optional[PositiveInteger]) -> "DiagnosticMemoryDestinationBuilder":
        """Set dtc_status attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.dtc_status = value
        return self

    def with_event(self, value: Optional[DiagnosticEvent]) -> "DiagnosticMemoryDestinationBuilder":
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

    def with_max_number_of(self, value: Optional[PositiveInteger]) -> "DiagnosticMemoryDestinationBuilder":
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

    def with_memory_entry(self, value: Optional[DiagnosticMemoryEntryStorageTriggerEnum]) -> "DiagnosticMemoryDestinationBuilder":
        """Set memory_entry attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.memory_entry = value
        return self

    def with_status_bit(self, value: Optional[Boolean]) -> "DiagnosticMemoryDestinationBuilder":
        """Set status_bit attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.status_bit = value
        return self

    def with_type_of_freeze(self, value: Optional[any (DiagnosticTypeOf)]) -> "DiagnosticMemoryDestinationBuilder":
        """Set type_of_freeze attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.type_of_freeze = value
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


    @abstractmethod
    def build(self) -> DiagnosticMemoryDestination:
        """Build and return the DiagnosticMemoryDestination instance (abstract)."""
        raise NotImplementedError