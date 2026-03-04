"""SwcToSwcOperationArguments AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 253)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SignalPaths.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SwcToSwcOperationArguments(ARObject):
    """AUTOSAR SwcToSwcOperationArguments."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SWC-TO-SWC-OPERATION-ARGUMENTS"


    direction: Optional[Any]
    operations: list[ClientServerOperation]
    _DESERIALIZE_DISPATCH = {
        "DIRECTION": lambda obj, elem: setattr(obj, "direction", SerializationHelper.deserialize_by_tag(elem, "any (SwcToSwcOperation)")),
        "OPERATIONS": lambda obj, elem: obj.operations.append(SerializationHelper.deserialize_by_tag(elem, "ClientServerOperation")),
    }


    def __init__(self) -> None:
        """Initialize SwcToSwcOperationArguments."""
        super().__init__()
        self.direction: Optional[Any] = None
        self.operations: list[ClientServerOperation] = []

    def serialize(self) -> ET.Element:
        """Serialize SwcToSwcOperationArguments to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwcToSwcOperationArguments, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize direction
        if self.direction is not None:
            serialized = SerializationHelper.serialize_item(self.direction, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DIRECTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize operations (list to container "OPERATIONS")
        if self.operations:
            wrapper = ET.Element("OPERATIONS")
            for item in self.operations:
                serialized = SerializationHelper.serialize_item(item, "ClientServerOperation")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwcToSwcOperationArguments":
        """Deserialize XML element to SwcToSwcOperationArguments object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwcToSwcOperationArguments object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwcToSwcOperationArguments, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DIRECTION":
                setattr(obj, "direction", SerializationHelper.deserialize_by_tag(child, "any (SwcToSwcOperation)"))
            elif tag == "OPERATIONS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.operations.append(SerializationHelper.deserialize_by_tag(item_elem, "ClientServerOperation"))

        return obj



class SwcToSwcOperationArgumentsBuilder(BuilderBase):
    """Builder for SwcToSwcOperationArguments with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SwcToSwcOperationArguments = SwcToSwcOperationArguments()


    def with_direction(self, value: Optional[any (SwcToSwcOperation)]) -> "SwcToSwcOperationArgumentsBuilder":
        """Set direction attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.direction = value
        return self

    def with_operations(self, items: list[ClientServerOperation]) -> "SwcToSwcOperationArgumentsBuilder":
        """Set operations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.operations = list(items) if items else []
        return self


    def add_operation(self, item: ClientServerOperation) -> "SwcToSwcOperationArgumentsBuilder":
        """Add a single item to operations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.operations.append(item)
        return self

    def clear_operations(self) -> "SwcToSwcOperationArgumentsBuilder":
        """Clear all items from operations list.

        Returns:
            self for method chaining
        """
        self._obj.operations = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "direction",
        "operation",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> SwcToSwcOperationArguments:
        """Build and return the SwcToSwcOperationArguments instance with validation."""
        self._validate_instance()
        return self._obj