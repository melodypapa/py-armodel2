"""VlanConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 106)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class VlanConfig(Identifiable):
    """AUTOSAR VlanConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    vlan_identifier: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize VlanConfig."""
        super().__init__()
        self.vlan_identifier: Optional[PositiveInteger] = None


class VlanConfigBuilder:
    """Builder for VlanConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: VlanConfig = VlanConfig()

    def build(self) -> VlanConfig:
        """Build and return VlanConfig object.

        Returns:
            VlanConfig instance
        """
        # TODO: Add validation
        return self._obj
