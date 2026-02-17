"""Std AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 318)

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


class Std(SingleLanguageReferrable):
    """AUTOSAR Std."""

    def __init__(self) -> None:
        """Initialize Std."""
        super().__init__()
        self.date: Optional[DateTime] = None
        self.position: Optional[String] = None
        self.state: Optional[String] = None
        self.subtitle: Optional[String] = None
        self.url: Optional[Any] = None


class StdBuilder:
    """Builder for Std."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Std = Std()

    def build(self) -> Std:
        """Build and return Std object.

        Returns:
            Std instance
        """
        # TODO: Add validation
        return self._obj
