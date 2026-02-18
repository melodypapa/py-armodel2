"""CanFrameTriggering AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 443)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.frame_triggering import (
    FrameTriggering,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication import (
    CanAddressingModeType,
    CanFrameRxBehaviorEnum,
    CanFrameTxBehaviorEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication.can_xl_frame_triggering_props import (
    CanXlFrameTriggeringProps,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication.rx_identifier_range import (
    RxIdentifierRange,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ttcan.TtcanCommunication.ttcan_absolutely_scheduled_timing import (
    TtcanAbsolutelyScheduledTiming,
)


class CanFrameTriggering(FrameTriggering):
    """AUTOSAR CanFrameTriggering."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    absolutelies: list[TtcanAbsolutelyScheduledTiming]
    can_addressing: Optional[CanAddressingModeType]
    can_frame_rx_behavior: Optional[CanFrameRxBehaviorEnum]
    can_frame_tx_behavior: Optional[CanFrameTxBehaviorEnum]
    can_xl_frame_ref: Optional[ARRef]
    identifier: Optional[Integer]
    j1939requestable: Optional[Boolean]
    rx_identifier_range_range: Optional[RxIdentifierRange]
    rx_mask: Optional[PositiveInteger]
    tx_mask: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize CanFrameTriggering."""
        super().__init__()
        self.absolutelies: list[TtcanAbsolutelyScheduledTiming] = []
        self.can_addressing: Optional[CanAddressingModeType] = None
        self.can_frame_rx_behavior: Optional[CanFrameRxBehaviorEnum] = None
        self.can_frame_tx_behavior: Optional[CanFrameTxBehaviorEnum] = None
        self.can_xl_frame_ref: Optional[ARRef] = None
        self.identifier: Optional[Integer] = None
        self.j1939requestable: Optional[Boolean] = None
        self.rx_identifier_range_range: Optional[RxIdentifierRange] = None
        self.rx_mask: Optional[PositiveInteger] = None
        self.tx_mask: Optional[PositiveInteger] = None


class CanFrameTriggeringBuilder:
    """Builder for CanFrameTriggering."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanFrameTriggering = CanFrameTriggering()

    def build(self) -> CanFrameTriggering:
        """Build and return CanFrameTriggering object.

        Returns:
            CanFrameTriggering instance
        """
        # TODO: Add validation
        return self._obj
