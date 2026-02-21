"""FlexrayCommunicationController AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 84)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 446)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Flexray_FlexrayTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET
from armodel.serialization.decorators import atp_variant

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    PositiveInteger,
    TimeValue,
)


@atp_variant()

class FlexrayCommunicationController(ARObject):
    """AUTOSAR FlexrayCommunicationController."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    accepted: Optional[Integer]
    allow_halt_due_to: Optional[Boolean]
    allow_passive_to: Optional[Integer]
    cluster_drift: Optional[Integer]
    decoding: Optional[Integer]
    delay: Optional[Integer]
    external_sync: Optional[Boolean]
    extern_offset: Optional[Integer]
    extern_rate: Optional[Integer]
    fall_back_internal: Optional[Boolean]
    flexray_fifos: list[Any]
    key_slot_id: Optional[PositiveInteger]
    key_slot_only: Optional[Boolean]
    key_slot_used_for: Optional[Boolean]
    latest_tx: Optional[Integer]
    listen_timeout: Optional[Integer]
    macro_initial: Optional[Integer]
    maximum: Optional[Integer]
    micro_initial: Optional[Integer]
    micro_per_cycle: Optional[Integer]
    microtick: Optional[TimeValue]
    nm_vector_early: Optional[Boolean]
    offset_correction: Optional[Integer]
    rate_correction: Optional[Integer]
    samples_per_microtick: Optional[Integer]
    second_key_slot: Optional[PositiveInteger]
    two_key_slot: Optional[Boolean]
    wake_up_pattern: Optional[Integer]
    def __init__(self) -> None:
        """Initialize FlexrayCommunicationController."""
        super().__init__()
        self.accepted: Optional[Integer] = None
        self.allow_halt_due_to: Optional[Boolean] = None
        self.allow_passive_to: Optional[Integer] = None
        self.cluster_drift: Optional[Integer] = None
        self.decoding: Optional[Integer] = None
        self.delay: Optional[Integer] = None
        self.external_sync: Optional[Boolean] = None
        self.extern_offset: Optional[Integer] = None
        self.extern_rate: Optional[Integer] = None
        self.fall_back_internal: Optional[Boolean] = None
        self.flexray_fifos: list[Any] = []
        self.key_slot_id: Optional[PositiveInteger] = None
        self.key_slot_only: Optional[Boolean] = None
        self.key_slot_used_for: Optional[Boolean] = None
        self.latest_tx: Optional[Integer] = None
        self.listen_timeout: Optional[Integer] = None
        self.macro_initial: Optional[Integer] = None
        self.maximum: Optional[Integer] = None
        self.micro_initial: Optional[Integer] = None
        self.micro_per_cycle: Optional[Integer] = None
        self.microtick: Optional[TimeValue] = None
        self.nm_vector_early: Optional[Boolean] = None
        self.offset_correction: Optional[Integer] = None
        self.rate_correction: Optional[Integer] = None
        self.samples_per_microtick: Optional[Integer] = None
        self.second_key_slot: Optional[PositiveInteger] = None
        self.two_key_slot: Optional[Boolean] = None
        self.wake_up_pattern: Optional[Integer] = None



class FlexrayCommunicationControllerBuilder:
    """Builder for FlexrayCommunicationController."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayCommunicationController = FlexrayCommunicationController()

    def build(self) -> FlexrayCommunicationController:
        """Build and return FlexrayCommunicationController object.

        Returns:
            FlexrayCommunicationController instance
        """
        # TODO: Add validation
        return self._obj
