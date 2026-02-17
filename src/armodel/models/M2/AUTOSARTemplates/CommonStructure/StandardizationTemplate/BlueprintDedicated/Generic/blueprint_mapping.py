"""BlueprintMapping AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 163)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_BlueprintDedicated_Generic.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure.atp_blueprint import (
    AtpBlueprint,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure.atp_blueprintable import (
    AtpBlueprintable,
)


class BlueprintMapping(ARObject):
    """AUTOSAR BlueprintMapping."""

    blueprint: AtpBlueprint
    derived_object: AtpBlueprintable
    def __init__(self) -> None:
        """Initialize BlueprintMapping."""
        super().__init__()
        self.blueprint: AtpBlueprint = None
        self.derived_object: AtpBlueprintable = None


class BlueprintMappingBuilder:
    """Builder for BlueprintMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BlueprintMapping = BlueprintMapping()

    def build(self) -> BlueprintMapping:
        """Build and return BlueprintMapping object.

        Returns:
            BlueprintMapping instance
        """
        # TODO: Add validation
        return self._obj
