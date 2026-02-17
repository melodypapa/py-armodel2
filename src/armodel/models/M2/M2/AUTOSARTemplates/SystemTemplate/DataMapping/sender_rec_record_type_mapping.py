"""SenderRecRecordTypeMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 235)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DataMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.sender_rec_composite_type_mapping import (
    SenderRecCompositeTypeMapping,
)


class SenderRecRecordTypeMapping(SenderRecCompositeTypeMapping):
    """AUTOSAR SenderRecRecordTypeMapping."""

    def __init__(self) -> None:
        """Initialize SenderRecRecordTypeMapping."""
        super().__init__()
        self.record_elements: list[Any] = []


class SenderRecRecordTypeMappingBuilder:
    """Builder for SenderRecRecordTypeMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SenderRecRecordTypeMapping = SenderRecRecordTypeMapping()

    def build(self) -> SenderRecRecordTypeMapping:
        """Build and return SenderRecRecordTypeMapping object.

        Returns:
            SenderRecRecordTypeMapping instance
        """
        # TODO: Add validation
        return self._obj
