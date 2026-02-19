"""DltLogChannel AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 722)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Dlt.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Dlt import (
    DltDefaultTraceStateEnum,
    LogTraceDefaultLogLevelEnum,
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    applications: list[DltContext]
    default_trace: Optional[DltDefaultTraceStateEnum]
    dlt_messages: list[DltMessage]
    log_channel_id: Optional[String]
    log_trace_default_log: Optional[LogTraceDefaultLogLevelEnum]
    non_verbose: Optional[Boolean]
    rx_pdu_triggering_channel_ref: Optional[ARRef]
    segmentation: Optional[Boolean]
    tx_pdu_triggering_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize DltLogChannel."""
        super().__init__()
        self.applications: list[DltContext] = []
        self.default_trace: Optional[DltDefaultTraceStateEnum] = None
        self.dlt_messages: list[DltMessage] = []
        self.log_channel_id: Optional[String] = None
        self.log_trace_default_log: Optional[LogTraceDefaultLogLevelEnum] = None
        self.non_verbose: Optional[Boolean] = None
        self.rx_pdu_triggering_channel_ref: Optional[ARRef] = None
        self.segmentation: Optional[Boolean] = None
        self.tx_pdu_triggering_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DltLogChannel":
        """Deserialize XML element to DltLogChannel object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DltLogChannel object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse applications (list)
        obj.applications = []
        for child in ARObject._find_all_child_elements(element, "APPLICATIONS"):
            applications_value = ARObject._deserialize_by_tag(child, "DltContext")
            obj.applications.append(applications_value)

        # Parse default_trace
        child = ARObject._find_child_element(element, "DEFAULT-TRACE")
        if child is not None:
            default_trace_value = child.text
            obj.default_trace = default_trace_value

        # Parse dlt_messages (list)
        obj.dlt_messages = []
        for child in ARObject._find_all_child_elements(element, "DLT-MESSAGES"):
            dlt_messages_value = ARObject._deserialize_by_tag(child, "DltMessage")
            obj.dlt_messages.append(dlt_messages_value)

        # Parse log_channel_id
        child = ARObject._find_child_element(element, "LOG-CHANNEL-ID")
        if child is not None:
            log_channel_id_value = child.text
            obj.log_channel_id = log_channel_id_value

        # Parse log_trace_default_log
        child = ARObject._find_child_element(element, "LOG-TRACE-DEFAULT-LOG")
        if child is not None:
            log_trace_default_log_value = child.text
            obj.log_trace_default_log = log_trace_default_log_value

        # Parse non_verbose
        child = ARObject._find_child_element(element, "NON-VERBOSE")
        if child is not None:
            non_verbose_value = child.text
            obj.non_verbose = non_verbose_value

        # Parse rx_pdu_triggering_channel_ref
        child = ARObject._find_child_element(element, "RX-PDU-TRIGGERING-CHANNEL")
        if child is not None:
            rx_pdu_triggering_channel_ref_value = ARObject._deserialize_by_tag(child, "PduTriggering")
            obj.rx_pdu_triggering_channel_ref = rx_pdu_triggering_channel_ref_value

        # Parse segmentation
        child = ARObject._find_child_element(element, "SEGMENTATION")
        if child is not None:
            segmentation_value = child.text
            obj.segmentation = segmentation_value

        # Parse tx_pdu_triggering_ref
        child = ARObject._find_child_element(element, "TX-PDU-TRIGGERING")
        if child is not None:
            tx_pdu_triggering_ref_value = ARObject._deserialize_by_tag(child, "PduTriggering")
            obj.tx_pdu_triggering_ref = tx_pdu_triggering_ref_value

        return obj



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
