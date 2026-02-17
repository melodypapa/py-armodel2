"""SenderRecRecordElementMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 236)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DataMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "application_record": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (ApplicationRecord),
        ),  # applicationRecord
        "complex_type": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SenderRecCompositeTypeMapping,
        ),  # complexType
        "implementation": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (ImplementationData),
        ),  # implementation
        "sender_to_signal": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TextTableMapping,
        ),  # senderToSignal
        "signal_to": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=TextTableMapping,
        ),  # signalTo
        "system_signal": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SystemSignal,
        ),  # systemSignal
    }

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
