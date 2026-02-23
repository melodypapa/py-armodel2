"""DiagnosticReadDataByPeriodicIDClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 130)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_ReadDataByPeriodicID.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import DiagnosticServiceClassBuilder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.ReadDataByPeriodicID.diagnostic_periodic_rate import (
    DiagnosticPeriodicRate,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class DiagnosticReadDataByPeriodicIDClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticReadDataByPeriodicIDClass."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    max_periodic_did: Optional[PositiveInteger]
    periodic_rates: list[DiagnosticPeriodicRate]
    scheduler_max: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DiagnosticReadDataByPeriodicIDClass."""
        super().__init__()
        self.max_periodic_did: Optional[PositiveInteger] = None
        self.periodic_rates: list[DiagnosticPeriodicRate] = []
        self.scheduler_max: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticReadDataByPeriodicIDClass to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticReadDataByPeriodicIDClass, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize max_periodic_did
        if self.max_periodic_did is not None:
            serialized = SerializationHelper.serialize_item(self.max_periodic_did, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-PERIODIC-DID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize periodic_rates (list to container "PERIODIC-RATES")
        if self.periodic_rates:
            wrapper = ET.Element("PERIODIC-RATES")
            for item in self.periodic_rates:
                serialized = SerializationHelper.serialize_item(item, "DiagnosticPeriodicRate")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize scheduler_max
        if self.scheduler_max is not None:
            serialized = SerializationHelper.serialize_item(self.scheduler_max, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SCHEDULER-MAX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticReadDataByPeriodicIDClass":
        """Deserialize XML element to DiagnosticReadDataByPeriodicIDClass object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticReadDataByPeriodicIDClass object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticReadDataByPeriodicIDClass, cls).deserialize(element)

        # Parse max_periodic_did
        child = SerializationHelper.find_child_element(element, "MAX-PERIODIC-DID")
        if child is not None:
            max_periodic_did_value = child.text
            obj.max_periodic_did = max_periodic_did_value

        # Parse periodic_rates (list from container "PERIODIC-RATES")
        obj.periodic_rates = []
        container = SerializationHelper.find_child_element(element, "PERIODIC-RATES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.periodic_rates.append(child_value)

        # Parse scheduler_max
        child = SerializationHelper.find_child_element(element, "SCHEDULER-MAX")
        if child is not None:
            scheduler_max_value = child.text
            obj.scheduler_max = scheduler_max_value

        return obj



class DiagnosticReadDataByPeriodicIDClassBuilder(DiagnosticServiceClassBuilder):
    """Builder for DiagnosticReadDataByPeriodicIDClass with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticReadDataByPeriodicIDClass = DiagnosticReadDataByPeriodicIDClass()


    def with_max_periodic_did(self, value: Optional[PositiveInteger]) -> "DiagnosticReadDataByPeriodicIDClassBuilder":
        """Set max_periodic_did attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.max_periodic_did = value
        return self

    def with_periodic_rates(self, items: list[DiagnosticPeriodicRate]) -> "DiagnosticReadDataByPeriodicIDClassBuilder":
        """Set periodic_rates list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.periodic_rates = list(items) if items else []
        return self

    def with_scheduler_max(self, value: Optional[PositiveInteger]) -> "DiagnosticReadDataByPeriodicIDClassBuilder":
        """Set scheduler_max attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.scheduler_max = value
        return self


    def add_periodic_rate(self, item: DiagnosticPeriodicRate) -> "DiagnosticReadDataByPeriodicIDClassBuilder":
        """Add a single item to periodic_rates list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.periodic_rates.append(item)
        return self

    def clear_periodic_rates(self) -> "DiagnosticReadDataByPeriodicIDClassBuilder":
        """Clear all items from periodic_rates list.

        Returns:
            self for method chaining
        """
        self._obj.periodic_rates = []
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


    def build(self) -> DiagnosticReadDataByPeriodicIDClass:
        """Build and return the DiagnosticReadDataByPeriodicIDClass instance with validation."""
        self._validate_instance()
        pass
        return self._obj