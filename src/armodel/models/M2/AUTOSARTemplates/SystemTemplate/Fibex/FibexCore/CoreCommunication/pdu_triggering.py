"""PduTriggering AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 303)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 348)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 234)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu_port import (
    IPduPort,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_triggering import (
    ISignalTriggering,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu import (
    Pdu,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.sec_oc_crypto_service_mapping import (
    SecOcCryptoServiceMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing.trigger_i_pdu_send_condition import (
    TriggerIPduSendCondition,
)


class PduTriggering(Identifiable):
    """AUTOSAR PduTriggering."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    i_pdu: Optional[Pdu]
    i_pdu_ports: list[IPduPort]
    i_signals: list[ISignalTriggering]
    sec_oc_crypto_service: Optional[SecOcCryptoServiceMapping]
    trigger_i_pdu_sends: list[TriggerIPduSendCondition]
    def __init__(self) -> None:
        """Initialize PduTriggering."""
        super().__init__()
        self.i_pdu: Optional[Pdu] = None
        self.i_pdu_ports: list[IPduPort] = []
        self.i_signals: list[ISignalTriggering] = []
        self.sec_oc_crypto_service: Optional[SecOcCryptoServiceMapping] = None
        self.trigger_i_pdu_sends: list[TriggerIPduSendCondition] = []


class PduTriggeringBuilder:
    """Builder for PduTriggering."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PduTriggering = PduTriggering()

    def build(self) -> PduTriggering:
        """Build and return PduTriggering object.

        Returns:
            PduTriggering instance
        """
        # TODO: Add validation
        return self._obj
