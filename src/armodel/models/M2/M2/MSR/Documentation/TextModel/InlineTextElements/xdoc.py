"""Xdoc AUTOSAR element.

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
    DateTime,
    String,
)


class Xdoc(SingleLanguageReferrable):
    """AUTOSAR Xdoc."""

    def __init__(self) -> None:
        """Initialize Xdoc."""
        super().__init__()
        self.date: Optional[DateTime] = None
        self.number: Optional[String] = None
        self.position: Optional[String] = None
        self.publisher: Optional[String] = None
        self.state: Optional[String] = None
        self.url: Optional[Any] = None


class XdocBuilder:
    """Builder for Xdoc."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Xdoc = Xdoc()

    def build(self) -> Xdoc:
        """Build and return Xdoc object.

        Returns:
            Xdoc instance
        """
        # TODO: Add validation
        return self._obj
