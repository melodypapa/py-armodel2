"""DdsHistory AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 537)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds import (
    DdsHistoryKindEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DdsHistory(ARObject):
    """AUTOSAR DdsHistory."""

    history_kind: Optional[DdsHistoryKindEnum]
    history_order: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DdsHistory."""
        super().__init__()
        self.history_kind: Optional[DdsHistoryKindEnum] = None
        self.history_order: Optional[PositiveInteger] = None


class DdsHistoryBuilder:
    """Builder for DdsHistory."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsHistory = DdsHistory()

    def build(self) -> DdsHistory:
        """Build and return DdsHistory object.

        Returns:
            DdsHistory instance
        """
        # TODO: Add validation
        return self._obj
