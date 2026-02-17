"""IEEE1722TpCrfConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 640)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols_IEEE1722Tp_IEEE1722TpAv.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.ieee1722_tp_av_connection import (
    IEEE1722TpAvConnection,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAv import (
    IEEE1722TpCrfPullEnum,
    IEEE1722TpCrfTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class IEEE1722TpCrfConnection(IEEE1722TpAvConnection):
    """AUTOSAR IEEE1722TpCrfConnection."""

    def __init__(self) -> None:
        """Initialize IEEE1722TpCrfConnection."""
        super().__init__()
        self.base_frequency: Optional[PositiveInteger] = None
        self.crf_pull_enum: Optional[IEEE1722TpCrfPullEnum] = None
        self.crf_type_enum: Optional[IEEE1722TpCrfTypeEnum] = None
        self.frame_sync: Optional[Boolean] = None
        self.timestamp: Optional[PositiveInteger] = None


class IEEE1722TpCrfConnectionBuilder:
    """Builder for IEEE1722TpCrfConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IEEE1722TpCrfConnection = IEEE1722TpCrfConnection()

    def build(self) -> IEEE1722TpCrfConnection:
        """Build and return IEEE1722TpCrfConnection object.

        Returns:
            IEEE1722TpCrfConnection instance
        """
        # TODO: Add validation
        return self._obj
