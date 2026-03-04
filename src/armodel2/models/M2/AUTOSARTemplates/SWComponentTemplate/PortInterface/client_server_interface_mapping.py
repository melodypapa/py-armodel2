"""ClientServerInterfaceMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 128)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface_mapping import (
    PortInterfaceMapping,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface_mapping import PortInterfaceMappingBuilder
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_application_error_mapping import (
    ClientServerApplicationErrorMapping,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ClientServerInterfaceMapping(PortInterfaceMapping):
    """AUTOSAR ClientServerInterfaceMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CLIENT-SERVER-INTERFACE-MAPPING"


    error_mappings: list[ClientServerApplicationErrorMapping]
    operations: list[ClientServerOperation]
    _DESERIALIZE_DISPATCH = {
        "ERROR-MAPPINGS": lambda obj, elem: obj.error_mappings.append(SerializationHelper.deserialize_by_tag(elem, "ClientServerApplicationErrorMapping")),
        "OPERATIONS": lambda obj, elem: obj.operations.append(SerializationHelper.deserialize_by_tag(elem, "ClientServerOperation")),
    }


    def __init__(self) -> None:
        """Initialize ClientServerInterfaceMapping."""
        super().__init__()
        self.error_mappings: list[ClientServerApplicationErrorMapping] = []
        self.operations: list[ClientServerOperation] = []

    def serialize(self) -> ET.Element:
        """Serialize ClientServerInterfaceMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ClientServerInterfaceMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize error_mappings (list to container "ERROR-MAPPINGS")
        if self.error_mappings:
            wrapper = ET.Element("ERROR-MAPPINGS")
            for item in self.error_mappings:
                serialized = SerializationHelper.serialize_item(item, "ClientServerApplicationErrorMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

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
    def deserialize(cls, element: ET.Element) -> "ClientServerInterfaceMapping":
        """Deserialize XML element to ClientServerInterfaceMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ClientServerInterfaceMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ClientServerInterfaceMapping, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ERROR-MAPPINGS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.error_mappings.append(SerializationHelper.deserialize_by_tag(item_elem, "ClientServerApplicationErrorMapping"))
            elif tag == "OPERATIONS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.operations.append(SerializationHelper.deserialize_by_tag(item_elem, "ClientServerOperation"))

        return obj



class ClientServerInterfaceMappingBuilder(PortInterfaceMappingBuilder):
    """Builder for ClientServerInterfaceMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ClientServerInterfaceMapping = ClientServerInterfaceMapping()


    def with_error_mappings(self, items: list[ClientServerApplicationErrorMapping]) -> "ClientServerInterfaceMappingBuilder":
        """Set error_mappings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.error_mappings = list(items) if items else []
        return self

    def with_operations(self, items: list[ClientServerOperation]) -> "ClientServerInterfaceMappingBuilder":
        """Set operations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.operations = list(items) if items else []
        return self


    def add_error_mapping(self, item: ClientServerApplicationErrorMapping) -> "ClientServerInterfaceMappingBuilder":
        """Add a single item to error_mappings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.error_mappings.append(item)
        return self

    def clear_error_mappings(self) -> "ClientServerInterfaceMappingBuilder":
        """Clear all items from error_mappings list.

        Returns:
            self for method chaining
        """
        self._obj.error_mappings = []
        return self

    def add_operation(self, item: ClientServerOperation) -> "ClientServerInterfaceMappingBuilder":
        """Add a single item to operations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.operations.append(item)
        return self

    def clear_operations(self) -> "ClientServerInterfaceMappingBuilder":
        """Clear all items from operations list.

        Returns:
            self for method chaining
        """
        self._obj.operations = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "errorMapping",
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


    def build(self) -> ClientServerInterfaceMapping:
        """Build and return the ClientServerInterfaceMapping instance with validation."""
        self._validate_instance()
        return self._obj