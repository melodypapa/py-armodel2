"""SomeipSdServerEventGroupTimingConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 517)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.request_response_delay import (
    RequestResponseDelay,
)


class SomeipSdServerEventGroupTimingConfig(ARElement):
    """AUTOSAR SomeipSdServerEventGroupTimingConfig."""

    def __init__(self) -> None:
        """Initialize SomeipSdServerEventGroupTimingConfig."""
        super().__init__()
        self.request: Optional[RequestResponseDelay] = None


class SomeipSdServerEventGroupTimingConfigBuilder:
    """Builder for SomeipSdServerEventGroupTimingConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SomeipSdServerEventGroupTimingConfig = SomeipSdServerEventGroupTimingConfig()

    def build(self) -> SomeipSdServerEventGroupTimingConfig:
        """Build and return SomeipSdServerEventGroupTimingConfig object.

        Returns:
            SomeipSdServerEventGroupTimingConfig instance
        """
        # TODO: Add validation
        return self._obj
