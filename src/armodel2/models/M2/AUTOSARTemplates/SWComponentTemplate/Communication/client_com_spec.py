"""ClientComSpec AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 187)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.r_port_com_spec import (
    RPortComSpec,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.r_port_com_spec import RPortComSpecBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.transformation_com_spec_props import (
    TransformationComSpecProps,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ClientComSpec(RPortComSpec):
    """AUTOSAR ClientComSpec."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    end_to_end_call_response_timeout: Optional[TimeValue]
    operation_ref: Optional[ARRef]
    transformation_com_spec_props: list[TransformationComSpecProps]
    def __init__(self) -> None:
        """Initialize ClientComSpec."""
        super().__init__()
        self.end_to_end_call_response_timeout: Optional[TimeValue] = None
        self.operation_ref: Optional[ARRef] = None
        self.transformation_com_spec_props: list[TransformationComSpecProps] = []

    def serialize(self) -> ET.Element:
        """Serialize ClientComSpec to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ClientComSpec, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize end_to_end_call_response_timeout
        if self.end_to_end_call_response_timeout is not None:
            serialized = SerializationHelper.serialize_item(self.end_to_end_call_response_timeout, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("END-TO-END-CALL-RESPONSE-TIMEOUT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize operation_ref
        if self.operation_ref is not None:
            serialized = SerializationHelper.serialize_item(self.operation_ref, "ClientServerOperation")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OPERATION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize transformation_com_spec_props (list to container "TRANSFORMATION-COM-SPEC-PROPS")
        if self.transformation_com_spec_props:
            wrapper = ET.Element("TRANSFORMATION-COM-SPEC-PROPS")
            for item in self.transformation_com_spec_props:
                serialized = SerializationHelper.serialize_item(item, "TransformationComSpecProps")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ClientComSpec":
        """Deserialize XML element to ClientComSpec object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ClientComSpec object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ClientComSpec, cls).deserialize(element)

        # Parse end_to_end_call_response_timeout
        child = SerializationHelper.find_child_element(element, "END-TO-END-CALL-RESPONSE-TIMEOUT")
        if child is not None:
            end_to_end_call_response_timeout_value = child.text
            obj.end_to_end_call_response_timeout = end_to_end_call_response_timeout_value

        # Parse operation_ref
        child = SerializationHelper.find_child_element(element, "OPERATION-REF")
        if child is not None:
            operation_ref_value = ARRef.deserialize(child)
            obj.operation_ref = operation_ref_value

        # Parse transformation_com_spec_props (list from container "TRANSFORMATION-COM-SPEC-PROPS")
        obj.transformation_com_spec_props = []
        container = SerializationHelper.find_child_element(element, "TRANSFORMATION-COM-SPEC-PROPS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.transformation_com_spec_props.append(child_value)

        return obj



class ClientComSpecBuilder(RPortComSpecBuilder):
    """Builder for ClientComSpec with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ClientComSpec = ClientComSpec()


    def with_end_to_end_call_response_timeout(self, value: Optional[TimeValue]) -> "ClientComSpecBuilder":
        """Set end_to_end_call_response_timeout attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.end_to_end_call_response_timeout = value
        return self

    def with_operation(self, value: Optional[ClientServerOperation]) -> "ClientComSpecBuilder":
        """Set operation attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.operation = value
        return self

    def with_transformation_com_spec_props(self, items: list[TransformationComSpecProps]) -> "ClientComSpecBuilder":
        """Set transformation_com_spec_props list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.transformation_com_spec_props = list(items) if items else []
        return self


    def add_transformation_com_spec_prop(self, item: TransformationComSpecProps) -> "ClientComSpecBuilder":
        """Add a single item to transformation_com_spec_props list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.transformation_com_spec_props.append(item)
        return self

    def clear_transformation_com_spec_props(self) -> "ClientComSpecBuilder":
        """Clear all items from transformation_com_spec_props list.

        Returns:
            self for method chaining
        """
        self._obj.transformation_com_spec_props = []
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


    def build(self) -> ClientComSpec:
        """Build and return the ClientComSpec instance with validation."""
        self._validate_instance()
        pass
        return self._obj