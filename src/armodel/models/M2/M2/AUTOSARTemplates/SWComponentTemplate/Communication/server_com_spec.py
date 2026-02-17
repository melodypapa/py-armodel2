"""ServerComSpec AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 188)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.p_port_com_spec import (
    PPortComSpec,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)


class ServerComSpec(PPortComSpec):
    """AUTOSAR ServerComSpec."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "operation": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ClientServerOperation,
        ),  # operation
        "queue_length": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # queueLength
        "transformation_coms": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=Any,
        ),  # transformationComs
    }

    def __init__(self) -> None:
        """Initialize ServerComSpec."""
        super().__init__()
        self.operation: Optional[ClientServerOperation] = None
        self.queue_length: Optional[PositiveInteger] = None
        self.transformation_coms: list[Any] = []


class ServerComSpecBuilder:
    """Builder for ServerComSpec."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ServerComSpec = ServerComSpec()

    def build(self) -> ServerComSpec:
        """Build and return ServerComSpec object.

        Returns:
            ServerComSpec instance
        """
        # TODO: Add validation
        return self._obj
