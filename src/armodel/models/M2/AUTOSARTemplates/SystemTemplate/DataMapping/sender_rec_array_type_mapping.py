"""SenderRecArrayTypeMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 235)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DataMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.sender_rec_composite_type_mapping import (
    SenderRecCompositeTypeMapping,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.text_table_mapping import (
    TextTableMapping,
)


class SenderRecArrayTypeMapping(SenderRecCompositeTypeMapping):
    """AUTOSAR SenderRecArrayTypeMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    array_elements: list[Any]
    sender_to_signal: Optional[TextTableMapping]
    signal_to: Optional[TextTableMapping]
    def __init__(self) -> None:
        """Initialize SenderRecArrayTypeMapping."""
        super().__init__()
        self.array_elements: list[Any] = []
        self.sender_to_signal: Optional[TextTableMapping] = None
        self.signal_to: Optional[TextTableMapping] = None


class SenderRecArrayTypeMappingBuilder:
    """Builder for SenderRecArrayTypeMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SenderRecArrayTypeMapping = SenderRecArrayTypeMapping()

    def build(self) -> SenderRecArrayTypeMapping:
        """Build and return SenderRecArrayTypeMapping object.

        Returns:
            SenderRecArrayTypeMapping instance
        """
        # TODO: Add validation
        return self._obj
