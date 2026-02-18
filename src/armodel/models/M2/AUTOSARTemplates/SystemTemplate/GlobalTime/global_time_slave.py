"""GlobalTimeSlave AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 860)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_connector import (
    CommunicationConnector,
)
from abc import ABC, abstractmethod


class GlobalTimeSlave(Identifiable, ABC):
    """AUTOSAR GlobalTimeSlave."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    communication_connector: Optional[CommunicationConnector]
    follow_up_timeout_value: Optional[TimeValue]
    icv_verification: Optional[Any]
    time_leap_future: Optional[TimeValue]
    time_leap: Optional[PositiveInteger]
    time_leap_past: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize GlobalTimeSlave."""
        super().__init__()
        self.communication_connector: Optional[CommunicationConnector] = None
        self.follow_up_timeout_value: Optional[TimeValue] = None
        self.icv_verification: Optional[Any] = None
        self.time_leap_future: Optional[TimeValue] = None
        self.time_leap: Optional[PositiveInteger] = None
        self.time_leap_past: Optional[TimeValue] = None


class GlobalTimeSlaveBuilder:
    """Builder for GlobalTimeSlave."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: GlobalTimeSlave = GlobalTimeSlave()

    def build(self) -> GlobalTimeSlave:
        """Build and return GlobalTimeSlave object.

        Returns:
            GlobalTimeSlave instance
        """
        # TODO: Add validation
        return self._obj
