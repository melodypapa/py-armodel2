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
