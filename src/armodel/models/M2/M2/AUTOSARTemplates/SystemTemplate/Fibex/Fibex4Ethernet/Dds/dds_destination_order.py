"""DdsDestinationOrder AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 536)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DdsDestinationOrder(ARObject):
    """AUTOSAR DdsDestinationOrder."""

    def __init__(self) -> None:
        """Initialize DdsDestinationOrder."""
        super().__init__()
        self.destination: Optional[DdsDestinationOrder] = None


class DdsDestinationOrderBuilder:
    """Builder for DdsDestinationOrder."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsDestinationOrder = DdsDestinationOrder()

    def build(self) -> DdsDestinationOrder:
        """Build and return DdsDestinationOrder object.

        Returns:
            DdsDestinationOrder instance
        """
        # TODO: Add validation
        return self._obj
