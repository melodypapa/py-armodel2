"""AtpBlueprint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 305)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 424)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 161)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_AbstractBlueprintStructure.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure.blueprint_policy import (
    BlueprintPolicy,
)


class AtpBlueprint(Identifiable):
    """AUTOSAR AtpBlueprint."""
    """Abstract base class - do not instantiate directly."""

    def __init__(self) -> None:
        """Initialize AtpBlueprint."""
        super().__init__()
        self.blueprint_policies: list[BlueprintPolicy] = []


class AtpBlueprintBuilder:
    """Builder for AtpBlueprint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AtpBlueprint = AtpBlueprint()

    def build(self) -> AtpBlueprint:
        """Build and return AtpBlueprint object.

        Returns:
            AtpBlueprint instance
        """
        # TODO: Add validation
        return self._obj
