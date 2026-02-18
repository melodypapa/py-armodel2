"""DdsDurabilityService AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 530)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DdsDurabilityService(ARObject):
    """AUTOSAR DdsDurabilityService."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    durability: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DdsDurabilityService."""
        super().__init__()
        self.durability: Optional[PositiveInteger] = None


class DdsDurabilityServiceBuilder:
    """Builder for DdsDurabilityService."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsDurabilityService = DdsDurabilityService()

    def build(self) -> DdsDurabilityService:
        """Build and return DdsDurabilityService object.

        Returns:
            DdsDurabilityService instance
        """
        # TODO: Add validation
        return self._obj
