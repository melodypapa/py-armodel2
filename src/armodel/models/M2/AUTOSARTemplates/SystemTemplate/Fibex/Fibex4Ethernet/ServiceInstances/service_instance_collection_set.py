"""ServiceInstanceCollectionSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 476)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.abstract_service_instance import (
    AbstractServiceInstance,
)


class ServiceInstanceCollectionSet(FibexElement):
    """AUTOSAR ServiceInstanceCollectionSet."""

    service_instances: list[AbstractServiceInstance]
    def __init__(self) -> None:
        """Initialize ServiceInstanceCollectionSet."""
        super().__init__()
        self.service_instances: list[AbstractServiceInstance] = []


class ServiceInstanceCollectionSetBuilder:
    """Builder for ServiceInstanceCollectionSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ServiceInstanceCollectionSet = ServiceInstanceCollectionSet()

    def build(self) -> ServiceInstanceCollectionSet:
        """Build and return ServiceInstanceCollectionSet object.

        Returns:
            ServiceInstanceCollectionSet instance
        """
        # TODO: Add validation
        return self._obj
