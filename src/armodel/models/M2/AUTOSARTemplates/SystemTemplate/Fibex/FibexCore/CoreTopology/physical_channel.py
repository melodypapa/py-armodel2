"""PhysicalChannel AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_connector import (
    CommunicationConnector,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.frame_triggering import (
    FrameTriggering,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_triggering import (
    ISignalTriggering,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import (
    PhysicalChannel,
)


class PhysicalChannel(Identifiable):
    """AUTOSAR PhysicalChannel."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("comm_connectors", None, False, True, CommunicationConnector),  # commConnectors
        ("frame_triggerings", None, False, True, FrameTriggering),  # frameTriggerings
        ("i_signals", None, False, True, ISignalTriggering),  # iSignals
        ("manageds", None, False, True, PhysicalChannel),  # manageds
        ("pdu_triggerings", None, False, True, PduTriggering),  # pduTriggerings
    ]

    def __init__(self) -> None:
        """Initialize PhysicalChannel."""
        super().__init__()
        self.comm_connectors: list[CommunicationConnector] = []
        self.frame_triggerings: list[FrameTriggering] = []
        self.i_signals: list[ISignalTriggering] = []
        self.manageds: list[PhysicalChannel] = []
        self.pdu_triggerings: list[PduTriggering] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert PhysicalChannel to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PhysicalChannel":
        """Create PhysicalChannel from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            PhysicalChannel instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to PhysicalChannel since parent returns ARObject
        return cast("PhysicalChannel", obj)


class PhysicalChannelBuilder:
    """Builder for PhysicalChannel."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PhysicalChannel = PhysicalChannel()

    def build(self) -> PhysicalChannel:
        """Build and return PhysicalChannel object.

        Returns:
            PhysicalChannel instance
        """
        # TODO: Add validation
        return self._obj
