"""AssemblySwConnector AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 289)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 80)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2000)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 423)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Composition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.sw_connector import (
    SwConnector,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_provided_port_prototype import (
    AbstractProvidedPortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_required_port_prototype import (
    AbstractRequiredPortPrototype,
)


class AssemblySwConnector(SwConnector):
    """AUTOSAR AssemblySwConnector."""

    def __init__(self) -> None:
        """Initialize AssemblySwConnector."""
        super().__init__()
        self.provider_instance_ref: Optional[AbstractProvidedPortPrototype] = None
        self.requester_instance_ref: Optional[AbstractRequiredPortPrototype] = None


class AssemblySwConnectorBuilder:
    """Builder for AssemblySwConnector."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AssemblySwConnector = AssemblySwConnector()

    def build(self) -> AssemblySwConnector:
        """Build and return AssemblySwConnector object.

        Returns:
            AssemblySwConnector instance
        """
        # TODO: Add validation
        return self._obj
