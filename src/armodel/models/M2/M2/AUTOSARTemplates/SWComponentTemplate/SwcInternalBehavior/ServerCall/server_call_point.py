"""ServerCallPoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 335)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 580)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2055)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_ServerCall.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount.abstract_access_point import (
    AbstractAccessPoint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)


class ServerCallPoint(AbstractAccessPoint):
    """AUTOSAR ServerCallPoint."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "operation_instance_ref": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ClientServerOperation,
        ),  # operationInstanceRef
        "timeout": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # timeout
    }

    def __init__(self) -> None:
        """Initialize ServerCallPoint."""
        super().__init__()
        self.operation_instance_ref: Optional[ClientServerOperation] = None
        self.timeout: Optional[TimeValue] = None


class ServerCallPointBuilder:
    """Builder for ServerCallPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ServerCallPoint = ServerCallPoint()

    def build(self) -> ServerCallPoint:
        """Build and return ServerCallPoint object.

        Returns:
            ServerCallPoint instance
        """
        # TODO: Add validation
        return self._obj
