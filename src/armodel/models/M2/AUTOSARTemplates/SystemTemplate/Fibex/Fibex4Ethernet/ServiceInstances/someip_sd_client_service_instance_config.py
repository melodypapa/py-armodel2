"""SomeipSdClientServiceInstanceConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2058)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.initial_sd_delay_config import (
    InitialSdDelayConfig,
)


class SomeipSdClientServiceInstanceConfig(ARElement):
    """AUTOSAR SomeipSdClientServiceInstanceConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    initial_find_behavior: Optional[InitialSdDelayConfig]
    priority: Optional[PositiveInteger]
    service_find: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize SomeipSdClientServiceInstanceConfig."""
        super().__init__()
        self.initial_find_behavior: Optional[InitialSdDelayConfig] = None
        self.priority: Optional[PositiveInteger] = None
        self.service_find: Optional[PositiveInteger] = None


class SomeipSdClientServiceInstanceConfigBuilder:
    """Builder for SomeipSdClientServiceInstanceConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SomeipSdClientServiceInstanceConfig = SomeipSdClientServiceInstanceConfig()

    def build(self) -> SomeipSdClientServiceInstanceConfig:
        """Build and return SomeipSdClientServiceInstanceConfig object.

        Returns:
            SomeipSdClientServiceInstanceConfig instance
        """
        # TODO: Add validation
        return self._obj
