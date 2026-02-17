"""DdsLiveliness AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 534)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds import (
    DdsLivenessKindEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Float,
)


class DdsLiveliness(ARObject):
    """AUTOSAR DdsLiveliness."""

    liveliness_lease: Optional[Float]
    liveness_kind: Optional[DdsLivenessKindEnum]
    def __init__(self) -> None:
        """Initialize DdsLiveliness."""
        super().__init__()
        self.liveliness_lease: Optional[Float] = None
        self.liveness_kind: Optional[DdsLivenessKindEnum] = None


class DdsLivelinessBuilder:
    """Builder for DdsLiveliness."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsLiveliness = DdsLiveliness()

    def build(self) -> DdsLiveliness:
        """Build and return DdsLiveliness object.

        Returns:
            DdsLiveliness instance
        """
        # TODO: Add validation
        return self._obj
