"""Xfile AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 319)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_InlineTextElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.single_language_referrable import (
    SingleLanguageReferrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class Xfile(SingleLanguageReferrable):
    """AUTOSAR Xfile."""

    def __init__(self) -> None:
        """Initialize Xfile."""
        super().__init__()
        self.tool: Optional[String] = None
        self.tool_version: Optional[String] = None
        self.url: Optional[Any] = None


class XfileBuilder:
    """Builder for Xfile."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Xfile = Xfile()

    def build(self) -> Xfile:
        """Build and return Xfile object.

        Returns:
            Xfile instance
        """
        # TODO: Add validation
        return self._obj
