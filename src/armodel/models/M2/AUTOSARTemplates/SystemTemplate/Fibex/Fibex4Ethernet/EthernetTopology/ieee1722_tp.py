"""Ieee1722Tp AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 460)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.transport_protocol_configuration import (
    TransportProtocolConfiguration,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)


class Ieee1722Tp(TransportProtocolConfiguration):
    """AUTOSAR Ieee1722Tp."""

    relative: Optional[TimeValue]
    stream_identifier: Optional[PositiveInteger]
    sub_type: Optional[PositiveInteger]
    version: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize Ieee1722Tp."""
        super().__init__()
        self.relative: Optional[TimeValue] = None
        self.stream_identifier: Optional[PositiveInteger] = None
        self.sub_type: Optional[PositiveInteger] = None
        self.version: Optional[PositiveInteger] = None


class Ieee1722TpBuilder:
    """Builder for Ieee1722Tp."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Ieee1722Tp = Ieee1722Tp()

    def build(self) -> Ieee1722Tp:
        """Build and return Ieee1722Tp object.

        Returns:
            Ieee1722Tp instance
        """
        # TODO: Add validation
        return self._obj
