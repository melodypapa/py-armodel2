"""LifeCycleInfoSet AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 391)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 195)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_LifeCycles.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel2.serialization.decorators import xml_element_name

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles.life_cycle_info import (
    LifeCycleInfo,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles.life_cycle_period import (
    LifeCyclePeriod,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles.life_cycle_state import (
    LifeCycleState,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles.life_cycle_state_definition_group import (
    LifeCycleStateDefinitionGroup,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class LifeCycleInfoSet(ARElement):
    """AUTOSAR LifeCycleInfoSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    default_lc_state_ref: ARRef
    default_period_begin: Optional[LifeCyclePeriod]
    default_period_end: Optional[LifeCyclePeriod]
    _life_cycle_infoes: list[LifeCycleInfo]
    used_life_cycle_state_definition_group_ref: ARRef
    def __init__(self) -> None:
        """Initialize LifeCycleInfoSet."""
        super().__init__()
        self.default_lc_state_ref: ARRef = None
        self.default_period_begin: Optional[LifeCyclePeriod] = None
        self.default_period_end: Optional[LifeCyclePeriod] = None
        self._life_cycle_infoes: list[LifeCycleInfo] = []
        self.used_life_cycle_state_definition_group_ref: ARRef = None
    @property
    @xml_element_name("LIFE-CYCLE-INFOS")
    def life_cycle_infoes(self) -> list[LifeCycleInfo]:
        """Get life_cycle_infoes with custom XML element name."""
        return self._life_cycle_infoes

    @life_cycle_infoes.setter
    def life_cycle_infoes(self, value: list[LifeCycleInfo]) -> None:
        """Set life_cycle_infoes with custom XML element name."""
        self._life_cycle_infoes = value


    def serialize(self) -> ET.Element:
        """Serialize LifeCycleInfoSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(LifeCycleInfoSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize default_lc_state_ref
        if self.default_lc_state_ref is not None:
            serialized = SerializationHelper.serialize_item(self.default_lc_state_ref, "LifeCycleState")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEFAULT-LC-STATE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize default_period_begin
        if self.default_period_begin is not None:
            serialized = SerializationHelper.serialize_item(self.default_period_begin, "LifeCyclePeriod")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEFAULT-PERIOD-BEGIN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize default_period_end
        if self.default_period_end is not None:
            serialized = SerializationHelper.serialize_item(self.default_period_end, "LifeCyclePeriod")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEFAULT-PERIOD-END")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize life_cycle_infoes (list to container "LIFE-CYCLE-INFOS")
        if self.life_cycle_infoes:
            wrapper = ET.Element("LIFE-CYCLE-INFOS")
            for item in self.life_cycle_infoes:
                serialized = SerializationHelper.serialize_item(item, "LifeCycleInfo")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize used_life_cycle_state_definition_group_ref
        if self.used_life_cycle_state_definition_group_ref is not None:
            serialized = SerializationHelper.serialize_item(self.used_life_cycle_state_definition_group_ref, "LifeCycleStateDefinitionGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("USED-LIFE-CYCLE-STATE-DEFINITION-GROUP-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LifeCycleInfoSet":
        """Deserialize XML element to LifeCycleInfoSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LifeCycleInfoSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(LifeCycleInfoSet, cls).deserialize(element)

        # Parse default_lc_state_ref
        child = SerializationHelper.find_child_element(element, "DEFAULT-LC-STATE-REF")
        if child is not None:
            default_lc_state_ref_value = ARRef.deserialize(child)
            obj.default_lc_state_ref = default_lc_state_ref_value

        # Parse default_period_begin
        child = SerializationHelper.find_child_element(element, "DEFAULT-PERIOD-BEGIN")
        if child is not None:
            default_period_begin_value = SerializationHelper.deserialize_by_tag(child, "LifeCyclePeriod")
            obj.default_period_begin = default_period_begin_value

        # Parse default_period_end
        child = SerializationHelper.find_child_element(element, "DEFAULT-PERIOD-END")
        if child is not None:
            default_period_end_value = SerializationHelper.deserialize_by_tag(child, "LifeCyclePeriod")
            obj.default_period_end = default_period_end_value

        # Parse life_cycle_infoes (list from container "LIFE-CYCLE-INFOS")
        obj.life_cycle_infoes = []
        container = SerializationHelper.find_child_element(element, "LIFE-CYCLE-INFOS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.life_cycle_infoes.append(child_value)

        # Parse used_life_cycle_state_definition_group_ref
        child = SerializationHelper.find_child_element(element, "USED-LIFE-CYCLE-STATE-DEFINITION-GROUP-REF")
        if child is not None:
            used_life_cycle_state_definition_group_ref_value = ARRef.deserialize(child)
            obj.used_life_cycle_state_definition_group_ref = used_life_cycle_state_definition_group_ref_value

        return obj



class LifeCycleInfoSetBuilder(ARElementBuilder):
    """Builder for LifeCycleInfoSet with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: LifeCycleInfoSet = LifeCycleInfoSet()


    def with_default_lc_state(self, value: LifeCycleState) -> "LifeCycleInfoSetBuilder":
        """Set default_lc_state attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.default_lc_state = value
        return self

    def with_default_period_begin(self, value: Optional[LifeCyclePeriod]) -> "LifeCycleInfoSetBuilder":
        """Set default_period_begin attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.default_period_begin = value
        return self

    def with_default_period_end(self, value: Optional[LifeCyclePeriod]) -> "LifeCycleInfoSetBuilder":
        """Set default_period_end attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.default_period_end = value
        return self

    def with_life_cycle_infoes(self, items: list[LifeCycleInfo]) -> "LifeCycleInfoSetBuilder":
        """Set life_cycle_infoes list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.life_cycle_infoes = list(items) if items else []
        return self

    def with_used_life_cycle_state_definition_group(self, value: LifeCycleStateDefinitionGroup) -> "LifeCycleInfoSetBuilder":
        """Set used_life_cycle_state_definition_group attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.used_life_cycle_state_definition_group = value
        return self


    def add_life_cycle_info(self, item: LifeCycleInfo) -> "LifeCycleInfoSetBuilder":
        """Add a single item to life_cycle_infoes list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.life_cycle_infoes.append(item)
        return self

    def clear_life_cycle_infoes(self) -> "LifeCycleInfoSetBuilder":
        """Clear all items from life_cycle_infoes list.

        Returns:
            self for method chaining
        """
        self._obj.life_cycle_infoes = []
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


    def build(self) -> LifeCycleInfoSet:
        """Build and return the LifeCycleInfoSet instance with validation."""
        self._validate_instance()
        pass
        return self._obj