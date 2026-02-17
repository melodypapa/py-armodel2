"""SomeipSdServerServiceInstanceConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 513)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.initial_sd_delay_config import (
    InitialSdDelayConfig,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.request_response_delay import (
    RequestResponseDelay,
)


class SomeipSdServerServiceInstanceConfig(ARElement):
    """AUTOSAR SomeipSdServerServiceInstanceConfig."""

    def __init__(self) -> None:
        """Initialize SomeipSdServerServiceInstanceConfig."""
        super().__init__()
        self.initial_offer_behavior: Optional[InitialSdDelayConfig] = None
        self.offer_cyclic_delay: Optional[TimeValue] = None
        self.priority: Optional[PositiveInteger] = None
        self.request: Optional[RequestResponseDelay] = None
        self.service_offer: Optional[PositiveInteger] = None


class SomeipSdServerServiceInstanceConfigBuilder:
    """Builder for SomeipSdServerServiceInstanceConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SomeipSdServerServiceInstanceConfig = SomeipSdServerServiceInstanceConfig()

    def build(self) -> SomeipSdServerServiceInstanceConfig:
        """Build and return SomeipSdServerServiceInstanceConfig object.

        Returns:
            SomeipSdServerServiceInstanceConfig instance
        """
        # TODO: Add validation
        return self._obj
