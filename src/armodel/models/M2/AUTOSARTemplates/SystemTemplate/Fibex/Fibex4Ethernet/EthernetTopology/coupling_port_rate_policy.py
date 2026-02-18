"""CouplingPortRatePolicy AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 124)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)


class CouplingPortRatePolicy(ARObject):
    """AUTOSAR CouplingPortRatePolicy."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_length: Optional[PositiveInteger]
    policy_action: Optional[CouplingPortRatePolicy]
    priority: Optional[PositiveInteger]
    time_interval: Optional[TimeValue]
    v_lans: list[Any]
    def __init__(self) -> None:
        """Initialize CouplingPortRatePolicy."""
        super().__init__()
        self.data_length: Optional[PositiveInteger] = None
        self.policy_action: Optional[CouplingPortRatePolicy] = None
        self.priority: Optional[PositiveInteger] = None
        self.time_interval: Optional[TimeValue] = None
        self.v_lans: list[Any] = []


class CouplingPortRatePolicyBuilder:
    """Builder for CouplingPortRatePolicy."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CouplingPortRatePolicy = CouplingPortRatePolicy()

    def build(self) -> CouplingPortRatePolicy:
        """Build and return CouplingPortRatePolicy object.

        Returns:
            CouplingPortRatePolicy instance
        """
        # TODO: Add validation
        return self._obj
