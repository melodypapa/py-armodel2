"""ServerComSpec AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 188)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.p_port_com_spec import (
    PPortComSpec,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.p_port_com_spec import PPortComSpecBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ServerComSpec(PPortComSpec):
    """AUTOSAR ServerComSpec."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SERVER-COM-SPEC"


    operation_ref: Optional[ARRef]
    queue_length: Optional[PositiveInteger]
    transformation_coms: list[Any]
    _DESERIALIZE_DISPATCH = {
        "OPERATION-REF": lambda obj, elem: setattr(obj, "operation_ref", ARRef.deserialize(elem)),
        "QUEUE-LENGTH": lambda obj, elem: setattr(obj, "queue_length", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "TRANSFORMATION-COMS": lambda obj, elem: obj.transformation_coms.append(SerializationHelper.deserialize_by_tag(elem, "any (TransformationCom)")),
    }


    def __init__(self) -> None:
        """Initialize ServerComSpec."""
        super().__init__()
        self.operation_ref: Optional[ARRef] = None
        self.queue_length: Optional[PositiveInteger] = None
        self.transformation_coms: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize ServerComSpec to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ServerComSpec, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

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

        # Serialize queue_length
        if self.queue_length is not None:
            serialized = SerializationHelper.serialize_item(self.queue_length, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("QUEUE-LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize transformation_coms (list to container "TRANSFORMATION-COMS")
        if self.transformation_coms:
            wrapper = ET.Element("TRANSFORMATION-COMS")
            for item in self.transformation_coms:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ServerComSpec":
        """Deserialize XML element to ServerComSpec object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ServerComSpec object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ServerComSpec, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "OPERATION-REF":
                setattr(obj, "operation_ref", ARRef.deserialize(child))
            elif tag == "QUEUE-LENGTH":
                setattr(obj, "queue_length", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "TRANSFORMATION-COMS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.transformation_coms.append(SerializationHelper.deserialize_by_tag(item_elem, "any (TransformationCom)"))

        return obj



class ServerComSpecBuilder(PPortComSpecBuilder):
    """Builder for ServerComSpec with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ServerComSpec = ServerComSpec()


    def with_operation(self, value: Optional[ClientServerOperation]) -> "ServerComSpecBuilder":
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

    def with_queue_length(self, value: Optional[PositiveInteger]) -> "ServerComSpecBuilder":
        """Set queue_length attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.queue_length = value
        return self

    def with_transformation_coms(self, items: list[any (TransformationCom)]) -> "ServerComSpecBuilder":
        """Set transformation_coms list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.transformation_coms = list(items) if items else []
        return self


    def add_transformation_com(self, item: any (TransformationCom)) -> "ServerComSpecBuilder":
        """Add a single item to transformation_coms list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.transformation_coms.append(item)
        return self

    def clear_transformation_coms(self) -> "ServerComSpecBuilder":
        """Clear all items from transformation_coms list.

        Returns:
            self for method chaining
        """
        self._obj.transformation_coms = []
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


    def build(self) -> ServerComSpec:
        """Build and return the ServerComSpec instance with validation."""
        self._validate_instance()
        pass
        return self._obj