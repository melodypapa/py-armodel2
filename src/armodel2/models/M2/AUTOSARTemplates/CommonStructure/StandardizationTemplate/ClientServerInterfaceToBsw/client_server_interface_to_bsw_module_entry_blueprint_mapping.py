"""ClientServerInterfaceToBswModuleEntryBlueprintMapping AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 174)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_ClientServerInterfaceToBsw.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_interface import (
    ClientServerInterface,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions.port_defined_argument_value import (
    PortDefinedArgumentValue,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ClientServerInterfaceToBswModuleEntryBlueprintMapping(ARElement):
    """AUTOSAR ClientServerInterfaceToBswModuleEntryBlueprintMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CLIENT-SERVER-INTERFACE-TO-BSW-MODULE-ENTRY-BLUEPRINT-MAPPING"


    client_server_ref: ARRef
    operation: ClientServerOperation
    port_defined_arguments: list[PortDefinedArgumentValue]
    _DESERIALIZE_DISPATCH = {
        "CLIENT-SERVER-REF": lambda obj, elem: setattr(obj, "client_server_ref", ARRef.deserialize(elem)),
        "OPERATION": lambda obj, elem: setattr(obj, "operation", SerializationHelper.deserialize_by_tag(elem, "ClientServerOperation")),
        "PORT-DEFINED-ARGUMENTS": lambda obj, elem: obj.port_defined_arguments.append(SerializationHelper.deserialize_by_tag(elem, "PortDefinedArgumentValue")),
    }


    def __init__(self) -> None:
        """Initialize ClientServerInterfaceToBswModuleEntryBlueprintMapping."""
        super().__init__()
        self.client_server_ref: ARRef = None
        self.operation: ClientServerOperation = None
        self.port_defined_arguments: list[PortDefinedArgumentValue] = []

    def serialize(self) -> ET.Element:
        """Serialize ClientServerInterfaceToBswModuleEntryBlueprintMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ClientServerInterfaceToBswModuleEntryBlueprintMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize client_server_ref
        if self.client_server_ref is not None:
            serialized = SerializationHelper.serialize_item(self.client_server_ref, "ClientServerInterface")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CLIENT-SERVER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize operation
        if self.operation is not None:
            serialized = SerializationHelper.serialize_item(self.operation, "ClientServerOperation")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OPERATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize port_defined_arguments (list to container "PORT-DEFINED-ARGUMENTS")
        if self.port_defined_arguments:
            wrapper = ET.Element("PORT-DEFINED-ARGUMENTS")
            for item in self.port_defined_arguments:
                serialized = SerializationHelper.serialize_item(item, "PortDefinedArgumentValue")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ClientServerInterfaceToBswModuleEntryBlueprintMapping":
        """Deserialize XML element to ClientServerInterfaceToBswModuleEntryBlueprintMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ClientServerInterfaceToBswModuleEntryBlueprintMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ClientServerInterfaceToBswModuleEntryBlueprintMapping, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CLIENT-SERVER-REF":
                setattr(obj, "client_server_ref", ARRef.deserialize(child))
            elif tag == "OPERATION":
                setattr(obj, "operation", SerializationHelper.deserialize_by_tag(child, "ClientServerOperation"))
            elif tag == "PORT-DEFINED-ARGUMENTS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.port_defined_arguments.append(SerializationHelper.deserialize_by_tag(item_elem, "PortDefinedArgumentValue"))

        return obj



class ClientServerInterfaceToBswModuleEntryBlueprintMappingBuilder(ARElementBuilder):
    """Builder for ClientServerInterfaceToBswModuleEntryBlueprintMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ClientServerInterfaceToBswModuleEntryBlueprintMapping = ClientServerInterfaceToBswModuleEntryBlueprintMapping()


    def with_client_server(self, value: ClientServerInterface) -> "ClientServerInterfaceToBswModuleEntryBlueprintMappingBuilder":
        """Set client_server attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.client_server = value
        return self

    def with_operation(self, value: ClientServerOperation) -> "ClientServerInterfaceToBswModuleEntryBlueprintMappingBuilder":
        """Set operation attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.operation = value
        return self

    def with_port_defined_arguments(self, items: list[PortDefinedArgumentValue]) -> "ClientServerInterfaceToBswModuleEntryBlueprintMappingBuilder":
        """Set port_defined_arguments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.port_defined_arguments = list(items) if items else []
        return self


    def add_port_defined_argument(self, item: PortDefinedArgumentValue) -> "ClientServerInterfaceToBswModuleEntryBlueprintMappingBuilder":
        """Add a single item to port_defined_arguments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.port_defined_arguments.append(item)
        return self

    def clear_port_defined_arguments(self) -> "ClientServerInterfaceToBswModuleEntryBlueprintMappingBuilder":
        """Clear all items from port_defined_arguments list.

        Returns:
            self for method chaining
        """
        self._obj.port_defined_arguments = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "clientServer",
        "operation",
    }
    _OPTIONAL_ATTRIBUTES = {
        "portDefinedArgument",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Validate required attributes using pre-computed constants (O(1) lookup)
        # This is much faster than calling get_type_hints() at runtime
        if getattr(self._obj, "clientServer", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'clientServer' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'clientServer' is None", UserWarning)
        if getattr(self._obj, "operation", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'operation' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'operation' is None", UserWarning)


    def build(self) -> ClientServerInterfaceToBswModuleEntryBlueprintMapping:
        """Build and return the ClientServerInterfaceToBswModuleEntryBlueprintMapping instance with validation."""
        self._validate_instance()
        return self._obj