"""DdsCpProvidedServiceInstance AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 472)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_cp_service_instance import (
    DdsCpServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.application_endpoint import (
    ApplicationEndpoint,
)


class DdsCpProvidedServiceInstance(DdsCpServiceInstance):
    """AUTOSAR DdsCpProvidedServiceInstance."""

    def __init__(self) -> None:
        """Initialize DdsCpProvidedServiceInstance."""
        super().__init__()
        self.local_unicast: Optional[ApplicationEndpoint] = None
        self.minor_version: Optional[PositiveInteger] = None
        self.provided_ddses: list[DdsCpServiceInstance] = []
        self.static_remotes: list[ApplicationEndpoint] = []


class DdsCpProvidedServiceInstanceBuilder:
    """Builder for DdsCpProvidedServiceInstance."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsCpProvidedServiceInstance = DdsCpProvidedServiceInstance()

    def build(self) -> DdsCpProvidedServiceInstance:
        """Build and return DdsCpProvidedServiceInstance object.

        Returns:
            DdsCpProvidedServiceInstance instance
        """
        # TODO: Add validation
        return self._obj
