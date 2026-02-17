"""StreamFilterPortRange AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 139)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class StreamFilterPortRange(ARObject):
    """AUTOSAR StreamFilterPortRange."""

    def __init__(self) -> None:
        """Initialize StreamFilterPortRange."""
        super().__init__()
        self.max: Optional[PositiveInteger] = None
        self.min: Optional[PositiveInteger] = None


class StreamFilterPortRangeBuilder:
    """Builder for StreamFilterPortRange."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: StreamFilterPortRange = StreamFilterPortRange()

    def build(self) -> StreamFilterPortRange:
        """Build and return StreamFilterPortRange object.

        Returns:
            StreamFilterPortRange instance
        """
        # TODO: Add validation
        return self._obj
