"""ClientServerOperationBlueprintMapping AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 68)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_ClientServerInterfaceToBsw.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_entry import (
    BswModuleEntry,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)


class ClientServerOperationBlueprintMapping(ARObject):
    """AUTOSAR ClientServerOperationBlueprintMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "blueprint": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DocumentationBlock,
        ),  # blueprint
        "bsw_module_entry": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=BswModuleEntry,
        ),  # bswModuleEntry
        "client_server": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=ClientServerOperation,
        ),  # clientServer
    }

    def __init__(self) -> None:
        """Initialize ClientServerOperationBlueprintMapping."""
        super().__init__()
        self.blueprint: Optional[DocumentationBlock] = None
        self.bsw_module_entry: BswModuleEntry = None
        self.client_server: ClientServerOperation = None


class ClientServerOperationBlueprintMappingBuilder:
    """Builder for ClientServerOperationBlueprintMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ClientServerOperationBlueprintMapping = ClientServerOperationBlueprintMapping()

    def build(self) -> ClientServerOperationBlueprintMapping:
        """Build and return ClientServerOperationBlueprintMapping object.

        Returns:
            ClientServerOperationBlueprintMapping instance
        """
        # TODO: Add validation
        return self._obj
