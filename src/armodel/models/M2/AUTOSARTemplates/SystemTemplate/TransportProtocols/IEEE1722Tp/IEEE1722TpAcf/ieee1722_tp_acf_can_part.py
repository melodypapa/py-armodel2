"""IEEE1722TpAcfCanPart AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 661)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols_IEEE1722Tp_IEEE1722TpAcf.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf.ieee1722_tp_acf_bus_part import (
    IEEE1722TpAcfBusPart,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication import (
    CanAddressingModeType,
    CanFrameTxBehaviorEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanCommunication.rx_identifier_range import (
    RxIdentifierRange,
)


class IEEE1722TpAcfCanPart(IEEE1722TpAcfBusPart):
    """AUTOSAR IEEE1722TpAcfCanPart."""

    can_addressing: Optional[CanAddressingModeType]
    can_bit_rate_switch: Optional[Boolean]
    can_frame_tx_behavior: Optional[CanFrameTxBehaviorEnum]
    can_identifier: Optional[RxIdentifierRange]
    sdu: Optional[PduTriggering]
    def __init__(self) -> None:
        """Initialize IEEE1722TpAcfCanPart."""
        super().__init__()
        self.can_addressing: Optional[CanAddressingModeType] = None
        self.can_bit_rate_switch: Optional[Boolean] = None
        self.can_frame_tx_behavior: Optional[CanFrameTxBehaviorEnum] = None
        self.can_identifier: Optional[RxIdentifierRange] = None
        self.sdu: Optional[PduTriggering] = None


class IEEE1722TpAcfCanPartBuilder:
    """Builder for IEEE1722TpAcfCanPart."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IEEE1722TpAcfCanPart = IEEE1722TpAcfCanPart()

    def build(self) -> IEEE1722TpAcfCanPart:
        """Build and return IEEE1722TpAcfCanPart object.

        Returns:
            IEEE1722TpAcfCanPart instance
        """
        # TODO: Add validation
        return self._obj
