"""DltConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 722)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Dlt.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.LogAndTraceExtract.dlt_ecu import (
    DltEcu,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Dlt.dlt_log_channel import (
    DltLogChannel,
)


class DltConfig(ARObject):
    """AUTOSAR DltConfig."""

    def __init__(self) -> None:
        """Initialize DltConfig."""
        super().__init__()
        self.dlt_ecu: Optional[DltEcu] = None
        self.dlt_log_channels: list[DltLogChannel] = []
        self.session_id: Optional[Boolean] = None
        self.timestamp: Optional[Boolean] = None


class DltConfigBuilder:
    """Builder for DltConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DltConfig = DltConfig()

    def build(self) -> DltConfig:
        """Build and return DltConfig object.

        Returns:
            DltConfig instance
        """
        # TODO: Add validation
        return self._obj
