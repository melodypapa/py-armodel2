"""DltLogChannel AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    String,
)
from armodel.models.M2.AUTOSARTemplates.LogAndTraceExtract.dlt_context import (
    DltContext,
)
from armodel.models.M2.AUTOSARTemplates.LogAndTraceExtract.dlt_message import (
    DltMessage,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)


class DltLogChannel(Identifiable):
    """AUTOSAR DltLogChannel."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("applications", None, False, True, DltContext),  # applications
        ("default_trace", None, False, False, DltDefaultTraceStateEnum),  # defaultTrace
        ("dlt_messages", None, False, True, DltMessage),  # dltMessages
        ("log_channel_id", None, True, False, None),  # logChannelId
        ("log_trace_default_log", None, False, False, LogTraceDefaultLogLevelEnum),  # logTraceDefaultLog
        ("non_verbose", None, True, False, None),  # nonVerbose
        ("rx_pdu_triggering_channel", None, False, False, PduTriggering),  # rxPduTriggeringChannel
        ("segmentation", None, True, False, None),  # segmentation
        ("tx_pdu_triggering", None, False, False, PduTriggering),  # txPduTriggering
    ]

    def __init__(self) -> None:
        """Initialize DltLogChannel."""
        super().__init__()
        self.applications: list[DltContext] = []
        self.default_trace: Optional[DltDefaultTraceStateEnum] = None
        self.dlt_messages: list[DltMessage] = []
        self.log_channel_id: Optional[String] = None
        self.log_trace_default_log: Optional[LogTraceDefaultLogLevelEnum] = None
        self.non_verbose: Optional[Boolean] = None
        self.rx_pdu_triggering_channel: Optional[PduTriggering] = None
        self.segmentation: Optional[Boolean] = None
        self.tx_pdu_triggering: Optional[PduTriggering] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DltLogChannel to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DltLogChannel":
        """Create DltLogChannel from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DltLogChannel instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DltLogChannel since parent returns ARObject
        return cast("DltLogChannel", obj)


class DltLogChannelBuilder:
    """Builder for DltLogChannel."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DltLogChannel = DltLogChannel()

    def build(self) -> DltLogChannel:
        """Build and return DltLogChannel object.

        Returns:
            DltLogChannel instance
        """
        # TODO: Add validation
        return self._obj
