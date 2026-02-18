"""CanClusterBusOffRecovery AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 62)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)


class CanClusterBusOffRecovery(ARObject):
    """AUTOSAR CanClusterBusOffRecovery."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    bor_counter_l1_to: Optional[PositiveInteger]
    bor_time_l1: Optional[TimeValue]
    bor_time_l2: Optional[TimeValue]
    bor_time_tx: Optional[TimeValue]
    main_function: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize CanClusterBusOffRecovery."""
        super().__init__()
        self.bor_counter_l1_to: Optional[PositiveInteger] = None
        self.bor_time_l1: Optional[TimeValue] = None
        self.bor_time_l2: Optional[TimeValue] = None
        self.bor_time_tx: Optional[TimeValue] = None
        self.main_function: Optional[TimeValue] = None


class CanClusterBusOffRecoveryBuilder:
    """Builder for CanClusterBusOffRecovery."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanClusterBusOffRecovery = CanClusterBusOffRecovery()

    def build(self) -> CanClusterBusOffRecovery:
        """Build and return CanClusterBusOffRecovery object.

        Returns:
            CanClusterBusOffRecovery instance
        """
        # TODO: Add validation
        return self._obj
