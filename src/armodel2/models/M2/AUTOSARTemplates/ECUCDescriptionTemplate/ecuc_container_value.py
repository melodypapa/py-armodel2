"""EcucContainerValue AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 119)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2021)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 439)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 185)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCDescriptionTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_container_def import (
    EcucContainerDef,
)
from armodel2.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_parameter_value import (
    EcucParameterValue,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class EcucContainerValue(Identifiable):
    """AUTOSAR EcucContainerValue."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    definition_ref: Optional[ARRef]
    parameter_values: list[EcucParameterValue]
    reference_value_refs: list[Any]
    sub_containers: list[EcucContainerValue]
    def __init__(self) -> None:
        """Initialize EcucContainerValue."""
        super().__init__()
        self.definition_ref: Optional[ARRef] = None
        self.parameter_values: list[EcucParameterValue] = []
        self.reference_value_refs: list[Any] = []
        self.sub_containers: list[EcucContainerValue] = []

    def serialize(self) -> ET.Element:
        """Serialize EcucContainerValue to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucContainerValue, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize definition_ref
        if self.definition_ref is not None:
            serialized = SerializationHelper.serialize_item(self.definition_ref, "EcucContainerDef")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEFINITION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize parameter_values (list to container "PARAMETER-VALUES")
        if self.parameter_values:
            wrapper = ET.Element("PARAMETER-VALUES")
            for item in self.parameter_values:
                serialized = SerializationHelper.serialize_item(item, "EcucParameterValue")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize reference_value_refs (list to container "REFERENCE-VALUE-REFS")
        if self.reference_value_refs:
            wrapper = ET.Element("REFERENCE-VALUE-REFS")
            for item in self.reference_value_refs:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("REFERENCE-VALUE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize sub_containers (list to container "SUB-CONTAINERS")
        if self.sub_containers:
            wrapper = ET.Element("SUB-CONTAINERS")
            for item in self.sub_containers:
                serialized = SerializationHelper.serialize_item(item, "EcucContainerValue")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucContainerValue":
        """Deserialize XML element to EcucContainerValue object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucContainerValue object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucContainerValue, cls).deserialize(element)

        # Parse definition_ref
        child = SerializationHelper.find_child_element(element, "DEFINITION-REF")
        if child is not None:
            definition_ref_value = ARRef.deserialize(child)
            obj.definition_ref = definition_ref_value

        # Parse parameter_values (list from container "PARAMETER-VALUES")
        obj.parameter_values = []
        container = SerializationHelper.find_child_element(element, "PARAMETER-VALUES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.parameter_values.append(child_value)

        # Parse reference_value_refs (list from container "REFERENCE-VALUE-REFS")
        obj.reference_value_refs = []
        container = SerializationHelper.find_child_element(element, "REFERENCE-VALUE-REFS")
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
                    obj.reference_value_refs.append(child_value)

        # Parse sub_containers (list from container "SUB-CONTAINERS")
        obj.sub_containers = []
        container = SerializationHelper.find_child_element(element, "SUB-CONTAINERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sub_containers.append(child_value)

        return obj



class EcucContainerValueBuilder(IdentifiableBuilder):
    """Builder for EcucContainerValue with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EcucContainerValue = EcucContainerValue()


    def with_definition(self, value: Optional[EcucContainerDef]) -> "EcucContainerValueBuilder":
        """Set definition attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.definition = value
        return self

    def with_parameter_values(self, items: list[EcucParameterValue]) -> "EcucContainerValueBuilder":
        """Set parameter_values list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.parameter_values = list(items) if items else []
        return self

    def with_reference_values(self, items: list[any (EcucAbstractReference)]) -> "EcucContainerValueBuilder":
        """Set reference_values list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.reference_values = list(items) if items else []
        return self

    def with_sub_containers(self, items: list[EcucContainerValue]) -> "EcucContainerValueBuilder":
        """Set sub_containers list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.sub_containers = list(items) if items else []
        return self


    def add_parameter_value(self, item: EcucParameterValue) -> "EcucContainerValueBuilder":
        """Add a single item to parameter_values list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.parameter_values.append(item)
        return self

    def clear_parameter_values(self) -> "EcucContainerValueBuilder":
        """Clear all items from parameter_values list.

        Returns:
            self for method chaining
        """
        self._obj.parameter_values = []
        return self

    def add_reference_value(self, item: any (EcucAbstractReference)) -> "EcucContainerValueBuilder":
        """Add a single item to reference_values list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.reference_values.append(item)
        return self

    def clear_reference_values(self) -> "EcucContainerValueBuilder":
        """Clear all items from reference_values list.

        Returns:
            self for method chaining
        """
        self._obj.reference_values = []
        return self

    def add_sub_container(self, item: EcucContainerValue) -> "EcucContainerValueBuilder":
        """Add a single item to sub_containers list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.sub_containers.append(item)
        return self

    def clear_sub_containers(self) -> "EcucContainerValueBuilder":
        """Clear all items from sub_containers list.

        Returns:
            self for method chaining
        """
        self._obj.sub_containers = []
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


    def build(self) -> EcucContainerValue:
        """Build and return the EcucContainerValue instance with validation."""
        self._validate_instance()
        pass
        return self._obj