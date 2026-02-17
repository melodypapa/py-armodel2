"""ClientIdDefinition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 45)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)


class ClientIdDefinition(Identifiable):
    """AUTOSAR ClientIdDefinition."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "client_id": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # clientId
        "client_server_instance_ref": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ClientServerOperation,
        ),  # clientServerInstanceRef
    }

    def __init__(self) -> None:
        """Initialize ClientIdDefinition."""
        super().__init__()
        self.client_id: Optional[Numerical] = None
        self.client_server_instance_ref: Optional[ClientServerOperation] = None


class ClientIdDefinitionBuilder:
    """Builder for ClientIdDefinition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ClientIdDefinition = ClientIdDefinition()

    def build(self) -> ClientIdDefinition:
        """Build and return ClientIdDefinition object.

        Returns:
            ClientIdDefinition instance
        """
        # TODO: Add validation
        return self._obj
