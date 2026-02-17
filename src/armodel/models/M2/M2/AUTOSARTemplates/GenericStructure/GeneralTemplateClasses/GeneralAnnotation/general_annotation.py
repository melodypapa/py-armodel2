"""GeneralAnnotation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 162)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 163)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_GeneralAnnotation.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multilanguage_long_name import (
    MultilanguageLongName,
)


class GeneralAnnotation(ARObject):
    """AUTOSAR GeneralAnnotation."""
    """Abstract base class - do not instantiate directly."""

    def __init__(self) -> None:
        """Initialize GeneralAnnotation."""
        super().__init__()
        self.annotation: String = None
        self.annotation_text: DocumentationBlock = None
        self.label: Optional[MultilanguageLongName] = None


class GeneralAnnotationBuilder:
    """Builder for GeneralAnnotation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: GeneralAnnotation = GeneralAnnotation()

    def build(self) -> GeneralAnnotation:
        """Build and return GeneralAnnotation object.

        Returns:
            GeneralAnnotation instance
        """
        # TODO: Add validation
        return self._obj
