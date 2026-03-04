"""ClientServerInterface AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 308)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 235)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 101)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2007)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 432)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface import (
    PortInterface,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface import PortInterfaceBuilder
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.application_error import (
    ApplicationError,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ClientServerInterface(PortInterface):
    """AUTOSAR ClientServerInterface."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CLIENT-SERVER-INTERFACE"


    operations: list[ClientServerOperation]
    possible_errors: list[ApplicationError]
    _DESERIALIZE_DISPATCH = {
        "OPERATIONS": lambda obj, elem: obj.operations.append(SerializationHelper.deserialize_by_tag(elem, "ClientServerOperation")),
        "POSSIBLE-ERRORS": lambda obj, elem: obj.possible_errors.append(SerializationHelper.deserialize_by_tag(elem, "ApplicationError")),
    }


    def __init__(self) -> None:
        """Initialize ClientServerInterface."""
        super().__init__()
        self.operations: list[ClientServerOperation] = []
        self.possible_errors: list[ApplicationError] = []

    def serialize(self) -> ET.Element:
        """Serialize ClientServerInterface to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ClientServerInterface, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize operations (list to container "OPERATIONS")
        if self.operations:
            wrapper = ET.Element("OPERATIONS")
            for item in self.operations:
                serialized = SerializationHelper.serialize_item(item, "ClientServerOperation")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize possible_errors (list to container "POSSIBLE-ERRORS")
        if self.possible_errors:
            wrapper = ET.Element("POSSIBLE-ERRORS")
            for item in self.possible_errors:
                serialized = SerializationHelper.serialize_item(item, "ApplicationError")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ClientServerInterface":
        """Deserialize XML element to ClientServerInterface object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ClientServerInterface object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ClientServerInterface, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "OPERATIONS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.operations.append(SerializationHelper.deserialize_by_tag(item_elem, "ClientServerOperation"))
            elif tag == "POSSIBLE-ERRORS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.possible_errors.append(SerializationHelper.deserialize_by_tag(item_elem, "ApplicationError"))

        return obj



class ClientServerInterfaceBuilder(PortInterfaceBuilder):
    """Builder for ClientServerInterface with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ClientServerInterface = ClientServerInterface()


    def with_operations(self, items: list[ClientServerOperation]) -> "ClientServerInterfaceBuilder":
        """Set operations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.operations = list(items) if items else []
        return self

    def with_possible_errors(self, items: list[ApplicationError]) -> "ClientServerInterfaceBuilder":
        """Set possible_errors list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.possible_errors = list(items) if items else []
        return self


    def add_operation(self, item: ClientServerOperation) -> "ClientServerInterfaceBuilder":
        """Add a single item to operations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.operations.append(item)
        return self

    def clear_operations(self) -> "ClientServerInterfaceBuilder":
        """Clear all items from operations list.

        Returns:
            self for method chaining
        """
        self._obj.operations = []
        return self

    def add_possible_error(self, item: ApplicationError) -> "ClientServerInterfaceBuilder":
        """Add a single item to possible_errors list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.possible_errors.append(item)
        return self

    def clear_possible_errors(self) -> "ClientServerInterfaceBuilder":
        """Clear all items from possible_errors list.

        Returns:
            self for method chaining
        """
        self._obj.possible_errors = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "operation",
        "possibleError",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> ClientServerInterface:
        """Build and return the ClientServerInterface instance with validation."""
        self._validate_instance()
        return self._obj