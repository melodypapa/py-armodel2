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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ClientServerInterfaceMapping":
        """Deserialize XML element to ClientServerInterfaceMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ClientServerInterfaceMapping object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse error_mappings (list)
        obj.error_mappings = []
        for child in ARObject._find_all_child_elements(element, "ERROR-MAPPINGS"):
            error_mappings_value = ARObject._deserialize_by_tag(child, "ClientServerApplicationErrorMapping")
            obj.error_mappings.append(error_mappings_value)

        # Parse operations (list)
        obj.operations = []
        for child in ARObject._find_all_child_elements(element, "OPERATIONS"):
            operations_value = ARObject._deserialize_by_tag(child, "ClientServerOperation")
            obj.operations.append(operations_value)

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
