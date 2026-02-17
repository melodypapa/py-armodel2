"""StreamFilterIEEE1722Tp AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 139)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveUnlimitedInteger,
)


class StreamFilterIEEE1722Tp(ARObject):
    """AUTOSAR StreamFilterIEEE1722Tp."""

    def __init__(self) -> None:
        """Initialize StreamFilterIEEE1722Tp."""
        super().__init__()
        self.stream_id: Optional[PositiveUnlimitedInteger] = None


class StreamFilterIEEE1722TpBuilder:
    """Builder for StreamFilterIEEE1722Tp."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: StreamFilterIEEE1722Tp = StreamFilterIEEE1722Tp()

    def build(self) -> StreamFilterIEEE1722Tp:
        """Build and return StreamFilterIEEE1722Tp object.

        Returns:
            StreamFilterIEEE1722Tp instance
        """
        # TODO: Add validation
        return self._obj
