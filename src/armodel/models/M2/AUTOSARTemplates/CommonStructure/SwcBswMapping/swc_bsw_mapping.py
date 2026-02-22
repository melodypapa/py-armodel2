"""SwcBswMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 110)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 656)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 217)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_SwcBswMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_internal_behavior import (
    BswInternalBehavior,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.SwcBswMapping.swc_bsw_runnable_mapping import (
    SwcBswRunnableMapping,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.swc_internal_behavior import (
    SwcInternalBehavior,
)


class SwcBswMapping(ARElement):
    """AUTOSAR SwcBswMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    bsw_behavior_ref: Optional[ARRef]
    runnable_mapping_refs: list[ARRef]
    swc_behavior_ref: Optional[ARRef]
    synchronizeds: list[Any]
    def __init__(self) -> None:
        """Initialize SwcBswMapping."""
        super().__init__()
        self.bsw_behavior_ref: Optional[ARRef] = None
        self.runnable_mapping_refs: list[ARRef] = []
        self.swc_behavior_ref: Optional[ARRef] = None
        self.synchronizeds: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize SwcBswMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwcBswMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize bsw_behavior_ref
        if self.bsw_behavior_ref is not None:
            serialized = SerializationHelper.serialize_item(self.bsw_behavior_ref, "BswInternalBehavior")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BSW-BEHAVIOR-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize runnable_mapping_refs (list to container "RUNNABLE-MAPPING-REFS")
        if self.runnable_mapping_refs:
            wrapper = ET.Element("RUNNABLE-MAPPING-REFS")
            for item in self.runnable_mapping_refs:
                serialized = SerializationHelper.serialize_item(item, "SwcBswRunnableMapping")
                if serialized is not None:
                    child_elem = ET.Element("RUNNABLE-MAPPING-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize swc_behavior_ref
        if self.swc_behavior_ref is not None:
            serialized = SerializationHelper.serialize_item(self.swc_behavior_ref, "SwcInternalBehavior")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SWC-BEHAVIOR-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize synchronizeds (list to container "SYNCHRONIZEDS")
        if self.synchronizeds:
            wrapper = ET.Element("SYNCHRONIZEDS")
            for item in self.synchronizeds:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwcBswMapping":
        """Deserialize XML element to SwcBswMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwcBswMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwcBswMapping, cls).deserialize(element)

        # Parse bsw_behavior_ref
        child = SerializationHelper.find_child_element(element, "BSW-BEHAVIOR-REF")
        if child is not None:
            bsw_behavior_ref_value = ARRef.deserialize(child)
            obj.bsw_behavior_ref = bsw_behavior_ref_value

        # Parse runnable_mapping_refs (list from container "RUNNABLE-MAPPING-REFS")
        obj.runnable_mapping_refs = []
        container = SerializationHelper.find_child_element(element, "RUNNABLE-MAPPING-REFS")
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
                    obj.runnable_mapping_refs.append(child_value)

        # Parse swc_behavior_ref
        child = SerializationHelper.find_child_element(element, "SWC-BEHAVIOR-REF")
        if child is not None:
            swc_behavior_ref_value = ARRef.deserialize(child)
            obj.swc_behavior_ref = swc_behavior_ref_value

        # Parse synchronizeds (list from container "SYNCHRONIZEDS")
        obj.synchronizeds = []
        container = SerializationHelper.find_child_element(element, "SYNCHRONIZEDS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.synchronizeds.append(child_value)

        return obj



class SwcBswMappingBuilder:
    """Builder for SwcBswMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: SwcBswMapping = SwcBswMapping()


    def with_short_name(self, value: Identifier) -> "SwcBswMappingBuilder":
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

    def with_short_name_fragments(self, items: list[ShortNameFragment]) -> "SwcBswMappingBuilder":
        """Set short_name_fragments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = list(items) if items else []
        return self

    def with_long_name(self, value: Optional[MultilanguageLongName]) -> "SwcBswMappingBuilder":
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

    def with_admin_data(self, value: Optional[AdminData]) -> "SwcBswMappingBuilder":
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

    def with_annotations(self, items: list[Annotation]) -> "SwcBswMappingBuilder":
        """Set annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.annotations = list(items) if items else []
        return self

    def with_desc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "SwcBswMappingBuilder":
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

    def with_category(self, value: Optional[CategoryString]) -> "SwcBswMappingBuilder":
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

    def with_introduction(self, value: Optional[DocumentationBlock]) -> "SwcBswMappingBuilder":
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

    def with_uuid(self, value: Optional[String]) -> "SwcBswMappingBuilder":
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

    def with_bsw_behavior(self, value: Optional[BswInternalBehavior]) -> "SwcBswMappingBuilder":
        """Set bsw_behavior attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.bsw_behavior = value
        return self

    def with_runnable_mappings(self, items: list[SwcBswRunnableMapping]) -> "SwcBswMappingBuilder":
        """Set runnable_mappings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.runnable_mappings = list(items) if items else []
        return self

    def with_swc_behavior(self, value: Optional[SwcInternalBehavior]) -> "SwcBswMappingBuilder":
        """Set swc_behavior attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.swc_behavior = value
        return self

    def with_synchronizeds(self, items: list[any (SwcBswSynchronized)]) -> "SwcBswMappingBuilder":
        """Set synchronizeds list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.synchronizeds = list(items) if items else []
        return self


    def add_short_name_fragment(self, item: ShortNameFragment) -> "SwcBswMappingBuilder":
        """Add a single item to short_name_fragments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments.append(item)
        return self

    def clear_short_name_fragments(self) -> "SwcBswMappingBuilder":
        """Clear all items from short_name_fragments list.

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = []
        return self

    def add_annotation(self, item: Annotation) -> "SwcBswMappingBuilder":
        """Add a single item to annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.annotations.append(item)
        return self

    def clear_annotations(self) -> "SwcBswMappingBuilder":
        """Clear all items from annotations list.

        Returns:
            self for method chaining
        """
        self._obj.annotations = []
        return self

    def add_runnable_mapping(self, item: SwcBswRunnableMapping) -> "SwcBswMappingBuilder":
        """Add a single item to runnable_mappings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.runnable_mappings.append(item)
        return self

    def clear_runnable_mappings(self) -> "SwcBswMappingBuilder":
        """Clear all items from runnable_mappings list.

        Returns:
            self for method chaining
        """
        self._obj.runnable_mappings = []
        return self

    def add_synchronized(self, item: any (SwcBswSynchronized)) -> "SwcBswMappingBuilder":
        """Add a single item to synchronizeds list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.synchronizeds.append(item)
        return self

    def clear_synchronizeds(self) -> "SwcBswMappingBuilder":
        """Clear all items from synchronizeds list.

        Returns:
            self for method chaining
        """
        self._obj.synchronizeds = []
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


    def build(self) -> SwcBswMapping:
        """Build and return the SwcBswMapping instance with validation."""
        self._validate_instance()
        pass
        return self._obj