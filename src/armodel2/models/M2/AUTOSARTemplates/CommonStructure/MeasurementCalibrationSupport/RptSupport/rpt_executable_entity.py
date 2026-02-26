"""RptExecutableEntity AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 200)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_MeasurementCalibrationSupport_RptSupport.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CIdentifier,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.role_based_mc_data_assignment import (
    RoleBasedMcDataAssignment,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class RptExecutableEntity(Identifiable):
    """AUTOSAR RptExecutableEntity."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    rpt_executable_entities: list[RptExecutableEntity]
    rpt_reads: list[RoleBasedMcDataAssignment]
    rpt_writes: list[RoleBasedMcDataAssignment]
    symbol: Optional[CIdentifier]
    def __init__(self) -> None:
        """Initialize RptExecutableEntity."""
        super().__init__()
        self.rpt_executable_entities: list[RptExecutableEntity] = []
        self.rpt_reads: list[RoleBasedMcDataAssignment] = []
        self.rpt_writes: list[RoleBasedMcDataAssignment] = []
        self.symbol: Optional[CIdentifier] = None

    def serialize(self) -> ET.Element:
        """Serialize RptExecutableEntity to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RptExecutableEntity, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize rpt_executable_entities (list to container "RPT-EXECUTABLE-ENTITIES")
        if self.rpt_executable_entities:
            wrapper = ET.Element("RPT-EXECUTABLE-ENTITIES")
            for item in self.rpt_executable_entities:
                serialized = SerializationHelper.serialize_item(item, "RptExecutableEntity")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize rpt_reads (list to container "RPT-READS")
        if self.rpt_reads:
            wrapper = ET.Element("RPT-READS")
            for item in self.rpt_reads:
                serialized = SerializationHelper.serialize_item(item, "RoleBasedMcDataAssignment")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize rpt_writes (list to container "RPT-WRITES")
        if self.rpt_writes:
            wrapper = ET.Element("RPT-WRITES")
            for item in self.rpt_writes:
                serialized = SerializationHelper.serialize_item(item, "RoleBasedMcDataAssignment")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize symbol
        if self.symbol is not None:
            serialized = SerializationHelper.serialize_item(self.symbol, "CIdentifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SYMBOL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RptExecutableEntity":
        """Deserialize XML element to RptExecutableEntity object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RptExecutableEntity object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RptExecutableEntity, cls).deserialize(element)

        # Parse rpt_executable_entities (list from container "RPT-EXECUTABLE-ENTITIES")
        obj.rpt_executable_entities = []
        container = SerializationHelper.find_child_element(element, "RPT-EXECUTABLE-ENTITIES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.rpt_executable_entities.append(child_value)

        # Parse rpt_reads (list from container "RPT-READS")
        obj.rpt_reads = []
        container = SerializationHelper.find_child_element(element, "RPT-READS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.rpt_reads.append(child_value)

        # Parse rpt_writes (list from container "RPT-WRITES")
        obj.rpt_writes = []
        container = SerializationHelper.find_child_element(element, "RPT-WRITES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.rpt_writes.append(child_value)

        # Parse symbol
        child = SerializationHelper.find_child_element(element, "SYMBOL")
        if child is not None:
            symbol_value = SerializationHelper.deserialize_by_tag(child, "CIdentifier")
            obj.symbol = symbol_value

        return obj



class RptExecutableEntityBuilder(IdentifiableBuilder):
    """Builder for RptExecutableEntity with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: RptExecutableEntity = RptExecutableEntity()


    def with_rpt_executable_entities(self, items: list[RptExecutableEntity]) -> "RptExecutableEntityBuilder":
        """Set rpt_executable_entities list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.rpt_executable_entities = list(items) if items else []
        return self

    def with_rpt_reads(self, items: list[RoleBasedMcDataAssignment]) -> "RptExecutableEntityBuilder":
        """Set rpt_reads list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.rpt_reads = list(items) if items else []
        return self

    def with_rpt_writes(self, items: list[RoleBasedMcDataAssignment]) -> "RptExecutableEntityBuilder":
        """Set rpt_writes list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.rpt_writes = list(items) if items else []
        return self

    def with_symbol(self, value: Optional[CIdentifier]) -> "RptExecutableEntityBuilder":
        """Set symbol attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.symbol = value
        return self


    def add_rpt_executable_entity(self, item: RptExecutableEntity) -> "RptExecutableEntityBuilder":
        """Add a single item to rpt_executable_entities list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.rpt_executable_entities.append(item)
        return self

    def clear_rpt_executable_entities(self) -> "RptExecutableEntityBuilder":
        """Clear all items from rpt_executable_entities list.

        Returns:
            self for method chaining
        """
        self._obj.rpt_executable_entities = []
        return self

    def add_rpt_read(self, item: RoleBasedMcDataAssignment) -> "RptExecutableEntityBuilder":
        """Add a single item to rpt_reads list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.rpt_reads.append(item)
        return self

    def clear_rpt_reads(self) -> "RptExecutableEntityBuilder":
        """Clear all items from rpt_reads list.

        Returns:
            self for method chaining
        """
        self._obj.rpt_reads = []
        return self

    def add_rpt_write(self, item: RoleBasedMcDataAssignment) -> "RptExecutableEntityBuilder":
        """Add a single item to rpt_writes list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.rpt_writes.append(item)
        return self

    def clear_rpt_writes(self) -> "RptExecutableEntityBuilder":
        """Clear all items from rpt_writes list.

        Returns:
            self for method chaining
        """
        self._obj.rpt_writes = []
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


    def build(self) -> RptExecutableEntity:
        """Build and return the RptExecutableEntity instance with validation."""
        self._validate_instance()
        pass
        return self._obj