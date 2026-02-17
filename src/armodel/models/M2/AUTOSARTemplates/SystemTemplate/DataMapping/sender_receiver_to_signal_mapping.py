"""SenderReceiverToSignalMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 1005)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 229)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DataMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.data_mapping import (
    DataMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.system_signal import (
    SystemSignal,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.text_table_mapping import (
    TextTableMapping,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class SenderReceiverToSignalMapping(DataMapping):
    """AUTOSAR SenderReceiverToSignalMapping."""

    data_element_system_instance_ref: Optional[VariableDataPrototype]
    sender_to_signal: Optional[TextTableMapping]
    signal_to: Optional[TextTableMapping]
    system_signal: Optional[SystemSignal]
    def __init__(self) -> None:
        """Initialize SenderReceiverToSignalMapping."""
        super().__init__()
        self.data_element_system_instance_ref: Optional[VariableDataPrototype] = None
        self.sender_to_signal: Optional[TextTableMapping] = None
        self.signal_to: Optional[TextTableMapping] = None
        self.system_signal: Optional[SystemSignal] = None


class SenderReceiverToSignalMappingBuilder:
    """Builder for SenderReceiverToSignalMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SenderReceiverToSignalMapping = SenderReceiverToSignalMapping()

    def build(self) -> SenderReceiverToSignalMapping:
        """Build and return SenderReceiverToSignalMapping object.

        Returns:
            SenderReceiverToSignalMapping instance
        """
        # TODO: Add validation
        return self._obj
