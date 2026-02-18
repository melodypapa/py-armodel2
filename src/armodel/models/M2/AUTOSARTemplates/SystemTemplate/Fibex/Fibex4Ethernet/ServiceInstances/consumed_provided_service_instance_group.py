"""ConsumedProvidedServiceInstanceGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 523)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)


class ConsumedProvidedServiceInstanceGroup(FibexElement):
    """AUTOSAR ConsumedProvidedServiceInstanceGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    consumed_services: list[Any]
    provided_services: list[Any]
    def __init__(self) -> None:
        """Initialize ConsumedProvidedServiceInstanceGroup."""
        super().__init__()
        self.consumed_services: list[Any] = []
        self.provided_services: list[Any] = []


class ConsumedProvidedServiceInstanceGroupBuilder:
    """Builder for ConsumedProvidedServiceInstanceGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ConsumedProvidedServiceInstanceGroup = ConsumedProvidedServiceInstanceGroup()

    def build(self) -> ConsumedProvidedServiceInstanceGroup:
        """Build and return ConsumedProvidedServiceInstanceGroup object.

        Returns:
            ConsumedProvidedServiceInstanceGroup instance
        """
        # TODO: Add validation
        return self._obj
