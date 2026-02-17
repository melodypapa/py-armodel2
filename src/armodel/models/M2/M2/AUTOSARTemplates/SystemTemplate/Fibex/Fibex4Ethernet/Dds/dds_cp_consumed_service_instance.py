"""DdsCpConsumedServiceInstance AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 474)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_cp_service_instance import (
    DdsCpServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AnyVersionString,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.application_endpoint import (
    ApplicationEndpoint,
)


class DdsCpConsumedServiceInstance(DdsCpServiceInstance):
    """AUTOSAR DdsCpConsumedServiceInstance."""

    def __init__(self) -> None:
        """Initialize DdsCpConsumedServiceInstance."""
        super().__init__()
        self.consumed_ddses: list[DdsCpServiceInstance] = []
        self.local_unicast: Optional[ApplicationEndpoint] = None
        self.minor_version: Optional[AnyVersionString] = None
        self.static_remote: Optional[ApplicationEndpoint] = None


class DdsCpConsumedServiceInstanceBuilder:
    """Builder for DdsCpConsumedServiceInstance."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsCpConsumedServiceInstance = DdsCpConsumedServiceInstance()

    def build(self) -> DdsCpConsumedServiceInstance:
        """Build and return DdsCpConsumedServiceInstance object.

        Returns:
            DdsCpConsumedServiceInstance instance
        """
        # TODO: Add validation
        return self._obj
