"""SenderReceiverCompositeElementToSignalMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 247)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DataMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.data_mapping import (
    DataMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.sender_rec_composite_type_mapping import (
    SenderRecCompositeTypeMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.system_signal import (
    SystemSignal,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class SenderReceiverCompositeElementToSignalMapping(DataMapping):
    """AUTOSAR SenderReceiverCompositeElementToSignalMapping."""

    def __init__(self) -> None:
        """Initialize SenderReceiverCompositeElementToSignalMapping."""
        super().__init__()
        self.data_element: Optional[VariableDataPrototype] = None
        self.system_signal: Optional[SystemSignal] = None
        self.type_mapping: Optional[SenderRecCompositeTypeMapping] = None


class SenderReceiverCompositeElementToSignalMappingBuilder:
    """Builder for SenderReceiverCompositeElementToSignalMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SenderReceiverCompositeElementToSignalMapping = SenderReceiverCompositeElementToSignalMapping()

    def build(self) -> SenderReceiverCompositeElementToSignalMapping:
        """Build and return SenderReceiverCompositeElementToSignalMapping object.

        Returns:
            SenderReceiverCompositeElementToSignalMapping instance
        """
        # TODO: Add validation
        return self._obj
