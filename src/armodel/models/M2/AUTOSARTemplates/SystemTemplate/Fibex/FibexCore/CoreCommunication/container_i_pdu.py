"""ContainerIPdu AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.contained_i_pdu_props import (
    ContainedIPduProps,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)


class ContainerIPdu(IPdu):
    """AUTOSAR ContainerIPdu."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("contained_i_pdu_propses", None, False, True, ContainedIPduProps),  # containedIPduPropses
        ("contained_pdus", None, False, True, PduTriggering),  # containedPdus
        ("container", None, True, False, None),  # container
        ("container_trigger", None, False, False, ContainerIPduTriggerEnum),  # containerTrigger
        ("header_type", None, False, False, ContainerIPduHeaderTypeEnum),  # headerType
        ("minimum_rx", None, True, False, None),  # minimumRx
        ("minimum_tx", None, True, False, None),  # minimumTx
        ("rx_accept", None, False, False, RxAcceptContainedIPduEnum),  # rxAccept
        ("threshold_size", None, True, False, None),  # thresholdSize
        ("unused_bit", None, True, False, None),  # unusedBit
    ]

    def __init__(self) -> None:
        """Initialize ContainerIPdu."""
        super().__init__()
        self.contained_i_pdu_propses: list[ContainedIPduProps] = []
        self.contained_pdus: list[PduTriggering] = []
        self.container: Optional[TimeValue] = None
        self.container_trigger: Optional[ContainerIPduTriggerEnum] = None
        self.header_type: Optional[ContainerIPduHeaderTypeEnum] = None
        self.minimum_rx: Optional[PositiveInteger] = None
        self.minimum_tx: Optional[PositiveInteger] = None
        self.rx_accept: Optional[RxAcceptContainedIPduEnum] = None
        self.threshold_size: Optional[PositiveInteger] = None
        self.unused_bit: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ContainerIPdu to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ContainerIPdu":
        """Create ContainerIPdu from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ContainerIPdu instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ContainerIPdu since parent returns ARObject
        return cast("ContainerIPdu", obj)


class ContainerIPduBuilder:
    """Builder for ContainerIPdu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ContainerIPdu = ContainerIPdu()

    def build(self) -> ContainerIPdu:
        """Build and return ContainerIPdu object.

        Returns:
            ContainerIPdu instance
        """
        # TODO: Add validation
        return self._obj
