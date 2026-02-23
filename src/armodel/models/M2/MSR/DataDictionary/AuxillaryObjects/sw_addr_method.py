"""SwAddrMethod AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 144)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 413)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 209)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_AuxillaryObjects.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel.models.M2.MSR.DataDictionary.AuxillaryObjects import (
    MemoryAllocationKeywordPolicyType,
    MemorySectionType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    SectionInitializationPolicyType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class SwAddrMethod(ARElement):
    """AUTOSAR SwAddrMethod."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    memory: Optional[MemoryAllocationKeywordPolicyType]
    options: list[Identifier]
    section: Optional[SectionInitializationPolicyType]
    section_type: Optional[MemorySectionType]
    def __init__(self) -> None:
        """Initialize SwAddrMethod."""
        super().__init__()
        self.memory: Optional[MemoryAllocationKeywordPolicyType] = None
        self.options: list[Identifier] = []
        self.section: Optional[SectionInitializationPolicyType] = None
        self.section_type: Optional[MemorySectionType] = None

    def serialize(self) -> ET.Element:
        """Serialize SwAddrMethod to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwAddrMethod, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize memory
        if self.memory is not None:
            serialized = SerializationHelper.serialize_item(self.memory, "MemoryAllocationKeywordPolicyType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MEMORY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

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

        # Serialize section
        if self.section is not None:
            serialized = SerializationHelper.serialize_item(self.section, "SectionInitializationPolicyType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SECTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize section_type
        if self.section_type is not None:
            serialized = SerializationHelper.serialize_item(self.section_type, "MemorySectionType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SECTION-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwAddrMethod":
        """Deserialize XML element to SwAddrMethod object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwAddrMethod object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwAddrMethod, cls).deserialize(element)

        # Parse memory
        child = SerializationHelper.find_child_element(element, "MEMORY")
        if child is not None:
            memory_value = MemoryAllocationKeywordPolicyType.deserialize(child)
            obj.memory = memory_value

        # Parse options (list from container "OPTIONS")
        obj.options = []
        container = SerializationHelper.find_child_element(element, "OPTIONS")
        if container is not None:
            for child in container:
                # Extract primitive value (Identifier) as text
                child_value = child.text
                if child_value is not None:
                    obj.options.append(child_value)

        # Parse section
        child = SerializationHelper.find_child_element(element, "SECTION")
        if child is not None:
            section_value = child.text
            obj.section = section_value

        # Parse section_type
        child = SerializationHelper.find_child_element(element, "SECTION-TYPE")
        if child is not None:
            section_type_value = MemorySectionType.deserialize(child)
            obj.section_type = section_type_value

        return obj



class SwAddrMethodBuilder(ARElementBuilder):
    """Builder for SwAddrMethod with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SwAddrMethod = SwAddrMethod()


    def with_memory(self, value: Optional[MemoryAllocationKeywordPolicyType]) -> "SwAddrMethodBuilder":
        """Set memory attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.memory = value
        return self

    def with_options(self, items: list[Identifier]) -> "SwAddrMethodBuilder":
        """Set options list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.options = list(items) if items else []
        return self

    def with_section(self, value: Optional[SectionInitializationPolicyType]) -> "SwAddrMethodBuilder":
        """Set section attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.section = value
        return self

    def with_section_type(self, value: Optional[MemorySectionType]) -> "SwAddrMethodBuilder":
        """Set section_type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.section_type = value
        return self


    def add_option(self, item: Identifier) -> "SwAddrMethodBuilder":
        """Add a single item to options list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.options.append(item)
        return self

    def clear_options(self) -> "SwAddrMethodBuilder":
        """Clear all items from options list.

        Returns:
            self for method chaining
        """
        self._obj.options = []
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


    def build(self) -> SwAddrMethod:
        """Build and return the SwAddrMethod instance with validation."""
        self._validate_instance()
        pass
        return self._obj