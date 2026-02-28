"""ClientServerOperationMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 129)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.data_prototype_mapping import (
    DataPrototypeMapping,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.data_transformation import (
    DataTransformation,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ClientServerOperationMapping(ARObject):
    """AUTOSAR ClientServerOperationMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CLIENT-SERVER-OPERATION-MAPPING"


    argument_refs: list[ARRef]
    first_operation_ref: Optional[ARRef]
    first_to_second_ref: Optional[ARRef]
    second_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "ARGUMENTS": lambda obj, elem: obj.argument_refs.append(ARRef.deserialize(elem)),
        "FIRST-OPERATION-REF": lambda obj, elem: setattr(obj, "first_operation_ref", ARRef.deserialize(elem)),
        "FIRST-TO-SECOND-REF": lambda obj, elem: setattr(obj, "first_to_second_ref", ARRef.deserialize(elem)),
        "SECOND-REF": lambda obj, elem: setattr(obj, "second_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize ClientServerOperationMapping."""
        super().__init__()
        self.argument_refs: list[ARRef] = []
        self.first_operation_ref: Optional[ARRef] = None
        self.first_to_second_ref: Optional[ARRef] = None
        self.second_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize ClientServerOperationMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ClientServerOperationMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize argument_refs (list to container "ARGUMENT-REFS")
        if self.argument_refs:
            wrapper = ET.Element("ARGUMENT-REFS")
            for item in self.argument_refs:
                serialized = SerializationHelper.serialize_item(item, "DataPrototypeMapping")
                if serialized is not None:
                    child_elem = ET.Element("ARGUMENT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize first_operation_ref
        if self.first_operation_ref is not None:
            serialized = SerializationHelper.serialize_item(self.first_operation_ref, "ClientServerOperation")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FIRST-OPERATION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize first_to_second_ref
        if self.first_to_second_ref is not None:
            serialized = SerializationHelper.serialize_item(self.first_to_second_ref, "DataTransformation")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FIRST-TO-SECOND-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize second_ref
        if self.second_ref is not None:
            serialized = SerializationHelper.serialize_item(self.second_ref, "ClientServerOperation")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SECOND-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ClientServerOperationMapping":
        """Deserialize XML element to ClientServerOperationMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ClientServerOperationMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ClientServerOperationMapping, cls).deserialize(element)

        # Parse argument_refs (list from container "ARGUMENT-REFS")
        obj.argument_refs = []
        container = SerializationHelper.find_child_element(element, "ARGUMENT-REFS")
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
                    obj.argument_refs.append(child_value)

        # Parse first_operation_ref
        child = SerializationHelper.find_child_element(element, "FIRST-OPERATION-REF")
        if child is not None:
            first_operation_ref_value = ARRef.deserialize(child)
            obj.first_operation_ref = first_operation_ref_value

        # Parse first_to_second_ref
        child = SerializationHelper.find_child_element(element, "FIRST-TO-SECOND-REF")
        if child is not None:
            first_to_second_ref_value = ARRef.deserialize(child)
            obj.first_to_second_ref = first_to_second_ref_value

        # Parse second_ref
        child = SerializationHelper.find_child_element(element, "SECOND-REF")
        if child is not None:
            second_ref_value = ARRef.deserialize(child)
            obj.second_ref = second_ref_value

        return obj



class ClientServerOperationMappingBuilder(BuilderBase):
    """Builder for ClientServerOperationMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ClientServerOperationMapping = ClientServerOperationMapping()


    def with_arguments(self, items: list[DataPrototypeMapping]) -> "ClientServerOperationMappingBuilder":
        """Set arguments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.arguments = list(items) if items else []
        return self

    def with_first_operation(self, value: Optional[ClientServerOperation]) -> "ClientServerOperationMappingBuilder":
        """Set first_operation attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.first_operation = value
        return self

    def with_first_to_second(self, value: Optional[DataTransformation]) -> "ClientServerOperationMappingBuilder":
        """Set first_to_second attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.first_to_second = value
        return self

    def with_second(self, value: Optional[ClientServerOperation]) -> "ClientServerOperationMappingBuilder":
        """Set second attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.second = value
        return self


    def add_argument(self, item: DataPrototypeMapping) -> "ClientServerOperationMappingBuilder":
        """Add a single item to arguments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.arguments.append(item)
        return self

    def clear_arguments(self) -> "ClientServerOperationMappingBuilder":
        """Clear all items from arguments list.

        Returns:
            self for method chaining
        """
        self._obj.arguments = []
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


    def build(self) -> ClientServerOperationMapping:
        """Build and return the ClientServerOperationMapping instance with validation."""
        self._validate_instance()
        pass
        return self._obj