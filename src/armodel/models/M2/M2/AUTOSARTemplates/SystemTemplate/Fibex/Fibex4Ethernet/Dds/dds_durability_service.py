"""DdsDurabilityService AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 530)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DdsDurabilityService(ARObject):
    """AUTOSAR DdsDurabilityService."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "durability": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # durability
    }

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
