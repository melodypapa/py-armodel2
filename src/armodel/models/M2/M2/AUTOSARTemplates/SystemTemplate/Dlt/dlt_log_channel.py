"""DltLogChannel AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 722)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Dlt.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "applications": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=DltContext,
        ),  # applications
        "default_trace": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DltDefaultTraceStateEnum,
        ),  # defaultTrace
        "dlt_messages": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=DltMessage,
        ),  # dltMessages
        "log_channel_id": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # logChannelId
        "log_trace_default_log": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=LogTraceDefaultLogLevelEnum,
        ),  # logTraceDefaultLog
        "non_verbose": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # nonVerbose
        "rx_pdu_triggering_channel": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=PduTriggering,
        ),  # rxPduTriggeringChannel
        "segmentation": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # segmentation
        "tx_pdu_triggering": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=PduTriggering,
        ),  # txPduTriggering
    }

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
