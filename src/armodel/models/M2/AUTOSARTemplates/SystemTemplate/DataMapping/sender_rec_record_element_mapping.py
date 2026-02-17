"""SenderRecRecordElementMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 236)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DataMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.sender_rec_composite_type_mapping import (
    SenderRecCompositeTypeMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.system_signal import (
    SystemSignal,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.text_table_mapping import (
    TextTableMapping,
)


class SenderRecRecordElementMapping(ARObject):
    """AUTOSAR SenderRecRecordElementMapping."""

    application_record: Optional[Any]
    complex_type: Optional[SenderRecCompositeTypeMapping]
    implementation: Optional[Any]
    sender_to_signal: Optional[TextTableMapping]
    signal_to: Optional[TextTableMapping]
    system_signal: Optional[SystemSignal]
    def __init__(self) -> None:
        """Initialize SenderRecRecordElementMapping."""
        super().__init__()
        self.application_record: Optional[Any] = None
        self.complex_type: Optional[SenderRecCompositeTypeMapping] = None
        self.implementation: Optional[Any] = None
        self.sender_to_signal: Optional[TextTableMapping] = None
        self.signal_to: Optional[TextTableMapping] = None
        self.system_signal: Optional[SystemSignal] = None


class SenderRecRecordElementMappingBuilder:
    """Builder for SenderRecRecordElementMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SenderRecRecordElementMapping = SenderRecRecordElementMapping()

    def build(self) -> SenderRecRecordElementMapping:
        """Build and return SenderRecRecordElementMapping object.

        Returns:
            SenderRecRecordElementMapping instance
        """
        # TODO: Add validation
        return self._obj
