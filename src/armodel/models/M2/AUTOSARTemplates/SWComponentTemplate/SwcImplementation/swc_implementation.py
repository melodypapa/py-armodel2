"""SwcImplementation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 344)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 623)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2069)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcImplementation.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization.decorators import xml_element_name

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation.implementation import (
    Implementation,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PerInstanceMemory.per_instance_memory import (
    PerInstanceMemory,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.swc_internal_behavior import (
    SwcInternalBehavior,
)


class SwcImplementation(Implementation):
    """AUTOSAR SwcImplementation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    behavior_ref: Optional[ARRef]
    _per_instance_memories: list[PerInstanceMemory]
    required: Optional[String]
    def __init__(self) -> None:
        """Initialize SwcImplementation."""
        super().__init__()
        self.behavior_ref: Optional[ARRef] = None
        self._per_instance_memories: list[PerInstanceMemory] = []
        self.required: Optional[String] = None
    @property
    @xml_element_name("PER-INSTANCE-MEMORYS")
    def per_instance_memories(self) -> list[PerInstanceMemory]:
        """Get per_instance_memories with custom XML element name."""
        return self._per_instance_memories

    @per_instance_memories.setter
    def per_instance_memories(self, value: list[PerInstanceMemory]) -> None:
        """Set per_instance_memories with custom XML element name."""
        self._per_instance_memories = value


    def serialize(self) -> ET.Element:
        """Serialize SwcImplementation to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwcImplementation, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize behavior_ref
        if self.behavior_ref is not None:
            serialized = SerializationHelper.serialize_item(self.behavior_ref, "SwcInternalBehavior")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BEHAVIOR-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize per_instance_memories (list to container "PER-INSTANCE-MEMORYS")
        if self.per_instance_memories:
            wrapper = ET.Element("PER-INSTANCE-MEMORYS")
            for item in self.per_instance_memories:
                serialized = SerializationHelper.serialize_item(item, "PerInstanceMemory")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize required
        if self.required is not None:
            serialized = SerializationHelper.serialize_item(self.required, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REQUIRED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwcImplementation":
        """Deserialize XML element to SwcImplementation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwcImplementation object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwcImplementation, cls).deserialize(element)

        # Parse behavior_ref
        child = SerializationHelper.find_child_element(element, "BEHAVIOR-REF")
        if child is not None:
            behavior_ref_value = ARRef.deserialize(child)
            obj.behavior_ref = behavior_ref_value

        # Parse per_instance_memories (list from container "PER-INSTANCE-MEMORYS")
        obj.per_instance_memories = []
        container = SerializationHelper.find_child_element(element, "PER-INSTANCE-MEMORYS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.per_instance_memories.append(child_value)

        # Parse required
        child = SerializationHelper.find_child_element(element, "REQUIRED")
        if child is not None:
            required_value = child.text
            obj.required = required_value

        return obj



class SwcImplementationBuilder:
    """Builder for SwcImplementation with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: SwcImplementation = SwcImplementation()


    def with_short_name(self, value: Identifier) -> "SwcImplementationBuilder":
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

    def with_short_name_fragments(self, items: list[ShortNameFragment]) -> "SwcImplementationBuilder":
        """Set short_name_fragments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = list(items) if items else []
        return self

    def with_long_name(self, value: Optional[MultilanguageLongName]) -> "SwcImplementationBuilder":
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

    def with_admin_data(self, value: Optional[AdminData]) -> "SwcImplementationBuilder":
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

    def with_annotations(self, items: list[Annotation]) -> "SwcImplementationBuilder":
        """Set annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.annotations = list(items) if items else []
        return self

    def with_desc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "SwcImplementationBuilder":
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

    def with_category(self, value: Optional[CategoryString]) -> "SwcImplementationBuilder":
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

    def with_introduction(self, value: Optional[DocumentationBlock]) -> "SwcImplementationBuilder":
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

    def with_uuid(self, value: Optional[String]) -> "SwcImplementationBuilder":
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

    def with_build_action_manifest(self, value: Optional[BuildActionManifest]) -> "SwcImplementationBuilder":
        """Set build_action_manifest attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.build_action_manifest = value
        return self

    def with_code_descriptors(self, items: list[Code]) -> "SwcImplementationBuilder":
        """Set code_descriptors list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.code_descriptors = list(items) if items else []
        return self

    def with_compilers(self, items: list[Compiler]) -> "SwcImplementationBuilder":
        """Set compilers list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.compilers = list(items) if items else []
        return self

    def with_generated_artifacts(self, items: list[DependencyOnArtifact]) -> "SwcImplementationBuilder":
        """Set generated_artifacts list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.generated_artifacts = list(items) if items else []
        return self

    def with_hw_elements(self, items: list[HwElement]) -> "SwcImplementationBuilder":
        """Set hw_elements list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.hw_elements = list(items) if items else []
        return self

    def with_linkers(self, items: list[Linker]) -> "SwcImplementationBuilder":
        """Set linkers list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.linkers = list(items) if items else []
        return self

    def with_mc_support(self, value: Optional[McSupportData]) -> "SwcImplementationBuilder":
        """Set mc_support attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.mc_support = value
        return self

    def with_programming_language(self, value: Optional[ProgramminglanguageEnum]) -> "SwcImplementationBuilder":
        """Set programming_language attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.programming_language = value
        return self

    def with_required_artifacts(self, items: list[DependencyOnArtifact]) -> "SwcImplementationBuilder":
        """Set required_artifacts list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.required_artifacts = list(items) if items else []
        return self

    def with_required_generator_tools(self, items: list[DependencyOnArtifact]) -> "SwcImplementationBuilder":
        """Set required_generator_tools list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.required_generator_tools = list(items) if items else []
        return self

    def with_resource_consumption(self, value: Optional[ResourceConsumption]) -> "SwcImplementationBuilder":
        """Set resource_consumption attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.resource_consumption = value
        return self

    def with_swc_bsw_mapping(self, value: Optional[SwcBswMapping]) -> "SwcImplementationBuilder":
        """Set swc_bsw_mapping attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.swc_bsw_mapping = value
        return self

    def with_sw_version(self, value: Optional[RevisionLabelString]) -> "SwcImplementationBuilder":
        """Set sw_version attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_version = value
        return self

    def with_used_code_generator(self, value: Optional[String]) -> "SwcImplementationBuilder":
        """Set used_code_generator attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.used_code_generator = value
        return self

    def with_vendor_id(self, value: Optional[PositiveInteger]) -> "SwcImplementationBuilder":
        """Set vendor_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.vendor_id = value
        return self

    def with_behavior(self, value: Optional[SwcInternalBehavior]) -> "SwcImplementationBuilder":
        """Set behavior attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.behavior = value
        return self

    def with_per_instance_memories(self, items: list[PerInstanceMemory]) -> "SwcImplementationBuilder":
        """Set per_instance_memories list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.per_instance_memories = list(items) if items else []
        return self

    def with_required(self, value: Optional[String]) -> "SwcImplementationBuilder":
        """Set required attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.required = value
        return self


    def add_short_name_fragment(self, item: ShortNameFragment) -> "SwcImplementationBuilder":
        """Add a single item to short_name_fragments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments.append(item)
        return self

    def clear_short_name_fragments(self) -> "SwcImplementationBuilder":
        """Clear all items from short_name_fragments list.

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = []
        return self

    def add_annotation(self, item: Annotation) -> "SwcImplementationBuilder":
        """Add a single item to annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.annotations.append(item)
        return self

    def clear_annotations(self) -> "SwcImplementationBuilder":
        """Clear all items from annotations list.

        Returns:
            self for method chaining
        """
        self._obj.annotations = []
        return self

    def add_code_descriptor(self, item: Code) -> "SwcImplementationBuilder":
        """Add a single item to code_descriptors list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.code_descriptors.append(item)
        return self

    def clear_code_descriptors(self) -> "SwcImplementationBuilder":
        """Clear all items from code_descriptors list.

        Returns:
            self for method chaining
        """
        self._obj.code_descriptors = []
        return self

    def add_compiler(self, item: Compiler) -> "SwcImplementationBuilder":
        """Add a single item to compilers list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.compilers.append(item)
        return self

    def clear_compilers(self) -> "SwcImplementationBuilder":
        """Clear all items from compilers list.

        Returns:
            self for method chaining
        """
        self._obj.compilers = []
        return self

    def add_generated_artifact(self, item: DependencyOnArtifact) -> "SwcImplementationBuilder":
        """Add a single item to generated_artifacts list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.generated_artifacts.append(item)
        return self

    def clear_generated_artifacts(self) -> "SwcImplementationBuilder":
        """Clear all items from generated_artifacts list.

        Returns:
            self for method chaining
        """
        self._obj.generated_artifacts = []
        return self

    def add_hw_element(self, item: HwElement) -> "SwcImplementationBuilder":
        """Add a single item to hw_elements list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.hw_elements.append(item)
        return self

    def clear_hw_elements(self) -> "SwcImplementationBuilder":
        """Clear all items from hw_elements list.

        Returns:
            self for method chaining
        """
        self._obj.hw_elements = []
        return self

    def add_linker(self, item: Linker) -> "SwcImplementationBuilder":
        """Add a single item to linkers list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.linkers.append(item)
        return self

    def clear_linkers(self) -> "SwcImplementationBuilder":
        """Clear all items from linkers list.

        Returns:
            self for method chaining
        """
        self._obj.linkers = []
        return self

    def add_required_artifact(self, item: DependencyOnArtifact) -> "SwcImplementationBuilder":
        """Add a single item to required_artifacts list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.required_artifacts.append(item)
        return self

    def clear_required_artifacts(self) -> "SwcImplementationBuilder":
        """Clear all items from required_artifacts list.

        Returns:
            self for method chaining
        """
        self._obj.required_artifacts = []
        return self

    def add_required_generator_tool(self, item: DependencyOnArtifact) -> "SwcImplementationBuilder":
        """Add a single item to required_generator_tools list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.required_generator_tools.append(item)
        return self

    def clear_required_generator_tools(self) -> "SwcImplementationBuilder":
        """Clear all items from required_generator_tools list.

        Returns:
            self for method chaining
        """
        self._obj.required_generator_tools = []
        return self

    def add_per_instance_memorie(self, item: PerInstanceMemory) -> "SwcImplementationBuilder":
        """Add a single item to per_instance_memories list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.per_instance_memories.append(item)
        return self

    def clear_per_instance_memories(self) -> "SwcImplementationBuilder":
        """Clear all items from per_instance_memories list.

        Returns:
            self for method chaining
        """
        self._obj.per_instance_memories = []
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


    def build(self) -> SwcImplementation:
        """Build and return the SwcImplementation instance with validation."""
        self._validate_instance()
        pass
        return self._obj