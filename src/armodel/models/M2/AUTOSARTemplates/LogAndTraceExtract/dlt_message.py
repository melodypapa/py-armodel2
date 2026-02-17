"""DltMessage AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2018)
  - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (page 12)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_LogAndTraceExtract.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)
from armodel.models.M2.AUTOSARTemplates.LogAndTraceExtract.dlt_argument import (
    DltArgument,
)
from armodel.models.M2.AUTOSARTemplates.LogAndTraceExtract.privacy_level import (
    PrivacyLevel,
)


class DltMessage(Identifiable):
    """AUTOSAR DltMessage."""

    dlt_arguments: list[DltArgument]
    message_id: Optional[PositiveInteger]
    message_line: Optional[PositiveInteger]
    message_source: Optional[String]
    message_type_info: Optional[String]
    privacy_level: Optional[PrivacyLevel]
    def __init__(self) -> None:
        """Initialize DltMessage."""
        super().__init__()
        self.dlt_arguments: list[DltArgument] = []
        self.message_id: Optional[PositiveInteger] = None
        self.message_line: Optional[PositiveInteger] = None
        self.message_source: Optional[String] = None
        self.message_type_info: Optional[String] = None
        self.privacy_level: Optional[PrivacyLevel] = None


class DltMessageBuilder:
    """Builder for DltMessage."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DltMessage = DltMessage()

    def build(self) -> DltMessage:
        """Build and return DltMessage object.

        Returns:
            DltMessage instance
        """
        # TODO: Add validation
        return self._obj
