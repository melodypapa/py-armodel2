"""TtcanCommunicationController AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 76)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ttcan_TtcanTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
)


class TtcanCommunicationController(ARObject):
    """AUTOSAR TtcanCommunicationController."""

    appl_watchdog: Optional[Integer]
    expected_tx: Optional[Integer]
    external_clock: Optional[Boolean]
    initial_ref_offset: Optional[Integer]
    master: Optional[Boolean]
    time_master: Optional[Integer]
    time_triggered: Optional[Integer]
    tx_enable: Optional[Integer]
    def __init__(self) -> None:
        """Initialize TtcanCommunicationController."""
        super().__init__()
        self.appl_watchdog: Optional[Integer] = None
        self.expected_tx: Optional[Integer] = None
        self.external_clock: Optional[Boolean] = None
        self.initial_ref_offset: Optional[Integer] = None
        self.master: Optional[Boolean] = None
        self.time_master: Optional[Integer] = None
        self.time_triggered: Optional[Integer] = None
        self.tx_enable: Optional[Integer] = None


class TtcanCommunicationControllerBuilder:
    """Builder for TtcanCommunicationController."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TtcanCommunicationController = TtcanCommunicationController()

    def build(self) -> TtcanCommunicationController:
        """Build and return TtcanCommunicationController object.

        Returns:
            TtcanCommunicationController instance
        """
        # TODO: Add validation
        return self._obj
