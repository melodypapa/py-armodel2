"""Documentation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 294)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 439)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 181)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_DocumentationOnM1.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.DocumentationOnM1.documentation_context import (
    DocumentationContext,
)
from armodel.models.M2.MSR.Documentation.Chapters.predefined_chapter import (
    PredefinedChapter,
)


class Documentation(ARElement):
    """AUTOSAR Documentation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    contexts: list[DocumentationContext]
    documentation: Optional[PredefinedChapter]
    def __init__(self) -> None:
        """Initialize Documentation."""
        super().__init__()
        self.contexts: list[DocumentationContext] = []
        self.documentation: Optional[PredefinedChapter] = None


class DocumentationBuilder:
    """Builder for Documentation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Documentation = Documentation()

    def build(self) -> Documentation:
        """Build and return Documentation object.

        Returns:
            Documentation instance
        """
        # TODO: Add validation
        return self._obj
