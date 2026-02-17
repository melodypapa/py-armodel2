"""ClientServerInterfaceToBswModuleEntryBlueprintMapping AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 174)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_ClientServerInterfaceToBsw.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "client_server": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=ClientServerInterface,
        ),  # clientServer
        "operation": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=ClientServerOperation,
        ),  # operation
        "port_defined_arguments": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=PortDefinedArgumentValue,
        ),  # portDefinedArguments
    }

    def __init__(self) -> None:
        """Initialize ClientServerInterfaceToBswModuleEntryBlueprintMapping."""
        super().__init__()
        self.client_server: ClientServerInterface = None
        self.operation: ClientServerOperation = None
        self.port_defined_arguments: list[PortDefinedArgumentValue] = []


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
