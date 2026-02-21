"""ClientServerInterfaceMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 128)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface_mapping import (
    PortInterfaceMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_application_error_mapping import (
    ClientServerApplicationErrorMapping,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)


class ClientServerInterfaceMapping(PortInterfaceMapping):
    """AUTOSAR ClientServerInterfaceMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    error_mappings: list[ClientServerApplicationErrorMapping]
    operations: list[ClientServerOperation]
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
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

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
                serialized = ARObject._serialize_item(item, "ClientServerApplicationErrorMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize operations (list to container "OPERATIONS")
        if self.operations:
            wrapper = ET.Element("OPERATIONS")
            for item in self.operations:
                serialized = ARObject._serialize_item(item, "ClientServerOperation")
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

        # Parse error_mappings (list from container "ERROR-MAPPINGS")
        obj.error_mappings = []
        container = ARObject._find_child_element(element, "ERROR-MAPPINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.error_mappings.append(child_value)

        # Parse operations (list from container "OPERATIONS")
        obj.operations = []
        container = ARObject._find_child_element(element, "OPERATIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.operations.append(child_value)

        return obj



class ClientServerInterfaceMappingBuilder:
    """Builder for ClientServerInterfaceMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ClientServerInterfaceMapping = ClientServerInterfaceMapping()

    def build(self) -> ClientServerInterfaceMapping:
        """Build and return ClientServerInterfaceMapping object.

        Returns:
            ClientServerInterfaceMapping instance
        """
        # TODO: Add validation
        return self._obj
