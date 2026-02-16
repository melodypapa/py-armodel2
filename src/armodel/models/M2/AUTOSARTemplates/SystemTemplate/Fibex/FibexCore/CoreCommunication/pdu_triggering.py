"""PduTriggering AUTOSAR element."""

from typing import Optional, cast
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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("i_pdu", None, False, False, Pdu),  # iPdu
        ("i_pdu_ports", None, False, True, IPduPort),  # iPduPorts
        ("i_signals", None, False, True, ISignalTriggering),  # iSignals
        ("sec_oc_crypto_service", None, False, False, SecOcCryptoServiceMapping),  # secOcCryptoService
        ("trigger_i_pdu_sends", None, False, True, TriggerIPduSendCondition),  # triggerIPduSends
    ]

    def __init__(self) -> None:
        """Initialize PduTriggering."""
        super().__init__()
        self.i_pdu: Optional[Pdu] = None
        self.i_pdu_ports: list[IPduPort] = []
        self.i_signals: list[ISignalTriggering] = []
        self.sec_oc_crypto_service: Optional[SecOcCryptoServiceMapping] = None
        self.trigger_i_pdu_sends: list[TriggerIPduSendCondition] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert PduTriggering to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PduTriggering":
        """Create PduTriggering from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            PduTriggering instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to PduTriggering since parent returns ARObject
        return cast("PduTriggering", obj)


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
