"""BlueprintGenerator AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 424)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_BlueprintGenerator.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    VerbatimString,
)
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)


class BlueprintGenerator(ARObject):
    """AUTOSAR BlueprintGenerator."""

    expression: Optional[VerbatimString]
    introduction: Optional[DocumentationBlock]
    def __init__(self) -> None:
        """Initialize BlueprintGenerator."""
        super().__init__()
        self.expression: Optional[VerbatimString] = None
        self.introduction: Optional[DocumentationBlock] = None


class BlueprintGeneratorBuilder:
    """Builder for BlueprintGenerator."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BlueprintGenerator = BlueprintGenerator()

    def build(self) -> BlueprintGenerator:
        """Build and return BlueprintGenerator object.

        Returns:
            BlueprintGenerator instance
        """
        # TODO: Add validation
        return self._obj
