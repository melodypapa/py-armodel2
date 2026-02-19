"""ClientServerInterfaceToBswModuleEntryBlueprintMapping AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 174)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_ClientServerInterfaceToBsw.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_interface import (
    ClientServerInterface,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions.port_defined_argument_value import (
    PortDefinedArgumentValue,
)


class ClientServerInterfaceToBswModuleEntryBlueprintMapping(ARElement):
    """AUTOSAR ClientServerInterfaceToBswModuleEntryBlueprintMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    client_server: ClientServerInterface
    operation: ClientServerOperation
    port_defined_arguments: list[PortDefinedArgumentValue]
    def __init__(self) -> None:
        """Initialize ClientServerInterfaceToBswModuleEntryBlueprintMapping."""
        super().__init__()
        self.client_server: ClientServerInterface = None
        self.operation: ClientServerOperation = None
        self.port_defined_arguments: list[PortDefinedArgumentValue] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ClientServerInterfaceToBswModuleEntryBlueprintMapping":
        """Deserialize XML element to ClientServerInterfaceToBswModuleEntryBlueprintMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ClientServerInterfaceToBswModuleEntryBlueprintMapping object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse client_server
        child = ARObject._find_child_element(element, "CLIENT-SERVER")
        if child is not None:
            client_server_value = ARObject._deserialize_by_tag(child, "ClientServerInterface")
            obj.client_server = client_server_value

        # Parse operation
        child = ARObject._find_child_element(element, "OPERATION")
        if child is not None:
            operation_value = ARObject._deserialize_by_tag(child, "ClientServerOperation")
            obj.operation = operation_value

        # Parse port_defined_arguments (list)
        obj.port_defined_arguments = []
        for child in ARObject._find_all_child_elements(element, "PORT-DEFINED-ARGUMENTS"):
            port_defined_arguments_value = ARObject._deserialize_by_tag(child, "PortDefinedArgumentValue")
            obj.port_defined_arguments.append(port_defined_arguments_value)

        return obj



class ClientServerInterfaceToBswModuleEntryBlueprintMappingBuilder:
    """Builder for ClientServerInterfaceToBswModuleEntryBlueprintMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ClientServerInterfaceToBswModuleEntryBlueprintMapping = ClientServerInterfaceToBswModuleEntryBlueprintMapping()

    def build(self) -> ClientServerInterfaceToBswModuleEntryBlueprintMapping:
        """Build and return ClientServerInterfaceToBswModuleEntryBlueprintMapping object.

        Returns:
            ClientServerInterfaceToBswModuleEntryBlueprintMapping instance
        """
        # TODO: Add validation
        return self._obj
