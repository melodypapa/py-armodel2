"""DltApplication AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2017)
  - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (page 8)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_LogAndTraceExtract.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.AUTOSARTemplates.LogAndTraceExtract.dlt_context import (
    DltContext,
)


class DltApplication(Identifiable):
    """AUTOSAR DltApplication."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    application: Optional[String]
    application_id: Optional[String]
    contexts: list[DltContext]
    def __init__(self) -> None:
        """Initialize DltApplication."""
        super().__init__()
        self.application: Optional[String] = None
        self.application_id: Optional[String] = None
        self.contexts: list[DltContext] = []


class DltApplicationBuilder:
    """Builder for DltApplication."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DltApplication = DltApplication()

    def build(self) -> DltApplication:
        """Build and return DltApplication object.

        Returns:
            DltApplication instance
        """
        # TODO: Add validation
        return self._obj
