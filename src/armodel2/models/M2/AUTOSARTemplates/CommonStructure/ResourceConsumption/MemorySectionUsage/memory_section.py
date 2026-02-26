"""MemorySection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 143)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 411)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2036)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ResourceConsumption_MemorySectionUsage.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AlignmentType,
    Identifier,
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.executable_entity import (
    ExecutableEntity,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.MemorySectionUsage.section_name_prefix import (
    SectionNamePrefix,
)
from armodel2.models.M2.MSR.DataDictionary.AuxillaryObjects.sw_addr_method import (
    SwAddrMethod,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class MemorySection(Identifiable):
    """AUTOSAR MemorySection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    alignment: Optional[AlignmentType]
    executable_entity_refs: list[ARRef]
    options: list[Identifier]
    prefix_ref: Optional[ARRef]
    size: Optional[PositiveInteger]
    sw_addrmethod_ref: Optional[ARRef]
    symbol: Optional[Identifier]
    def __init__(self) -> None:
        """Initialize MemorySection."""
        super().__init__()
        self.alignment: Optional[AlignmentType] = None
        self.executable_entity_refs: list[ARRef] = []
        self.options: list[Identifier] = []
        self.prefix_ref: Optional[ARRef] = None
        self.size: Optional[PositiveInteger] = None
        self.sw_addrmethod_ref: Optional[ARRef] = None
        self.symbol: Optional[Identifier] = None

    def serialize(self) -> ET.Element:
        """Serialize MemorySection to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(MemorySection, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize alignment
        if self.alignment is not None:
            serialized = SerializationHelper.serialize_item(self.alignment, "AlignmentType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ALIGNMENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize executable_entity_refs (list to container "EXECUTABLE-ENTITY-REFS")
        if self.executable_entity_refs:
            wrapper = ET.Element("EXECUTABLE-ENTITY-REFS")
            for item in self.executable_entity_refs:
                serialized = SerializationHelper.serialize_item(item, "ExecutableEntity")
                if serialized is not None:
                    child_elem = ET.Element("EXECUTABLE-ENTITY-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize options (list to container "OPTIONS")
        if self.options:
            wrapper = ET.Element("OPTIONS")
            for item in self.options:
                serialized = SerializationHelper.serialize_item(item, "Identifier")
                if serialized is not None:
                    child_elem = ET.Element("OPTION")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize prefix_ref
        if self.prefix_ref is not None:
            serialized = SerializationHelper.serialize_item(self.prefix_ref, "SectionNamePrefix")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PREFIX-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize size
        if self.size is not None:
            serialized = SerializationHelper.serialize_item(self.size, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SIZE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_addrmethod_ref
        if self.sw_addrmethod_ref is not None:
            serialized = SerializationHelper.serialize_item(self.sw_addrmethod_ref, "SwAddrMethod")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-ADDRMETHOD-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize symbol
        if self.symbol is not None:
            serialized = SerializationHelper.serialize_item(self.symbol, "Identifier")
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
    def deserialize(cls, element: ET.Element) -> "MemorySection":
        """Deserialize XML element to MemorySection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MemorySection object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(MemorySection, cls).deserialize(element)

        # Parse alignment
        child = SerializationHelper.find_child_element(element, "ALIGNMENT")
        if child is not None:
            alignment_value = child.text
            obj.alignment = alignment_value

        # Parse executable_entity_refs (list from container "EXECUTABLE-ENTITY-REFS")
        obj.executable_entity_refs = []
        container = SerializationHelper.find_child_element(element, "EXECUTABLE-ENTITY-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.executable_entity_refs.append(child_value)

        # Parse options (list from container "OPTIONS")
        obj.options = []
        container = SerializationHelper.find_child_element(element, "OPTIONS")
        if container is not None:
            for child in container:
                # Extract primitive value (Identifier) as text
                child_value = child.text
                if child_value is not None:
                    obj.options.append(child_value)

        # Parse prefix_ref
        child = SerializationHelper.find_child_element(element, "PREFIX-REF")
        if child is not None:
            prefix_ref_value = ARRef.deserialize(child)
            obj.prefix_ref = prefix_ref_value

        # Parse size
        child = SerializationHelper.find_child_element(element, "SIZE")
        if child is not None:
            size_value = child.text
            obj.size = size_value

        # Parse sw_addrmethod_ref
        child = SerializationHelper.find_child_element(element, "SW-ADDRMETHOD-REF")
        if child is not None:
            sw_addrmethod_ref_value = ARRef.deserialize(child)
            obj.sw_addrmethod_ref = sw_addrmethod_ref_value

        # Parse symbol
        child = SerializationHelper.find_child_element(element, "SYMBOL")
        if child is not None:
            symbol_value = SerializationHelper.deserialize_by_tag(child, "Identifier")
            obj.symbol = symbol_value

        return obj



class MemorySectionBuilder(IdentifiableBuilder):
    """Builder for MemorySection with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: MemorySection = MemorySection()


    def with_alignment(self, value: Optional[AlignmentType]) -> "MemorySectionBuilder":
        """Set alignment attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.alignment = value
        return self

    def with_executable_entities(self, items: list[ExecutableEntity]) -> "MemorySectionBuilder":
        """Set executable_entities list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.executable_entities = list(items) if items else []
        return self

    def with_options(self, items: list[Identifier]) -> "MemorySectionBuilder":
        """Set options list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.options = list(items) if items else []
        return self

    def with_prefix(self, value: Optional[SectionNamePrefix]) -> "MemorySectionBuilder":
        """Set prefix attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.prefix = value
        return self

    def with_size(self, value: Optional[PositiveInteger]) -> "MemorySectionBuilder":
        """Set size attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.size = value
        return self

    def with_sw_addrmethod(self, value: Optional[SwAddrMethod]) -> "MemorySectionBuilder":
        """Set sw_addrmethod attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_addrmethod = value
        return self

    def with_symbol(self, value: Optional[Identifier]) -> "MemorySectionBuilder":
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


    def add_executable_entity(self, item: ExecutableEntity) -> "MemorySectionBuilder":
        """Add a single item to executable_entities list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.executable_entities.append(item)
        return self

    def clear_executable_entities(self) -> "MemorySectionBuilder":
        """Clear all items from executable_entities list.

        Returns:
            self for method chaining
        """
        self._obj.executable_entities = []
        return self

    def add_option(self, item: Identifier) -> "MemorySectionBuilder":
        """Add a single item to options list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.options.append(item)
        return self

    def clear_options(self) -> "MemorySectionBuilder":
        """Clear all items from options list.

        Returns:
            self for method chaining
        """
        self._obj.options = []
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


    def build(self) -> MemorySection:
        """Build and return the MemorySection instance with validation."""
        self._validate_instance()
        pass
        return self._obj