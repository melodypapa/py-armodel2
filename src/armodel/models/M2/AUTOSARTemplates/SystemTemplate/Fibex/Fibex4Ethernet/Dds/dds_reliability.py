"""DdsReliability AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 534)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds import (
    DdsReliabilityKindEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Float,
)


class DdsReliability(ARObject):
    """AUTOSAR DdsReliability."""

    def __init__(self) -> None:
        """Initialize DdsReliability."""
        super().__init__()
        self.reliability_kind: Optional[DdsReliabilityKindEnum] = None
        self.reliability_max: Optional[Float] = None


class DdsReliabilityBuilder:
    """Builder for DdsReliability."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsReliability = DdsReliability()

    def build(self) -> DdsReliability:
        """Build and return DdsReliability object.

        Returns:
            DdsReliability instance
        """
        # TODO: Add validation
        return self._obj
