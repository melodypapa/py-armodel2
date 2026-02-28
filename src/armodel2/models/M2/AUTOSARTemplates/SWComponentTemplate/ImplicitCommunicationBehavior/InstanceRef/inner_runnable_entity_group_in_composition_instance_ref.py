"""InnerRunnableEntityGroupInCompositionInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 956)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_ImplicitCommunicationBehavior_InstanceRef.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.composition_sw_component_type import (
    CompositionSwComponentType,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior.runnable_entity_group import (
    RunnableEntityGroup,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class InnerRunnableEntityGroupInCompositionInstanceRef(ARObject):
    """AUTOSAR InnerRunnableEntityGroupInCompositionInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "INNER-RUNNABLE-ENTITY-GROUP-IN-COMPOSITION-INSTANCE-REF"


    base_ref: Optional[ARRef]
    context_sw_refs: list[Any]
    target_runnable_ref: ARRef
    _DESERIALIZE_DISPATCH = {
        "BASE-REF": lambda obj, elem: setattr(obj, "base_ref", ARRef.deserialize(elem)),
        "CONTEXT-SWS": lambda obj, elem: obj.context_sw_refs.append(ARRef.deserialize(elem)),
        "TARGET-RUNNABLE-REF": lambda obj, elem: setattr(obj, "target_runnable_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize InnerRunnableEntityGroupInCompositionInstanceRef."""
        super().__init__()
        self.base_ref: Optional[ARRef] = None
        self.context_sw_refs: list[Any] = []
        self.target_runnable_ref: ARRef = None

    def serialize(self) -> ET.Element:
        """Serialize InnerRunnableEntityGroupInCompositionInstanceRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(InnerRunnableEntityGroupInCompositionInstanceRef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize base_ref
        if self.base_ref is not None:
            serialized = SerializationHelper.serialize_item(self.base_ref, "CompositionSwComponentType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BASE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize context_sw_refs (list to container "CONTEXT-SW-REFS")
        if self.context_sw_refs:
            wrapper = ET.Element("CONTEXT-SW-REFS")
            for item in self.context_sw_refs:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("CONTEXT-SW-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize target_runnable_ref
        if self.target_runnable_ref is not None:
            serialized = SerializationHelper.serialize_item(self.target_runnable_ref, "RunnableEntityGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-RUNNABLE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "InnerRunnableEntityGroupInCompositionInstanceRef":
        """Deserialize XML element to InnerRunnableEntityGroupInCompositionInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized InnerRunnableEntityGroupInCompositionInstanceRef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(InnerRunnableEntityGroupInCompositionInstanceRef, cls).deserialize(element)

        # Parse base_ref
        child = SerializationHelper.find_child_element(element, "BASE-REF")
        if child is not None:
            base_ref_value = ARRef.deserialize(child)
            obj.base_ref = base_ref_value

        # Parse context_sw_refs (list from container "CONTEXT-SW-REFS")
        obj.context_sw_refs = []
        container = SerializationHelper.find_child_element(element, "CONTEXT-SW-REFS")
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
                    obj.context_sw_refs.append(child_value)

        # Parse target_runnable_ref
        child = SerializationHelper.find_child_element(element, "TARGET-RUNNABLE-REF")
        if child is not None:
            target_runnable_ref_value = ARRef.deserialize(child)
            obj.target_runnable_ref = target_runnable_ref_value

        return obj



class InnerRunnableEntityGroupInCompositionInstanceRefBuilder(BuilderBase):
    """Builder for InnerRunnableEntityGroupInCompositionInstanceRef with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: InnerRunnableEntityGroupInCompositionInstanceRef = InnerRunnableEntityGroupInCompositionInstanceRef()


    def with_base(self, value: Optional[CompositionSwComponentType]) -> "InnerRunnableEntityGroupInCompositionInstanceRefBuilder":
        """Set base attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.base = value
        return self

    def with_context_sws(self, items: list[any (SwComponent)]) -> "InnerRunnableEntityGroupInCompositionInstanceRefBuilder":
        """Set context_sws list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.context_sws = list(items) if items else []
        return self

    def with_target_runnable(self, value: RunnableEntityGroup) -> "InnerRunnableEntityGroupInCompositionInstanceRefBuilder":
        """Set target_runnable attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.target_runnable = value
        return self


    def add_context_sw(self, item: any (SwComponent)) -> "InnerRunnableEntityGroupInCompositionInstanceRefBuilder":
        """Add a single item to context_sws list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.context_sws.append(item)
        return self

    def clear_context_sws(self) -> "InnerRunnableEntityGroupInCompositionInstanceRefBuilder":
        """Clear all items from context_sws list.

        Returns:
            self for method chaining
        """
        self._obj.context_sws = []
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


    def build(self) -> InnerRunnableEntityGroupInCompositionInstanceRef:
        """Build and return the InnerRunnableEntityGroupInCompositionInstanceRef instance with validation."""
        self._validate_instance()
        pass
        return self._obj