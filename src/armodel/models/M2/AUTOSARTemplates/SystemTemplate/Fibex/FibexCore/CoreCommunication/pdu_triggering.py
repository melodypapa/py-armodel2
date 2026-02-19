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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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
    i_signal_refs: list[ARRef]
    sec_oc_crypto_service: Optional[SecOcCryptoServiceMapping]
    trigger_i_pdu_send_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize PduTriggering."""
        super().__init__()
        self.i_pdu: Optional[Pdu] = None
        self.i_pdu_ports: list[IPduPort] = []
        self.i_signal_refs: list[ARRef] = []
        self.sec_oc_crypto_service: Optional[SecOcCryptoServiceMapping] = None
        self.trigger_i_pdu_send_refs: list[ARRef] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "PduTriggering":
        """Deserialize XML element to PduTriggering object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PduTriggering object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PduTriggering, cls).deserialize(element)

        # Parse i_pdu
        child = ARObject._find_child_element(element, "I-PDU")
        if child is not None:
            i_pdu_value = ARObject._deserialize_by_tag(child, "Pdu")
            obj.i_pdu = i_pdu_value

        # Parse i_pdu_ports (list from container "I-PDU-PORTS")
        obj.i_pdu_ports = []
        container = ARObject._find_child_element(element, "I-PDU-PORTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.i_pdu_ports.append(child_value)

        # Parse i_signal_refs (list from container "I-SIGNALS")
        obj.i_signal_refs = []
        container = ARObject._find_child_element(element, "I-SIGNALS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.i_signal_refs.append(child_value)

        # Parse sec_oc_crypto_service
        child = ARObject._find_child_element(element, "SEC-OC-CRYPTO-SERVICE")
        if child is not None:
            sec_oc_crypto_service_value = ARObject._deserialize_by_tag(child, "SecOcCryptoServiceMapping")
            obj.sec_oc_crypto_service = sec_oc_crypto_service_value

        # Parse trigger_i_pdu_send_refs (list from container "TRIGGER-I-PDU-SENDS")
        obj.trigger_i_pdu_send_refs = []
        container = ARObject._find_child_element(element, "TRIGGER-I-PDU-SENDS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.trigger_i_pdu_send_refs.append(child_value)

        return obj



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
