"""IEEE1722TpAcfCanPart AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf.ieee1722_tp_acf_bus_part import (
    IEEE1722TpAcfBusPart,
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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("can_addressing", None, False, False, CanAddressingModeType),  # canAddressing
        ("can_bit_rate_switch", None, True, False, None),  # canBitRateSwitch
        ("can_frame_tx_behavior", None, False, False, CanFrameTxBehaviorEnum),  # canFrameTxBehavior
        ("can_identifier", None, False, False, RxIdentifierRange),  # canIdentifier
        ("sdu", None, False, False, PduTriggering),  # sdu
    ]

    def __init__(self) -> None:
        """Initialize IEEE1722TpAcfCanPart."""
        super().__init__()
        self.can_addressing: Optional[CanAddressingModeType] = None
        self.can_bit_rate_switch: Optional[Boolean] = None
        self.can_frame_tx_behavior: Optional[CanFrameTxBehaviorEnum] = None
        self.can_identifier: Optional[RxIdentifierRange] = None
        self.sdu: Optional[PduTriggering] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert IEEE1722TpAcfCanPart to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IEEE1722TpAcfCanPart":
        """Create IEEE1722TpAcfCanPart from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            IEEE1722TpAcfCanPart instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to IEEE1722TpAcfCanPart since parent returns ARObject
        return cast("IEEE1722TpAcfCanPart", obj)


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
