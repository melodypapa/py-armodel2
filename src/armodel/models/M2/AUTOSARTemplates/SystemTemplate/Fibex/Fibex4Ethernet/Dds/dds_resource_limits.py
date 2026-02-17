"""DdsResourceLimits AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 537)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DdsResourceLimits(ARObject):
    """AUTOSAR DdsResourceLimits."""

    max_instances: Optional[PositiveInteger]
    max_samples: Optional[PositiveInteger]
    max_samples_per_instance: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DdsResourceLimits."""
        super().__init__()
        self.max_instances: Optional[PositiveInteger] = None
        self.max_samples: Optional[PositiveInteger] = None
        self.max_samples_per_instance: Optional[PositiveInteger] = None


class DdsResourceLimitsBuilder:
    """Builder for DdsResourceLimits."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsResourceLimits = DdsResourceLimits()

    def build(self) -> DdsResourceLimits:
        """Build and return DdsResourceLimits object.

        Returns:
            DdsResourceLimits instance
        """
        # TODO: Add validation
        return self._obj
