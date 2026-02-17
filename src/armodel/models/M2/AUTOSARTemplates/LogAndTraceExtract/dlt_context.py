"""DltContext AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2017)
  - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (page 9)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_LogAndTraceExtract.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.AUTOSARTemplates.LogAndTraceExtract.dlt_message import (
    DltMessage,
)


class DltContext(ARElement):
    """AUTOSAR DltContext."""

    context: Optional[String]
    context_id: Optional[String]
    dlt_messages: list[DltMessage]
    def __init__(self) -> None:
        """Initialize DltContext."""
        super().__init__()
        self.context: Optional[String] = None
        self.context_id: Optional[String] = None
        self.dlt_messages: list[DltMessage] = []


class DltContextBuilder:
    """Builder for DltContext."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DltContext = DltContext()

    def build(self) -> DltContext:
        """Build and return DltContext object.

        Returns:
            DltContext instance
        """
        # TODO: Add validation
        return self._obj
