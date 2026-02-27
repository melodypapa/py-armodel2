"""RunnableEntityGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 222)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 206)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_ImplicitCommunicationBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.runnable_entity import (
        RunnableEntity,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class RunnableEntityGroup(Identifiable):
    """AUTOSAR RunnableEntityGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    runnable_entities: list[RunnableEntity]
    runnable_entity_group_group_in_composition_instance_ref: list[ARRef]
    def __init__(self) -> None:
        """Initialize RunnableEntityGroup."""
        super().__init__()
        self.runnable_entities: list[RunnableEntity] = []
        self.runnable_entity_group_group_in_composition_instance_ref: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize RunnableEntityGroup to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RunnableEntityGroup, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize runnable_entities (list to container "RUNNABLE-ENTITYS")
        if self.runnable_entities:
            wrapper = ET.Element("RUNNABLE-ENTITYS")
            for item in self.runnable_entities:
                serialized = SerializationHelper.serialize_item(item, "RunnableEntity")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize runnable_entity_group_group_in_composition_instance_ref (list to container "RUNNABLE-ENTITY-GROUP-GROUP-IN-COMPOSITION-INSTANCE-REFS")
        if self.runnable_entity_group_group_in_composition_instance_ref:
            wrapper = ET.Element("RUNNABLE-ENTITY-GROUP-GROUP-IN-COMPOSITION-INSTANCE-REFS")
            for item in self.runnable_entity_group_group_in_composition_instance_ref:
                serialized = SerializationHelper.serialize_item(item, "RunnableEntityGroup")
                if serialized is not None:
                    child_elem = ET.Element("RUNNABLE-ENTITY-GROUP-GROUP-IN-COMPOSITION-INSTANCE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RunnableEntityGroup":
        """Deserialize XML element to RunnableEntityGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RunnableEntityGroup object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RunnableEntityGroup, cls).deserialize(element)

        # Parse runnable_entities (list from container "RUNNABLE-ENTITYS")
        obj.runnable_entities = []
        container = SerializationHelper.find_child_element(element, "RUNNABLE-ENTITYS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.runnable_entities.append(child_value)

        # Parse runnable_entity_group_group_in_composition_instance_ref (list from container "RUNNABLE-ENTITY-GROUP-GROUP-IN-COMPOSITION-INSTANCE-REFS")
        obj.runnable_entity_group_group_in_composition_instance_ref = []
        container = SerializationHelper.find_child_element(element, "RUNNABLE-ENTITY-GROUP-GROUP-IN-COMPOSITION-INSTANCE-REFS")
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
                    obj.runnable_entity_group_group_in_composition_instance_ref.append(child_value)

        return obj



class RunnableEntityGroupBuilder(IdentifiableBuilder):
    """Builder for RunnableEntityGroup with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: RunnableEntityGroup = RunnableEntityGroup()


    def with_runnable_entities(self, items: list[RunnableEntity]) -> "RunnableEntityGroupBuilder":
        """Set runnable_entities list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.runnable_entities = list(items) if items else []
        return self

    def with_runnable_entity_group_group_in_composition_instance_refs(self, items: list[RunnableEntityGroup]) -> "RunnableEntityGroupBuilder":
        """Set runnable_entity_group_group_in_composition_instance_refs list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.runnable_entity_group_group_in_composition_instance_refs = list(items) if items else []
        return self


    def add_runnable_entity(self, item: RunnableEntity) -> "RunnableEntityGroupBuilder":
        """Add a single item to runnable_entities list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.runnable_entities.append(item)
        return self

    def clear_runnable_entities(self) -> "RunnableEntityGroupBuilder":
        """Clear all items from runnable_entities list.

        Returns:
            self for method chaining
        """
        self._obj.runnable_entities = []
        return self

    def add_runnable_entity_group_group_in_composition_instance_ref(self, item: RunnableEntityGroup) -> "RunnableEntityGroupBuilder":
        """Add a single item to runnable_entity_group_group_in_composition_instance_refs list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.runnable_entity_group_group_in_composition_instance_refs.append(item)
        return self

    def clear_runnable_entity_group_group_in_composition_instance_refs(self) -> "RunnableEntityGroupBuilder":
        """Clear all items from runnable_entity_group_group_in_composition_instance_refs list.

        Returns:
            self for method chaining
        """
        self._obj.runnable_entity_group_group_in_composition_instance_refs = []
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


    def build(self) -> RunnableEntityGroup:
        """Build and return the RunnableEntityGroup instance with validation."""
        self._validate_instance()
        pass
        return self._obj