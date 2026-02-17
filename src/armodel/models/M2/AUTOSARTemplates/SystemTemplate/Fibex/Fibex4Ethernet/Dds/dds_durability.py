"""DdsDurability AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 530)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds import (
    DdsDurabilityKindEnum,
)


class DdsDurability(ARObject):
    """AUTOSAR DdsDurability."""

    durability_kind: Optional[DdsDurabilityKindEnum]
    def __init__(self) -> None:
        """Initialize DdsDurability."""
        super().__init__()
        self.durability_kind: Optional[DdsDurabilityKindEnum] = None


class DdsDurabilityBuilder:
    """Builder for DdsDurability."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsDurability = DdsDurability()

    def build(self) -> DdsDurability:
        """Build and return DdsDurability object.

        Returns:
            DdsDurability instance
        """
        # TODO: Add validation
        return self._obj
