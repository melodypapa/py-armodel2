"""ClientComSpec AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.r_port_com_spec import (
    RPortComSpec,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)


class ClientComSpec(RPortComSpec):
    """AUTOSAR ClientComSpec."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "end_to_end_call": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # endToEndCall
        "operation": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ClientServerOperation,
        ),  # operation
        "transformation_coms": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (TransformationCom),
        ),  # transformationComs
    }

    def __init__(self) -> None:
        """Initialize ClientComSpec."""
        super().__init__()
        self.end_to_end_call: Optional[TimeValue] = None
        self.operation: Optional[ClientServerOperation] = None
        self.transformation_coms: list[Any] = []


class ClientComSpecBuilder:
    """Builder for ClientComSpec."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ClientComSpec = ClientComSpec()

    def build(self) -> ClientComSpec:
        """Build and return ClientComSpec object.

        Returns:
            ClientComSpec instance
        """
        # TODO: Add validation
        return self._obj
