"""DdsLatencyBudget AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 532)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Float,
)


class DdsLatencyBudget(ARObject):
    """AUTOSAR DdsLatencyBudget."""

    def __init__(self) -> None:
        """Initialize DdsLatencyBudget."""
        super().__init__()
        self.latency_budget: Optional[Float] = None


class DdsLatencyBudgetBuilder:
    """Builder for DdsLatencyBudget."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsLatencyBudget = DdsLatencyBudget()

    def build(self) -> DdsLatencyBudget:
        """Build and return DdsLatencyBudget object.

        Returns:
            DdsLatencyBudget instance
        """
        # TODO: Add validation
        return self._obj
